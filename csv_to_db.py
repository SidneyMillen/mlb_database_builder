# Import required libraries
import sqlite3
import pandas as pd

from schemas import pitch_schema, chadwick_schema

year = "2025"
csv_file = f"{year}_statcast_cleaned.csv"
chadwick_file = "chadwick_register.csv"
db_file = f"{year}_statcast.db"

# Create a connection to the database
print("Connecting to database...")
conn = sqlite3.connect(db_file)

# Read the CSV file into a pandas dataframe
print(f"Reading CSV files: {csv_file}, {chadwick_file}")
df = pd.read_csv(csv_file)
chadwick_df = pd.read_csv(chadwick_file)

# Create tables with custom schemas first
print("Creating chadwick table with custom schema...")
conn.execute(f'DROP TABLE IF EXISTS chadwick;')
conn.execute(f'CREATE TABLE chadwick ({chadwick_schema});')

print("Creating pitches table with custom schema...")
conn.execute(f'DROP TABLE IF EXISTS pitches_{year};')
conn.execute(f'CREATE TABLE pitches_{year} ({pitch_schema});')

# Write the dataframes to the database
print("Writing chadwick data to database...")
# append since we just made the table with the correct schema
chadwick_df.to_sql('chadwick', conn, if_exists="append", index=False)

print("Writing pitches data to database...")
df.to_sql(f'pitches_{year}', conn, if_exists="append", index=False)

print("Creating index on pitches table...")
conn.execute(f'DROP INDEX IF EXISTS idx_pitches_game_pk_{year}')
conn.execute(f'CREATE INDEX idx_pitches_game_pk_{year} ON pitches_{year}(game_pk);')

print("Creating view of batters in chadwick for " )
conn.execute(f'DROP VIEW IF EXISTS batters_in_chadwick_{year}')
conn.execute(f'CREATE VIEW batters_in_chadwick_{year} AS SELECT * FROM chadwick WHERE key_mlbam IN (SELECT DISTINCT batter FROM pitches_{year} WHERE batter IS NOT NULL);')

print("Creating view of pitchers in chadwick")
conn.execute(f'DROP VIEW IF EXISTS pitchers_in_chadwick_{year}')
conn.execute(f'CREATE VIEW pitchers_in_chadwick_{year} AS SELECT * FROM chadwick WHERE key_mlbam IN (SELECT DISTINCT pitcher FROM pitches_{year} WHERE pitcher IS NOT NULL);')

# Close the connection
print("Closing connection to database.")
conn.close()

print(f"Data successfully written to {db_file}")