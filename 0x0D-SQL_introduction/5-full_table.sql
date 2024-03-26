-- Prints the full description of the table
-- Te database name will be passed as an argument of the mysql command
-- without using DESCRIBE or EXPLAIN statements.
SELECT 
   information_schema.COLUMNS.COLUMN_NAME AS 'Field'
 , information_schema.COLUMNS.COLUMN_TYPE AS 'Type'
 , information_schema.COLUMNS.IS_NULLABLE AS 'Null'
 , information_schema.COLUMNS.COLUMN_KEY AS 'Key'
 , information_schema.COLUMNS.COLUMN_DEFAULT AS 'Default'
 , information_schema.COLUMNS.EXTRA AS 'Extra'
FROM 
 information_schema.TABLES
INNER JOIN
 information_schema.COLUMNS
ON
 information_schema.TABLES.TABLE_NAME =  information_schema.COLUMNS.TABLE_NAME
WHERE
 information_schema.TABLES.TABLE_NAME = 'first_table'