# MIDIAS EM MONGODB
## DESCRIÇÃO:
Este bot foi desenvolvido para permitir que os usuários escolham entre uma lista de arquivos disponíveis. O bot lista os arquivos armazenados em um banco de dados (MongoDB) e os apresenta como botões inline para o usuário selecionar. Uma vez selecionado, o bot responde com uma mensagem indicando qual arquivo foi escolhido.

1. **Interface de Seleção de Arquivos**: Ao iniciar o bot com o comando `/start`, os usuários recebem uma lista de botões com os nomes dos arquivos disponíveis para seleção.

2. **Armazenamento de Dados**: Os nomes dos arquivos são armazenados em um banco de dados (MongoDB) para fácil gerenciamento e escalabilidade.

3. **Interação Inline**: O bot responde às seleções dos usuários de forma inline, exibindo uma mensagem com o arquivo selecionado.

## PROPOSITO:
- Este bot é útil para casos em que os usuários precisam selecionar entre uma lista de opções disponíveis, como arquivos, imagens, documentos, etc. Ele pode ser facilmente adaptado para atender a diferentes necessidades, incluindo a expansão para lidar com outros tipos de interações e operações de banco de dados.

## EXPLICAÇÃO:
1. ```python
   import pymongo
   import telebot
   from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
   ```
   - Importações das bibliotecas necessárias: `pymongo` para interagir com o MongoDB e `telebot` para criar o bot Telegram. `InlineKeyboardMarkup` e `InlineKeyboardButton` são usados para criar botões inline.

2. ```python
   client = pymongo.MongoClient("mongodb://localhost:27017")
   db = client["upload"]
   collection = db["media"]
   ```
   - Estabelecimento da conexão com o banco de dados MongoDB. Um cliente MongoDB é criado para se conectar ao servidor MongoDB local na porta padrão 27017. O banco de dados utilizado é denominado "upload", e a coleção é denominada "media".

3. ```python
   def get_filenames():
       filenames = collection.distinct("filename")
       return filenames
   ```
   - Define uma função `get_filenames` que recupera os nomes únicos de arquivos da coleção "media" no banco de dados MongoDB. O método `distinct` é usado para obter valores únicos para o campo "filename".

4. ```python
   @bot.message_handler(commands=["start"])
   def start(message):
       ...
   ```
   - Define um manipulador de mensagens para o comando `/start`. Quando o usuário envia esse comando, a função `start` é chamada. Dentro desta função, são recuperados os nomes dos arquivos usando a função `get_filenames` e enviados como botões inline para o usuário.

5. ```python
   @bot.callback_query_handler(func=lambda call: True)
   def callback_query(call):
       ...
   ```
   - Define um manipulador de chamadas de retorno para responder quando o usuário clica em um dos botões inline. Quando um botão é clicado, a função `callback_query` é chamada, e uma mensagem é enviada para o chat com o nome do arquivo selecionado.

6. ```python
   if __name__ == "__main__":
       ...
   ```
   - Verifica se o script está sendo executado como um programa principal. Se for o caso, inicia o bot chamando `bot.polling()`, fazendo com que o bot comece a receber atualizações do Telegram.

