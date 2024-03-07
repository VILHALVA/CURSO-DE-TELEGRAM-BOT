from telegram.ext import Updater, CommandHandler
from TOKEN import TOKEN
from API_KEY import API_KEY
from TRANSLATE import*

# Função para lidar com o comando /translate
def translate_text(bot, update):
    # Verifica se foram fornecidos os parâmetros necessários
    if len(update.message.text.split()) < 3:
        update.message.reply_text('Por favor, forneça o idioma de origem e o idioma de destino seguidos do texto para traduzir.')
        return
    
    # Extrai os parâmetros da mensagem do usuário
    source_language = update.message.text.split()[1]
    target_language = update.message.text.split()[2]
    text_to_translate = ' '.join(update.message.text.split()[3:])
    
    # Chama a API do Google Cloud Translate para traduzir o texto
    try:
        translation = translate_client.translate(text_to_translate, source_language=source_language, target_language=target_language)
        
        # Envia a tradução de volta para o usuário
        update.message.reply_text(translation['translatedText'])
    except Exception as e:
        update.message.reply_text('Ocorreu um erro ao processar sua solicitação.')

def main():
    # Cria um Updater para receber atualizações do Telegram
    updater = Updater(TOKEN, use_context=True)

    # Obtém o despachante para registrar manipuladores de comando
    dp = updater.dispatcher

    # Registra um manipulador de comando para o comando /translate
    dp.add_handler(CommandHandler("translate", translate_text))

    # Inicia o bot
    updater.start_polling()

    # Aguarda o bot receber comandos
    updater.idle()

if __name__ == '__main__':
    main()
