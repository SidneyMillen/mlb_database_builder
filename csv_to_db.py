# Import required libraries
import sqlite3
import pandas as pd

year = "2025"
csv_file = f"{year}_statcast_cleaned.csv"
db_file = f"{year}_statcast.db"

# Create a connection to the database
conn = sqlite3.connect(db_file)

# Read the CSV file into a pandas dataframe
df = pd.read_csv(csv_file)

# Write the dataframe to the database
df.to_sql('pitches', conn, if_exists='replace', index=False)

# Close the connection
conn.close()

print(f"Data successfully written to {db_file}")