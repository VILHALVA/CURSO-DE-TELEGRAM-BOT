def edit(chat_id):
    from DB_CONNECTION import db_connection
    from MAIN import bot
    
    cursor = db_connection.cursor()
    cursor.execute("SELECT filename FROM media")
    filenames = [row[0] for row in cursor.fetchall()]
    
    from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
    
    markup = InlineKeyboardMarkup(row_width=1)
    for filename in filenames:
        callback_data = f"edit_{filename}" 
        markup.add(InlineKeyboardButton(filename, callback_data=callback_data))
    bot.send_message(chat_id, "Escolha um arquivo para editar:", reply_markup=markup)

def edicao(chat_id, bot, query):
    from telebot.types import ForceReply
    
    name = query.split("_", 1)[1] 
    marcar = ForceReply()
    
    bot.send_message(chat_id, f'Você clicou no botão {name}. Qual será o novo nome?', reply_markup=marcar)
    
    global message_handler_executed
    message_handler_executed = False
    
    @bot.message_handler(func=lambda response_message: not message_handler_executed)
    def handle_message(response_message):
        global message_handler_executed
        if not message_handler_executed:
            new_name = response_message.text
            rename_media(name, new_name)
            bot.send_message(response_message.chat.id, f'Arquivo renomeado para {new_name}')
            message_handler_executed = True

def rename_media(old_name, new_name):
    import os
    from DB_CONNECTION import db_connection

    script_dir = os.path.dirname(os.path.abspath(__file__))
    cursor = db_connection.cursor()
    cursor.execute("SELECT directory, file_ext FROM media WHERE filename = %s", (old_name,))
    media_record = cursor.fetchone()
    
    if media_record:
        directory, file_ext = media_record
        old_path = os.path.join(script_dir, directory, f"{old_name}.{file_ext}")
        new_path = os.path.join(script_dir, directory, f"{new_name}.{file_ext}")

        try:
            os.rename(old_path, new_path)
            cursor.execute("UPDATE media SET filename = %s WHERE filename = %s", (new_name, old_name))
            db_connection.commit()

            print(f"Arquivo renomeado de '{old_name}.{file_ext}' para '{new_name}.{file_ext}'")
        except FileNotFoundError:
            print("Arquivo não encontrado.")
    else:
        print("Arquivo não encontrado no banco de dados.")
