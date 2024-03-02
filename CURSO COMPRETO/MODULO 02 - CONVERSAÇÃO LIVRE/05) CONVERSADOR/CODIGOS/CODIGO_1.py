import telebot

TOKEN = "TOKEN_AQUI"
bot = telebot.TeleBot(TOKEN)

# Função para verificar se a mensagem deve ser processada
def verificar(mensagem):
    return True

# Comando /start
@bot.message_handler(func=verificar, commands=["start"])
def start(mensagem):
    bot.send_message(mensagem.chat.id, "Olá! Eu sou o seu bot assistente. Como posso ajudar você hoje?")

# Comando /help
@bot.message_handler(func=verificar, commands=["help"])
def help(mensagem):
    bot.send_message(mensagem.chat.id, "Você pode me enviar mensagens como 'TOP' para ver uma resposta divertida.")

# Resposta a mensagens contendo a palavra "TOP"
@bot.message_handler(func=verificar, content_types=["text"])
def top(mensagem):
    if "TOP" in mensagem.text.upper():
        bot.reply_to(mensagem, "Sim, é muito top!")

# Resposta padrão para mensagens não reconhecidas
@bot.message_handler(func=lambda mensagem: True)
def resposta_padrao(mensagem):
    bot.reply_to(mensagem, "Desculpe, não entendi o que você quis dizer. Se precisar de ajuda, digite /help.")

# Tratamento de erros
@bot.error_handler()
def handle_error(message, error):
    bot.reply_to(message, f"Ocorreu um erro: {error}")

# Iniciando o polling
bot.polling()
