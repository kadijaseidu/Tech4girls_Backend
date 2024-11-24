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

-- Create Posts table with the stated columns
CREATE TABLE IF NOT EXISTS Posts (
    id INT AUTO_INCREMENT PRIMARY KEY,          
    user_id INT,                               
    title VARCHAR(255) NOT NULL,                 
    content TEXT NOT NULL,                      
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
    FOREIGN KEY (user_id) REFERENCES Users(id)   
);

-- Show a list of all the tables
SHOW TABLES;

-- Insert sample data into the Posts table to establish a one-to-many relationship
INSERT INTO Posts (user_id, title, content, created_at) 
VALUES  (1, "Poll: Which One Are You: Early Bird vs Night Owl? ", "Are you more productive at the crack of dawn, or do you get your best ideas late at night? Vote below!", "2024-11-01 11:00:00"),
    (2, "Are You Making These Common Mistakes? Find Out Now!", "You could be unknowingly making these 5 common mistakes that could be holding you back. Let's break them down and avoid them together!", "2024-11-02 12:00:00"),
    (3,  "5 Simple Ways to Boost Your Productivity Today!", "Struggling with staying on track? Here are 5 quick productivity hacks to help you crush your goals today. From time-blocking to taking intentional breaks, these tips will get you moving!", "2024-11-03 13:00:00"),
    (1, "Engage your mind", "Emotional intuition vs. Logical reasoning! let's discuss", "2024-11-02 15:00:00"),
    (2, "What's Your Go-To Self-Care Ritual? Share with Us!",  "Self-care is different for everyone! Whether it's a bubble bath, reading a book, or a walk in the park, we want to know how YOU unwind. Share your favorite rituals with us", "2024-11-04 16:30:00");

SELECT * FROM Posts;