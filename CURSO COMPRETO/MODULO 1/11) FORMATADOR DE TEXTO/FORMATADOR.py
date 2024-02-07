import telebot
from telebot import types
import re

TOKEN = "SEU_TOKEN_AQUI"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    instructions = '''
Bem-vindo ao FormatBot! ✨

Este bot permite que você formate seu texto de maneiras criativas. 
Aqui estão algumas das formatações disponíveis:

*grassetto* - **grassetto**
_corsivo_ - _corsivo_
`code` - `code`
[Google](https://www.google.com) - [Google](https://www.google.com/)
%blu% - 🇧 🇱 🇺
-barrato- - ~~barrato~~
;sottolineato; - sottolineato
^grande^ - ｇｒａｎｄｅ
&maiuscoletto& - ᴍᴀɪᴜsᴄᴏʟᴇᴛᴛᴏ
@bolle@ - ⒷⓄⓁⓁⒺ

Envie a mensagem que você deseja formatar e veja a mágica acontecer!
'''
    bot.send_message(message.chat.id, instructions, parse_mode='Markdown')

@bot.message_handler(func=lambda message: True)
def format_text(message):
    text = message.text

    # Formatação do texto
    formatted_text = text
    formatted_text = re.sub(r'\*(.*?)\*', r'*\1*', formatted_text)
    formatted_text = re.sub(r'_(.*?)_', r'_\1_', formatted_text)
    formatted_text = re.sub(r'`(.*?)`', r'`\1`', formatted_text)
    formatted_text = re.sub(r'\[(.*?)\]\((.*?)\)', r'[\1](\2)', formatted_text)
    formatted_text = re.sub(r'-(.*?)-', r'~~\1~~', formatted_text)
    formatted_text = re.sub(r';(.*?);', r's̲\1', formatted_text)
    formatted_text = re.sub(r'\^(.*?)\^', r'ｇｒａｎｄｅ', formatted_text)
    formatted_text = re.sub(r'&([^&]*)&', r'ᴍᴀɪᴜsᴄᴏʟᴇᴛᴛᴏ', formatted_text)
    formatted_text = re.sub(r'@([^@]*)@', r'ⒷⓄⓁⓁⒺ', formatted_text)
    formatted_text = re.sub(r'%([^%]*)%', r'*\1*', formatted_text)

    bot.send_message(message.chat.id, formatted_text, parse_mode='Markdown')

bot.polling()
