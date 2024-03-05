# ANTI-SPAM
## DESCRIÇÃO:
O Bot Moderador Anti-Spam é uma ferramenta de moderação projetada para manter grupos de chat do Telegram livres de spam e links não autorizados. Ele monitora todas as mensagens enviadas pelos membros e verifica se contêm algum tipo de link. Se um link for detectado, o bot apaga a mensagem e bane o membro responsável por enviar o spam. (Ele não penaliza os ADMS).

1. Detecção de Links: O bot utiliza expressões regulares para verificar se uma mensagem contém links HTTP ou HTTPS, incluindo links de sites da web (por exemplo, www.example.com).

2. Ação de Moderação: Quando um link é detectado, o bot remove automaticamente a mensagem do membro e o bane do grupo como medida de moderação.

3. Notificação ao Grupo: O bot envia uma mensagem de aviso ao grupo informando que um membro foi banido por enviar spam.

4. Personalização: Os administradores do grupo podem personalizar as mensagens de aviso e as ações de moderação de acordo com as regras do grupo.

## EXPLICAÇÃO:
1. ```python
   import telebot
   import re
   ```
   - Importa os módulos `telebot` para interagir com a API do Telegram e `re` para realizar operações de expressão regular.

2. ```python
   TOKEN = "SEU_TOKEN"  # Substitua pelo token do seu bot
   bot = telebot.TeleBot(TOKEN)
   ```
   - Define o token do bot do Telegram e inicializa o bot.

3. ```python
   @bot.message_handler(func=lambda message: True)
   def anti_spam(message):
       ...
   ```
   - Define um manipulador de mensagens que será chamado para todas as mensagens recebidas.

4. ```python
   user_id = message.from_user.id
   chat_id = message.chat.id
   text = message.text
   ```
   - Obtém o ID do usuário que enviou a mensagem, o ID do chat em que a mensagem foi enviada e o texto da mensagem.

5. ```python
   if not message.from_user.is_bot:
       ...
   ```
   - Verifica se o remetente da mensagem não é um bot.

6. ```python
   member = bot.get_chat_member(chat_id, user_id)
   if not member.status in ["creator", "administrator"]:
       ...
   ```
   - Verifica se o remetente não é um administrador ou criador do grupo.

7. ```python
   if re.search(r'http[s]?://[^\s<>"]+|www\.[^\s<>"]+', text):
       ...
   ```
   - Utiliza uma expressão regular para verificar se a mensagem contém algum tipo de link.

8. ```python
   bot.delete_message(chat_id, message.message_id)
   bot.kick_chat_member(chat_id, user_id)
   bot.send_message(chat_id, f"Usuário @{message.from_user.username} foi banido por enviar spam.")
   ```
   - Se um link for encontrado na mensagem, exclui a mensagem, bane o usuário que enviou a mensagem e envia uma mensagem de aviso ao grupo.

9. ```python
   if __name__ == '__main__':
       print("Bot Anti-Spam Iniciado!")
       bot.polling()
   ```
   - Inicia o bot e imprime uma mensagem indicando que o bot anti-spam foi iniciado.

