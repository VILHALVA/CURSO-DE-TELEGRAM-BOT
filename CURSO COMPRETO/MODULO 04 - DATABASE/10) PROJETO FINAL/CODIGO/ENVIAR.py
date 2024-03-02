SAVE_DIR = "./MIDIAS"

def process_send_media(message):
    from MAIN import bot
    from datetime import datetime
    import os
    
    try:
        content_type = message.content_type
        file_id = (message.document.file_id if content_type == "document" else
                   message.audio.file_id if content_type == "audio" else
                   message.video.file_id if content_type == "video" else
                   message.photo[-1].file_id)
        file_info = bot.get_file(file_id)
        file_ext = file_info.file_path.split(".")[-1]
        filename = message.caption if message.caption else f"{content_type}_{datetime.now().strftime('%Y%m%d%H%M%S')}"
        
        save_path = os.path.join(SAVE_DIR, f"{filename}.{file_ext}")
        downloaded_file = bot.download_file(file_info.file_path)
        with open(save_path, "wb") as file:
            file.write(downloaded_file)
        bot.reply_to(message, f"Arquivo {content_type} salvo com sucesso!")
        add_media_to_database(filename, SAVE_DIR, file_ext)
    except Exception as e:
        bot.reply_to(message, f"Ocorreu um erro ao salvar o arquivo: {str(e)}")

def add_media_to_database(filename, directory, file_ext):
    from DB_CONNECTION import db_connection
    
    cursor = db_connection.cursor()
    cursor.execute("INSERT INTO media (filename, directory, file_ext) VALUES (%s, %s, %s)", (filename, directory, file_ext))
    db_connection.commit()
    cursor.close()

