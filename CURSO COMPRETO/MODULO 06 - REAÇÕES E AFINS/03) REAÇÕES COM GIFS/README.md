# REAÇÕES COM GIFS
## DESCRIÇÃO:
Este bot é um assistente de mensagens que responde a palavras-chave específicas encontradas nas mensagens dos usuários. Ele é projetado para enviar arquivos MP4 em resposta a determinadas palavras-chave. O bot carrega as palavras-chave e os nomes dos arquivos MP4 correspondentes de um arquivo JSON chamado "WORD.json". Quando uma mensagem contendo uma palavra-chave é recebida, o bot verifica se existe um arquivo MP4 correspondente no diretório "MIDIAS" e o envia como resposta. Se o arquivo de mídia correspondente não for encontrado, uma mensagem de erro será enviada ao usuário.

## EXPLICAÇÃO:
1. ```python
   import telebot
   import json
   import os
   from TOKEN import *
   ```
   - `import telebot`: Importa a biblioteca Telebot, que é usada para interagir com a API do Telegram.
   - `import json`: Importa o módulo json, que é usado para trabalhar com dados no formato JSON.
   - `import os`: Importa o módulo os, que fornece funções para interagir com o sistema operacional.
   - `from TOKEN import *`: Importa o token do bot a partir de um arquivo chamado TOKEN para garantir segurança.

2. ```python
   bot = telebot.TeleBot(TOKEN)
   ```
   - Cria uma instância do bot Telebot usando o token importado.

3. ```python
   def load_responses():
       with open("WORD.json", "r", encoding="utf-8") as file:
           return json.load(file)
   
   responses = load_responses()
   ```
   - Define uma função chamada `load_responses()` que lê o arquivo JSON "WORD.json" contendo as associações entre palavras-chave e nomes de arquivos de vídeo. Carrega essas associações em um dicionário chamado `responses`.

4. ```python
   def should_respond(message):
       for keyword in responses.keys():
           if keyword.lower() in message.text.lower():
               return True
       return False
   ```
   - Define uma função chamada `should_respond()` que verifica se a mensagem contém uma palavra-chave para a qual o bot deve responder. Ele itera sobre as chaves do dicionário `responses` e verifica se alguma delas está presente na mensagem.

5. ```python
   @bot.message_handler(func=lambda message: should_respond(message))
   def handle_message(message):
       for keyword, media_file in responses.items():
           if keyword.lower() in message.text.lower():
               # Verifica se o arquivo de mídia existe
               if os.path.exists(f"MIDIAS/{media_file}"):
                   # Envia o arquivo de mídia MP4
                   bot.send_video(message.chat.id, open(f"MIDIAS/{media_file}", 'rb'))
               else:
                   bot.reply_to(message, "Desculpe, não consegui encontrar o arquivo de mídia correspondente.")
               break
   ```
   - Define um manipulador de mensagens que será acionado quando uma mensagem for recebida. Ele verifica se a mensagem deve ser respondida usando a função `should_respond()` e, em seguida, itera sobre as palavras-chave no dicionário `responses`. Se uma palavra-chave correspondente for encontrada na mensagem, o bot envia o vídeo correspondente para o chat onde a mensagem foi recebida.

6. ```python
   if __name__ == '__main__':
       bot.infinity_polling()
   ```
   - Inicia o processo de polling para receber e responder às mensagens. Se o script for executado como um programa principal, ele iniciará o bot.

