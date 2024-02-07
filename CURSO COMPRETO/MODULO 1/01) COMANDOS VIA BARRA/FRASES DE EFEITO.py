#=================== [ A ] ALMA DO BOT: ==============================
import telebot
TOKEN = "TOKEN_AQUI"
bot = telebot.TeleBot(TOKEN)
def verificar(mensagem):
    return True
# bot.send_message > "print"
# bot.reply_to > "input"
# @bot.message_handler > "if" / "else" do "def"

#=================== [ B ] COMANDOS DO BOT: ============================
#--------------------[ 2 ] OPÇÕES DO MENU: -----------------------------
@bot.message_handler(commands=["amor"])
def amor(mensagem):
    bot.send_message(mensagem.chat.id,"😍️O DINHEIRO NÃO COMPRA AMOR!")

@bot.message_handler(commands=["raiva"])
def raiva(mensagem):
    bot.send_message(mensagem.chat.id,"😡️SUA FALTA DE INCUPETÊNCIA ME INFURECE!")

@bot.message_handler(commands=["tristeza"])
def tristeza(mensagem):
    bot.send_message(mensagem.chat.id,"😥️O QUE MAIS ME INTRISTECE É O DESPERDICIO!")

@bot.message_handler(commands=["alegria"])
def alegria(mensagem):
    bot.send_message(mensagem.chat.id,"😀️O QUE MAIS ME ALEGRA NA ESPÉCIE HUMANA É A HUMILDADE!")

#--------------------[ 1 ] MENU INICIAL: -------------------------------
@bot.message_handler(func=verificar, commands=["start", "menu", "help"])
def responder(mensagem):
    texto = '''
🛑ESCOLHA UMA DAS OPÇÕES (CLIQUE EM UMA DELAS):

    /amor > Frase de amor
    /raiva > Frase de raiva
    /tristeza > Frase de Tristeza
    /alegria > Frase de alegria

💚RESPONDER QUALQUER MENSAGEM NÃO IRÁ FUNCIONAR!!'''
    bot.reply_to(mensagem,texto)

#=================== [ C ] START DO BOT: ============================
bot.polling()
