import telebot
from telebot.types import ForceReply

TOKEN = 'SEU_TOKEN_AQUI'
bot = telebot.TeleBot(TOKEN)

notas = {}

@bot.message_handler(commands=["start"])
def start(message):
    saudacao = "Olá! Bem-vindo ao Bot da Média de Notas. Por favor, digite suas 4 notas separadas por espaços."
    bot.send_message(message.chat.id, saudacao, reply_markup=ForceReply(selective=True))
    bot.register_next_step_handler(message, validar_notas)

def validar_notas(message):
    try:
        notas_str = message.text.split()
        if len(notas_str) != 4:
            raise ValueError("Por favor, insira exatamente 4 notas.")
        
        notas_float = [float(nota) for nota in notas_str]
        
        if any(nota < 0 or nota > 10 for nota in notas_float):
            raise ValueError("Notas devem estar entre 0 e 10.")
        
        media = sum(notas_float) / 4
        bot.send_message(message.chat.id, f"Sua média é: {media:.2f}")
    except ValueError as e:
        bot.send_message(message.chat.id, str(e))
        start(message)

if __name__ == '__main__':
    print("BOT EM EXECUÇÃO!")
    bot.infinity_polling()
    print("FIM")
