
"""Download Statcast data for a given year and save to CSV."""

from config import year

from pybaseball import batting_stats_bref, pitching_stats_bref
import pybaseball

def fix_encoding(text):
    """fixes some weird encoding issues"""
    if isinstance(text, str):
        return text.encode('latin-1').decode('unicode_escape').encode('latin-1').decode('utf-8')
    return text

def main():
    pybaseball.cache.enable()

    batter_data = batting_stats_bref(year)
    batter_data['Name'] = batter_data['Name'].apply(fix_encoding)
    batter_data.to_csv(f"bref_batting_{year}.csv", index=False)
    print(f"Wrote bref_batting_{year}.csv")

    pitcher_data = pitching_stats_bref(year)
    pitcher_data['Name'] = pitcher_data['Name'].apply(fix_encoding)
    pitcher_data.to_csv(f"bref_pitching_{year}.csv", index=False)
    print(f"Wrote bref_pitching_{year}.csv")


if __name__ == "__main__":
    main()
