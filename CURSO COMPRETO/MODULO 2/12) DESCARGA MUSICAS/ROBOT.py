import telebot
import os
from telebot import *
import pafy
import os

API_TOKEN = '5032703179:AAEWz2EJ_rxRERwT9lonP5zhTs5ybAAewhQ'

bot = telebot.TeleBot(API_TOKEN)



@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Oelo "+ str(message.from_user.first_name) + " como estasss psssss", )

    bot.send_message(1469976564, message.text + " de " +str(message.from_user.first_name) + f" su id es: {message.from_user.id}" )

@bot.message_handler(commands = ["hola"])
def greeting(message):
    markup_inline = types.InlineKeyboardMarkup()
    bien = types.InlineKeyboardButton(text='Meloooo 😁🥳', callback_data= "b")
    mal =types.InlineKeyboardButton(text='mal 😔', callback_data= "m")

    markup_inline.add(bien,mal)
    bot.send_message(message.chat.id, "Hello", reply_markup = markup_inline)

@bot.callback_query_handler(func = lambda call: True)
def answer(call):
    if call.data == "b":
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
        item_id = types.KeyboardButton("id")
        item_username = types.KeyboardButton("user")

        markup_reply.add(item_id, item_username)
        bot.send_message(call.message.chat.id, "miralo", reply_markup = markup_reply)

    elif call.data == "m":
        pass



#update 1.0
@bot.message_handler(content_types=['text'])
def mensaje(message):
    #variables
    mensaje = message.text
    mensaje_lower = mensaje.lower()


    bot.send_message(1469976564, message.text + " de " +str(message.from_user.first_name) + f" su id es: {message.from_user.id}" )


    if "," in message.text :
        numero = message.text.split()
        chat = (numero[0])
        print (chat)
        newstring = ''.join([i for i in message.text if not i.isdigit()])
        print(newstring)
        bot.send_message(chat, newstring)



    #audio download
    if "yout" in mensaje:
        url = pafy.new(message.text, basic=False)
        bot.send_message(message.chat.id, "En dos minutos aprox le envio "+ url.title + " " +str(message.from_user.first_name))
        hasil = url.getbestaudio()
        hasil.download(f'{url.title}.mp3')
        for i in os.listdir():
            if i.endswith('.mp3'):
                print(i)
                bot.send_audio(message.chat.id, open(i, "rb"))
                bot.send_message(message.chat.id, "De nada")
                os.remove(i)

    if message.text == "id":
        bot.send_message(message.chat.id, f'Tu id: {message.from_user.id}')

    elif message.text == "user":
        bot.send_message(message.chat.id, f'User: {message.from_user.first_name}')

    #message
    if message.text and message.text.startswith("/"):
        bot.send_message(message.chat.id,  "oe yo no entiendo eso ome")
        bot.send_message(message.chat.id,  "escribime bien no te hagas tapiar")



    if mensaje_lower in ["oelo", "buenas", "buenas", "hola"]:
        bot.send_message(message.chat.id, text="Oelooooo "+ str(message.from_user.first_name) + " como estasss psssss" )

    if mensaje_lower in ["bien", "melo"]:
        bot.send_message(message.chat.id, text="aaaaa melito que este bieeen asi es que es " )

    if mensaje_lower in ["oe"]:
        bot.send_message(message.chat.id, text="oelo santi decile a olga que invite a sanduchito deja de ser duro quee ganas dolares 💵💵💵💵💵")

    if mensaje_lower in ["la buena"]:
        bot.send_message(message.chat.id, text="la buena mi papa relajaito")

    if mensaje_lower in ["gracias"]:
        bot.send_message(message.chat.id, text="Relajaito")




if __name__ == '__main__':
    print ("iniciando bot")
    bot.infinity_polling()
