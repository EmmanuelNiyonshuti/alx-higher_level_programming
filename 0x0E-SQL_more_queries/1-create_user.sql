-- creates the MySQL server user user_0d_1
-- user_0d_1 will have all privileges
-- should not fail if the user already exists
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
