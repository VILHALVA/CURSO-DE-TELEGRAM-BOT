from TOKEN import *
import telebot
import time

bot = telebot.TeleBot(TOKEN)

# Dicionário para armazenar o timestamp da última mensagem de cada usuário
last_message_times = {}

# Função para monitorar as mensagens
@bot.message_handler(func=lambda message: message.chat.type in ["group", "supergroup"] and not message.from_user.is_bot)
def anti_flood(message):
    user_id = message.from_user.id
    
    # Verifica se o usuário já enviou mensagens antes
    if user_id in last_message_times:
        # Calcula o intervalo de tempo desde a última mensagem
        last_timestamp = last_message_times[user_id]["timestamp"]
        interval = time.time() - last_timestamp
        
        # Se o intervalo for inferior a 10 segundos, incrementa o contador de mensagens do usuário
        if interval < 10:
            if "message_count" in last_message_times[user_id]:
                last_message_times[user_id]["message_count"] += 1
            else:
                last_message_times[user_id]["message_count"] = 2  # Contando a mensagem atual e a anterior
        else:
            last_message_times[user_id] = {"timestamp": time.time(), "message_count": 1, "messages": []}
    else:
        last_message_times[user_id] = {"timestamp": time.time(), "message_count": 1, "messages": []}

    # Verifica se o usuário enviou mais de 3 mensagens em menos de 10 segundos
    if "message_count" in last_message_times[user_id] and last_message_times[user_id]["message_count"] > 3:
        # Silencia o usuário
        bot.restrict_chat_member(message.chat.id, user_id, can_send_messages=False)
        
        # Apaga todas as mensagens do usuário
        for msg_id in last_message_times[user_id]["messages"]:
            try:
                bot.delete_message(message.chat.id, msg_id)
            except Exception as e:
                print(f"Erro ao excluir mensagem: {e}")
        
        bot.send_message(message.chat.id, f"Usuário {message.from_user.first_name} foi silenciado por flood de mensagens.")

    # Atualiza o timestamp da última mensagem do usuário
    last_message_times[user_id]["timestamp"] = time.time()
    # Adiciona a mensagem atual à lista de mensagens do usuário
    last_message_times[user_id]["messages"].append(message.message_id)

# Inicialização do bot
bot.polling()
