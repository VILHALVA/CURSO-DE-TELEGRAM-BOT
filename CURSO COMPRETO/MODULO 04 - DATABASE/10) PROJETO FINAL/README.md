# PROJETO FINAL: CRUD DE MULTIMIDIAS
## DESCRIÇÃO:
- No `MODULO 03`, `10) PROJETO FINAL`: Criamos um bot para fazer upload de arquivos. O problema é que só era possivel enviar arquivos, não tinha como recuperar através do bot. Nesse projeto iremos resolver isso, com um simples CRUD MYSQL.

- Este bot é um aplicativo de mensagens instantâneas que opera na plataforma Telegram e foi desenvolvido para gerenciar um banco de dados de multimídias. Ele oferece funcionalidades básicas de um CRUD (Create, Read, Update, Delete) para manipular arquivos de mídia, como imagens, vídeos ou áudios.

1. **Enviar Mídia:** Os usuários podem enviar arquivos de mídia para serem armazenados no banco de dados do bot. Isso é feito iniciando uma conversa com o bot e selecionando a opção "ENVIAR" no menu principal.

2. **Exibir Mídias:** Os usuários podem visualizar todas as mídias armazenadas no banco de dados do bot. Ao selecionar a opção "EXIBIR" no menu principal, o bot exibirá uma lista de todas as mídias disponíveis.

3. **Editar Mídia:** Os usuários podem renomear os arquivos de mídia armazenados no banco de dados. Ao selecionar a opção "EDITAR" no menu principal, o bot permite que os usuários escolham a mídia que desejam editar e forneçam um novo nome para ela.

4. **Apagar Mídia:** Os usuários podem excluir arquivos de mídia do banco de dados. Ao selecionar a opção "APAGAR" no menu principal, o bot exibe uma lista de todas as mídias disponíveis e permite que os usuários escolham qual deseja excluir.

O bot é capaz de interagir com os usuários por meio de mensagens de texto e botões interativos, facilitando a comunicação e a execução das operações CRUD de maneira intuitiva e eficiente. Ele ajuda os usuários a gerenciar suas coleções de mídia de forma conveniente e organizada diretamente do aplicativo Telegram.

## EXPLICAÇÃO (MAIN.PY):
1. ```python
   import telebot
   ```
   - Aqui, importamos o módulo `telebot`, que fornece uma interface conveniente para trabalhar com a API do Telegram.

2. ```python
   from TOKEN import *
   ```
   - Esta linha importa as variáveis de ambiente contendo o token do bot. Isso é útil para manter o token fora do código-fonte por motivos de segurança.

3. ```python
   from DB_CONNECTION import *
   ```
   - Esta linha importa as configurações de conexão com o banco de dados. Isso é necessário para realizar operações relacionadas ao banco de dados, como salvar, apagar ou editar dados.

4. ```python
   from ENVIAR import process_send_media
   ```
   - Aqui, importamos a função `process_send_media` do arquivo `ENVIAR.py`. Essa função processa o envio de mídia pelo bot.

5. ```python
   from APAGAR import delete_media, delete_media_record
   ```
   - Similar ao anterior, importamos duas funções relacionadas a apagar mídia e registros de mídia do arquivo `APAGAR.py`.

6. ```python
   from EDITAR import edit_media, edicao
   ```
   - Importamos duas funções relacionadas à edição de mídia do arquivo `EDITAR.py`.

7. ```python
   from EXIBIR import display_media, send_media
   ```
   - Importamos duas funções relacionadas à exibição de mídia do arquivo `EXIBIR.py`.

8. ```python
   bot = telebot.TeleBot(TOKEN)
   ```
   - Aqui, inicializamos o bot usando o token fornecido. Isso cria uma instância de `TeleBot`, que representa nosso bot Telegram.

9. ```python
   @bot.message_handler(commands=["start"])
   def start(message):
       ...
   ```
   - Esta é uma função de manipulador de mensagens. Ela é chamada sempre que o bot recebe o comando `/start`. Ela cria um menu principal com botões inline para as ações disponíveis.

10. ```python
    @bot.callback_query_handler(func=lambda call: True)
    def callback_query(call):
        ...
    ```
    - Esta é uma função de manipulador de chamadas de retorno. Ela é chamada sempre que um botão inline é clicado. Ela redireciona para a função apropriada com base no botão clicado.

11. ```python
    if __name__ == "__main__":
        ...
    ```
    - Esta é uma construção comum em Python que verifica se o script está sendo executado como um programa principal. Se estiver, inicia o bot chamando `bot.polling()`. Isso faz com que o bot comece a receber atualizações do Telegram.

## SAIBA MAIS:
* [CLIQUE AQUI PARA APRENDER MAIS O SOBRE CALLBACK](./CALLBACK.md)




