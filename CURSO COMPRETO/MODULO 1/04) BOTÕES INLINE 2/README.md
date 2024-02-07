# BOTÕES INLINE 2
## DESCRIÇÃO:
Esse é um bot que envia uma mensagem quando um usuário clica em um botão inline.

## FUNCIONAMENTO:
Vamos utilizar a classe InlineKeyboardButton para criar um botão inline e a classe InlineKeyboardMarkup para colocar esse botão em uma mensagem. Quando o usuário clicar no botão, o Telegram enviará uma consulta para o nosso bot, que deve responder com a mensagem desejada.

No código acima, a função send_inline_button cria um botão inline com o texto "Clique aqui" e o callback data "button_clicked". Em seguida, essa função envia uma mensagem para o usuário com o botão inline usando a função update.message.reply_text.

A função button_handler é registrada como um handler para consultas de botão inline usando a classe CallbackQueryHandler. Quando o usuário clica no botão, o Telegram envia uma consulta para o nosso bot contendo o callback data do botão. A função button_handler é executada para lidar com essa consulta, enviando uma mensagem com o texto "Você clicou no botão!" usando a função query.edit_message_text.

Por fim, registramos os handlers e iniciamos o bot usando as funções add_handler, start_polling e idle.

Com esse código, o usuário pode clicar no botão inline para receber a mensagem "Você clicou no botão!" do nosso bot.