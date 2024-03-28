-- This script creates the database hbtn_0d_usa and the table states inside hbtn_0d_usa
-- the script will not fail if the database hbtn_0d_usa already exists
-- the script will not fail if the table states already exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states
(id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY, name VARCHAR(256) NOT NULL);