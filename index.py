import psycopg2
import json
import re
import os
from dotenv import load_dotenv

load_dotenv()

con = psycopg2.connect(
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT")
)

# Define a helper function to extract the date from the filename


def extract_date_from_filename(filename):
    match = re.search(r"\d{4}-\d{2}-\d{2}", filename)
    if match:
        return match.group()
    else:
        return None

# Define a helper function to construct the JSON file path


def get_json_file_path(level_name):
    directory = "psgc_json"
    files = os.listdir(directory)
    for file in files:
        if file.startswith(level_name):
            file_date = extract_date_from_filename(file)
            if file_date:
                return os.path.join(directory, file)
    return None


# Load the JSON data for each geographic level
with open(get_json_file_path("regions")) as json_file:
    regions_data = json.load(json_file)

with open(get_json_file_path("provinces")) as json_file:
    provinces_data = json.load(json_file)

with open(get_json_file_path("cities")) as json_file:
    cities_data = json.load(json_file)

with open(get_json_file_path("municipalities")) as json_file:
    municipalities_data = json.load(json_file)

with open(get_json_file_path("barangays")) as json_file:
    barangays_data = json.load(json_file)

with open(get_json_file_path("submunicipalities")) as json_file:
    submunicipalities_data = json.load(json_file)


def insert_data(table_name, data):
    if table_name == "submunicipalities":
        return  # Skip insertion for the "submunicipalities" table
    cursor = con.cursor()
    for row in data:
        placeholders = ', '.join(['%s'] * len(row))
        columns = ', '.join(row.keys())
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders}) ON CONFLICT DO NOTHING"
        values = tuple(row.values())
        cursor.execute(query, values)
    con.commit()


insert_data("regions", regions_data)
insert_data("provinces", provinces_data)
insert_data("cities", cities_data)
insert_data("municipalities", municipalities_data)
insert_data("barangays", barangays_data)
insert_data("submunicipalities", submunicipalities_data)

con.close()
