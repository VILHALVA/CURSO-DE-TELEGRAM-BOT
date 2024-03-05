CREATE DATABASE IF NOT EXISTS moderacao;

USE moderacao;

CREATE TABLE group_punishments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    group_id BIGINT NOT NULL,
    punishment VARCHAR(50) NOT NULL,
    UNIQUE KEY unique_group_id (group_id)
);

