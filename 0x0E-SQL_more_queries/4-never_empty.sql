-- This script creates a table id_not_null in mysql server
-- it will not fail if the table already exists
CREATE TABLE IF NOT EXISTS id_not_null(id INT DEFAULT 1, name VARCHAR(256))