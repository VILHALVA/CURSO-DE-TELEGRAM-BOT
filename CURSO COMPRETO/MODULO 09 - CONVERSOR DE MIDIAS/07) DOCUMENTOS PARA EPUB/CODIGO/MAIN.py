from TOKEN import *
import os
from telegram.ext import Updater, MessageHandler, Filters
from ebooklib import epub

# Função para converter documentos em EPUB
def convert_document_to_epub(update, context):
    document_file = update.message.document.get_file()
    document_file_path = document_file.download('input_document')

    # Converter documento para EPUB
    output_epub_path = 'output_document.epub'
    book = epub.EpubBook()

    # Adicionar arquivo do documento ao EPUB
    book.set_identifier('document_conversion')
    book.set_title('Converted Document')
    book.set_language('en')

    with open(document_file_path, 'rb') as f:
        contents = f.read()

    # Adicionar conteúdo do documento ao EPUB
    chapter = epub.EpubHtml(title='Converted Document', file_name='document.xhtml', lang='en')
    chapter.content = contents
    book.add_item(chapter)
    book.toc = (epub.Link('document.xhtml', 'Converted Document', 'converted_document'), )
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())
    style = 'body { font-family: Times, Times New Roman, serif; }'
    nav_css = epub.EpubItem(uid="style_nav", file_name="style/nav.css", media_type="text/css", content=style)
    book.add_item(nav_css)
    book.spine = ['nav', chapter]

    # Salvar o EPUB
    epub.write_epub(output_epub_path, book, {})

    # Enviar o EPUB convertido
    context.bot.send_document(chat_id=update.effective_chat.id, document=open(output_epub_path, 'rb'))

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.document & ~Filters.command, convert_document_to_epub))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
