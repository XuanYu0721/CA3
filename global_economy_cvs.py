import csv
import sqlite3

# open the connection to the database
conn = sqlite3.connect('economic_data.db')
cur = conn.cursor()

# Drop the data from the table so that if we rerun the file, we don't repeat values
conn.execute('DROP TABLE IF EXISTS countries')
print("Countries table dropped successfully")

# Create EU countries table
conn.execute('''
CREATE TABLE IF NOT EXISTS countries (
    CountryID TEXT PRIMARY KEY,
    CountryName TEXT UNIQUE,
    Population2000 REAL,
    Population2022 REAL,
    AvgAnnualGrowth REAL,
    Age0_14 REAL,
    Age15_64 REAL,
    Age65Plus REAL,
    DependencyRatioYoung REAL,
    DependencyRatioOld REAL,
    CrudeDeathRate REAL,
    CrudeBirthRate REAL
)
''')
print("Countries table created successfully")

# Drop the economic data table if it exists
conn.execute('DROP TABLE IF EXISTS economic_data')
print("Economic data table dropped successfully")

# Create the economic data table again
conn.execute('''
CREATE TABLE IF NOT EXISTS economic_data (
    RecordID TEXT PRIMARY KEY,
    Year INTEGER,
    CountryID TEXT,
    GDP REAL,
    GDPGrowth REAL,
    EmployersTotal REAL,
    UnemploymentRate REAL,
    FOREIGN KEY (CountryID) REFERENCES countries(CountryID)
)
''')
print("Economic data table created successfully")

# Read and insert data into the countries table
with open('eu_countries.csv', newline='') as f:
    reader = csv.reader(f, delimiter=",")
    next(reader)  # skip the header line
    for row in reader:
        cur.execute('''
            INSERT INTO countries (CountryID, CountryName, Population2000, Population2022, AvgAnnualGrowth, 
                                   Age0_14, Age15_64, Age65Plus, DependencyRatioYoung, 
                                   DependencyRatioOld, CrudeDeathRate, CrudeBirthRate) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
              (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11]))
    conn.commit()
print("EU countries data parsed successfully")

# Read and insert data into the economic_data table
with open('global_economy.csv', newline='') as f:
    reader = csv.reader(f, delimiter=",")
    next(reader)  # skip the header line
    for row in reader:
        cur.execute('''
            INSERT OR IGNORE INTO economic_data (RecordID, Year, CountryID, GDP, GDPGrowth, EmployersTotal, UnemploymentRate) 
            VALUES (?, ?, ?, ?, ?, ?, ?)''',
            (row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
    conn.commit()
print("Economic data parsed successfully")

conn.close()
