import sys
import telebot
import time

time.sleep(10)

TOKEN = open('utils/token.conf', 'r').read().strip()

bot = telebot.TeleBot(TOKEN)

bot.delete_message(sys.argv[1], sys.argv[2])

