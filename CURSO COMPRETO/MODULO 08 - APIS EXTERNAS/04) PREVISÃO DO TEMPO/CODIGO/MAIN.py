import requests
from telegram.ext import Updater, CommandHandler
from TOKEN import TOKEN
from API_KEY import API_KEY

# Função para lidar com o comando /weather
def weather(bot, update):
    # Verifica se foi fornecido um local para obter a previsão do tempo
    if len(update.message.text.split()) == 1:
        update.message.reply_text('Por favor, forneça um local para obter a previsão do tempo.')
        return
    
    # Extrai o local da mensagem do usuário
    location = ' '.join(update.message.text.split()[1:])
    
    # Chama a API da OpenWeatherMap para obter a previsão do tempo
    try:
        url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}&units=metric'
        response = requests.get(url)
        data = response.json()
        
        # Verifica se a consulta foi bem-sucedida
        if response.status_code == 200:
            # Extrai informações relevantes da resposta
            description = data['weather'][0]['description']
            temp = data['main']['temp']
            humidity = data['main']['humidity']
            
            # Formata a resposta da previsão do tempo
            weather_info = f"Condição: {description}\nTemperatura: {temp}°C\nUmidade: {humidity}%"
            
            # Envia a previsão do tempo de volta para o usuário
            update.message.reply_text(weather_info)
        else:
            update.message.reply_text('Não foi possível obter a previsão do tempo para o local fornecido.')
    except Exception as e:
        update.message.reply_text('Ocorreu um erro ao processar sua solicitação.')

def main():
    # Cria um Updater para receber atualizações do Telegram
    updater = Updater(TOKEN, use_context=True)

    # Obtém o despachante para registrar manipuladores de comando
    dp = updater.dispatcher

    # Registra um manipulador de comando para o comando /weather
    dp.add_handler(CommandHandler("weather", weather))

    # Inicia o bot
    updater.start_polling()

    # Aguarda o bot receber comandos
    updater.idle()

if __name__ == '__main__':
    main()
