"""Download Statcast data for a given year and save to CSV."""

from config import year

from pybaseball import statcast
import pybaseball

#this will index all the pitches and make that index the primary key of the pitch table.
#otherwise the PK is (game_pk, at_bat_number, pitch_number)
index_pitches=True


def main():
    """Download Statcast data and save to CSV."""
    pybaseball.cache.enable()
    
    #TODO add functionality for season to-date and season/postseason splits
    start_date = f"{year}-03-10"
    end_date = f"{year}-11-30"
    output_file = f"{year}_statcast.csv"
    
    print(f"Downloading Statcast data for {year}...")
    #this throws tons and tons of warnings, but its an issue in pybaseball. it does work for now
    results = statcast(start_dt=start_date, end_dt=end_date)
    
    print(f"Saving data to {output_file}...")
    results.to_csv(output_file, index=False)
    print(f"Successfully saved {len(results)} records to {output_file}")


if __name__ == "__main__":
    main()
