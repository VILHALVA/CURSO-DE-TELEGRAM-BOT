# ENVIANDO ENQUETE
## DESCRIÇÃO:
Este bot foi desenvolvido para enviar uma enquete quando o comando "/enquete" é enviado em um grupo ou supergrupo no Telegram. Ao receber o comando, o bot verifica se a mensagem foi enviada em um contexto de grupo. Se sim, ele cria uma enquete com a pergunta "Qual é a sua cor favorita?" e as opções "Vermelho", "Verde" e "Azul", e a envia para o grupo. Se o comando for enviado em um chat privado, o bot responderá informando que o comando só pode ser usado em grupos.

## EXPLICAÇÃO:
1. **Importações:**
   ```python
   import telebot
   from TOKEN import TOKEN
   ```
   - `telebot`: Biblioteca para interagir com a API do Telegram e criar bots.
   - `TOKEN`: Constante que armazena o token de acesso do bot, importada de um arquivo `TOKEN.py`.

2. **Inicialização do Bot:**
   ```python
   bot = telebot.TeleBot(TOKEN)
   ```
   - Criação de uma instância do bot utilizando o token de acesso.

3. **Handler para o Comando `/enquete`:**
   ```python
   @bot.message_handler(commands=['enquete'])
   def enviar_enquete(message):
       # Verificar se a mensagem veio de um grupo ou supergrupo
       if message.chat.type == 'group' or message.chat.type == 'supergroup':
           # Definir o texto da enquete e as opções
           enquete_texto = "Qual é a sua cor favorita?"
           opcoes = ["Vermelho", "Verde", "Azul"]
           # Enviar a enquete para o grupo ou supergrupo
           bot.send_poll(message.chat.id, enquete_texto, options=opcoes, is_anonymous=False)
       else:
           # Responder ao remetente se o comando for usado em um chat privado
           bot.reply_to(message, "Esse comando só pode ser usado em grupos ou supergrupos!")
   ```
   - O decorator `@bot.message_handler(commands=['enquete'])` define uma função para lidar com mensagens que começam com o comando `/enquete`.
   - Dentro da função `enviar_enquete`, é verificado se a mensagem veio de um grupo ou supergrupo.
   - Se sim, é definido o texto da enquete e as opções.
   - Em seguida, a enquete é enviada para o grupo ou supergrupo usando o método `bot.send_poll`.
   - Se o comando for usado em um chat privado, o bot responde informando que o comando só pode ser usado em grupos ou supergrupos.

4. **Início do Polling:**
   ```python
   bot.polling()
   ```
   - Inicia o polling para receber atualizações do Telegram e manter o bot ativo.


