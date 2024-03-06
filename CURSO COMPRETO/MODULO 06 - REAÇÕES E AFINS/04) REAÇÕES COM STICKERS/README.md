# REAÇÕES COM STICKERS
## DESCRIÇÃO:
Este bot é um assistente de conversação que responde a mensagens contendo palavras-chave específicas com stickers correspondentes. Ele carrega as palavras-chave e os nomes dos arquivos de mídia a partir de um arquivo JSON chamado "WORD.json". Quando recebe uma mensagem, verifica se ela contém uma palavra-chave e, em caso afirmativo, procura o arquivo de mídia correspondente na pasta "MIDIAS". Se o arquivo for encontrado, o bot envia o sticker associado à palavra-chave encontrada. Se o arquivo de mídia não for encontrado, o bot responde dizendo que não conseguiu encontrar o arquivo correspondente.

## EXPLICAÇÃO:
1. Importações:
```python
import telebot
import json
import os
from TOKEN import *
```
- `import telebot`: Importa a biblioteca Telebot, que é usada para interagir com a API do Telegram.
- `import json`: Importa o módulo json, que é usado para trabalhar com dados no formato JSON.
- `import os`: Importa o módulo os, que fornece funções para interagir com o sistema operacional.
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
- Define uma função chamada `load_responses()` que lê o arquivo JSON "WORD.json" contendo as associações entre palavras-chave e nomes de arquivos de sticker. Carrega essas associações em um dicionário chamado `responses`.

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
    for keyword, media_file in responses.items():
        if keyword.lower() in message.text.lower():
            # Verifica se o arquivo de mídia existe
            if os.path.exists(f"MIDIAS/{media_file}"):
                # Envia o STICKER
                bot.send_sticker(message.chat.id, open(f"MIDIAS/{media_file}", 'rb'))
            else:
                bot.reply_to(message, "Desculpe, não consegui encontrar o arquivo de mídia correspondente.")
            break
```
- Define um manipulador de mensagens que será acionado quando uma mensagem for recebida. Ele verifica se a mensagem deve ser respondida usando a função `should_respond()` e, em seguida, itera sobre as palavras-chave no dicionário `responses`. Se uma palavra-chave correspondente for encontrada na mensagem, o bot envia o sticker correspondente para o chat onde a mensagem foi recebida.

6. Início do polling:
```python
if __name__ == '__main__':
    bot.infinity_polling()
```
- Inicia o processo de polling para receber e responder às mensagens. Se o script for executado como um programa principal, ele iniciará o bot.

