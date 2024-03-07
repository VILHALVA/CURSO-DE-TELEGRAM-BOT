CREATE DATABASE IF NOT EXISTS assinatura;
USE assinatura;

CREATE TABLE IF NOT EXISTS subscriptions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT UNIQUE,
    expiration_date DATETIME
);
