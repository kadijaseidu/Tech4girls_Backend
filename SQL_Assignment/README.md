# SQL Database Scripts for Tech4Girls
# Author
- [Khadijah Seidu](https://github.com/kadijaseidu)

This repository contains SQL scripts for setting up a simple database for Tech4Girls_DB with users, posts, and courses.

You can find the project repository [here](https://github.com/kadijaseidu/Tech4girls_Backend).


## 1. Setting Up and Populating a Database [question1.sql](https://github.com/kadijaseidu/Tech4girls_Backend/blob/main/SQL_Assignment/question1.sql).

### Purpose:
This script creates a database `Tech4Girls_DB` and a `Users` table. It also inserts sample data for three users.

### SQL Concepts:
- Creating a database.
- Creating a table with `PRIMARY KEY`, `AUTO_INCREMENT`, and `TIMESTAMP`.
- Inserting sample data into a table.

## 2. Building Relationships [question2.sql](https://github.com/kadijaseidu/Tech4girls_Backend/blob/main/SQL_Assignment/question2.sql).

### Purpose:
This script creates a `Posts` table and establishes a **one-to-many** relationship between `Users` and `Posts` using a foreign key.

### SQL Concepts:
- Creating a table with a foreign key.
- Establishing a one-to-many relationship between tables.

## 3. Creating Many-to-Many Relationships [question3.sql](https://github.com/kadijaseidu/Tech4girls_Backend/blob/main/SQL_Assignment/question3.sql).

### Purpose:
This script creates a `Courses` table and an intermediate `User_Courses` table to establish a **many-to-many** relationship between `Users` and `Courses`.

### SQL Concepts:
- Creating an intermediate table to establish a many-to-many relationship.
- Using composite primary keys and foreign keys to link tables.