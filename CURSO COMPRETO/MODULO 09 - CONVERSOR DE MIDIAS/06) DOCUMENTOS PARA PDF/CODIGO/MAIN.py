from TOKEN import *
import os
from telegram.ext import Updater, MessageHandler, Filters

# Função para converter documentos em PDF
def convert_document_to_pdf(update, context):
    document_file = update.message.document.get_file()
    document_file_path = document_file.download('input_document')

    # Converter documento para PDF usando LibreOffice
    output_pdf_path = 'output_document.pdf'
    os.system(f'libreoffice --headless --convert-to pdf --outdir . {document_file_path}')

    # Enviar o PDF convertido
    context.bot.send_document(chat_id=update.effective_chat.id, document=open(output_pdf_path, 'rb'))

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.document & ~Filters.command, convert_document_to_pdf))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
