# BOTÕES INLINE 1
## DESCRIÇÃO:
Este exemplo de bot cria um teclado inline com dois botões, "Yes" e "No", e aguarda que os usuários pressionem um desses botões. Quando um botão é pressionado, o bot responde com uma mensagem indicando se a resposta é "Yes" ou "No" em POP-UP.

## EXPLICAÇÃO:
Este trecho de código Python é destinado a um bot do Telegram e é responsável por lidar com callback queries e mensagens enviadas pelos usuários. Vamos explicar cada parte:

1. **Função `gen_markup()`:**
   ```python
   def gen_markup():
       markup = InlineKeyboardMarkup()
       markup.row_width = 2
       markup.add(InlineKeyboardButton("Yes", callback_data="cb_yes"),
                  InlineKeyboardButton("No", callback_data="cb_no"))
       return markup
   ```
   - Esta função cria e retorna um teclado de marcação inline (InlineKeyboardMarkup).
   - O teclado é configurado com duas colunas (row_width = 2).
   - Duas opções são adicionadas ao teclado: "Yes" e "No", cada uma associada a um callback_data específico ("cb_yes" e "cb_no", respectivamente).

2. **Handler para callback queries:**
   ```python
   @bot.callback_query_handler(func=lambda call: True)
   def callback_query(call):
       if call.data == "cb_yes":
           bot.answer_callback_query(call.id, "Answer is Yes")
       elif call.data == "cb_no":
           bot.answer_callback_query(call.id, "Answer is No")
   ```
   - Este handler é acionado sempre que o bot recebe uma callback query (uma interação do usuário com um botão inline).
   - Ele verifica o callback_data associado à callback query e responde de acordo com o valor recebido. Se o callback_data for "cb_yes", ele responde "Answer is Yes"; se for "cb_no", responde "Answer is No".

3. **Handler para mensagens:**
   ```python
   @bot.message_handler(func=lambda message: True)
   def message_handler(message):
       bot.send_message(message.chat.id, "Yes/no?", reply_markup=gen_markup())
   ```
   - Este handler é acionado sempre que o bot recebe uma mensagem de texto de um usuário.
   - Ele envia uma mensagem para o chat, perguntando "Yes/no?", e inclui o teclado de marcação inline gerado pela função `gen_markup()` para que o usuário possa selecionar uma opção.

Em resumo, este código cria um bot que envia uma mensagem "Yes/no?" para o usuário, juntamente com opções "Yes" e "No" como botões inline. Quando o usuário seleciona uma opção, o bot responde com "Answer is Yes" ou "Answer is No" dependendo da opção escolhida.


