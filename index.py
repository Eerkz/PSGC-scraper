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
columns_to_select = ["10-digit PSGC", "Name", "2020 Population", "Status"]

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
                print("Files are up to date. Exiting...")
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

    # Convert XLSX to separate CSV files for each geographic level
    excel_data = pd.read_excel(file_path, sheet_name="PSGC")

    # Convert XLSX to separate CSV files for each geographic level
    for level_code, level_name in [("Bgy", "barangays"), ("Mun", "municipalities"), ("City", "cities"), ("Prov", "provinces"), ("Reg", "regions"), ("SubMun", "submunicipalities")]:
        mask = excel_data["Geographic Level"].fillna("").astype(str).apply(
            lambda x: x.strip().lower() if pd.notnull(x) else "") == level_code.lower()
        # Make a copy to avoid SettingWithCopyWarning
        level_data = excel_data[mask].copy()
        level_filename = f"{level_name}_{today.strftime('%Y-%m-%d')}.csv"
        level_filepath = os.path.join(output_path, level_filename)
        
        level_data["population"] = level_data["2020 Population"]
        level_data["name"] = level_data["Name"]

        # Add the requested columns based on geographic levels
        if level_name == "regions":
            level_data["code"] = level_data["10-digit PSGC"].astype(
                str).str[:2]
            
            level_data["region_code"] = level_data["10-digit PSGC"].astype(
                str).str[:2]
        elif level_name in ["provinces", "cities", "municipalities"]:
            if level_name == "provinces":
                level_data["code"] = level_data["10-digit PSGC"].astype(
                str).str[:3]
            elif level_name == "cities":
                level_data["city_code"] = level_data["10-digit PSGC"].astype(
                str).str[:2]
                level_data["code"] = level_data["10-digit PSGC"].astype(
                str).str[:2]
            else:
                level_data["city_code"] = level_data["10-digit PSGC"].astype(
                str).str[:2]
                level_data["code"] = level_data["10-digit PSGC"].astype(
                str).str[:2]

            level_data["region_code"] = level_data["10-digit PSGC"].astype(
                str).str[:2]
            level_data["province_code"] = level_data["10-digit PSGC"].astype(
                str).str[:3]
            
        elif level_name == "submunicipalities":
            level_data["region_code"] = level_data["10-digit PSGC"].astype(
                str).str[:2]
            level_data["province_code"] = level_data["10-digit PSGC"].astype(
                str).str[:3]
            level_data["municipality_code"] = level_data["10-digit PSGC"].astype(
                str).str[:2]
            
        elif level_name == "barangays":
            level_data["code"] = level_data["10-digit PSGC"].astype(
                str).str[-3:]
            
            level_data["region_code"] = level_data["10-digit PSGC"].astype(
                str).str[:2]
            level_data["province_code"] = level_data["10-digit PSGC"].astype(
                str).str[:3]
            level_data["municipality_code"] = level_data["10-digit PSGC"].astype(
                str).str[:2]
            level_data["barangay_code"] = level_data["10-digit PSGC"].astype(
                str).str[-3:]

        # Get the final list of columns to select
        existing_columns = [col for col in columns_to_select if col not in ["10-digit PSGC","2020 Population", "Status", "Name"] ] + \
            [col for col in level_data.columns if col.endswith("_code") or col in ["name", "population","code"]]


        # Select the columns that exist in the dataframe
        level_data = level_data[existing_columns]
        level_data.to_csv(level_filepath, index=False)

    print("Files downloaded and converted to CSV successfully.")

else:
    print("Publication file not found.")
