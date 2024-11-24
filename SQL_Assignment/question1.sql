-- Create Tech4Girls_DB database
CREATE DATABASE IF NOT EXISTS Tech4Girls_DB;

-- Show a list of all databases
SHOW DATABASES;

-- Switch to Tech4Girls_DB database
USE Tech4Girls_DB;

-- Create Users table with stated columns
CREATE TABLE IF NOT EXISTS Users (
    id INT AUTO_INCREMENT PRIMARY KEY,      
    username VARCHAR(50) NOT NULL,          
    email VARCHAR(100) NOT NULL,             
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP 
);

-- Insert sample data into the Users table
INSERT INTO Users (username, email, created_at) 
VALUES 
    ('ama', 'ama@example.com', '2024-11-01 10:30:00'),
    ('Abena', 'abena@example.com', '2024-11-02 12:00:00'),
    ('adjoa', 'adjoa@example.com', '2024-11-03 14:15:00');

SELECT * FROM Users;