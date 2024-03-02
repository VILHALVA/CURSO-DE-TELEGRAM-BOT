import telebot
from CONVERSA import ConversationHandler

TOKEN = "SEU_TOKEN"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def handle_start(message):
    response = "Olá! Eu sou um bot conversador!\n\n" \
               "Você pode me fazer perguntas como:\n" \
               "- Qual é o seu nome?\n" \
               "- Como você está?\n" \
               "- O que você pode fazer?\n" \
               "- Tchau..."
    bot.reply_to(message, response)
    
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    input_text = message.text   
    response = ConversationHandler.generate_response(input_text)
    bot.reply_to(message, response)

bot.polling()
