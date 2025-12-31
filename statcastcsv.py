"""Download Statcast data for a given year and save to CSV."""

from pybaseball import statcast
import pybaseball


def main():
    """Download Statcast data and save to CSV."""
    pybaseball.cache.enable()
    
    year = "2025"
    start_date = f"{year}-03-10"
    end_date = f"{year}-11-30"
    output_file = f"{year}_statcast.csv"
    
    print(f"Downloading Statcast data for {year}...")
    results = statcast(start_dt=start_date, end_dt=end_date)
    
    print(f"Saving data to {output_file}...")
    results.to_csv(output_file, index=False)
    print(f"Successfully saved {len(results)} records to {output_file}")


if __name__ == "__main__":
    main()
