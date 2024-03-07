import mysql.connector

db_connection = mysql.connector.connect(
    host="seu_host",
    user="seu_user",
    password="sua_senha",
    database="moderacao"
)