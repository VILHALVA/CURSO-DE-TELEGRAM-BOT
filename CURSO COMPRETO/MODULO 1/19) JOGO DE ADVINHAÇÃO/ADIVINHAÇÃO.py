import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import random

TOKEN = "TOKEN_AQUI"

bot = telebot.TeleBot(TOKEN)

# Dicionário para armazenar o estado do jogo para cada usuário
game_states = {}

@bot.message_handler(commands=["start"])
def start_game(message):
    markup = InlineKeyboardMarkup(row_width=5)
    for num in range(1, 11):
        markup.add(InlineKeyboardButton(str(num), callback_data=f"guess {num}"))
    
    bot.reply_to(message, "Bem-vindo ao jogo de adivinhação! Escolha um número de 1 a 10:", reply_markup=markup)
    game_states[message.chat.id] = {"state": "waiting_for_guess", "correct_number": random.randint(1, 10)}

@bot.callback_query_handler(func=lambda call: game_states.get(call.message.chat.id)["state"] == "waiting_for_guess")
def guess_number(call):
    guessed_number = int(call.data.split()[1])
    correct_number = game_states[call.message.chat.id]["correct_number"]
    chat_id = call.message.chat.id
    
    if guessed_number == correct_number:
        bot.send_message(chat_id, "Parabéns! Você adivinhou o número corretamente.")
    else:
        bot.send_message(chat_id, f"Número incorreto. O número correto era {correct_number}.")
    
    bot.edit_message_reply_markup(chat_id, call.message.message_id)
    game_states[chat_id]["state"] = None

if __name__ == '__main__':
    print("BOT EM EXECUÇÃO!")
    bot.infinity_polling()
    print("FIM")
