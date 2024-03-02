# BOTÕES INLINE 2
## DESCRIÇÃO:
Esse é um bot que envia uma mensagem quando um usuário clica em um botão inline.

## EXPLICAÇÃO:
1. **Função `button_handler`:**
   ```python
   def button_handler(update, context):
       query = update.callback_query
       query.answer()
       query.edit_message_text(text="Você clicou no botão!")
   ```
   - Esta função é chamada sempre que um botão inline é pressionado.
   - `update.callback_query` contém informações sobre a consulta do botão.
   - `query.answer()` envia uma resposta de confirmação para o Telegram.
   - `query.edit_message_text()` atualiza a mensagem original com um novo texto, neste caso, "Você clicou no botão!".

2. **Função `send_inline_button`:**
   ```python
   def send_inline_button(update, context):
       keyboard = [[InlineKeyboardButton("Clique aqui", callback_data='button_clicked')]]
       reply_markup = InlineKeyboardMarkup(keyboard)
       update.message.reply_text('Clique no botão abaixo:', reply_markup=reply_markup)
   ```
   - Esta função é chamada quando o comando "/start" é enviado ao bot.
   - Ela cria um teclado inline com um único botão "Clique aqui" que possui o `callback_data` definido como 'button_clicked'.
   - Em seguida, responde ao usuário com a mensagem "Clique no botão abaixo:" e envia o teclado inline.

3. **Registro dos handlers:**
   ```python
   updater.dispatcher.add_handler(CallbackQueryHandler(button_handler))
   updater.dispatcher.add_handler(CommandHandler('start', send_inline_button))
   ```
   - O `CallbackQueryHandler` é usado para lidar com as consultas dos botões inline. Quando um botão é pressionado, ele chama a função `button_handler`.
   - O `CommandHandler` é usado para lidar com comandos enviados pelo usuário. Quando o usuário envia "/start", ele chama a função `send_inline_button`.

Juntos, essas funções e handlers permitem que o bot envie uma mensagem inicial com um botão inline "Clique aqui". Quando o botão é clicado, a mensagem é atualizada para indicar que o botão foi pressionado.