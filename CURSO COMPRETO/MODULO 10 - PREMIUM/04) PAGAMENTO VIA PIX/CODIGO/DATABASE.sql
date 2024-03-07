CREATE DATABASE IF NOT EXISTS pagamento_pix;
USE pagamento_pix;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT UNIQUE
);
