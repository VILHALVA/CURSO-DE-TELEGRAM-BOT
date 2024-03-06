# REAÇÕES COM PACOTES DE STICKERS
## DESCRIÇÃO:
Este bot é projetado para responder a mensagens com stickers aleatórios com base em palavras-chave encontradas na mensagem. Ele carrega as palavras-chave e os URLs dos pacotes de stickers a partir de um arquivo JSON chamado "WORD.json". Quando uma mensagem contendo uma palavra-chave é recebida, o bot envia um sticker aleatório do pacote correspondente associado à palavra-chave.

## EXPLICAÇÃO:
1. Importações:
```python
import telebot
import json
import random
from TOKEN import *
```
- `import telebot`: Importa a biblioteca Telebot, que é usada para interagir com a API do Telegram.
- `import json`: Importa o módulo json, que é usado para trabalhar com dados no formato JSON.
- `import random`: Importa o módulo random, que é usado para gerar números aleatórios.
- `from TOKEN import *`: Importa o token do bot a partir de um arquivo chamado TOKEN para garantir segurança.

2. Criação do objeto bot:
```python
bot = telebot.TeleBot(TOKEN)
```
- Cria uma instância do bot Telebot usando o token importado.

3. Carregamento das respostas do arquivo JSON:
```python
def load_responses():
    with open("WORD.json", "r", encoding="utf-8") as file:
        return json.load(file)

responses = load_responses()
```
- Define uma função chamada `load_responses()` que lê o arquivo JSON "WORD.json" contendo as associações entre palavras-chave e URLs de pacotes de stickers. Carrega essas associações em um dicionário chamado `responses`.

4. Função para verificar se a mensagem contém uma palavra-chave:
```python
def should_respond(message):
    for keyword in responses.keys():
        if keyword.lower() in message.text.lower():
            return True
    return False
```
- Define uma função chamada `should_respond()` que verifica se a mensagem contém uma palavra-chave para a qual o bot deve responder. Ele itera sobre as chaves do dicionário `responses` e verifica se alguma delas está presente na mensagem.

5. Manipulador de mensagens:
```python
@bot.message_handler(func=lambda message: should_respond(message))
def handle_message(message):
    for keyword, sticker_pack_url in responses.items():
        if keyword.lower() in message.text.lower():
            # Envia um sticker aleatório do pacote
            bot.send_sticker(message.chat.id, sticker_pack_url)
            break
```
- Define um manipulador de mensagens que será acionado quando uma mensagem for recebida. Ele verifica se a mensagem deve ser respondida usando a função `should_respond()` e, em seguida, itera sobre as palavras-chave no dicionário `responses`. Se uma palavra-chave correspondente for encontrada na mensagem, o bot envia um sticker aleatório do pacote associado.

6. Início do polling:
```python
if __name__ == '__main__':
    bot.infinity_polling()
```
- Inicia o processo de polling para receber e responder às mensagens. Se o script for executado como um programa principal, ele iniciará o bot.

