from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import logging

# Configuração básica de logging para ver possíveis erros
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Função para o comando /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        'Bem-vindo! Este bot pode te ajudar a calcular tanto aumentos quanto descontos percentuais.\n'
        'Por favor, envie o valor original seguido do percentual de aumento ou desconto.\n'
        'EXEMPLO: "100 10" calcula um aumento de 10 porcento em 100'
    )

# Função para lidar com mensagens contendo valores e porcentagens
def calculate_percentage(update: Update, context: CallbackContext) -> None:
    # Obter a mensagem enviada pelo usuário
    message_text = update.message.text

    # Verificar se a mensagem contém um valor e uma porcentagem separados por espaço
    if ' ' in message_text:
        # Dividir a mensagem em valor e porcentagem
        value, percentage = message_text.split(' ', 1)

        try:
            # Converter valor para float
            value = float(value)

            # Remover qualquer caractere não numérico da porcentagem e converter para float
            percentage = float(''.join(filter(str.isdigit, percentage)))

            # Calcular o resultado do aumento ou desconto
            result = value * (1 + percentage / 100)

            # Enviar a resposta ao usuário
            update.message.reply_text(f'O resultado é: {result:.2f}')
        except ValueError:
            update.message.reply_text('Por favor, envie um valor numérico e uma porcentagem válida.')
    else:
        update.message.reply_text('Por favor, envie o valor original seguido do percentual de aumento ou desconto.')

def main() -> None:
    # Criando um Updater que irá receber as atualizações do bot
    updater = Updater("SEU_TOKEN_AQUI")

    # Obtendo o despachante para registrar manipuladores
    dp = updater.dispatcher

    # Registrando os manipuladores de comando
    dp.add_handler(CommandHandler("start", start))

    # Registrando um manipulador de mensagem para calcular a porcentagem
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, calculate_percentage))

    # Iniciando o bot
    updater.start_polling()

    # Executando o bot até que o usuário pressione Ctrl-C
    updater.idle()

if __name__ == '__main__':
    main()
