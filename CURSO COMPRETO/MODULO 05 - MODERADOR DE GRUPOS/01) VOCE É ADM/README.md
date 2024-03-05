# VOCÊ É ADM DO GRUPO?
## DESCRIÇÃO:
- Este bot foi desenvolvido para verificar se o usuário que o aciona é um administrador de algum grupo do Telegram em que o bot também está presente. Quando o usuário envia o comando "/start" em um grupo, o bot verifica se ele é um administrador desse grupo. Se o usuário for um administrador, o bot responde com uma mensagem informando que o usuário é um administrador do grupo em questão, juntamente com o nome do grupo. Se o usuário não for um administrador de nenhum grupo, o bot responde com uma mensagem informando que o usuário não é um administrador de nenhum grupo. Este bot é útil para verificar rapidamente se o usuário tem permissões de administrador em algum grupo do Telegram em que o bot está presente.

## COMO ELE ENCONTRA OS ADMS?
O bot utiliza a função `get_chat_administrators(chat_id)` da biblioteca Telebot para obter a lista de administradores do grupo em que recebeu a mensagem. Essa função retorna uma lista de objetos `ChatMember`, que representam os administradores do grupo.

Em seguida, o bot verifica se o ID do usuário que enviou a mensagem está presente na lista de IDs dos administradores do grupo. Se estiver, significa que o usuário é um administrador do mesmo, e o bot reconhece isso. Se não estiver, o bot assume que o usuário não é um administrador do mesmo.

Dessa forma, o bot consegue determinar se o usuário que o acionou é um administrador do grupo em questão, permitindo que ele envie uma resposta apropriada.

## EXPLICAÇÃO:
1. ```python
   from TOKEN import *
   import telebot
   ```
   - Importa o token do bot do arquivo `TOKEN.py` e a biblioteca Telebot.

2. ```python
   bot = telebot.TeleBot(TOKEN)
   ```
   - Inicializa o bot do Telegram com o token fornecido.

3. ```python
   @bot.message_handler(commands=['start'])
   def start(message):
       ...
   ```
   - Define um manipulador de mensagens para o comando `/start`. Este manipulador será chamado sempre que o bot receber uma mensagem com o comando `/start`.

4. ```python
   user_id = message.from_user.id
   ```
   - Obtém o ID do usuário que enviou a mensagem.

5. ```python
   if message.chat.type in ["group", "supergroup", "channel"]:
       ...
   ```
   - Verifica se a mensagem foi enviada de um chat em grupo, supergrupo ou canal.

6. ```python
   chat_admins = bot.get_chat_administrators(message.chat.id)
   admin_ids = [admin.user.id for admin in chat_admins]
   ```
   - Obtém uma lista de IDs de usuários que são administradores do grupo.

7. ```python
   if user_id in admin_ids:
       ...
   ```
   - Verifica se o ID do usuário que enviou a mensagem está na lista de IDs de administradores do grupo.

8. ```python
   chat_info = bot.get_chat(message.chat.id)
   group_name = chat_info.title
   ```
   - Obtém informações sobre o grupo, incluindo o nome do grupo.

9. ```python
   bot.reply_to(message, f"SIM. VOCÊ É ADM DO GRUPO {group_name}!")
   ```
   - Responde à mensagem informando que o usuário é um administrador do grupo e exibe o nome do grupo.

10. ```python
    bot.reply_to(message, "VOCÊ NÃO É ADM DESSE GRUPO!")
    ```
    - Responde à mensagem informando que o usuário não é um administrador do grupo.

11. ```python
    bot.polling()
    ```
    - Inicia o bot, aguardando por atualizações.

## TUDO COMEÇA AQUI:
Nos próximos bots do módulo de moderação de grupos, podemos utilizar este código como parte do processo de validação de usuários que desejam configurar os bots de moderação. A validação do usuário pode ser feita antes de conceder acesso às funcionalidades de configuração do bot.

Por exemplo, ao receber o comando de configuração de um bot de moderação, o bot pode primeiro verificar se o usuário que enviou o comando é um administrador do grupo. Se o usuário for um administrador, o bot pode permitir que ele prossiga com a configuração do bot de moderação. Caso contrário, o bot pode responder informando que apenas administradores do grupo têm permissão para realizar essa configuração.

Essa abordagem garante que apenas administradores autorizados do grupo possam configurar e usar os bots de moderação, ajudando a manter a segurança e a integridade dos grupos do Telegram.