import sys
import telebot
import time

time.sleep(300)

TOKEN = open('utils/token.conf', 'r').read().strip()

bot = telebot.TeleBot(TOKEN)

try:
    bot.decline_chat_join_request(sys.argv[1], sys.argv[2])
except:
    pass
try:
    bot.delete_message(sys.argv[2], sys.argv[3])
except:
    pass
