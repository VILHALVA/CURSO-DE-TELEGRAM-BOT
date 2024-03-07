from CONFIG import bot
from time import sleep
import re

@bot.message_handler(commands=['ajuda'])
def mensagem_ajuda(message):
    bot.send_chat_action(message.chat.id, 'typing')
    sleep(1)
    
    resposta = (
        "Aqui estão os comandos disponíveis:\n"
        "\n"
        "*/start* - Inicia a interação com o bot\n"
        "*/ajuda* - Mostra esta mensagem de ajuda\n"
        "*somar {valor1} e {valor2}* - Calcula a soma de dois valores\n"
        "*subtrair {valor1} e {valor2}* - Calcula a subtração de dois valores\n"
        "*multiplicar {valor1} e {valor2}* - Calcula a multiplicação de dois valores\n"
        "*dividir {valor1} e {valor2}* - Calcula a divisão de dois valores\n"
        )
    
    bot.send_message(
        message.chat.id,
        resposta,
        parse_mode="Markdown")

@bot.message_handler(commands=['start'])
def mensagem_inicio(message):
    bot.send_chat_action(message.chat.id, 'typing')
    sleep(1)
    bot.send_message(
        message.chat.id,
        "Olá! Eu sou um bot de cálculo. Como posso ajudar você? Envie /ajuda para saber mais!",
        parse_mode="Markdown")

@bot.message_handler(regexp=r"^somar ([+-]?([0-9]*[.])?[0-9]+) e ([+-]?([0-9]*[.])?[0-9]+)$")
def mensagem_soma(message):
    bot.send_chat_action(message.chat.id, 'typing')
    sleep(1)
    
    valores = extrair_valores(r"^somar ([+-]?([0-9]*[.])?[0-9]+) e ([+-]?([0-9]*[.])?[0-9]+)$", message.text)
    
    resultado = valores[0] + valores[1]
    
    bot.reply_to(
        message,
        f"O resultado da soma é: {resultado}")

@bot.message_handler(regexp=r"^subtrair ([+-]?([0-9]*[.])?[0-9]+) e ([+-]?([0-9]*[.])?[0-9]+)$")
def mensagem_subtracao(message):
    bot.send_chat_action(message.chat.id, 'typing')
    sleep(1)
    
    valores = extrair_valores(r"^subtrair ([+-]?([0-9]*[.])?[0-9]+) e ([+-]?([0-9]*[.])?[0-9]+)$", message.text)
    
    resultado = valores[0] - valores[1]
    
    bot.reply_to(
        message,
        f"O resultado da subtração é: {resultado}")

@bot.message_handler(regexp=r"^multiplicar ([+-]?([0-9]*[.])?[0-9]+) e ([+-]?([0-9]*[.])?[0-9]+)$")
def mensagem_multiplicacao(message):
    bot.send_chat_action(message.chat.id, 'typing')
    sleep(1)
    
    valores = extrair_valores(r"^multiplicar ([+-]?([0-9]*[.])?[0-9]+) e ([+-]?([0-9]*[.])?[0-9]+)$", message.text)
    
    resultado = valores[0] * valores[1]
    
    bot.reply_to(
        message,
        f"O resultado da multiplicação é: {resultado}")

@bot.message_handler(regexp=r"^dividir ([+-]?([0-9]*[.])?[0-9]+) e ([+-]?([0-9]*[.])?[0-9]+)$")
def mensagem_divisao(message):
    bot.send_chat_action(message.chat.id, 'typing')
    sleep(1)
    
    valores = extrair_valores(r"^dividir ([+-]?([0-9]*[.])?[0-9]+) e ([+-]?([0-9]*[.])?[0-9]+)$", message.text)
    
    if valores[1] == 0:
        bot.reply_to(
            message,
            f"Não é possível dividir por zero.")
    else:
        resultado = valores[0] / valores[1]
        bot.reply_to(
            message,
            f"O resultado da divisão é: {resultado}")

@bot.message_handler(func=lambda message: True)
def mensagem_desconhecida(message):
    bot.send_chat_action(message.chat.id, 'typing')
    sleep(1)
    
    bot.reply_to(
        message,
        "Desculpe, não entendi o que você disse.")

def extrair_valores(expressao, texto):
    partes = re.match(
        expressao,
        texto,
        flags=re.IGNORECASE)
    
    valores = []
    valores.append(float(partes[1]))
    valores.append(float(partes[3]))
    
    return valores

if __name__ == '__main__':
    bot.polling(timeout=20)
