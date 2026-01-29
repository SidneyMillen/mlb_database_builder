# Import required libraries
import os
import duckdb
import pandas as pd

from table_definitions import pitch_definition, chadwick_definition, bref_batting_definition, bref_pitching_definition

year = "2025"
statcast_csv_path = f"{year}_statcast_cleaned.csv"
chadwick_csv_path = "chadwick_register.csv"
bref_batting_csv_path = f"bref_batting_{year}.csv"
bref_pitching_csv_path = f"bref_pitching_{year}.csv"
db_file = f"baseball_{year}.duckdb"

def drop_table(name):
    conn.execute(f"DROP TABLE IF EXISTS \"{name}\"")

# Create a connection to the database
print("Connecting to database...")
conn = duckdb.connect(database = db_file, read_only = False)

drop_table('pitches')
drop_table('bref_batting')
drop_table('bref_pitching')
drop_table('chadwick')

# Report which CSV files exist
print("Checking CSV file availability...")
files = {
    "statcast_pitches": statcast_csv_path,
    "chadwick": chadwick_csv_path,
    "bref_batting": bref_batting_csv_path,
    "bref_pitching": bref_pitching_csv_path
}
for name, path in files.items():
    if os.path.exists(path):
        print(f"  Found {name} CSV: {path}")
    else:
        print(f"  MISSING {name} CSV: {path}")

pitches_created = False

# Conditionally read/write Chadwick data
if os.path.exists(chadwick_csv_path):
    print(f"Reading Chadwick CSV: {chadwick_csv_path}")
    print("Writing chadwick table to database...")
    conn.sql(chadwick_definition)
    conn.sql(f"INSERT INTO chadwick (SELECT * FROM '{chadwick_csv_path}')")
else:
    print("Skipping chadwick table creation; CSV file not found.")

# Conditionally read/write pitches data
if os.path.exists(statcast_csv_path):
    print(f"Reading pitches CSV: {statcast_csv_path}")
    print("Writing pitches table to database...")
    conn.sql(pitch_definition)
    conn.sql(f"INSERT INTO pitches (SELECT * FROM '{statcast_csv_path}')")
    pitches_created = True
else:
    print("Skipping pitches table creation; CSV file not found.")

# Create index only if pitches table was created
if pitches_created:
    print("Creating index on pitches table...")
    conn.sql('CREATE INDEX idx_pitches_game_pk ON pitches(game_pk);')
else:
    print("Skipping index creation; no pitches table created.")

if os.path.exists(bref_batting_csv_path):
    print("Writing bref batting csv")
    conn.sql(bref_batting_definition)
    conn.sql(f"INSERT INTO bref_batting (SELECT * FROM '{bref_batting_csv_path}')")
else:
    print(f"{bref_batting_csv_path} not found")

if os.path.exists(bref_pitching_csv_path):
    print("Writing bref pitching csv")
    conn.sql(bref_pitching_definition)
    conn.sql(f"INSERT INTO bref_pitching (SELECT * FROM '{bref_pitching_csv_path}')")
else:
    print(f"{bref_pitching_csv_path} not found")


# Close the connection
print("Closing connection to database.")
conn.close()

print(f"Finished writing available data to {db_file}")
