CREATE DATABASE IF NOT EXISTS aprovacao;
USE aprovacao;

CREATE TABLE IF NOT EXISTS approved_users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT UNIQUE
);
