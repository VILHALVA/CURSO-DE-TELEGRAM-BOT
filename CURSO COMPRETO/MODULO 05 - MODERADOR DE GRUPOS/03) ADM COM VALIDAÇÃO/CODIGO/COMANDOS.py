def COMANDOS(bot):
    @bot.message_handler(commands=['ban'])
    def ban_user(message):
        user_id = message.from_user.id
        chat_id = message.chat.id
        user_to_ban = message.reply_to_message.from_user.id
        bot.kick_chat_member(chat_id, user_to_ban)
        bot.send_message(chat_id, f"Usuário {user_to_ban} foi banido!")

    @bot.message_handler(commands=['mute'])
    def mute_user(message):
        user_id = message.from_user.id
        chat_id = message.chat.id
        user_to_mute = message.reply_to_message.from_user.id
        bot.restrict_chat_member(chat_id, user_to_mute, can_send_messages=False)
        bot.send_message(chat_id, f"Usuário {user_to_mute} foi silenciado!")

    @bot.message_handler(commands=['kick'])
    def kick_user(message):
        user_id = message.from_user.id
        chat_id = message.chat.id
        user_to_kick = message.reply_to_message.from_user.id
        bot.kick_chat_member(chat_id, user_to_kick)
        bot.send_message(chat_id, f"Usuário {user_to_kick} foi expulso!")
