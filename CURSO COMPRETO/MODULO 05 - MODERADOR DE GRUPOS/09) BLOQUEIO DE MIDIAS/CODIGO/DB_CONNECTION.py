import mysql.connector

db_connection = mysql.connector.connect(
    host="seu_host",
    user="seu_usuario",
    password="sua_senha",
    database="bloqueio_midias"
)