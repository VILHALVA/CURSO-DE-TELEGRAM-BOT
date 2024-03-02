# MENSAGEIRO
## [CODIGO 1](CODIGOS/CODIGO_1.py):
### DESCRIÇÃO:
Este é um bot para Telegram desenvolvido em Python, usando a biblioteca telebot, que permite enviar recados para grupos do Telegram.
### EXPLICAÇÃO:
Para enviar uma mensagem para um grupo específico usando o `python-telegram-bot`, você precisa da ID desse grupo. Aqui está como você pode fazer isso:

1. Primeiro, você precisa encontrar o ID do grupo para o qual deseja enviar a mensagem. Você pode fazer isso adicionando o seu bot ao grupo e, em seguida, enviando o comando `/getgroupid` ao grupo. Este comando geralmente é configurado no seu código Python para responder com a ID do grupo.

2. Depois de ter a ID do grupo, você pode usar o método `send_message` do seu bot para enviar a mensagem para esse grupo. Aqui está um exemplo:

```python
chat_id = "ID_DO_GRUPO_AQUI"  # Substitua "ID_DO_GRUPO_AQUI" pela ID do grupo

# Enviando a mensagem para o grupo
bot.send_message(chat_id, "TEXTO_DA_MENSAGEM_AQUI")
```

Certifique-se de substituir `"ID_DO_GRUPO_AQUI"` pela ID real do grupo e `"TEXTO_DA_MENSAGEM_AQUI"` pelo texto da mensagem que você deseja enviar. Este trecho de código enviará a mensagem para o grupo específico com a ID fornecida.

## [CODIGO 2](CODIGOS/CODIGO_2.py):
### DESCRIÇÃO:
- O bot é capaz de responder a qualquer mensagem que você digitar na interface gráfica.
- As mensagens enviadas e recebidas são exibidas na janela.
- A interface gráfica inclui uma entrada para digitar mensagens e um botão para enviá-las.
### EXPLICAÇÃO:
Esse é um exemplo de como criar uma interface gráfica simples para interagir com um bot do Telegram usando a biblioteca `telebot` e `tkinter` em Python. 

1. **Configuração do Bot do Telegram:**
   ```python
   TOKEN = "SEU_TOKEN_AQUI"
   bot = telebot.TeleBot(TOKEN)
   ```
   - Você precisa substituir `"SEU_TOKEN_AQUI"` pelo token do seu bot do Telegram.

2. **Função `echo_all`:**
   ```python
   @bot.message_handler(func=lambda message: True)
   def echo_all(message):
       resposta = f"Bot: Você disse '{message.text}'"
       update_chat(resposta)
   ```
   - Esta função é chamada sempre que o bot recebe uma mensagem.
   - Ela responde à mensagem do usuário com uma mensagem padrão indicando o que o usuário disse.

3. **Função `update_chat`:**
   ```python
   def update_chat(message):
       chat_text.config(state=tk.NORMAL)
       chat_text.insert(tk.END, message + "\n")
       chat_text.config(state=tk.DISABLED)
       chat_text.see(tk.END)
   ```
   - Esta função atualiza a janela de chat com a mensagem fornecida.
   - Ela insere a mensagem na caixa de texto e rola automaticamente para a última mensagem.

4. **Função `enviar_mensagem`:**
   ```python
   def enviar_mensagem():
       mensagem = entrada_mensagem.get()
       entrada_mensagem.delete(0, tk.END)
       update_chat(f"Você: {mensagem}")
       bot.send_message(chat_id, mensagem)
   ```
   - Esta função é chamada quando o botão "Enviar" é pressionado.
   - Ela recupera a mensagem digitada pelo usuário, limpa a entrada, atualiza o chat com a mensagem do usuário e envia a mensagem para o bot do Telegram.

5. **Configuração da Interface Gráfica (`tkinter`):**
   - Cria uma janela com a interface gráfica para o chat, entrada de mensagem e botão de envio.
   - Inicia o loop principal (`root.mainloop()`) para manter a janela aberta e interativa.

