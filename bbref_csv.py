
"""Download Statcast data for a given year and save to CSV."""

from pybaseball import batting_stats_bref
import pybaseball

def main():
    """Download Statcast data and save to CSV."""
    pybaseball.cache.enable()

    year = "2025"

    batter_data = batting_stats_bref(year)
    batter_data.to_csv(f"bref_batting_{year}.csv", index=False)
    print(f"Wrote bref_batting_{year}.csv to db")

    pitcher_data = batting_stats_bref(year)
    pitcher_data.to_csv(f"bref_pitching_{year}.csv", index=False)
    print(f"Wrote bref_pitching_{year}.csv to db")


if __name__ == "__main__":
    main()
