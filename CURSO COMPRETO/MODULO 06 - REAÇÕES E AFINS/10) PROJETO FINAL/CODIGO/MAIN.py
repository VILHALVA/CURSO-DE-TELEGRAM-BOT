from telegram.ext import Updater,CommandHandler,CallbackContext,MessageHandler,Filters,CallbackQueryHandler
from telegram import Update,ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardMarkup,InlineKeyboardButton
import os
from LIKE_DB import LikeDB
from TOKEN import*

TOKEN = os.environ[TOKEN]

like_db = LikeDB('likes.json')
def start(update: Update,context: CallbackContext):
    bot = context.bot
    bot.send_message(chat_id='@image_like',text="Hello World")
    update.message.reply_text("Hello World")

def sendImage(update: Update,context: CallbackContext):
    bot = context.bot
    # Get image id from update
    image_id = update.message.photo[-1].file_id
    # Add image to database
    like_db.addImage(image_id)
    # Create inline keyboard
    like_emoji = u'\U0001F44D'
    dislike_emoji = u'\U0001F44E'
    keyboard = InlineKeyboardMarkup([[
        InlineKeyboardButton(like_emoji,callback_data='like'),
        InlineKeyboardButton(dislike_emoji,callback_data='dislike')
        ]])
    bot.send_photo(
        chat_id='@image_like',
        photo=image_id,
        caption="Hello World",
        reply_markup=keyboard)

    update.message.reply_text("Image has been sent to @image_like")

updater = Updater(token=TOKEN)

updater.dispatcher.add_handler(CommandHandler('start',start))
updater.dispatcher.add_handler(MessageHandler(Filters.photo,sendImage))

updater.start_polling()
updater.idle()
