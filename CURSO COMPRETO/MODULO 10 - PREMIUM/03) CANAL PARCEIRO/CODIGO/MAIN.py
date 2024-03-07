from TOKEN import TOKEN
from CANAL import CANAL_PARCEIRO
import telebot

# Inicialize o bot
bot = telebot.TeleBot(TOKEN)

# Manipulador de comando '/start'
@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id

    # Verifica se o usuário é membro do canal parceiro
    if is_member_of_channel(user_id):
        bot.reply_to(message, "Bem-vindo! Você pode usar este bot.")
        # AQUI VOCÊ PODE COLOCAR A LÓGICA PARA O SEU BOT!
    else:
        bot.reply_to(message, "Desculpe, você precisa ser membro do canal parceiro para usar este bot.")

# Função para verificar se o usuário é membro do canal parceiro
def is_member_of_channel(user_id):
    try:
        member = bot.get_chat_member(CANAL_PARCEIRO, user_id)
        if member.status in ['member', 'administrator', 'creator']:
            return True
        else:
            return False
    except Exception as e:
        print("Erro ao verificar a associação ao canal:", e)
        return False

# Inicia o bot
bot.polling()
