-- lists all records with score >= 10 in the table
-- displays both the score and the name
-- Records ordered by score(top first)
-- the database name will be passed as an argument
SELECT score, name FROM second_table
WHERE score >= 10 ORDER BY score DESC;