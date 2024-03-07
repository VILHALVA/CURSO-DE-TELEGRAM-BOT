from telebot import types

def submenu_ciencia():
    markup = types.InlineKeyboardMarkup(row_width=2)
    fisica_button = types.InlineKeyboardButton("FISICA", callback_data='fisica')
    quimica_button = types.InlineKeyboardButton("QUIMICA", callback_data='quimica')
    biologia_button = types.InlineKeyboardButton("BIOLOGIA", callback_data='biologia')
    matematica_button = types.InlineKeyboardButton("MATEMATICA", callback_data='matematica')
    astronomia_button = types.InlineKeyboardButton("ASTRONOMIA", callback_data='astronomia')
    
    markup.add(fisica_button, quimica_button, biologia_button, matematica_button, astronomia_button)
    
    return markup

# Handler para os callbacks dos botões do submenu de Ciência
def callback_query(bot, call):
    if call.data == 'fisica':
        bot.send_message(call.message.chat.id, "A Física é a ciência que estuda os fenômenos naturais relacionados com a matéria e a energia.")
    elif call.data == 'quimica':
        bot.send_message(call.message.chat.id, "A Química é a ciência que estuda a composição, estrutura, propriedades da matéria, as mudanças que ela sofre durante as reações químicas e a energia envolvida nesses processos.")
    elif call.data == 'biologia':
        bot.send_message(call.message.chat.id, "A Biologia é a ciência que estuda os seres vivos e suas interações com o meio ambiente.")
    elif call.data == 'matematica':
        bot.send_message(call.message.chat.id, "A Matemática é a ciência que estuda os números, as suas propriedades e as operações realizadas sobre eles.")
    elif call.data == 'astronomia':
        bot.send_message(call.message.chat.id, "A Astronomia é a ciência que estuda os corpos celestes, como estrelas, planetas, cometas, galáxias, entre outros.")
    else:
        pass
