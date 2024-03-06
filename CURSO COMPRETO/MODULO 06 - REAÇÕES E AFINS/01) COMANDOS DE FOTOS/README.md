# COMANDOS DE FOTOS
## DESCRIÇÃO:
Este bot é um simples bot de Telegram que responde a três comandos diferentes ("/alegria", "/tristeza" e "/raiva") enviando imagens correspondentes de acordo com o comando solicitado. Ele foi projetado para fornecer uma experiência interativa aos usuários, permitindo-lhes expressar diferentes emoções através de imagens. Ao enviar um desses comandos, o bot responde imediatamente com a imagem associada à emoção especificada no comando.

## EXPLICAÇÃO:
```python
import os
import telebot
from TOKEN import *
```
1. `import os`: Importa o módulo os, que fornece funções para interagir com o sistema operacional.
2. `import telebot`: Importa a biblioteca Telebot, que é usada para interagir com a API do Telegram.
3. `from TOKEN import *`: Importa o token do bot a partir de um arquivo chamado TOKEN para garantir segurança.

```python
bot = telebot.TeleBot(TOKEN)
```
Cria uma instância do bot Telebot usando o token importado.

```python
MEDIA_DIR = "MIDIAS"
```
Define o diretório onde as imagens estão armazenadas.

```python
comandos_imagens = {
    "/alegria": "alegria.png",
    "/tristeza": "tristeza.png",
    "/raiva": "raiva.png"
}
```
Um dicionário que mapeia os comandos para os nomes dos arquivos de imagem correspondentes.

```python
@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.reply_to(message, "Olá! Envie um dos seguintes comandos para ver uma imagem: /alegria, /tristeza, /raiva")
```
Define um handler para o comando "/start". Quando o comando "/start" é enviado, esta função responde com uma mensagem explicando como usar os comandos.

```python
@bot.message_handler(commands=['alegria', 'tristeza', 'raiva'])
def handle_command(message):
    command = message.text.split()[0]  # Obtém o comando digitado pelo usuário
    if command in comandos_imagens:
        file_name = comandos_imagens[command]
        file_path = os.path.join(MEDIA_DIR, file_name)
        if os.path.exists(file_path):
            photo = open(file_path, 'rb')
            bot.send_photo(message.chat.id, photo)
        else:
            bot.reply_to(message, "Desculpe, imagem não encontrada.")
    else:
        bot.reply_to(message, "Comando inválido. Por favor, use /alegria, /tristeza ou /raiva.")
```
Define um handler para os comandos que têm imagens correspondentes. Quando um desses comandos é enviado, esta função envia a imagem correspondente ao usuário.

```python
bot.polling()
```
Inicia o processo de polling para receber e responder às mensagens.

