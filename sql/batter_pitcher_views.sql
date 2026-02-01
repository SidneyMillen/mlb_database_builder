DROP VIEW IF EXISTS batters_in_chadwick_2025;
CREATE view batters_in_chadwick_2025 AS 
select DISTINCT key_mlbam, name_first, name_last from statcast_pitches inner join chadwick on statcast_pitches.batter = chadwick.key_mlbam;

DROP VIEW IF EXISTS pitchers_in_chadwick_2025;
CREATE view pitchers_in_chadwick_2025 AS 
select DISTINCT key_mlbam, name_first, name_last from statcast_pitches inner join chadwick on statcast_pitches.pitcher = chadwick.key_mlbam;
