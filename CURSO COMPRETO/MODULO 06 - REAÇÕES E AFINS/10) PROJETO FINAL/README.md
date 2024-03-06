# PROJETO FINAL: LIKEBOT
## DESCRIÇÃO:
Este é um bot que envia imagens para um canal e permite aos usuários reagirem a essas imagens com botões de reação (curtir ou descurtir).

## EXPLICAÇÃO (MAIN.PY):
1. **Importações:**
   ```python
   from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters, CallbackQueryHandler
   from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
   import os
   from LIKE_DB import LikeDB
   from TOKEN import *
   ```
   - `Updater`: Classe principal do `python-telegram-bot` que controla a comunicação com a API do Telegram.
   - `CommandHandler`, `MessageHandler`, `CallbackQueryHandler`: Manipuladores de eventos para lidar com comandos, mensagens e queries de callback, respectivamente.
   - `Filters`: Utilizado para filtrar mensagens.
   - `Update`: Classe que representa uma atualização recebida do Telegram.
   - `ReplyKeyboardMarkup`, `KeyboardButton`, `InlineKeyboardMarkup`, `InlineKeyboardButton`: Utilizados para criar teclados e botões de resposta.
   - `os`: Módulo para interagir com o sistema operacional.
   - `LikeDB`: Classe para interagir com o banco de dados de likes.
   - `TOKEN`: Token de acesso do bot, importado de um arquivo `TOKEN.py`.

2. **Inicialização:**
   ```python
   TOKEN = os.environ[TOKEN]

   like_db = LikeDB('likes.json')
   ```
   - O token é obtido a partir de uma variável de ambiente.
   - É criada uma instância de `LikeDB` para interagir com o banco de dados de likes.

3. **Handlers:**
   ```python
   def start(update: Update, context: CallbackContext):
       # Envia uma mensagem de boas-vindas
       update.message.reply_text("Hello World")

   def sendImage(update: Update, context: CallbackContext):
       # Obtém o ID da imagem
       image_id = update.message.photo[-1].file_id
       # Adiciona a imagem ao banco de dados de likes
       like_db.addImage(image_id)
       # Cria um teclado inline com botões de reação (curtir/descurtir)
       keyboard = InlineKeyboardMarkup([
           [InlineKeyboardButton("👍", callback_data='like'), InlineKeyboardButton("👎", callback_data='dislike')]
       ])
       # Envia a imagem para o canal com o teclado inline
       context.bot.send_photo(chat_id='@image_like', photo=image_id, caption="Hello World", reply_markup=keyboard)
       # Responde ao usuário que a imagem foi enviada com sucesso
       update.message.reply_text("Image has been sent to @image_like")
   ```
   - `start`: Função para lidar com o comando `/start`, envia uma mensagem de boas-vindas.
   - `sendImage`: Função para lidar com o envio de imagens, adiciona a imagem ao banco de dados, cria um teclado inline com botões de reação e envia a imagem para o canal.

4. **Configuração do Updater:**
   ```python
   updater = Updater(token=TOKEN)
   updater.dispatcher.add_handler(CommandHandler('start', start))
   updater.dispatcher.add_handler(MessageHandler(Filters.photo, sendImage))
   ```
   - Cria um objeto `Updater` passando o token.
   - Adiciona handlers para lidar com comandos e mensagens de foto.

5. **Início do Polling:**
   ```python
   updater.start_polling()
   updater.idle()
   ```
   - Inicia o polling para receber atualizações do Telegram.
   - `updater.idle()` mantém o bot ativo até que o programa seja encerrado.

## CREDITOS E MAIS:
* [ESSE BOT FOI CRIADO PELO "Backend-assignment"](https://github.com/Backend-assignment/LikeBot)
* [ESSE BOT FOI EDITADO PELO VILHALVA](https://github.com/VILHALVA)
* [VEJA O MANUAL CLICANDO AQUI](./MANUAL.md)