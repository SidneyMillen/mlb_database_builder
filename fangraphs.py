
"""Download Fangraphs data for a given year and save to CSV."""

from config import year

from pybaseball import cache, batting_stats, pitching_stats, fielding_stats, team_batting, team_pitching, team_fielding

batter_data_file = f"fangraphs_batters_{year}.csv"
pitcher_data_file = f"fangraphs_pitcher_{year}.csv"
fielder_data_file = f"fangraphs_fielder_{year}.csv"
team_batting_data_file = f"fangraphs_team_batting_{year}.csv"
team_pitching_data_file = f"fangraphs_team_pitching_{year}.csv"
team_fielding_data_file = f"fangraphs_team_fielding_{year}.csv"

    
def main():
    cache.enable()

    batter_data = batting_stats(year)
    batter_data.to_csv(batter_data_file, index=False)
    print(f"Wrote {batter_data_file}")

    pitcher_data = pitching_stats(year)
    pitcher_data.to_csv(pitcher_data_file, index=False)
    print(f"Wrote {pitcher_data_file}")
    
    fielder_data = fielding_stats(year)
    fielder_data.to_csv(fielder_data_file, index=False)
    print(f"Wrote {fielder_data_file}")

    team_batting_data = team_batting(year)
    team_batting_data.to_csv(team_batting_data_file, index=False)
    print(f"Wrote {team_batting_data_file}")
    
    team_pitching_data = team_pitching(year)
    team_pitching_data.to_csv(team_pitching_data_file, index=False)
    print(f"Wrote {team_pitching_data_file}")
    
    team_fielding_data = team_fielding(year)
    team_fielding_data.to_csv(team_fielding_data_file, index=False)
    print(f"Wrote {team_fielding_data_file}")

if __name__ == "__main__":
    main()

