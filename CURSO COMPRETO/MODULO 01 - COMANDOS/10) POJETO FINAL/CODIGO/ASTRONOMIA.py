from telebot import types

def submenu_astronomia():
    markup = types.InlineKeyboardMarkup(row_width=2)
    sol_button = types.InlineKeyboardButton("SOL", callback_data='sol')
    mercurio_button = types.InlineKeyboardButton("MERCURIO", callback_data='mercurio')
    venus_button = types.InlineKeyboardButton("VENUS", callback_data='venus')
    terra_button = types.InlineKeyboardButton("TERRA", callback_data='terra')
    marte_button = types.InlineKeyboardButton("MARTE", callback_data='marte')
    jupiter_button = types.InlineKeyboardButton("JUPITER", callback_data='jupiter')
    saturno_button = types.InlineKeyboardButton("SATURNO", callback_data='saturno')
    urano_button = types.InlineKeyboardButton("URANO", callback_data='urano')
    netuno_button = types.InlineKeyboardButton("NETUNO", callback_data='netuno')
    
    markup.add(sol_button, mercurio_button, venus_button, terra_button, marte_button,
               jupiter_button, saturno_button, urano_button, netuno_button)
    
    return markup

# Handler para os callbacks dos botões do submenu de Astronomia
def callback_query(bot, call):
    if call.data == 'sol':
        bot.send_message(call.message.chat.id, "O Sol é uma estrela localizada no centro do sistema solar. É uma esfera em constante atividade nuclear, produzindo luz e calor.")
    elif call.data == 'mercurio':
        bot.send_message(call.message.chat.id, "Mercúrio é o planeta mais próximo do Sol e o menor planeta do sistema solar. É conhecido por suas temperaturas extremas e falta de atmosfera significativa.")
    elif call.data == 'venus':
        bot.send_message(call.message.chat.id, "Vênus é o segundo planeta do sistema solar e é conhecido por ser o planeta mais quente, devido à sua atmosfera densa de dióxido de carbono.")
    elif call.data == 'terra':
        bot.send_message(call.message.chat.id, "A Terra é o terceiro planeta do sistema solar e o único planeta conhecido por abrigar vida. Possui uma atmosfera que sustenta a vida e uma grande variedade de ecossistemas.")
    elif call.data == 'marte':
        bot.send_message(call.message.chat.id, "Marte é o quarto planeta do sistema solar e é conhecido por sua cor avermelhada. Possui características geológicas semelhantes à Terra e é foco de estudos sobre a possibilidade de vida extraterrestre.")
    elif call.data == 'jupiter':
        bot.send_message(call.message.chat.id, "Júpiter é o quinto planeta do sistema solar e é o maior planeta, conhecido por sua grande mancha vermelha e suas muitas luas, incluindo a maior lua do sistema solar, Ganimedes.")
    elif call.data == 'saturno':
        bot.send_message(call.message.chat.id, "Saturno é o sexto planeta do sistema solar, conhecido por seus impressionantes anéis. É um dos destinos de interesse na exploração espacial.")
    elif call.data == 'urano':
        bot.send_message(call.message.chat.id, "Urano é o sétimo planeta do sistema solar, conhecido por sua inclinação axial extrema, resultando em estações incomuns e uma rotação de lado.")
    elif call.data == 'netuno':
        bot.send_message(call.message.chat.id, "Netuno é o oitavo e último planeta do sistema solar, conhecido por sua cor azul e seus ventos extremamente rápidos.")
    else:
        pass