-- Creates a table first_table with attributes id and name
-- script should not fail if table already exists
CREATE TABLE IF NOT EXISTS first_table(
	id INT DEFAULT NULL,
	name VARCHAR(256) DEFAULT NULL
);