6. **ID do Chat/Grupo:**
   ```python
   chat_id = "ID_DO_CHAT_AQUI"
   ```
   - Você precisa substituir `"ID_DO_CHAT_AQUI"` pelo ID do chat ou grupo onde o bot responderá.

Este código cria uma interface gráfica simples onde você pode enviar mensagens para o bot do Telegram e ver as respostas do bot na janela. Certifique-se de substituir o token do bot e o ID do chat/grupo corretamente para que o código funcione conforme esperado. Se você não sabe como utilizar o `tkinter` para trabalhar com interface gráfica, [CLIQUE AQUI PARA FAZER O CURSO DE TKINTER](https://github.com/VILHALVA/CURSO-DE-TKINTER)

## [CODIGO 3](CODIGOS/CODIGO_3.py):
### DESCRIÇÃO:
- Os usuários podem iniciar uma conversa com o bot e se inscrever para receber mensagens de recados.
- O administrador do bot pode enviar mensagens de recados para todos os inscritos.
### EXPLICAÇÃO:
Este script Python cria um bot do Telegram que permite que um administrador envie mensagens de recado para todos os usuários que se inscreveram no bot. Vou explicar o funcionamento do código:

1. **Configuração de Logging:**
   ```python
   logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
   ```
   - Configura o formato e o nível de logging para o programa.

2. **Inicialização do Updater:**
   ```python
   token = 'YOUR_BOT_TOKEN'
   updater = Updater(token=token)
   ```
   - Substitua `'YOUR_BOT_TOKEN'` pelo token do seu bot. Isso inicializa o `Updater`, que é a parte central da biblioteca `python-telegram-bot` que recebe as atualizações do Telegram e envia comandos para os handlers correspondentes.

3. **Gerenciamento de Inscritos:**
   ```python
   subscribers = set()
   ```
   - Inicializa um conjunto vazio para armazenar os IDs dos usuários inscritos para receber mensagens de recado.

4. **Handler para o Comando "/start":**
   ```python
   def start(update, context):
       user_id = update.effective_user.id
       if user_id not in subscribers:
           subscribers.add(user_id)
           update.message.reply_text('Você foi inscrito para receber mensagens de recados!')
   ```
   - Esta função é chamada quando um usuário envia o comando "/start".
   - Ela verifica se o usuário já está inscrito. Se não estiver, adiciona o ID do usuário ao conjunto `subscribers` e envia uma mensagem confirmando a inscrição.

5. **Handler para o Comando "/send":**
   ```python
   def send(update, context):
       if update.effective_user.id == YOUR_ADMIN_USER_ID:
           message = ' '.join(context.args)
           for subscriber_id in subscribers:
               context.bot.send_message(subscriber_id, message)
           update.message.reply_text('Mensagem enviada para todos os inscritos!')
   ```
   - Esta função é chamada quando o administrador envia o comando "/send".
   - Ela verifica se o usuário que enviou o comando é o administrador (com base no ID do usuário).
   - Se for o administrador, a função envia a mensagem fornecida como argumento para todos os usuários inscritos.

6. **Registro dos Handlers:**
   ```python
   updater.dispatcher.add_handler(CommandHandler('start', start))
   updater.dispatcher.add_handler(CommandHandler('send', send))
   ```
   - Registra os handlers para os comandos "/start" e "/send".

7. **Início do Bot e Manutenção Ativa:**
   ```python
   updater.start_polling()
   updater.idle()
   ```
   - Inicia o bot, fazendo com que ele comece a buscar atualizações do Telegram e responda a comandos conforme configurado.
   - Mantém o bot em execução até que seja interrompido manualmente.

Certifique-se de substituir `'YOUR_BOT_TOKEN'` pelo token do seu bot e `YOUR_ADMIN_USER_ID` pelo ID do administrador real. Assim, o administrador pode enviar mensagens de recado para todos os usuários inscritos usando o comando "/send".


