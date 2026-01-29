SELECT avg(release_speed),
       count(release_speed) AS num_pitches,
       pitchers_in_chadwick_2025.name_first || ' ' || pitchers_in_chadwick_2025.name_last AS pitcher_name,
       batters_in_chadwick_2025.name_first || ' ' || batters_in_chadwick_2025.name_last AS batter_name
FROM pitches
INNER JOIN batters_in_chadwick_2025 ON pitches.batter = batters_in_chadwick_2025.key_mlbam
INNER JOIN pitchers_in_chadwick_2025 ON pitches.pitcher = pitchers_in_chadwick_2025.key_mlbam
WHERE pitches.pitch_type = 'FF'
  OR pitches.pitch_type = 'SI'
GROUP BY pitcher,
         batter
HAVING num_pitches > 10
ORDER BY avg(release_speed) DESC