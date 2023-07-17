DROP TABLE IF EXISTS regions;
CREATE TABLE IF NOT EXISTS regions (
    code CHAR(2) NOT NULL,
    name TEXT NOT NULL,
    PRIMARY KEY (code, name)
);
DROP TABLE IF EXISTS provinces;
-- Create the "provinces" table if it doesn't exist
CREATE TABLE IF NOT EXISTS provinces (
    code CHAR(3) NOT NULL,
    region_code CHAR(2) NOT NULL,
    name TEXT NOT NULL,
    PRIMARY KEY (code, name, region_code)
);
DROP TABLE IF EXISTS cities;
-- Create the "cities" table if it doesn't exist
CREATE TABLE IF NOT EXISTS cities (
    code CHAR(2) NOT NULL,
    province_code CHAR(3) NOT NULL,
    region_code CHAR(2) NOT NULL,
    name TEXT NOT NULL,
    PRIMARY KEY (code, name, province_code, region_code)
);
DROP TABLE IF EXISTS municipalities;
-- Create the "municipalities" table if it doesn't exist
CREATE TABLE IF NOT EXISTS municipalities (
    code CHAR(2) NOT NULL,
    province_code CHAR(3) NOT NULL,
    region_code CHAR(2) NOT NULL,
    name TEXT NOT NULL,
    PRIMARY KEY (code, name, province_code, region_code)
);
DROP TABLE IF EXISTS barangays;
-- Create the "barangays" table if it doesn't exist
CREATE TABLE IF NOT EXISTS barangays (
    code CHAR(3) NOT NULL,
    municipality_code CHAR(2) NOT NULL,
    province_code CHAR(3) NOT NULL,
    region_code CHAR(2) NOT NULL,
    name TEXT NOT NULL,
    PRIMARY KEY (
        code,
        name,
        municipality_code,
        province_code,
        region_code
    )
);
