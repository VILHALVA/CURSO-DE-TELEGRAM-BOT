from TOKEN import *
import os
from io import BytesIO
from telegram.ext import Updater, MessageHandler, Filters, CallbackQueryHandler
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from PIL import Image
from gtts import gTTS
from moviepy.editor import VideoFileClip
from ebooklib import epub
from google.cloud import speech
from google.cloud import translate_v2 as translate

# Configurar as credenciais do Google Cloud
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "caminho/para/seu/arquivo-de-credenciais.json"

# Função para converter foto para diferentes formatos
def convert_photo(update, context):
    reply_markup = InlineKeyboardMarkup([
        [InlineKeyboardButton("PNG", callback_data="png"),
         InlineKeyboardButton("ICO", callback_data="ico"),
         InlineKeyboardButton("JPEG", callback_data="jpeg"),
         InlineKeyboardButton("JPG", callback_data="jpg")]
    ])
    update.message.reply_text("Escolha o formato para converter a foto:", reply_markup=reply_markup)

# Função para converter áudio para diferentes formatos
def convert_audio(update, context):
    reply_markup = InlineKeyboardMarkup([
        [InlineKeyboardButton("MP3", callback_data="mp3"),
         InlineKeyboardButton("M4A", callback_data="m4a"),
         InlineKeyboardButton("Para Texto", callback_data="texto")]
    ])
    update.message.reply_text("Escolha o formato para converter o áudio:", reply_markup=reply_markup)

# Função para converter vídeo para diferentes formatos
def convert_video(update, context):
    reply_markup = InlineKeyboardMarkup([
        [InlineKeyboardButton("MP4", callback_data="mp4"),
         InlineKeyboardButton("MP3", callback_data="mp3")]
    ])
    update.message.reply_text("Escolha o formato para converter o vídeo:", reply_markup=reply_markup)

# Função para converter documento para diferentes formatos
def convert_document(update, context):
    reply_markup = InlineKeyboardMarkup([
        [InlineKeyboardButton("PDF", callback_data="pdf"),
         InlineKeyboardButton("EPUB", callback_data="epub")]
    ])
    update.message.reply_text("Escolha o formato para converter o documento:", reply_markup=reply_markup)

# Função para converter texto para áudio MP3
def convert_text_to_audio(update, context):
    text = update.message.text
    tts = gTTS(text=text, lang='pt-br')  # 'pt-br' para português brasileiro, você pode alterar conforme necessário
    bio = BytesIO()
    tts.write_to_fp(bio)
    bio.seek(0)
    context.bot.send_audio(chat_id=update.effective_chat.id, audio=bio)

# Função para lidar com a seleção de formato
def handle_format_selection(update, context):
    query = update.callback_query
    query.answer()
    convert_format = query.data

    if query.message.photo:
        photo_file = query.message.photo[-1].get_file()
        photo_file_path = photo_file.download('input_photo.jpg') # Salvando a foto localmente

        if convert_format == "png":
            image = Image.open(photo_file_path)
            image.save('output_photo.png', 'PNG')
            query.message.reply_photo(photo=open('output_photo.png', 'rb'))
        elif convert_format == "ico":
            image = Image.open(photo_file_path)
            image.save('output_photo.ico', 'ICO')
            query.message.reply_document(document=open('output_photo.ico', 'rb'))
        elif convert_format == "jpeg":
            image = Image.open(photo_file_path)
            image.save('output_photo.jpeg', 'JPEG')
            query.message.reply_photo(photo=open('output_photo.jpeg', 'rb'))
        elif convert_format == "jpg":
            image = Image.open(photo_file_path)
            image.save('output_photo.jpg', 'JPEG')
            query.message.reply_photo(photo=open('output_photo.jpg', 'rb'))

    elif query.message.audio:
        audio_file = query.message.audio.get_file()
        audio_file_path = audio_file.download('input_audio.ogg') # Salvando o arquivo de áudio localmente

        if convert_format == "mp3":
            clip = VideoFileClip(audio_file_path)
            clip.audio.write_audiofile('output_audio.mp3')
            query.message.reply_audio(audio=open('output_audio.mp3', 'rb'))
        elif convert_format == "mp4":
            video_file = VideoFileClip(video_file_path)
            video_file.write_videofile('output_video.mp4')
            query.message.reply_video(video=open('output_video.mp4', 'rb'))
        elif convert_format == "texto":
            audio_client = speech.SpeechClient()
            audio_file = open(audio_file_path, "rb")
            audio_content = audio_file.read()
            audio = speech.RecognitionAudio(content=audio_content)
            config = speech.RecognitionConfig(
                encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
                language_code="pt-BR"  # idioma pode ser ajustado conforme necessário
            )
            response = audio_client.recognize(config=config, audio=audio)
            text = ""
            for result in response.results:
                text += result.alternatives[0].transcript
            query.message.reply_text(text)

    elif query.message.video:
        video_file = query.message.video.get_file()
        video_file_path = video_file.download('input_video.mp4') # Salvando o arquivo de vídeo localmente

        if convert_format == "mp4":
            output_mp4_path = 'output_video.mp4'
            # Carregar o arquivo de vídeo
            video = VideoFileClip(video_file_path)
            # Salvar o vídeo no formato MP4
            video.write_videofile(output_mp4_path)
            # Enviar o vídeo convertido de volta ao usuário
            query.message.reply_video(video=open(output_mp4_path, 'rb'))

        elif convert_format == "mp3":
            clip = VideoFileClip(video_file_path)
            clip.audio.write_audiofile('output_audio.mp3')
            query.message.reply_audio(audio=open('output_audio.mp3', 'rb'))

    elif query.message.document:
        document_file = query.message.document.get_file()
        document_file_path = document_file.download('input_document')

        if convert_format == "pdf":
            output_pdf_path = 'output_document.pdf'
            os.system(f'libreoffice --headless --convert-to pdf --outdir . {document_file_path}')
            query.message.reply_document(document=open(output_pdf_path, 'rb'))
        elif convert_format == "epub":
            output_epub_path = 'output_document.epub'
            book = epub.EpubBook()

            # Configurar metadados do livro EPUB
            book.set_identifier('document_conversion')
            book.set_title('Converted Document')
            book.set_language('pt')  # Defina o idioma conforme necessário

            # Adicionar conteúdo do documento ao EPUB
            with open(document_file_path, 'rb') as f:
                content = f.read()
            chapter = epub.EpubHtml(title='Converted Document', file_name='document.xhtml', lang='pt')
            chapter.content = content
            book.add_item(chapter)
            book.toc = (epub.Link('document.xhtml', 'Converted Document', 'converted_document'),)
            book.add_item(epub.EpubNcx())
            book.add_item(epub.EpubNav())
            book.spine = ['nav', chapter]

            # Salvar o EPUB
            epub.write_epub(output_epub_path, book, {})
            query.message.reply_document(document=open(output_epub_path, 'rb'))

# Função principal
def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.photo, convert_photo))
    dp.add_handler(MessageHandler(Filters.audio, convert_audio))
    dp.add_handler(MessageHandler(Filters.video, convert_video))
    dp.add_handler(MessageHandler(Filters.document, convert_document))
    dp.add_handler(MessageHandler(Filters.text, convert_text_to_audio))
    dp.add_handler(CallbackQueryHandler(handle_format_selection))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
