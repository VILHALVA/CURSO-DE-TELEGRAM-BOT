import sqlite3
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackContext

# Defina os estados da conversa
NAME, AGE = range(2)

# Função para iniciar a entrevista
def start(update: Update, context: CallbackContext) -> int:
    update.message.reply_text("Olá! Vou fazer algumas perguntas. Qual é o seu nome?")
    return NAME

# Função para obter o nome do membro
def get_name(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    context.user_data['name'] = update.message.text
    update.message.reply_text(f"Ótimo, {context.user_data['name']}! Agora, qual é a sua idade?")
    return AGE

# Função para obter a idade do membro
def get_age(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    context.user_data['age'] = update.message.text

    # Salve os dados no banco de dados SQLite
    conn = sqlite3.connect('entrevista')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS entrevistas (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, age TEXT)")
    cursor.execute("INSERT INTO entrevistas (name, age) VALUES (?, ?)", (context.user_data['name'], context.user_data['age']))
    conn.commit()
    conn.close()

    update.message.reply_text(f"Ótimo, você tem {context.user_data['age']} anos! Entrevista concluída.")
    return ConversationHandler.END

# Função para cancelar a entrevista
def cancel(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    update.message.reply_text("Entrevista cancelada. Você pode reiniciar a entrevista a qualquer momento com /start.")
    return ConversationHandler.END

# Função principal para iniciar o bot
def main():
    updater = Updater(token='5774876922:AAHhVE8ljltOuKD6dn0T0ZB-dah3b_akK8U', use_context=True)
    dp = updater.dispatcher

    # Crie uma instância de ConversationHandler com os estados e gatilhos
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            NAME: [MessageHandler(Filters.text & ~Filters.command, get_name)],
            AGE: [MessageHandler(Filters.text & ~Filters.command, get_age)],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    dp.add_handler(conv_handler)
    
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
