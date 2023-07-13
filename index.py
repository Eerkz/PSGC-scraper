import requests
from bs4 import BeautifulSoup
from datetime import date, datetime
import os
import pandas as pd
import re

# Base URL and file base URL
baseURL = "https://psa.gov.ph/classification/psgc/?q=psgc/"
fileBaseURL = "https://psa.gov.ph"

# Create a directory to save the files if it doesn't exist
output_directory = "psgc_files"
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Columns to select from the "PSGC" sheet
columns_to_select = ["10-digit PSGC", "Name", "Correspondence Code",
                     "Geographic Level", "2020 Population", "Status"]

# Make a request to the webpage and parse the HTML
response = requests.get(baseURL)
soup = BeautifulSoup(response.content, "html.parser")

# Find the <p> tag containing the latest update date
update_date_tag = soup.find(string=re.compile(
    r"Philippine Standard Geographic Codes as of \d{1,2} \w+ \d{4}"))

if update_date_tag:
    # Extract the latest update date from the entire text content
    latest_update_date_text = update_date_tag.text.replace(
        "Philippine Standard Geographic Codes as of ", "")
    latest_update_date = datetime.strptime(
        latest_update_date_text, "%d %B %Y").date()
else:
    # Skip processing if update date tag is not found
    print("Latest update date not found. Exiting...")
    exit()

# Check if the file already exists
output_path = output_directory
if os.path.exists(output_path):
    existing_files = os.listdir(output_path)
    if existing_files:
        latest_file_name = existing_files[-1]
        file_date_match = re.search(r"\d{4}-\d{2}-\d{2}", latest_file_name)
        if file_date_match:
            latest_file_date = datetime.strptime(
                file_date_match.group(), "%Y-%m-%d").date()
            if latest_update_date <= latest_file_date:
                print("File is up to date. Exiting...")
                exit()
        else:
            print(f"Invalid file name format: {latest_file_name}")

# Find the <a> tag containing the link to the "Publication" file
publication_link = soup.find("a", string="Publication")

# Check if the link exists and extract the file URL
if publication_link:
    file_url = publication_link["href"]

    # Download the file
    today = date.today()
    filename = f"psgc_{today.strftime('%Y-%m-%d')}.xlsx"
    file_path = os.path.join(output_path, filename)

    response = requests.get(fileBaseURL + file_url)
    with open(file_path, "wb") as file:
        file.write(response.content)

    # Convert XLSX to CSV and select specific columns
    excel_data = pd.read_excel(
        file_path, sheet_name="PSGC", usecols=columns_to_select)
    csv_filename = os.path.splitext(filename)[0] + ".csv"
    csv_filepath = os.path.join(output_path, csv_filename)
    excel_data.to_csv(csv_filepath, index=False)

    print("File downloaded and converted to CSV successfully.")
else:
    print("Publication file not found.")
