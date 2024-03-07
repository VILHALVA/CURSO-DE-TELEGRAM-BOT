import telebot
from telebot.types import LabeledPrice, ShippingOption

token = 'TOKEN_BOT'
provider_token = 'TOKEN_PAGAMENTO'  
bot = telebot.TeleBot(token)

precos = [LabeledPrice(label='Máquina do Tempo Funcionando', amount=5750), LabeledPrice('Embrulho para Presente', 500)]

opcoes_de_envio = [
    ShippingOption(id='instant', title='Teletransporte Mundial').add_price(LabeledPrice('Teletransporte', 1000)),
    ShippingOption(id='pickup', title='Retirada Local').add_price(LabeledPrice('Retirada', 300))]


@bot.message_handler(commands=['start'])
def command_start(message):
    bot.send_message(message.chat.id,
                     "Olá, eu sou o bot de demonstração de comerciante."
                     " Eu posso vender uma Máquina do Tempo para você."
                     " Use /buy para encomendar uma, /terms para Termos e Condições")


@bot.message_handler(commands=['terms'])
def command_terms(message):
    bot.send_message(message.chat.id,
                     'Obrigado por fazer compras com o nosso bot de demonstração. Esperamos que você goste da sua nova máquina do tempo!\n'
                     '1. Se a sua máquina do tempo não foi entregue a tempo, por favor, repense seu conceito de tempo e tente novamente.\n'
                     '2. Se você descobrir que sua máquina do tempo não está funcionando, por favor, entre em contato com nossas oficinas de serviço futuras em Trappist-1e.'
                     ' Elas estarão acessíveis em qualquer lugar entre maio de 2075 e novembro de 4000 D.C.\n'
                     '3. Se você deseja um reembolso, gentilmente aplique um ontem e nós teremos enviado a você imediatamente.')


@bot.message_handler(commands=['buy'])
def command_pay(message):
    bot.send_message(message.chat.id,
                     "Cartões reais não funcionarão comigo, nenhum dinheiro será debitado de sua conta."
                     " Use este número de teste de cartão para pagar pela sua Máquina do Tempo: `4242 4242 4242 4242`"
                     "\n\nEste é o seu fatura de demonstração:", parse_mode='Markdown')
    bot.send_invoice(
                     message.chat.id,  #chat_id
                     'Máquina do Tempo Funcionando', #title
                     'Quer visitar seus tataravós? Fazer fortuna nas corridas? Apertar as mãos com Hamurábi e dar um passeio nos Jardins Suspensos? Encomende hoje a nossa Máquina do Tempo Funcionando!', #description
                     'COUPON DE SEXTA-FEIRA FELIZ', #invoice_payload
                     provider_token, #provider_token
                     'usd', #currency
                     precos, #prices
                     photo_url='http://erkelzaar.tsudao.com/models/perrotta/TIME_MACHINE.jpg',
                     photo_height=512,  # !=0/None or picture won't be shown
                     photo_width=512,
                     photo_size=512,
                     is_flexible=False,  # True If you need to set up Shipping Fee
                     start_parameter='exemplo-de-maquina-do-tempo')


@bot.shipping_query_handler(func=lambda query: True)
def shipping(shipping_query):
    print(shipping_query)
    bot.answer_shipping_query(shipping_query.id, ok=True, shipping_options=opcoes_de_envio,
                              error_message='Ah, parece que nossos mensageiros caninos estão almoçando agora. Tente novamente mais tarde!')


@bot.pre_checkout_query_handler(func=lambda query: True)
def checkout(pre_checkout_query):
    bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True,
                                  error_message="Alienígenas tentaram roubar o CVV do seu cartão, mas nós protegemos com sucesso suas credenciais,"
                                                " tente pagar novamente em alguns minutos, precisamos de um pequeno descanso.")


@bot.message_handler(content_types=['successful_payment'])
def got_payment(message):
    bot.send_message(message.chat.id,
                     'Hoooooray! Obrigado pelo pagamento! Vamos processar seu pedido de `{} {}` o mais rápido possível! '
                     'Fique em contato.\n\nUse /buy novamente para obter uma Máquina do Tempo para seu amigo!'.format(
                         message.successful_payment.total_amount / 100, message.successful_payment.currency),
                     parse_mode='Markdown')


bot.infinity_polling(skip_pending = True)
