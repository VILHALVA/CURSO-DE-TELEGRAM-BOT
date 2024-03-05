# COMANDOS DE ADM COM VALIDAÇÃO
## DESCRIÇÃO:
O bot é um assistente de moderação para grupos no Telegram. Ele permite que os administradores gerenciem o comportamento dos usuários dentro do grupo. As principais funcionalidades do bot incluem:

1. Banir usuários: Os administradores podem usar o comando `/ban` para banir um usuário do grupo.
2. Silenciar usuários: Os administradores podem usar o comando `/mute` para silenciar um usuário, impedindo-o de enviar mensagens no grupo.
3. Expulsar usuários: Os administradores podem usar o comando `/kick` para expulsar um usuário temporariamente do grupo.

O bot ajuda a manter a ordem e a segurança dentro do grupo, permitindo que os administradores tomem medidas rápidas e eficazes contra comportamentos indesejados.

## EXPLICAÇÃO (COMANDOS.PY):
Este arquivo define uma função chamada `COMANDOS` que recebe o objeto `bot` como argumento. Dentro dessa função, são definidos quatro manipuladores de mensagens para diferentes comandos de moderação (`/ban`, `/mute`, `/kick` e `/warn`). Aqui está uma explicação linha por linha do código:

1. ```python
   def COMANDOS(bot):
   ```
   - Define uma função chamada `COMANDOS` que recebe um objeto `bot` como argumento.

2. ```python
   @bot.message_handler(commands=['ban'])
   def ban_user(message):
       ...
   ```
   - Define um manipulador de mensagens para o comando `/ban`. Este manipulador será chamado sempre que o bot receber uma mensagem com o comando `/ban`.

3. ```python
   user_id = message.from_user.id
   chat_id = message.chat.id
   user_to_ban = message.reply_to_message.from_user.id
   ```
   - Obtém o ID do usuário que enviou a mensagem, o ID do chat onde a mensagem foi enviada e o ID do usuário que está sendo respondido (se houver).

4. ```python
   bot.kick_chat_member(chat_id, user_to_ban)
   bot.send_message(chat_id, f"Usuário {user_to_ban} foi banido!")
   ```
   - Bane o usuário alvo do chat usando o método `kick_chat_member` e envia uma mensagem informando que o usuário foi banido usando `send_message`.

5. Os manipuladores de mensagens para os comandos `/mute` e `/kick` seguem a mesma lógica, mas com ações de silenciar (`restrict_chat_member`) e expulsar (`kick_chat_member`) o usuário alvo, respectivamente. Além disso, eles enviam mensagens informando sobre a ação realizada.

Essa função `COMANDOS` pode ser chamada passando o objeto `bot` como argumento para definir os manipuladores de mensagens para os comandos de moderação no seu bot do Telegram.