CREATE DATABASE IF NOT EXISTS members_database;
USE members_database;

CREATE TABLE IF NOT EXISTS members (
    user_id INT PRIMARY KEY,
    added_contacts INT
);
