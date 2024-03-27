-- lists the number of records with the same score in the table.
-- the result should display
-- the score
-- the number of records for that score with the label number
-- the list will be sorted by the number of records (descending)
-- the database name will be passed as an argument
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;