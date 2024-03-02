# REVERSOR - MENSAGEM REVERSA
## DESCRIÇÃO:
Este é um bot simples do Telegram criado em Python que recebe uma mensagem do usuário e retorna a mesma mensagem ao contrário.

1. O usuário envia uma mensagem para o bot.
2. O bot recebe a mensagem e inverte a ordem dos caracteres.
3. O bot envia a mensagem invertida de volta para o usuário.

## EXPLICAÇÃO:
Esse bot define um handler para mensagens de texto recebidas pelo bot do Telegram, que reverte o texto da mensagem e responde ao remetente com o texto revertido. Vamos entender o código em detalhes:

1. **Handler de Mensagem:**
   ```python
   @bot.message_handler(func=lambda message: True)
   def reverse_message(message):
       user_message = message.text
       reversed_message = user_message[::-1]
       bot.reply_to(message, reversed_message)
   ```
   - Este código cria um handler para todas as mensagens de texto recebidas pelo bot (`func=lambda message: True`). Isso significa que a função `reverse_message` será acionada para qualquer mensagem de texto que o bot receber.
  
2. **Revertendo a Mensagem:**
   ```python
   user_message = message.text
   reversed_message = user_message[::-1]
   ```
   - Ele obtém o texto da mensagem do usuário usando `message.text`.
   - Em seguida, reverte o texto usando a técnica de slicing do Python (`[::-1]`), que inverte a ordem dos elementos em uma lista ou sequência. Neste caso, inverte a ordem dos caracteres no texto da mensagem.

3. **Resposta do Bot:**
   ```python
   bot.reply_to(message, reversed_message)
   ```
   - Por fim, o bot responde ao remetente com o texto revertido.
   - `bot.reply_to` é usado para enviar uma mensagem de resposta ao mesmo chat de onde veio a mensagem original (`message`).
   - A mensagem de resposta é o texto revertido (`reversed_message`).

Portanto, quando um usuário enviar uma mensagem de texto para o bot, o bot responderá com a versão revertida da mensagem original. Por exemplo, se o usuário enviar "Olá, mundo!", o bot responderá com "!odnum ,álO".
