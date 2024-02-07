-- Comando para criar o banco de dados SQLite
CREATE DATABASE IF NOT EXISTS bot_database;

-- Comando para usar o banco de dados
USE bot_database;

-- Crie uma tabela para armazenar os usuários
CREATE TABLE usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    idade INTEGER
);

-- Insira 10 registros de exemplo
INSERT INTO usuarios (nome, idade) VALUES ('Alice', 30);
INSERT INTO usuarios (nome, idade) VALUES ('Bob', 25);
-- Adicione mais registros de exemplo conforme necessário
