import mysql.connector

# Configurações do MySQL
MYSQL_HOST = 'seu_host_mysql'
MYSQL_USER = 'seu_usuario_mysql'
MYSQL_PASSWORD = 'sua_senha_mysql'
MYSQL_DATABASE = 'pagamento_pix'

# Conecta ao banco de dados MySQL
try:
    mysql_conn = mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DATABASE
    )
    cursor = mysql_conn.cursor()
except mysql.connector.Error as err:
    print("Erro ao conectar ao MySQL:", err)