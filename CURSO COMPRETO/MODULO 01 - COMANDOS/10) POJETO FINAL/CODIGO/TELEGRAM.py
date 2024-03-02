from telebot import types

def submenu_telegram():
    markup = types.InlineKeyboardMarkup(row_width=2)
    telegram_info_button = types.InlineKeyboardButton("ℹ️ Informações", callback_data='telegram_info')
    telegram_features_button = types.InlineKeyboardButton("✨Recursos", callback_data='telegram_features')
    telegram_tips_button = types.InlineKeyboardButton("💡Dicas", callback_data='telegram_tips')
    
    markup.add(telegram_info_button, telegram_features_button, telegram_tips_button)
    
    return markup

# Handler para os callbacks dos botões do submenu sobre o Telegram
def callback_query(bot, call):
    if call.data == 'telegram_info':
        bot.send_message(call.message.chat.id, "O Telegram é um aplicativo de mensagens focado em privacidade e segurança, que permite trocar mensagens e arquivos de forma segura.")
    elif call.data == 'telegram_features':
        bot.send_message(call.message.chat.id, "O Telegram oferece uma variedade de recursos, incluindo chats secretos, canais, bots, stickers, criptografia de ponta a ponta e muito mais.")
    elif call.data == 'telegram_tips':
        bot.send_message(call.message.chat.id, "Algumas dicas para usar o Telegram de forma eficaz incluem personalizar suas configurações de privacidade, aproveitar os bots disponíveis, usar chats secretos para comunicações sensíveis e explorar os recursos avançados.")
    else:
        pass
