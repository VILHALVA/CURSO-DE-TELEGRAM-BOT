-- Comando para criar o banco de dados SQLite
CREATE DATABASE IF NOT EXISTS bot_database;

-- Comando para usar o banco de dados
USE bot_database;

-- Comando para criar a tabela "users"
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    chat_id INTEGER,
    group_info TEXT
);
