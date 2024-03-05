# ANTIFLOD
## DESCRIÇÃO:
Este bot é um sistema de proteção contra flood de mensagens em grupos do Telegram. Quando um usuário envia mais de 3 mensagens em menos de 10 segundos, o bot detecta essa atividade como flood e toma medidas para mitigá-la. 

1. **Monitoramento de Mensagens:** O bot monitora todas as mensagens enviadas em grupos ou supergrupos.

2. **Detecção de Flood:** Ele calcula o intervalo de tempo entre as mensagens de um usuário e verifica se o usuário enviou mais de 3 mensagens em menos de 10 segundos.

3. **Silenciamento e Remoção de Mensagens:** Se um usuário for detectado enviando flood de mensagens, o bot o silencia, impedindo-o de enviar novas mensagens por um período de tempo. Além disso, o bot apaga todas as mensagens enviadas pelo usuário durante o período de flood.

4. **Notificação:** O bot envia uma mensagem no grupo informando que o usuário foi silenciado por flood de mensagens, mencionando o nome do usuário.

5. **Atualização em Tempo Real:** O bot monitora continuamente as mensagens e atualiza o status dos usuários em tempo real, garantindo uma resposta rápida ao flood de mensagens.

## EXPLICAÇÃO:
1. ```python
   from TOKEN import *
   import telebot
   import time
   ```
   - Importa o token do bot do Telegram a partir de um arquivo `TOKEN.py`, além de importar os módulos `telebot` e `time`.

2. ```python
   bot = telebot.TeleBot(TOKEN)
   ```
   - Inicializa o bot do Telegram com o token fornecido.

3. ```python
   last_message_times = {}
   ```
   - Cria um dicionário vazio para armazenar o timestamp da última mensagem de cada usuário.

4. ```python
   @bot.message_handler(func=lambda message: message.chat.type in ["group", "supergroup"] and not message.from_user.is_bot)
   def anti_flood(message):
       ...
   ```
   - Define uma função para monitorar as mensagens em grupos, excluindo mensagens de bots.

5. ```python
   user_id = message.from_user.id
   ```
   - Obtém o ID do usuário que enviou a mensagem.

6. ```python
   if user_id in last_message_times:
       ...
   ```
   - Verifica se o usuário já enviou mensagens anteriormente.

7. ```python
   last_timestamp = last_message_times[user_id]["timestamp"]
   interval = time.time() - last_timestamp
   ```
   - Calcula o intervalo de tempo desde a última mensagem do usuário.

8. ```python
   if interval < 10:
       if "message_count" in last_message_times[user_id]:
           last_message_times[user_id]["message_count"] += 1
       else:
           last_message_times[user_id]["message_count"] = 2  # Contando a mensagem atual e a anterior
   else:
       last_message_times[user_id] = {"timestamp": time.time(), "message_count": 1, "messages": []}
   ```
   - Se o intervalo for inferior a 10 segundos, incrementa o contador de mensagens do usuário. Caso contrário, inicializa um novo registro para o usuário.

9. ```python
   if "message_count" in last_message_times[user_id] and last_message_times[user_id]["message_count"] > 3:
       ...
   ```
   - Verifica se o usuário enviou mais de 3 mensagens em menos de 10 segundos.

10. ```python
    bot.restrict_chat_member(message.chat.id, user_id, can_send_messages=False)
    ```
    - Silencia o usuário.

11. ```python
    for msg_id in last_message_times[user_id]["messages"]:
        try:
            bot.delete_message(message.chat.id, msg_id)
        except Exception as e:
            print(f"Erro ao excluir mensagem: {e}")
    ```
    - Apaga todas as mensagens do usuário.

12. ```python
    bot.send_message(message.chat.id, f"Usuário {message.from_user.first_name} foi silenciado por flood de mensagens.")
    ```
    - Envia uma mensagem no grupo informando sobre o silenciamento do usuário.

13. ```python
    last_message_times[user_id]["timestamp"] = time.time()
    last_message_times[user_id]["messages"].append(message.message_id)
    ```
    - Atualiza o timestamp da última mensagem do usuário e adiciona a mensagem atual à lista de mensagens do usuário.

14. ```python
    bot.polling()
    ```
    - Inicia o bot, permitindo que ele receba e envie mensagens.

