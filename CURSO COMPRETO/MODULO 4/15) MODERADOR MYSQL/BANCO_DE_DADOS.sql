CREATE DATABASE IF NOT EXISTS nome_do_banco;

USE nome_do_banco;

CREATE TABLE IF NOT EXISTS group_settings (
    group_id BIGINT PRIMARY KEY,
    admin_id BIGINT,
    action ENUM('ban', 'kick', 'mute', 'delete') DEFAULT 'delete'
);
