CREATE DATABASE IF NOT EXISTS bloqueio_midias;

USE bloqueio_midias;

CREATE TABLE group_punishments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    group_id INT NOT NULL,
    photo VARCHAR(20) NOT NULL,
    video VARCHAR(20) NOT NULL,
    gif VARCHAR(20) NOT NULL,
    audio VARCHAR(20) NOT NULL,
    UNIQUE KEY (group_id),
    FOREIGN KEY (group_id) REFERENCES your_group_table(id) ON DELETE CASCADE
);


