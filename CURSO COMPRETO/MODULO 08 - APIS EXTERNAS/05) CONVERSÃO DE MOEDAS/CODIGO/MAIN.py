import requests
from telegram.ext import Updater, CommandHandler
from TOKEN import TOKEN
from API_KEY import API_KEY

# Função para lidar com o comando /convert
def convert(bot, update):
    # Verifica se foram fornecidos os parâmetros necessários
    if len(update.message.text.split()) != 4:
        update.message.reply_text('Por favor, forneça a moeda de origem, a moeda de destino e o valor para conversão.')
        return
    
    # Extrai os parâmetros da mensagem do usuário
    source_currency = update.message.text.split()[1].upper()
    target_currency = update.message.text.split()[2].upper()
    amount = update.message.text.split()[3]
    
    # Chama a API da ExchangeRatesAPI para obter a taxa de câmbio
    try:
        url = f'https://api.exchangeratesapi.io/latest?base={source_currency}&symbols={target_currency}&access_key={API_KEY}'
        response = requests.get(url)
        data = response.json()
        
        # Verifica se a consulta foi bem-sucedida
        if response.status_code == 200:
            # Extrai a taxa de câmbio da resposta
            exchange_rate = data['rates'][target_currency]
            
            # Calcula o valor convertido
            converted_amount = float(amount) * exchange_rate
            
            # Formata a resposta da conversão de moeda
            conversion_info = f"{amount} {source_currency} equivale a {converted_amount:.2f} {target_currency}"
            
            # Envia a resposta da conversão de moeda de volta para o usuário
            update.message.reply_text(conversion_info)
        else:
            update.message.reply_text('Não foi possível realizar a conversão de moeda.')
    except Exception as e:
        update.message.reply_text('Ocorreu um erro ao processar sua solicitação.')

def main():
    # Cria um Updater para receber atualizações do Telegram
    updater = Updater(TOKEN, use_context=True)

    # Obtém o despachante para registrar manipuladores de comando
    dp = updater.dispatcher

    # Registra um manipulador de comando para o comando /convert
    dp.add_handler(CommandHandler("convert", convert))

    # Inicia o bot
    updater.start_polling()

    # Aguarda o bot receber comandos
    updater.idle()

if __name__ == '__main__':
    main()
