# Import required libraries
import os
import sqlite3
import pandas as pd

from schemas import pitch_schema, chadwick_schema, bref_batting_schema, bref_pitching_schema

year = "2025"
statcast_csv_path = f"{year}_statcast_cleaned.csv"
chadwick_csv_path = "chadwick_register.csv"
bref_batting_csv_path = f"bref_batting_{year}.csv"
bref_pitching_csv_path = f"bref_pitching_{year}.csv"
db_file = f"{year}_statcast.db"

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

# Create a connection to the database
print("Connecting to database...")
conn = sqlite3.connect(db_file)

pitches_created = False

# Conditionally read/write Chadwick data
if os.path.exists(chadwick_csv_path):
    print(f"Reading Chadwick CSV: {chadwick_csv_path}")
    chadwick_df = pd.read_csv(chadwick_csv_path)

    print("Writing chadwick table to database...")
    chadwick_df.to_sql('chadwick', conn, if_exists='replace', index=False, schema=chadwick_schema)
else:
    print("Skipping chadwick table creation; CSV file not found.")

# Conditionally read/write pitches data
if os.path.exists(statcast_csv_path):
    print(f"Reading pitches CSV: {statcast_csv_path}")
    df = pd.read_csv(statcast_csv_path)

    print("Writing pitches table to database...")
    df.to_sql('pitches', conn, if_exists='replace', index=False, schema=pitch_schema)
    pitches_created = True
else:
    print("Skipping pitches table creation; CSV file not found.")

# Create index only if pitches table was created
if pitches_created:
    print("Creating index on pitches table...")
    conn.execute('CREATE INDEX idx_pitches_game_pk ON pitches(game_pk);')
else:
    print("Skipping index creation; no pitches table created.")

if os.path.exists(bref_batting_csv_path):
    print("Writing bref batting csv")
    bref_bat_df = pd.read_csv(bref_batting_csv_path)
    bref_bat_df.to_sql('bref_batting', conn, if_exists='replace', index=False, schema=bref_batting_schema)
else:
    print(f"{bref_batting_csv_path} not found")

if os.path.exists(bref_pitching_csv_path):
    print("Writing bref pitching csv")
    bref_pitch_df = pd.read_csv(bref_pitching_csv_path)
    bref_pitch_df.to_sql('bref_pitching', conn, if_exists='replace', index=False, schema=bref_pitching_schema)
else:
    print(f"{bref_pitching_csv_path} not found")

# Close the connection
print("Closing connection to database.")
conn.close()

print(f"Finished writing available data to {db_file}")