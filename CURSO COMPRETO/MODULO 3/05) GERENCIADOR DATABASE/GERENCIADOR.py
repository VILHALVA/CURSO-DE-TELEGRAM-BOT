import sqlite3
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Defina o ID do dono do bot
OWNER_ID = 123456789  # Substitua pelo seu ID

# Defina as informações de login do XAMPP
XAMPP_USERNAME = 'seu_usuario_xampp'
XAMPP_PASSWORD = 'sua_senha_xampp'
DATABASE_NAME = 'exemplo.db'

# Função para verificar se o usuário é o dono do bot
def is_owner(update: Update) -> bool:
    return update.message.from_user.id == OWNER_ID

# Função para adicionar um novo usuário ao banco de dados
def add_user(update: Update, context: CallbackContext) -> None:
    if not is_owner(update):
        update.message.reply_text("Você não tem permissão para adicionar usuários.")
        return

    # Extrai o nome e a idade do comando
    try:
        command_parts = update.message.text.split()
        name = command_parts[1]
        age = int(command_parts[2])
    except (IndexError, ValueError):
        update.message.reply_text("Formato incorreto. Use /adduser Nome Idade")
        return

    # Conecta-se ao banco de dados
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    # Insere o novo usuário no banco de dados
    cursor.execute("INSERT INTO usuarios (nome, idade) VALUES (?, ?)", (name, age))
    conn.commit()
    conn.close()

    update.message.reply_text(f"Usuário {name} adicionado com sucesso!")

# Função para listar todos os usuários do banco de dados
def list_users(update: Update, context: CallbackContext) -> None:
    if not is_owner(update):
        update.message.reply_text("Você não tem permissão para listar usuários.")
        return

    # Conecta-se ao banco de dados
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    # Recupera todos os usuários
    cursor.execute("SELECT nome, idade FROM usuarios")
    users = cursor.fetchall()
    conn.close()

    # Formata a lista de usuários
    user_list = "\n".join([f"{name}: {age} anos" for name, age in users])

    update.message.reply_text(f"Lista de Usuários:\n{user_list}")

# Crie o Updater e adicione os manipuladores de comandos
updater = Updater(token='SEU_TOKEN', use_context=True)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('adduser', add_user))
dispatcher.add_handler(CommandHandler('listusers', list_users))

# Inicie o bot
updater.start_polling()
updater.idle()
