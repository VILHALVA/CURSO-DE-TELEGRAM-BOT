# PALAVRAS PROIBIDAS
## DESCRIÇÃO:
O Anti-Palavras Proibidas é um bot de moderação para grupos do Telegram que detecta e penaliza usuários que enviam mensagens contendo palavras proibidas. Ele mantém uma lista de palavras proibidas em um arquivo JSON e verifica todas as mensagens enviadas pelos membros do grupo em busca dessas palavras. Quando uma palavra proibida é encontrada, o bot apaga a mensagem do usuário e, opcionalmente, pode silenciar ou banir o usuário do grupo, dependendo da configuração. Além disso, ele envia uma mensagem no grupo informando que o usuário foi penalizado.

1. Detecta automaticamente mensagens contendo palavras proibidas.
2. Apaga a mensagem do usuário que enviou a palavra proibida.
3. Pode silenciar ou banir o usuário, dependendo da configuração.
4. Envia uma mensagem no grupo informando sobre a penalização do usuário.
5. Mantém uma lista de palavras proibidas em um arquivo JSON, permitindo fácil personalização.

## COMO USAR?
1. **Banir Usuário**: Se você deseja banir um usuário quando uma palavra proibida é detectada, você pode usar a função `bot.kick_chat_member(chat_id, user_id)` para banir o usuário do grupo. Você precisa obter o `chat_id` e o `user_id` da mensagem que contém a palavra proibida.

2. **Silenciar Usuário**: Se preferir silenciar um usuário em vez de banir, você pode usar a função `bot.restrict_chat_member(chat_id, user_id, can_send_messages=False)` para restringir as permissões de envio de mensagens do usuário. Isso silenciará o usuário, impedindo-o de enviar mensagens no grupo.

3. **WORD.json**: No arquivo `WORD.json`, você pode mapear as palavras proibidas para a ação que deseja executar quando essas palavras forem detectadas. Por exemplo:

```json
{
    "palavra1": "banir",
    "palavra2": "silenciar"
}
```

Nesse exemplo, quando o bot detectar a palavra "palavra1", ele banirá o usuário; quando detectar a palavra "palavra2", ele silenciará o usuário; e assim por diante.

## EXPLICAÇÃO:
1. ```python
   import telebot
   import json
   import re
   ```
   - Importa os módulos necessários: `telebot` para interagir com a API do Telegram, `json` para lidar com arquivos JSON e `re` para operações de expressão regular.

2. ```python
   TOKEN = "SEU_TOKEN"  # Substitua pelo token do seu bot
   bot = telebot.TeleBot(TOKEN)
   ```
   - Define o token do bot do Telegram e inicializa o bot.

3. ```python
   with open("WORD.json", "r", encoding="utf-8") as file:
       banned_words = json.load(file)
   ```
   - Carrega as palavras proibidas e suas ações do arquivo JSON `WORD.json`.

4. ```python
   def check_banned_words(message):
       ...
   ```
   - Define uma função para verificar as palavras proibidas nas mensagens.

5. ```python
   def ban_user(chat_id, user_id):
       ...
   ```
   - Define uma função para banir um usuário do grupo.

6. ```python
   def silence_user(chat_id, user_id):
       ...
   ```
   - Define uma função para silenciar um usuário do grupo.

7. ```python
   @bot.message_handler(func=lambda message: True)
   def handle_message(message):
       ...
   ```
   - Define um manipulador de mensagens que será chamado para todas as mensagens recebidas.

8. ```python
   chat_id = message.chat.id
   user_id = message.from_user.id
   user_name = message.from_user.username
   ```
   - Obtém o ID do chat, o ID do usuário que enviou a mensagem e o nome de usuário do remetente da mensagem.

9. ```python
   action = check_banned_words(message)
   ```
   - Chama a função `check_banned_words` para verificar as palavras proibidas na mensagem.

10. ```python
    if action:
        ...
    ```
    - Verifica se alguma palavra proibida foi encontrada na mensagem.

11. ```python
    chat_admins = bot.get_chat_administrators(chat_id)
    admin_ids = [admin.user.id for admin in chat_admins]
    ```
    - Obtém uma lista de IDs dos administradores do grupo.

12. ```python
    if user_id in admin_ids:
        ...
    ```
    - Verifica se o remetente da mensagem é um administrador do grupo.

13. ```python
    else:
        ...
    ```
    - Se o remetente da mensagem não for um administrador, executa a ação associada à palavra proibida.

14. ```python
    bot.delete_message(chat_id, message.message_id)
    ```
    - Remove a mensagem que contém a palavra proibida.

15. ```python
    bot.send_message(chat_id, f"O usuário @{user_name} foi penalizado por enviar uma mensagem com conteúdo proibido.")
    ```
    - Envia uma mensagem no grupo informando sobre a penalização do usuário.

16. ```python
    bot.polling()
    ```
    - Inicia o bot, permitindo que ele receba e envie mensagens.



