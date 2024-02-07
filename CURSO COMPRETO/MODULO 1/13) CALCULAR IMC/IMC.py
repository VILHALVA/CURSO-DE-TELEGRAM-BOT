import telebot

# Insira seu token do Telegram aqui
TOKEN = 'SEU_TOKEN_AQUI'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message, "Bem-vindo ao Bot de Cálculo de IMC! Por favor, me envie seu peso em quilogramas.")

@bot.message_handler(func=lambda message: True)
def calcular_imc(message):
    try:
        peso = float(message.text)
        if peso <= 0:
            raise ValueError
        bot.send_message(message.chat.id, "Ótimo! Agora, me envie sua altura em metros.")
        bot.register_next_step_handler(message, calcular_altura, peso)
    except ValueError:
        bot.send_message(message.chat.id, "Por favor, insira um valor válido para o peso em quilogramas.")
    
def calcular_altura(message, peso):
    try:
        altura = float(message.text)
        if altura <= 0:
            raise ValueError
        imc = peso / (altura ** 2)
        resposta = f"Seu IMC é {imc:.2f}."
        if imc < 18.5:
            resposta += " Você está abaixo do peso."
        elif imc < 24.9:
            resposta += " Seu peso está saudável."
        elif imc < 29.9:
            resposta += " Você está com sobrepeso."
        else:
            resposta += " Você está obeso."
        bot.send_message(message.chat.id, resposta)
    except ValueError:
        bot.send_message(message.chat.id, "Por favor, insira um valor válido para a altura em metros.")

if __name__ == '__main__':
    print("Bot de Cálculo de IMC em execução!")
    bot.infinity_polling()
