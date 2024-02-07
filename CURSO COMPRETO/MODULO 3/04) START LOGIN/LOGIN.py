import logging
import sqlite3
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackContext

# Configure logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Define states for conversation
USER_ID, GROUP_INFO = range(2)

# SQLite database initialization
conn = sqlite3.connect('bot_database.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        chat_id INTEGER,
        group_info TEXT
    )
''')
conn.commit()

# Define a callback function for the /start command
def start(update: Update, context: CallbackContext) -> int:
    user = update.effective_user
    chat_id = update.effective_chat.id
    user_id = user.id
    user_name = user.username
    welcome_message = f"Olá, {user_name}! Bem-vindo ao bot de boas-vindas."

    # Check if the user has a username
    if user_name:
        welcome_message += f"\nSeu nome de usuário: @{user_name}"

    update.message.reply_text(welcome_message)

    # Save user ID and chat ID in the database
    cursor.execute('INSERT OR REPLACE INTO users (user_id, chat_id) VALUES (?, ?)', (user_id, chat_id))
    conn.commit()

    return USER_ID

# Define a callback function to handle group information
def group_info(update: Update, context: CallbackContext) -> int:
    chat_id = update.effective_chat.id
    group_info = f"{chat_id}: {update.effective_chat.title}"

    # Save group information in the database
    cursor.execute('UPDATE users SET group_info = ? WHERE chat_id = ?', (group_info, chat_id))
    conn.commit()

    update.message.reply_text(f"Grupo {update.effective_chat.title} registrado. Obrigado!")

    return ConversationHandler.END

# Define a function to cancel the conversation
def cancel(update: Update, context: CallbackContext) -> int:
    update.message.reply_text("Conversa cancelada.")
    return ConversationHandler.END

# Define the main function to run the bot
def main() -> None:
    # Set your bot token here
    bot_token = 'YOUR_BOT_TOKEN'
    updater = Updater(token=bot_token, use_context=True)

    dispatcher = updater.dispatcher

    # Create a conversation handler
    conversation_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            USER_ID: [MessageHandler(Filters.text & ~Filters.command, group_info)],
            GROUP_INFO: [MessageHandler(Filters.text & ~Filters.command, group_info)]
        },
        fallbacks=[CommandHandler('cancel', cancel)]
    )

    dispatcher.add_handler(conversation_handler)

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
