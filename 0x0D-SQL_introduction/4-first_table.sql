-- Creates a table in the current database
-- table description: id int, name VARCHAR(256)
-- data base name will be passed as an argument of the mysql command
-- script will not fail if the table already exists
CREATE table IF NOT EXISTS first_table(
    id INT,
    name VARCHAR(256)
);