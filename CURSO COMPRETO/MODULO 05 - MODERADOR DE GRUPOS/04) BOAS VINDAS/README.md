# BOAS VINDAS
## DESCRIÇÃO
Este bot é um moderador de grupo para o Telegram que realiza as seguintes funções:

1. **Boas-Vindas Personalizadas**: Quando um novo membro entra no grupo, o bot saúda o membro com uma mensagem de boas-vindas personalizada, incluindo o nome do membro, seu ID e o nome do grupo.

2. **Canal Parceiro**: Além da mensagem de boas-vindas, o bot inclui um botão inline que leva os novos membros a um canal parceiro.

3. **Exclusão Automática**: Para manter o chat do grupo limpo, o bot programa automaticamente a exclusão da mensagem de boas-vindas após 1 minuto.

## EXPLICAÇÃO
1. ```python
   import telebot
   import time
   from telebot import types
   ```
   - Importa as bibliotecas necessárias: `telebot` para criar o bot do Telegram, `time` para controlar o tempo e `types` para lidar com tipos de mensagem do Telegram, como botões inline.

2. ```python
   TOKEN = 'SEU_TOKEN_AQUI'
   bot = telebot.TeleBot(TOKEN)
   ```
   - Define o token do bot e inicializa o objeto `TeleBot` passando o token.

3. ```python
   @bot.message_handler(func=lambda message: message.new_chat_members is not None)
   def welcome_new_members(message):
       ...
   ```
   - Define um manipulador de mensagens que é acionado sempre que novos membros entram no grupo. A função `welcome_new_members` é chamada quando `message.new_chat_members` não é `None`, ou seja, quando novos membros entram no grupo.

4. ```python
   for member in message.new_chat_members:
   ```
   - Itera sobre a lista de novos membros do grupo.

5. ```python
   member_name = member.first_name
   member_id = member.id
   group_name = message.chat.title
   ```
   - Obtém o nome, ID do membro recém-chegado e o nome do grupo onde a mensagem foi enviada.

6. ```python
   welcome_message = f"Bem-vindo(a) ao grupo {group_name}, {member_name} (ID: {member_id})!\n\n" \
                     "Confira nosso canal parceiro:"
   ```
   - Cria uma mensagem de boas-vindas personalizada que inclui o nome do grupo, o nome do novo membro e um convite para conferir o canal parceiro.

7. ```python
   inline_button = types.InlineKeyboardMarkup()
   inline_button.add(types.InlineKeyboardButton(text="Canal Parceiro", url="https://t.me/DIVULGACAO2023"))
   ```
   - Cria um botão inline com o texto "Canal Parceiro" e o link para o canal parceiro.

8. ```python
   sent_message = bot.send_message(message.chat.id, welcome_message, reply_markup=inline_button)
   ```
   - Envia a mensagem de boas-vindas com o botão inline para o chat onde o novo membro entrou.

9. ```python
   time.sleep(60)
   bot.delete_message(message.chat.id, sent_message.message_id)
   ```
   - Aguarda 60 segundos usando `time.sleep` e, em seguida, exclui a mensagem de boas-vindas usando `bot.delete_message`.

10. ```python
    if __name__ == '__main__':
        bot.polling()
    ```
    - Inicia o bot para começar a receber e enviar mensagens.

## OBSERVAÇÃO
Esse bot é uma adição útil para grupos do Telegram que desejam receber novos membros de uma forma amigável e fornecer informações sobre um canal parceiro. Além disso, ajuda a manter o grupo organizado, removendo automaticamente as mensagens de boas-vindas após um curto período de tempo. Para utilizá-lo, basta adicionar o bot ao grupo e configurar o token do bot e o URL do canal parceiro no código.

Lembre-se de configurar as permissões do bot para enviar mensagens e excluir mensagens no grupo.