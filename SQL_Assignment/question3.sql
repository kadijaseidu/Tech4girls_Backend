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





-- Switch to Tech4Girls_DB database
USE Tech4Girls_DB;

-- Create Courses table with the stated columns
CREATE TABLE IF NOT EXISTS Courses (
    id INT AUTO_INCREMENT PRIMARY KEY,         
    course_name VARCHAR(100) NOT NULL           
);

-- Create User_Courses intermediate table to establish a many-to-many relationship between Users and Courses
CREATE TABLE IF NOT EXISTS User_Courses (
    user_id INT,                              
    course_id INT,                           
    PRIMARY KEY (user_id, course_id),         
    FOREIGN KEY (user_id) REFERENCES Users(id), 
    FOREIGN KEY (course_id) REFERENCES Courses(id) 
);

-- Insert sample data into the Courses table
INSERT INTO Courses (course_name) 
VALUES 
    ('Public Speaking'),
    ('Introduction to Web Design'),
    ('Theories of PR');

-- Insert sample data into the User_Courses table to demonstrate the many-to-many relationship
INSERT INTO User_Courses (user_id, course_id)
VALUES 
    (1, 1),  -- Ama is enrolled in Public Speaking
    (2, 2),  -- Abena is enrolled in Introduction to Web Design
    (3, 3),  -- Adjoa is enrolled in Theories of PR
    (1, 3),  -- Ama is enrolled in Theories of PR
    (2, 1),  -- Abena is enrolled in Public Speaking
    (1, 2);  -- Ama is enrolled inIntroduction to Web Design

SELECT * FROM Courses;
SELECT * FROM User_Courses;