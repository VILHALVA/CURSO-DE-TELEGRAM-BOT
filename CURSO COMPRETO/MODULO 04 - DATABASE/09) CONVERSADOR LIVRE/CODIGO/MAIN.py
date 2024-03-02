import telebot
import json
import sys
import os
from TOKEN import *

bot = telebot.TeleBot(TOKEN)

def load_responses():
    with open("./WORD.json", "r", encoding="utf-8") as file:
        return json.load(file)
responses = load_responses()

def check_always_respond():
    with open("./CONFIG.json", "r", encoding="utf-8") as file:
        config_data = json.load(file)
        return config_data.get("SEMPRE", "OFF") == "ON"

def should_respond(message):
    if message.chat.type == "private":
        return True
    if check_always_respond():
        return True
    
    criar_enabled = config.get("CRIAR", "OFF") == "ON"
    erro_enabled = config.get("ERRO", "OFF") == "ON"

    if criar_enabled and erro_enabled:
        return True
    return bot.get_me().username.upper() in message.text.upper()

@bot.message_handler(commands=['start'])
def handle_start(message):
    response = "Olá! Eu sou um bot conversador!\n\n" \
               "Você pode me fazer perguntas como:\n" \
               "- Qual é o seu nome?\n" \
               "- Como você está?\n" \
               "- O que você pode fazer?\n" \
               "- Tchau..."
    bot.reply_to(message, response)

def load_config():
    with open("./CONFIG.json", "r", encoding="utf-8") as file:
        return json.load(file)
config = load_config()

def save_response_to_file(word, response):
    word = word.lower()
    response = response.lower()
    try:
        with open("./WORD.json", "r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}
    data[word] = response

    with open("./WORD.json", "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def handle_error_mode(message):
    criar_enabled = config.get("CRIAR", "OFF") == "ON"
    erro_enabled = config.get("ERRO", "OFF") == "ON"

    if criar_enabled and erro_enabled:
        if ':' in message.text:
            word, response = map(str.strip, message.text.split(":", 1))
            save_response_to_file(word, response)
            bot.reply_to(message, "😃NOVA RESPOSTA ADICIONADA COM SUCESSO!")
            print("BOT REINICIADO!")
            bot.stop_polling()
            os.execv(sys.executable, [sys.executable] + sys.argv)
        else:
            bot.reply_to(message, "🤔PARECE QUE ESSA FRASE NÃO ESTÁ NO MEU DATABASE. POR FAVOR, ENVIE A FRASE SEGUINDO ESSE MODELO: 'PALAVRA CHAVE': 'RESPOSTA'")
    elif not criar_enabled and erro_enabled:
        bot.reply_to(message, "🤬INFELIZMENTE NÃO ENTENDO O QUE DIZES!")

@bot.message_handler(func=lambda message: should_respond(message))
def handle_message(message):
    input_text = message.text.lower()
    input_text = input_text.replace(f"@{bot.get_me().username}", "", 1).strip()
    
    keyword_found = False
    for keyword, response in responses.items():
        if keyword in input_text:
            bot.reply_to(message, response)
            keyword_found = True
            break
    if keyword_found:
        return
        
    response = responses.get(input_text, "🥵DESCULPE, NÃO ENTENDI. TENTE OUTRA PERGUNTA!")
    if response == "🥵DESCULPE, NÃO ENTENDI. TENTE OUTRA PERGUNTA!":
        handle_error_mode(message)
    else:
        bot.reply_to(message, response)

if __name__ == '__main__':
    print("BOT EM EXECUÇÃO!")
    bot.infinity_polling(timeout=60)
    print("FIM")