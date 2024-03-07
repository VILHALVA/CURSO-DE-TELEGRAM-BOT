import mysql.connector

# CONEXÃO COM MYSQL:
db_connection = mysql.connector.connect(
    host="seu_host",
    user="seu_usuario",
    password="sua_senha",
    database="UPLOAD"
)