from datetime import datetime
import telebot
import os

TOKEN = "TOKEN_AQUI"
bot = telebot.TeleBot(TOKEN)

def verificar(mensagem):
    return True

@bot.message_handler(func=verificar, commands=["start"])
def start(mensagem):
    bot.send_message(mensagem.chat.id, "Olá usuário!")

@bot.message_handler(func=verificar)
def sample_responses(input_text):
    user_message = str(input_text).lower()
    if user_message in ("ola", "hi", "oi"):
        return "Iai! Beleza? Como está?"
    elif user_message in ("bem", "otimo", "top"):
        return "Que Bom!"
    elif user_message in ("mal", "mau", "ruim"):
        return "O problema não é meu!"
    elif user_message in ("time", "horas", "dia", "data"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")
        return str(date_time)
    else:
        return "Sinto muito! Não compreendir o que você disse"

def handle_message(update, context):
    text = str(update.message.text).lower()
    response = sample_responses(text)
    update.message.reply_to(response)
    
def error(update, context):
    print(f"Update {update} Causa do error: {context.error}")

bot.polling()