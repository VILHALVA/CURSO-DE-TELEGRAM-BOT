def get_media_list():
    from DB_CONNECTION import db_connection
    
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM media")
    media_list = cursor.fetchall()
    cursor.close()
    return media_list

def display_media(chat_id):
    from DB_CONNECTION import db_connection
    from MAIN import bot
    import telebot
    
    cursor = db_connection.cursor()
    cursor.execute("SELECT filename FROM media")
    media_records = cursor.fetchall()
    
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    for media in media_records:
        filename = media[0]
        button = telebot.types.InlineKeyboardButton(filename, callback_data=f"send_media_{filename}")
        markup.add(button)
    
    bot.send_message(chat_id, "Escolha uma mídia para visualizar:", reply_markup=markup)

def send_media(chat_id, filename):  
    import os
    from DB_CONNECTION import db_connection
    from MAIN import bot
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    cursor = db_connection.cursor()
    cursor.execute("SELECT directory, file_ext FROM media WHERE filename = %s", (filename,))
    media_record = cursor.fetchone()
    if media_record:
        directory, file_ext = media_record
        file_path = os.path.join(script_dir, directory, f"{filename}.{file_ext}")
        try:
            with open(file_path, 'rb') as file:
                bot.send_photo(chat_id, file)  
        except FileNotFoundError:
            bot.send_message(chat_id, "EXCEPT: Arquivo não encontrado.")
    else:
        bot.send_message(chat_id, "MEDIA: Arquivo não encontrado.")
