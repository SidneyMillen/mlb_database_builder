DROP TABLE IF EXISTS game_state;
create table game_state as 
SELECT inning, outs_when_up,
(SELECT basepath_state_id from basepath_states bs where
bs.on_1b = (p.on_1b IS NOT NULL)
AND bs.on_2b = (p.on_2b IS NOT NULL)
and bs.on_3b = (p.on_3b IS NOT NULL)) as basepath_state_id,
inning_topbot, 'index' from statcast_pitches p
