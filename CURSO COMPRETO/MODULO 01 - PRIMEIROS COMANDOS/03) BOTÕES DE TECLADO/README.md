# BOTÕES DE TECLADO
Os botões de teclado são semelhantes ao [@MANYBOT](https://t.me/Manybot). Eles são uma maneira eficaz de fornecer opções pré-definidas para que eles possam selecionar uma resposta com apenas um toque, tornando a interação mais intuitiva e amigável.

## EXPLICAÇÃO:
1. **Handler para o comando "/start":**
   ```python
   @bot.message_handler(commands=["start"])
   def start(message):
       markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
       item1 = types.KeyboardButton("Opção 1")
       item2 = types.KeyboardButton("Opção 2")
       markup.add(item1, item2)
       
       bot.send_message(message.chat.id, "Escolha uma opção:", reply_markup=markup)
   ```
   - Este código cria um handler para mensagens que começam com o comando "/start".
   - Quando o bot recebe o comando "/start", ele executa a função `start`.
   - A função `start` cria um teclado de resposta com duas opções ("Opção 1" e "Opção 2") utilizando `types.ReplyKeyboardMarkup`.
   - Em seguida, envia uma mensagem para o chat com o texto "Escolha uma opção:" e o teclado de resposta.

2. **Handler para qualquer mensagem:**
   ```python
   @bot.message_handler(func=lambda message: True)
   def handle_message(message):
       if message.text == "Opção 1":
           bot.send_message(message.chat.id, "Você selecionou a Opção 1.")
       elif message.text == "Opção 2":
           bot.send_message(message.chat.id, "Você selecionou a Opção 2.")
       else:
           bot.send_message(message.chat.id, "Por favor, escolha uma das opções.")
   ```
   - Este código cria um handler para qualquer mensagem que o bot recebe.
   - A função `handle_message` é executada sempre que o bot recebe uma mensagem.
   - Ele verifica se o texto da mensagem é "Opção 1" ou "Opção 2" e responde de acordo.
   - Se o texto da mensagem não corresponder a nenhuma das opções, ele envia uma mensagem solicitando ao usuário que escolha uma das opções disponíveis.

Essencialmente, este código permite que o bot ofereça duas opções ao usuário quando ele inicia uma conversa com o bot usando o comando "/start", e depois responde de acordo com a opção selecionada pelo usuário, independentemente da mensagem recebida.
