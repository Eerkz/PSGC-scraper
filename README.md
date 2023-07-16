# PSGC Data Scraper

The PSGC Data Scraper is a Python script that scrapes the Philippine Standard Geographic Codes (PSGC) webpage, downloads the latest PSGC data file, and converts it into CSV and JSON files for various geographic levels.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [License](#license)

## Introduction

The Philippine Standard Geographic Codes (PSGC) is a system developed by the Philippine Statistics Authority (PSA) for standardizing geographic information in the country. The PSGC provides unique codes for various geographic levels such as regions, provinces, cities, municipalities, and barangays. These codes are essential for data management, analysis, and administrative purposes.

The PSGC Data Scraper is a Python script that automates the process of downloading the PSGC data file from the PSA website and converting it into CSV and JSON formats for easy usage and integration into other applications. By using this scraper, you can ensure that you always have the most up-to-date PSGC data in a readily accessible format.

## Installation

To use the PSGC Data Scraper, follow these steps:

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/psgc-data-scraper.git
   ```

2. Navigate to the project directory:

   ```bash
   cd psgc-data-scraper
   ```

3. Install the required dependencies using pip:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

To scrape the PSGC data, follow these steps:

1. Open the `scraper.py` file in a text editor.

2. Modify the output directories, if desired. By default, the script creates `psgc_csv` and `psgc_json` directories in the project folder to store the output files.

3. Run the `scraper.py` script:

   ```bash
   python scraper.py
   ```

   The script will perform the following tasks:
   
   - Scrape the PSGC webpage to extract the latest update date.
   - Check if the PSGC data is already up to date by comparing the update date with the existing files in the output directory.
   - If an update is required, download the latest PSGC data file.
   - Convert the downloaded file into separate CSV and JSON files for each geographic level.
   - Save the CSV files in the `psgc_csv` directory and the JSON files in the `psgc_json` directory.

4. After running the script, you will find the generated CSV and JSON files in their respective output directories (`psgc_csv` and `psgc_json`).

## Dependencies

The PSGC Data Scraper requires the following dependencies:

- requests
- beautifulsoup4
- pandas

You can install the required dependencies using the following command:

```bash
pip install -r requirements.txt
```

## License

The PSGC Data Scraper is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute the code as per the terms of the license.