select avg(release_speed), count(release_speed) as num_pitches,
pitchers_in_chadwick_2025.name_first || ' ' || pitchers_in_chadwick_2025.name_last as pitcher_name,
batters_in_chadwick_2025.name_first || ' ' || batters_in_chadwick_2025.name_last as batter_name
from pitches_2025
inner join batters_in_chadwick_2025 on pitches_2025.batter = batters_in_chadwick_2025.key_mlbam
inner join pitchers_in_chadwick_2025 on pitches_2025.pitcher = pitchers_in_chadwick_2025.key_mlbam
where pitches_2025.pitch_type = 'FF' or pitches_2025.pitch_type = 'SI'
group by pitcher, batter
having num_pitches > 10
order by avg(release_speed) DESC
