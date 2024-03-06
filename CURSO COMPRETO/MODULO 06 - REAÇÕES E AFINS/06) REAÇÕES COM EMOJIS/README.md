# REAÇÕES COM EMOJIS
## DESCRIÇÃO:
Este bot é um assistente de mensagens que responde a determinadas palavras-chave com emojis correspondentes. Ele funciona recebendo mensagens dos usuários e verificando se contêm alguma palavra-chave definida no arquivo JSON "WORD.json". Se a mensagem tiver uma correspondência, o bot enviará um emoji associado à palavra-chave como resposta.

## EXPLICAÇÃO:
1. **Importações:**
```python
import telebot
import json
from TOKEN import *
```
   - `telebot`: É a biblioteca utilizada para interagir com a API do Telegram.
   - `json`: É usada para trabalhar com dados no formato JSON.
   - `TOKEN`: É importado de um arquivo chamado `TOKEN.py`, que contém o token de acesso do bot. Isso é feito para proteger o token e evitar que seja compartilhado diretamente no código.

2. **Criação do objeto bot:**
```python
bot = telebot.TeleBot(TOKEN)
```
   - Cria uma instância do bot Telebot utilizando o token de acesso.

3. **Carregamento das respostas do arquivo JSON:**
```python
def load_responses():
    with open("WORD.json", "r", encoding="utf-8") as file:
        return json.load(file)

responses = load_responses()
```
   - Define uma função `load_responses()` para ler o arquivo JSON chamado "WORD.json" que contém as associações entre palavras-chave e emojis.
   - Carrega essas associações em um dicionário chamado `responses`.

4. **Função para verificar se a mensagem contém uma palavra-chave:**
```python
def should_respond(message):
    for keyword in responses.keys():
        if keyword.lower() in message.text.lower():
            return True
    return False
```
   - Define uma função `should_respond()` para verificar se a mensagem contém uma palavra-chave para a qual o bot deve responder.
   - Itera sobre as chaves do dicionário `responses` e verifica se alguma delas está presente no texto da mensagem, ignorando maiúsculas e minúsculas.

5. **Manipulador de mensagens:**
```python
@bot.message_handler(func=lambda message: should_respond(message))
def handle_message(message):
    for keyword, emoji in responses.items():
        if keyword.lower() in message.text.lower():
            # Envia o emoji correspondente
            bot.send_message(message.chat.id, emoji)
            break
```
   - Define um manipulador de mensagens que será acionado quando uma mensagem for recebida e a função `should_respond()` retornar `True`.
   - Itera sobre as palavras-chave no dicionário `responses` e verifica se alguma delas está presente no texto da mensagem.
   - Se uma palavra-chave correspondente for encontrada, o bot envia o emoji associado.

6. **Início do polling:**
```python
if __name__ == '__main__':
    bot.infinity_polling()
```
   - Inicia o processo de polling para receber e responder às mensagens. Se o script for executado como um programa principal, ele iniciará o bot.

