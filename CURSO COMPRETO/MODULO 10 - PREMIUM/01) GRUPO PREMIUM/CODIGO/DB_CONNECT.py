import sqlite3

conn = sqlite3.connect('members.db')

# Inicialize o banco de dados SQLite
cursor = conn.cursor()

# Crie uma tabela para armazenar os membros que adicionaram 20 contatos
cursor.execute('''
    CREATE TABLE IF NOT EXISTS members (
        user_id INTEGER PRIMARY KEY,
        added_contacts INTEGER
    )
''')
conn.commit()