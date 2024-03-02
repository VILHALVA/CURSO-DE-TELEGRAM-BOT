import telebot
import logging

TOKEN_DO_SEU_BOT_TELEGRAM = "AQUI_VAI_O_TOKEN_DO_SEU_BOT_TELEGRAM"

bot = telebot.TeleBot(TOKEN_DO_SEU_BOT_TELEGRAM)
telebot.logger.setLevel(logging.INFO)
