#=================== [ A ] ALMA DO BOT: ==============================
import telebot
from time import sleep
TOKEN = "TOKEN_AQUI"
bot = telebot.TeleBot(TOKEN)
def verificar(mensagem):
    return True
# bot.send_message > "print"
# bot.reply_to > "input"
# @bot.message_handler > "if" / "else" do "def"

#=================== [ B ] COMANDOS DO BOT: ============================
#--------------------[ 2 ] OPÇÕES DO MENU: -----------------------------
@bot.message_handler(commands=["pedir"])
def pedir(mensagem):
    texto = '''
🛑O QUE VOCÊ QUER COMER? (CLIQUE EM UMA DELAS):

    /pizza > Comer Pizza
    /cascalho > Comer cascalho
    /batatas > Comer batatas
    /pastel > Comer pastel
    /sanduiche > Comer sanduiche
    /sonho > Comer Sonho
    /suco > Comer Suco
    /menu > Voltar ao menu principal

💚RESPONDER QUALQUER MENSAGEM NÃO IRÁ FUNCIONAR!!'''
    bot.reply_to(mensagem,texto)

@bot.message_handler(commands=["pizza"])
def pizza(mensagem):
    bot.send_message(mensagem.chat.id,"😠SUA PIZZA ESTÁ CHEGANDO!")

@bot.message_handler(commands=["cascalho"])
def cascalho(mensagem):
    bot.send_message(mensagem.chat.id,"😠DAQUI A POUCO O SEU CASCALHO ESTÁ CHEGANDO!")

@bot.message_handler(commands=["batatas"])
def batatas(mensagem):
    bot.send_message(mensagem.chat.id,"😠EM BREVE SUAS BATATAS ESTARÃO CHEGANDO!")
    
@bot.message_handler(commands=["pastel"])
def pastel(mensagem):
    bot.send_message(mensagem.chat.id,"😠EM BREVE SEU PASTEL ESTARÁ CHEGANDO!")

@bot.message_handler(commands=["sanduiche"])
def sanduiche(mensagem):
    bot.send_message(mensagem.chat.id,"😠EM BREVE SEU SANDUICHE ESTARÁ CHEGANDO!")
    
@bot.message_handler(commands=["sonho"])
def sonho(mensagem):
    bot.send_message(mensagem.chat.id,"😠EM BREVE SEU SONHO ESTARÁ CHEGANDO!")

@bot.message_handler(commands=["suco"])
def suco(mensagem):
    bot.send_message(mensagem.chat.id,"😠EM BREVE SEU SUCO ESTARÁ CHEGANDO!")
    
@bot.message_handler(commands=["cancelar"])
def cancelar(mensagem):
    bot.send_message(mensagem.chat.id,"😠SEU PEDIDO FOI CANCELADO!")
    sleep(1)
    bot.send_message(mensagem.chat.id,"😠DESEJA MAIS ALGUMA COISA?")

@bot.message_handler(commands=["reclamar"])
def reclamar(mensagem):
    bot.send_message(mensagem.chat.id,"😍Envie sua reclamação para o departamento do FODA-SE!")

@bot.message_handler(commands=["abracar"])
def abracar(mensagem):
    bot.send_message(mensagem.chat.id,"😍O Patrão te mandou um abraço de volta!")

#-----------------[ 1 ] MENU INICIAL: -------------------------------   
@bot.message_handler(func=verificar, commands=["start", "menu"])
def responder(mensagem):
    texto = '''
🛑ESCOLHA UMA DAS OPÇÕES (CLIQUE EM UMA DELAS):

    /pedir > Fazer um pedido
    /cancelar > Cancelar o pedido
    /reclamar > Reclamar de um pedido
    /abracar > Mandar um abraço para o patrão

💚RESPONDER QUALQUER MENSAGEM NÃO IRÁ FUNCIONAR!!'''
    bot.reply_to(mensagem,texto)

#=================== [ C ] START DO BOT: ============================
bot.polling()