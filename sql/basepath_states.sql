DROP TABLE IF EXISTS basepath_states;
create table basepath_states (
    basepath_state_id INTEGER PRIMARY KEY,
    on_1b BOOLEAN,
    on_2b BOOLEAN,
    on_3b BOOLEAN,
    UNIQUE(on_1b, on_2b, on_3b)
);
insert into basepath_states (basepath_state_id, on_1b, on_2b, on_3b)
values
	(0, 0, 0, 0),
	(1, 1, 0, 0),
	(2, 0, 1, 0),
	(3, 1, 1, 0),
	(4, 0, 0, 1),
	(5, 1, 0, 1),
	(6, 0, 1, 1),
	(7, 1, 1, 1);