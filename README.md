# Empirical Study of Zero-Knowledge Proof (ZKP) Languages

This repository presents an empirical study of Zero-Knowledge Proof (ZKP) languages (including zkVMs), offering an overview of the most prominent ones. The study leverages the GitHub API to gather and analyze key metrics about repositories related to each language (e.g., number of stars, date of last update, etc.).

## Overview

This repository includes:

- A quantitative analysis of repositories for many ZKP languages using metrics such as:
  - Number of stars
  - Number of open issues
  - Date of last update
  - Number of contributors
- Visualizations to highlight interesting trends.
- All code used for data collection and visualization.

## Studied ZKP Languages

This study covers the following ZKP languages:

| Name          | Type |
| ------------- | ---- |
| **Circom**    | DSL  |
| **ZoKrates**  | DSL  |
| **Noir**      | DSL  |
| **Cairo**     | DSL  |
| **Leo**       | DSL  |
| **Nexus VM**  | zkVM |
| **RISC Zero** | zkVM |
| **snarkVM**   | zkVM |
| **SP1**       | zkVM |
| **Jolt**      | zkVM |

- **DSL**: Domain-Specific Language, designed specifically for writing ZKP programs.
- **zkVM**: Zero-Knowledge Virtual Machine, a virtual machine designed to execute programs written in standard programming languages while generating zero-knowledge proofs of their correctness.

## Visualizations

Graphs are provided to illustrate:

- Number of repositories with more than 1 star for each language.
- Number of repositories updated after 1 January 2024 for each language.
- Number of repositories with more than 10 total issues for each language.
- Percentage of Circom VS ZoKrates VS Noir programs.
- Comparison of the total number of repositories across all zkVMs VS Circom.

## GitHub API Search Queries

The study utilized GitHub's API to search for repositories. Below are the specific search queries used to identify relevant repositories for each language:

| Language         | GitHub Search Query             |
|------------------|---------------------------------|
| **Circom**       | `filename:.circom`              |
| **ZoKrates**     | `filename:.zok`                 |
| **Noir**         | `filename:nargo.toml`           |
| **Cairo**        | `filename:scarb.toml`           |
| **Leo**          | `filename:.leo`                 |
| **Nexus VM**     | `nexus_rt`                      |
| **RISC Zero**    | `risc0-build`                   |
| **snarkVM**      | `snarkvm`                       |
| **SP1**          | `SP1_zkvm`                      |
| **Jolt**         | `jolt-sdk`                      |

### Explanation of Queries:

- **File-based Searches (`filename:`):**  
  Some queries, like `filename:.circom` for Circom and `filename:scarb.toml` for Cairo, target specific file extensions or package manager files unique to the language.
- **Build Tools or SDKs:**  
  Queries such as `risc0-build`  and `nexus_rt` focus on build tools or SDKs that are central to these zkVMs.
- **zkVM Identifiers:**  
  For zkVMs like SP1 and SNARKVM, the queries target unique identifiers (`SP1_zkvm` and `snarkvm`) associated with these projects.

## Results

The analysis revealed the following key insights:

- **Circom** appears to be the most popular ZKP language, likely due to its strong performance and optimization capabilities for building circuits.
- **Cairo** stands out as the most widely adopted zkVM, most likely because it was released early and powers *StarkNet*, a popular Layer-2 scaling solution on Ethereum.
- **zkVMs** have seen great usage from 2024, surpassing Circom in growth trends, indicating a shift toward virtual machine-based ZKP solutions. This shift likely reflects the growing preference for zkVMs, which offer greater usability by enabling developers to write general-purpose programs rather than focusing on low-level circuit design.
- **ZoKrates** shows very limited usage, likely due to its comparatively lower performance and stagnated development (with the last commit recorded in April 2024).

## Repository Structure

- **`graphs/`**  
  Contains visualizations of the study in `.png` format.
- **`metrics/`**  
  Contains `.csv` files with detailed metrics for each language.

- **`src/`**  
  Contains source files for data collection and analysis:

  - `data_analyzer.ipynb`: Jupyter notebook for analysing and visualizing data.
  - `data_collector.py`: Python script for fetching data using the GitHub API.
  - `requirements.txt`: Lists Python dependencies required for running the project.

- **`README.md`**  
  This file.

## Getting Started

### Prerequisites

- Python 3.8 or later
- Git
- Jupyter Notebook (for running `.ipynb` files)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ArmanKolozyan/ZKP-Languages.git
   cd zkp-languages
   ```
2. Install dependencies:
   ```bash
   cd src
   pip install -r requirements.txt
   ```

### Usage

1. Fill in your GitHub API token:

   - Generate a token at [GitHub Personal Access Tokens](https://github.com/settings/tokens).
   - Add your token in the appropriate location in `data_collector.py`.

2. Run `data_collector.py` to collect data. When prompted, enter the desired search term in the terminal:

   ```bash
   python src/data_collector.py
   ```

3. Run all cells in `data_analyzer.ipynb` to process and visualize the data:
   ```bash
   jupyter notebook src/data_analyzer.ipynb
   ```

## Contributing

Contributions are welcome! Please create an issue or submit a pull request if you have ideas to improve the project.

## TODO

- [ ] Support more ZKP languages 
  - [x] Noir
  - [x] Leo
  - [x] Jolt zkVM
  - [ ] Zinc
  - [ ] Halo2
- [ ] Add more details to the languages table.  
- [ ] Manually analyze GitHub issues of the top 5 repositories for each language.  
- [ ] Manually clean the `.csv` files.  
- [ ] Add more conclusions to the results.
- [ ] Conduct a historical analysis: e.g., comparing number of zkVM repositories to Circom repositories over the years.
- [ ] Distinguish between the 2 use cases of Cairo (writing smart contracts vs. proof-related applications).
- [ ] Explore GitHub’s dependency tracking feature (e.g., https://github.com/risc0/risc0/network/dependents).
- [ ] Design a front-end dashboard for improved data visualization.
