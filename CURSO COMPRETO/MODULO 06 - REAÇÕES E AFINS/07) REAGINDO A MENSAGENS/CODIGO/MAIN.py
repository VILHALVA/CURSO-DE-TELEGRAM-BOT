from telebot import TeleBot
from TOKEN import *

bot = TeleBot(TOKEN)

# Função para responder a mensagens
@bot.message_handler(func=lambda mensagem: True)
def responder(mensagem):
    # Definir uma reação de coração na mensagem
    reaction = [{"type": "heart"}]  # Reação de coração
    bot.set_message_reaction(mensagem.chat.id, mensagem.message_id, reaction)

# Iniciar o bot
bot.polling()
