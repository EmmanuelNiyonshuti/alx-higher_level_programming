-- creates the table on mysql server
-- the database name will be passed as an argument
-- should not fail if the table already exists
CREATE TABLE IF NOT EXISTS force_name(id INT, name VARCHAR(256));
