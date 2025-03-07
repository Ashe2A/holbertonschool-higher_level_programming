-- full creation (second table and some rows, should not fail)

CREATE TABLE IF NOT EXISTS second_table
(
	id INT,
	name VARCHAR(256),
	score INT
);
INSERT INTO second_table (id, name, score)
VALUES (1, "John", 10),
(1, "Alex", 3),
(1, "Bob", 14),
(1, "George", 8);
