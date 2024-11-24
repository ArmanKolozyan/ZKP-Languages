# Empirical Study of Zero-Knowledge Proof (ZKP) Languages
This repository presents an empirical study of Zero-Knowledge Proof (ZKP) languages (including zkVMs), offering an overview of the most prominent ones. The study leverages the GitHub API to gather and analyse key metrics about repositories related to each language (e.g., number of stars, date of last update, etc.).

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

| Name          | Type       |
|---------------|------------|
| **Circom**    | HDL        |
| **ZoKrates**  | DSL        |
| **Cairo**     | DSL        |
| **Nexus VM**  | zkVM       |
| **RISC Zero** | zkVM       |
| **snarkVM**   | zkVM       |
| **SP1**       | zkVM       |

- **HDL**: Hardware Description Language, used for circuit descriptions.
- **DSL**: Domain-Specific Language, designed specifically for writing ZKP programs.
- **zkVM**: Zero-Knowledge Virtual Machine, a virtual machine designed to execute programs written in standard programming languages while generating zero-knowledge proofs of their correctness.

## Visualizations

Graphs are provided to illustrate:
- Number of repositories with more than 1 star for each language.
- Number of repositories updated after 1 January 2024 for each language.
- Number of repositories with more than 10 total issues for each language.
- Percentage of Circom VS ZoKrates programs.
- Comparison of the total number of repositories across all zkVMs VS Circom VS ZoKrates.

## Repository Structure

- **`graphs/`**  
  Contains visualizations of the study in `.png` format.
- **`metrics/`**  
  Contains `.csv` files with detailed metrics for each language and zkVM.

- **`src/`**  
  Contains source files for data collection and analysis:
  - `data_analyzer.ipynb`: Jupyter notebook for analysing and visualising data.
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

3. Run all cells in `data_analyzer.ipynb` to process and visualise the data:
   ```bash
   jupyter notebook src/data_analyzer.ipynb
   ```