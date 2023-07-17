# PSGC Data Scraper

The PSGC Data Scraper is a Python script that scrapes the Philippine Standard Geographic Codes (PSGC) webpage, downloads the latest PSGC data file, and converts it into CSV and JSON files for various geographic levels. It also provides functionality to populate a database with the scraped data.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Setting Up the Environment](#setting-up-the-environment)
- [Downloading Dependencies](#downloading-dependencies)
- [Running the Scraper](#running-the-scraper)
- [Setting Up the Database](#setting-up-the-database)
- [Populating the Database](#populating-the-database)
- [License](#license)

## Introduction

The Philippine Standard Geographic Codes (PSGC) is a system developed by the Philippine Statistics Authority (PSA) for standardizing geographic information in the country. The PSGC provides unique codes for various geographic levels such as regions, provinces, cities, municipalities, and barangays. These codes are essential for data management, analysis, and administrative purposes.

The PSGC Data Scraper is a Python script that automates the process of downloading the PSGC data file from the PSA website and converting it into CSV and JSON formats for easy usage and integration into other applications. It also provides functionality to populate a database with the scraped data, allowing for efficient storage and retrieval.

## Installation

To use the PSGC Data Scraper, follow these steps:

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/psgc-data-scraper.git
   ```

2. Navigate to the project directory
   ```bash 
   cd psgc-data-scraper
   ```
## Setting Up the Environment
1. Create a virtual environment using venv or conda:
   ```bash
   # Using venv
   python -m venv env

   # Using conda
   conda create --name env
   ```
2. Activate the virtual environment:
   ```
   # Using venv
   source env/bin/activate

   # Using conda
   conda activate env
   ```

## Downloading Dependencies 
1. Install the required dependencies using pip and the provided requirements.txt file:
   ```
   pip install -r requirements.txt
   ```
2. Modify the database credentials in the index.py file to match your database configuration.

## Running the Scraper
To scrape the PSGC data and generate CSV and JSON files, follow these steps:

1. Run the `scraper.py` script:
   ```
   python scraper.py
   ```
   The script will perform the following tasks:

   * Scrape the PSGC webpage to extract the latest update date.
   * Check if the PSGC data is already up to date by comparing the update date with the existing files in the output directory.
   * If an update is required, download the latest PSGC data file.
   * Convert the downloaded file into separate CSV and JSON files for each geographic level.
   * Save the CSV files in the psgc_csv directory and the JSON files in the psgc_json directory.

2. After running the script, you will find the generated CSV and JSON files in their respective output directories (psgc_csv and psgc_json).


## Setting Up the Database
1. Import the psgcdb.sql file into your preferred database management tool to create the database and tables.

2. Modify the database credentials in the .env file to match your database configuration.

## Populating the Database
To populate the database with the scraped data, follow these steps:
1. Run the `index.py` script:
   ```
   python index.py
   ```
   The script will connect to the database using the provided credentials and insert the data from the generated CSV files into the appropriate tables.
2. After running the script, your database should be populated with the PSGC data.

## Dependencies
The PSGC Data Scraper requires the following dependencies:

* requests
* beautifulsoup4
* pandas
* python-dotenv

You can install the required dependencies using the following command:
   ```
   pip install -r requirements.txt
   ```

## License 
The PSGC Data Scraper is licensed under the MIT License. Feel free to use, modify, and distribute the code as per the terms of the license.