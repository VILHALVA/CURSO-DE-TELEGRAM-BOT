# REAÇÕES COM FOTOS
## DESCRIÇÃO:
Este bot é um bot de resposta automática baseado em palavras-chave. Ele examina as mensagens recebidas em busca de palavras-chave especificadas em um arquivo JSON chamado "WORD.json". Quando uma palavra-chave é identificada na mensagem, o bot responde enviando uma imagem associada a essa palavra-chave, que está armazenada no diretório "MIDIAS". O bot funciona de forma autônoma, respondendo às mensagens em tempo real. Ele pode ser configurado facilmente modificando o conteúdo do arquivo JSON com novas palavras-chave e associando-as a imagens correspondentes.

## EXPLICAÇÃO:
```python
import telebot
import json
import os
from TOKEN import *
```
1. `import telebot`: Importa a biblioteca Telebot, que é usada para interagir com a API do Telegram.
2. `import json`: Importa o módulo json, que é usado para trabalhar com dados no formato JSON.
3. `import os`: Importa o módulo os, que fornece funções para interagir com o sistema operacional.
4. `from TOKEN import *`: Importa o token do bot a partir de um arquivo chamado TOKEN para garantir segurança.

```python
bot = telebot.TeleBot(TOKEN)
```
Cria uma instância do bot Telebot usando o token importado.

```python
def load_responses():
    with open("WORD.json", "r", encoding="utf-8") as file:
        return json.load(file)

responses = load_responses()
```
Define uma função chamada `load_responses()` que lê o arquivo JSON "WORD.json" contendo as associações entre palavras-chave e nomes de arquivos de imagem. Carrega essas associações em um dicionário chamado `responses`.

```python
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    for keyword, filename in responses.items():
        if keyword.lower() in message.text.lower():
            send_image(message.chat.id, filename)
            break
```
Define um handler para mensagens de texto. Itera sobre as palavras-chave no dicionário `responses` e verifica se alguma palavra-chave está presente na mensagem recebida. Se uma correspondência for encontrada, chama a função `send_image()` para enviar a imagem correspondente ao chat.

```python
def send_image(chat_id, filename):
    try:
        with open(os.path.join("MIDIAS", filename), "rb") as img:
            bot.send_photo(chat_id, img)
    except FileNotFoundError:
        print(f"Arquivo {filename} não encontrado.")
```
Define uma função chamada `send_image()` que envia uma imagem para o chat especificado pelo `chat_id`. Ele lê a imagem do arquivo com o nome `filename` no diretório "MIDIAS" e a envia usando `bot.send_photo()`. Se o arquivo não for encontrado, ele imprime uma mensagem de erro.

```python
if __name__ == '__main__':
    print("Bot em execução...")
    bot.polling()
```
Inicia o processo de polling para receber e responder às mensagens. Se o script for executado como um programa principal, ele iniciará o bot.

