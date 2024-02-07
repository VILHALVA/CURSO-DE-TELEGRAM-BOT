import telebot
import time
import sqlite3

# Configure o seu token do bot aqui
TOKEN = 'SEU_TOKEN_AQUI'

# Inicialize o bot
bot = telebot.TeleBot(TOKEN)

# Inicialize o banco de dados SQLite
conn = sqlite3.connect('members.db')
cursor = conn.cursor()

# Crie uma tabela para armazenar os membros que adicionaram 20 contatos
cursor.execute('''
    CREATE TABLE IF NOT EXISTS members (
        user_id INTEGER PRIMARY KEY,
        added_contacts INTEGER
    )
''')
conn.commit()

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_id = message.from_user.id

    # Verifique se o usuário já adicionou 20 contatos
    cursor.execute('SELECT * FROM members WHERE user_id = ?', (user_id,))
    member = cursor.fetchone()

    if member:
        # O usuário já adicionou 20 contatos, permita a mensagem
        bot.send_message(message.chat.id, message.text)
    else:
        # O usuário não adicionou 20 contatos
        # Aplique a punição e envie uma mensagem de advertência
        bot.delete_message(message.chat.id, message.message_id)
        bot.restrict_chat_member(message.chat.id, user_id, until_date=int(time.time()) + 300)
        bot.send_message(message.chat.id, f"PARA VOCÊ PARTICIPAR ADICIONE 20 PESSOAS DOS SEUS CONTATOS A ESTE GRUPO")

# Comando para adicionar contatos
@bot.message_handler(commands=['adicionar_contatos'])
def add_contacts(message):
    user_id = message.from_user.id

    # Verifique se o usuário já está registrado na tabela
    cursor.execute('SELECT * FROM members WHERE user_id = ?', (user_id,))
    member = cursor.fetchone()

    if member:
        # Atualize o número de contatos adicionados pelo usuário
        cursor.execute('UPDATE members SET added_contacts = ? WHERE user_id = ?', (member[1] + 20, user_id,))
    else:
        # Insira o usuário na tabela com 20 contatos
        cursor.execute('INSERT INTO members (user_id, added_contacts) VALUES (?, ?)', (user_id, 20))

    conn.commit()
    bot.send_message(message.chat.id, "Você adicionou 20 contatos com sucesso!")

if __name__ == '__main__':
    bot.polling()
