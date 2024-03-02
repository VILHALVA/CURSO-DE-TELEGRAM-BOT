import telebot
from telebot.types import ReplyKeyboardMarkup
from telebot.types import ForceReply

TOKEN = 'TOKEN_AQUI'
bot = telebot.TeleBot(TOKEN)

usuarios = {}

@bot.message_handler(commands=["start", "ayuda", "help"])
def cmd_start(message):
    marcar = ForceReply()
    bot.reply_to(message, "QUAL É O SEU NOME?", reply_markup=marcar)
    bot.register_next_step_handler(message, perguntar_nome)

def perguntar_nome(message):
    nome = message.text
    usuarios[message.chat.id] = {"nome": nome}
    marcar = ForceReply()
    bot.reply_to(message, f"OLÁ, {nome}! QUAL É A SUA IDADE?", reply_markup=marcar)
    bot.register_next_step_handler(message, perguntar_idade)

def perguntar_idade(message):
    if not message.text.isdigit():
        marcar = ForceReply()
        bot.reply_to(message, "ERRO! DIGITE UM NÚMERO: QUAL É A SUA IDADE?", reply_markup=marcar)
        bot.register_next_step_handler(message, perguntar_idade)
    else:
        usuarios[message.chat.id]["idade"] = int(message.text)
        marcar = ReplyKeyboardMarkup(
            one_time_keyboard=True,
            input_field_placeholder="CLICA NO BOTÃO!",
            resize_keyboard=True
        )
        marcar.add("HOMEM", "MULHER")
        bot.reply_to(message, "QUAL É O SEU SEXO?", reply_markup=marcar)
        bot.register_next_step_handler(message, dados_usuario)

def dados_usuario(message):
    if message.text != "HOMEM" and message.text != "MULHER":
        marcar = ReplyKeyboardMarkup(
            one_time_keyboard=True,
            input_field_placeholder="CLICA NO BOTÃO!",
            resize_keyboard=True
        )
        marcar.add("HOMEM", "MULHER")
        bot.reply_to(message, "ERRO! APERTE NO BOTÃO!", reply_markup=marcar)
        bot.register_next_step_handler(message, dados_usuario)
    else:
        usuarios[message.chat.id]["sexo"] = message.text
        texto = "DADOS INTRODUZIDOS:\n"
        texto += f"<code>NOME..: </code>{usuarios[message.chat.id]['nome']}\n"
        texto += f"<code>IDADE..: </code>{usuarios[message.chat.id]['idade']}\n"
        texto += f"<code>SEXO..: </code>{usuarios[message.chat.id]['sexo']}\n"
        bot.send_message(message.chat.id, texto, parse_mode="html")
        print(usuarios)

if __name__ == '__main__':
    print("BOT EM EXECUÇÃO!")
    bot.infinity_polling()
    print("FIM")
