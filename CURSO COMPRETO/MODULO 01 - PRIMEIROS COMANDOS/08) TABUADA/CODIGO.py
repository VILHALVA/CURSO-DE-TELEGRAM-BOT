from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

def start(update: Update, context: CallbackContext) -> None:
    mensagem = ("Olá! Eu sou o Bot de Tabuada.\n"
                "Eu posso te ajudar a calcular a tabuada de um número.\n"
                "Aqui estão os comandos disponíveis:\n"
                "/start - Exibe esta mensagem de ajuda\n"
                "/tbm <número> - Mostra a tabuada de multiplicação\n"
                "/tbd <número> - Mostra a tabuada de divisão\n"
                "/tba <número> - Mostra a tabuada de adição\n"
                "/tbs <número> - Mostra a tabuada de subtração\n"
                "Para usar, envie o comando desejado seguido do número. Por exemplo: /tbm 5")
    update.message.reply_text(mensagem)

def tabuada_multiplicacao(update: Update, context: CallbackContext) -> None:
    try:
        numero = int(context.args[0])
        mensagem = f"Tabuada de multiplicação do {numero}:\n"
        for i in range(1, 11):
            resultado = numero * i
            mensagem += f"{numero} x {i} = {resultado}\n"
        update.message.reply_text(mensagem)
    except (IndexError, ValueError):
        update.message.reply_text("Por favor, envie um número válido para obter a tabuada de multiplicação.")

def tabuada_divisao(update: Update, context: CallbackContext) -> None:
    try:
        numero = int(context.args[0])
        mensagem = f"Tabuada de divisão do {numero}:\n"
        for i in range(1, 11):
            resultado = numero / i
            mensagem += f"{numero} ÷ {i} = {resultado:.2f}\n"  # Arredonda para 2 casas decimais
        update.message.reply_text(mensagem)
    except (IndexError, ValueError, ZeroDivisionError):
        update.message.reply_text("Por favor, envie um número válido (diferente de zero) para obter a tabuada de divisão.")

def tabuada_adicao(update: Update, context: CallbackContext) -> None:
    try:
        numero = int(context.args[0])
        mensagem = f"Tabuada de adição do {numero}:\n"
        for i in range(1, 11):
            resultado = numero + i
            mensagem += f"{numero} + {i} = {resultado}\n"
        update.message.reply_text(mensagem)
    except (IndexError, ValueError):
        update.message.reply_text("Por favor, envie um número válido para obter a tabuada de adição.")

def tabuada_subtracao(update: Update, context: CallbackContext) -> None:
    try:
        numero = int(context.args[0])
        mensagem = f"Tabuada de subtração do {numero}:\n"
        for i in range(1, 11):
            resultado = numero - i
            mensagem += f"{numero} - {i} = {resultado}\n"
        update.message.reply_text(mensagem)
    except (IndexError, ValueError):
        update.message.reply_text("Por favor, envie um número válido para obter a tabuada de subtração.")

def main() -> None:
    updater = Updater("TOKEN_DO_SEU_BOT")  # Substitua "TOKEN_DO_SEU_BOT" pelo token do seu bot
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))  # Registra o manipulador de comando para /start
    dp.add_handler(CommandHandler("tbm", tabuada_multiplicacao, pass_args=True))  # Registra o manipulador de comando para /tbm
    dp.add_handler(CommandHandler("tbd", tabuada_divisao, pass_args=True))  # Registra o manipulador de comando para /tbd
    dp.add_handler(CommandHandler("tba", tabuada_adicao, pass_args=True))  # Registra o manipulador de comando para /tba
    dp.add_handler(CommandHandler("tbs", tabuada_subtracao, pass_args=True))  # Registra o manipulador de comando para /tbs

    updater.start_polling()  # Inicia o bot
    updater.idle()

if __name__ == '__main__':
    main()
