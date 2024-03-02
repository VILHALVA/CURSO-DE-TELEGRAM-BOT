import telebot

TOKEN = 'TOKEN_DO-BOT'
CHAT_ID = 'ID_DO-CHAT'

bot = telebot.TeleBot(TOKEN)

ret_msg = bot.send_voice(CHAT_ID, open('./AUDIO/audio.ogg', 'rb'))

file_info = bot.get_file(ret_msg.voice.file_id)

downloaded_file = bot.download_file(file_info.file_path)

with open('audio.ogg', 'wb') as new_file:
    new_file.write(downloaded_file)