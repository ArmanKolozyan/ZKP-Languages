import requests
import pandas as pd
from bs4 import BeautifulSoup

# GitHub personal access token
GITHUB_TOKEN = "" # please put your token here!
GITHUB_API_URL = "https://api.github.com"

# headers for authentication
headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

# helper function to scrape the number of contributors from a GitHub repository page
def get_number_of_contributors(repo_name):
    try:
        url = f"https://github.com/{repo_name}"
        response = requests.get(url)
        
        if response.status_code != 200:
            print(f"Failed to access {url}")
            return 0

        soup = BeautifulSoup(response.content, "html.parser")
        
        # looking for the element that contains the number of contributors
        contributors_element = soup.find("a", href=f"/{repo_name}/graphs/contributors")
        
        if contributors_element:
            # extracting the number of contributors from the text
            contributors_text = contributors_element.get_text(strip=True)
            contributors_number = int("".join(filter(str.isdigit, contributors_text)))
            return contributors_number
        else:
            return 1
        
    except Exception as e:
        print(f"Error scraping contributors for {repo_name}: {e}")
        return 0
    

# function to query GitHub API and get repositories with .zok files
# REMARK: 
#   if you want to search by file extension, please use the 'filename' selector 
#   instead of 'path'! 
#   For more details, see: https://github.com/orgs/community/discussions/64618#discussioncomment-8473570
def analyse_repositories(search_term):
    url = f"{GITHUB_API_URL}/search/code?q={search_term}&per_page=50"
    repos = [] # result
    repo_names_set = set()  # to keep track of unique repository names
    page = 0
    
    while True:
        
        response = requests.get(url + f"&page={page}", headers=headers)
        
        # checking if the response is successful
        if response.status_code != 200:
            print(f"Error: Received status code {response.status_code}")
            print(response.json())  # Print the error details
            break
        
        data = response.json()

        # checking if items are present
        if "items" not in data or not data["items"]:
            print("No items found in the response or no more items to process.")
            break

        for item in data["items"]:
            repo_name = item["repository"]["full_name"]
            if repo_name in repo_names_set:  # skip if already added
                continue
            
            # add repo_name to the set to eliminate duplicates
            repo_names_set.add(repo_name)
            
            # fetching the repository details to get additional metrics
            repo_url = f"{GITHUB_API_URL}/repos/{repo_name}"
            repo_response = requests.get(repo_url, headers=headers)
            
            if repo_response.status_code == 200:
                repo_data = repo_response.json()

                # fetching total number of issues (open + closed)
                issues_url = f"{GITHUB_API_URL}/repos/{repo_name}/issues?state=all&per_page=50"
                issues_response = requests.get(issues_url, headers=headers)

                if issues_response.status_code == 200:
                    # extracting total issue count from headers if pagination exists
                    link_header = issues_response.headers.get("Link")
                    if link_header and 'rel="last"' in link_header:
                        last_page = int(link_header.split("page=")[-1].split(">")[0])
                        total_issues_count = last_page # since per_page=1
                    else:
                        total_issues_count = len(issues_response.json())
                else:
                    total_issues_count = 0

                # scraping the number of contributors via helper function
                num_contributors = get_number_of_contributors(repo_name)

                # formatting the last updated datetime to only include the date
                last_updated = repo_data.get("updated_at", "N/A").split("T")[0]

                repos.append({
                    "Repository": repo_name,
                    "Stars": repo_data.get("stargazers_count", 0),
                    "Forks": repo_data.get("forks_count", 0),
                    "Open Issues": repo_data.get("open_issues_count", 0),
                    "Total Issues": total_issues_count,
                    "Last Updated": last_updated,
                    "Primary Language": repo_data.get("language", "N/A"),
                    "Contributors": num_contributors
                })

        # checking if there are more pages
        if "next" not in response.links:
            print("no next anymore")
            break
        page += 1

    return repos


# fetching the repositories and their metrics
search_term = input("Enter search term: ")
repositories = analyse_repositories(search_term)

# converting the data into a sorted DataFrame
df = pd.DataFrame(repositories)
df = df.sort_values(by="Stars", ascending=False)  # sorting in descending order

# saving the DataFrame to a CSV file
df.to_csv(f"../metrics/metrics_for_{search_term}.csv", index=False)

print(f"Data has been written to metrics_for_{search_term}.csv")