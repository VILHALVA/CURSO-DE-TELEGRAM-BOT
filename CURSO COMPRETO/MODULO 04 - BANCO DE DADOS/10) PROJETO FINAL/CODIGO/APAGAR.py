def delete_media(chat_id):
    from DB_CONNECTION import db_connection
    from MAIN import bot
    
    cursor = db_connection.cursor()
    cursor.execute("SELECT filename FROM media")
    filenames = [row[0] for row in cursor.fetchall()]
    
    from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
    
    markup = InlineKeyboardMarkup(row_width=1)
    for filename in filenames:
        callback_data = f"delete_{filename}" 
        markup.add(InlineKeyboardButton(filename, callback_data=callback_data))
    bot.send_message(chat_id, "Escolha um arquivo para apagar:", reply_markup=markup)

def delete_media_record(filename, chat_id, bot):
    from DB_CONNECTION import db_connection
    import os

    script_dir = os.path.dirname(os.path.abspath(__file__))
    cursor = db_connection.cursor()
    cursor.execute("SELECT directory, file_ext FROM media WHERE filename = %s", (filename,))
    media_record = cursor.fetchone()

    if media_record:
        directory, file_ext = media_record
        file_path = os.path.join(script_dir, directory, f"{filename}.{file_ext}")
        try:
            os.remove(file_path)
            cursor.execute("DELETE FROM media WHERE filename = %s", (filename,))
            db_connection.commit()
            bot.send_message(chat_id, f"Arquivo '{filename}.{file_ext}' foi apagado.")
        except FileNotFoundError:
            print("Arquivo não encontrado.")
    else:
        print("Arquivo não encontrado no banco de dados.")
