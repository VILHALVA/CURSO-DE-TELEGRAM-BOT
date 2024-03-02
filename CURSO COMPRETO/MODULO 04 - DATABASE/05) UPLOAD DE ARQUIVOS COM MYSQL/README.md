# UPLOAD DE ARQUIVOS COM MYSQL
## DESCRIÇÃO:
- No `MODULO 03/ BOT 09`, Criamos um bot que apenas faz upload de arquivos no diretório local. Agora iremos incrementar esse recurso com o `MYSQL`.

- Este bot foi desenvolvido para permitir que os usuários enviem diversos tipos de arquivos (como áudio, foto, vídeo ou documento) e o bot os salve localmente em um diretório específico, além de armazenar os detalhes do arquivo em um banco de dados MySQL.

1. **Recebimento de Arquivos**: O bot aceita arquivos de áudio, foto, vídeo ou documento enviados pelos usuários.

2. **Salvamento Local**: Os arquivos recebidos são salvos localmente em um diretório especificado (neste caso, `./MIDIAS`).

3. **Armazenamento em Banco de Dados**: Os detalhes de cada arquivo (nome, diretório e extensão) são armazenados em uma tabela MySQL chamada `media`.

4. **Interatividade**: O bot responde aos usuários informando sobre o sucesso ou falha ao salvar o arquivo.

5. **Comandos de Inicialização**: Ao iniciar uma conversa com o bot usando o comando `/start`, os usuários recebem instruções sobre como usar o bot para enviar arquivos.

## PROPOSITO:
- Este bot é útil para situações em que os usuários precisam compartilhar arquivos com um sistema centralizado, como em um ambiente de trabalho colaborativo ou para coletar arquivos de usuários em uma plataforma específica. Ele pode ser facilmente personalizado para atender a diferentes necessidades, incluindo a expansão para lidar com outros tipos de arquivos ou a integração com serviços de armazenamento em nuvem.

## EXPLICAÇÃO:
1. ```python
   import os
   import telebot
   import mysql.connector
   from telebot.types import Message
   from datetime import datetime
   ```
   - Importações das bibliotecas necessárias: `os` para manipulação de arquivos e diretórios, `telebot` para criar o bot do Telegram, `mysql.connector` para a conexão com o banco de dados MySQL, `Message` para trabalhar com mensagens do Telegram e `datetime` para manipulação de datas e horas.

2. ```python
   TOKEN = "SEU_TOKEN"
   ```
   - Definição do token do bot Telegram.

3. ```python
   bot = telebot.TeleBot(TOKEN)
   ```
   - Inicialização do bot Telegram.

4. ```python
   SAVE_DIR = "./MIDIAS"
   ```
   - Diretório onde os arquivos recebidos serão salvos localmente.

5. ```python
   if not os.path.exists(SAVE_DIR):
       os.makedirs(SAVE_DIR)
   ```
   - Verificação e criação do diretório de salvamento, se ele não existir.

6. ```python
   mysql_connection = mysql.connector.connect(
       host="seu_host",
       user="seu_user",
       password="sua_senha",
       database="upload"
   )
   mysql_cursor = mysql_connection.cursor()
   ```
   - Estabelecimento da conexão com o banco de dados MySQL.

7. ```python
   @bot.message_handler(commands=["start"])
   def start(message: Message):
       ...
   ```
   - Definição de um manipulador de mensagens para o comando `/start`, que fornece instruções sobre como usar o bot.

8. ```python
   @bot.message_handler(content_types=["audio", "photo", "video", "document"])
   def save_media(message: Message):
       ...
   ```
   - Definição de um manipulador de mensagens para arquivos de áudio, foto, vídeo ou documento. Este manipulador baixa e salva o arquivo recebido localmente, além de registrar as informações sobre o arquivo no banco de dados MySQL.

9. ```python
   if __name__ == "__main__":
       ...
   ```
   - Verifica se o script está sendo executado como programa principal e inicia o bot Telegram chamando `bot.polling()`.

