import telebot
import os

TOKEN = "TOKEN_AQUI"
bot = telebot.TeleBot(TOKEN)

def verificar(mensagem):
    return True

@bot.message_handler(func=verificar, commands=["start"])
def responder(mensagem):
    bot.send_message(mensagem.chat.id, "Iai cara! Tá fazendo o quê?")
 
@bot.message_handler(commands=["ola"])   
def ola(mensagem):
    bot.reply_to(mensagem,"Olá! Como vai?")
    
@bot.message_handler(func=verificar, text=["TOP"])
def TOP(mensagem):
    bot.reply_to(mensagem,"É muito top mesmo!")
    
bot.polling()