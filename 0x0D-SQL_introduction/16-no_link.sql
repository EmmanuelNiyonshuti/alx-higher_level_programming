-- lists all records of the table.
-- don't list rows without a name value
-- results should display the score and the name
-- records should be listed by descending score
-- the database name will be passed as an argument to the mysql command
SELECT score, name from second_table WHERE name IS NOT NULL ORDER BY score DESC;