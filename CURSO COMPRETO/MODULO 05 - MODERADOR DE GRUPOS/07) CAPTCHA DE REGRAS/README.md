# CAPTCHA DE REGRAS
## DESCRIÇÃO:
Este é um bot para o Telegram que lida com várias interações, incluindo solicitações de entrada em grupos, manipulação de teclado inline, gerenciamento de regras de grupo e envio de mensagens de boas-vindas.

## EXPLICAÇÃO (MAIN.PY):
1. **Imports e Configuração:**
   - O script importa vários módulos, incluindo `telebot`, `redis`, `sqlite3` e `subprocess`.
   - O token do bot é lido de um arquivo de configuração `utils/token.conf`.
   - Um objeto `telebot.TeleBot` é criado com o token fornecido.

2. **Funções Auxiliares:**
   - `get_emoji()`: Retorna uma lista de emojis selecionados aleatoriamente.
   - `create_buttons(chat_id)`: Cria botões de teclado inline com emojis e respostas aleatórias.
   - `create_table(table)`: Cria uma tabela no banco de dados SQLite para armazenar informações do grupo.
   - `insert_on_table(table, values)`: Insere dados na tabela do banco de dados.
   - `select_from_table(table)`: Seleciona dados da tabela do banco de dados.
   - `update_database(table, query)`: Atualiza os dados na tabela do banco de dados.

3. **Handlers de Mensagem:**
   - `chat_join_request_handler`: Manipula solicitações de entrada em grupos.
   - `callback_query_handler`: Manipula interações de teclado inline.
   - `message_handler`: Manipula mensagens de texto e comandos.
   
4. **Métodos para Lidar com Diferentes Tipos de Mensagens:**
   - `member_joined`: Manipula eventos como membros entrando ou saindo de grupos.
   - `start`: Manipula o comando `/start`, enviando informações sobre o bot.
   - `set_here`: Configura o bot para lidar com regras em um grupo específico.
   - `send_rules`: Envia as regras do grupo quando solicitado.
   - `send_pix`: Envia informações de doação quando solicitado.
   - `message_to_bot`: Manipula mensagens de texto e armazena informações sobre as regras do grupo.

5. **Execução do Bot:**
   - O bot começa a receber atualizações do Telegram usando o método `polling`, permitindo que ele responda às interações dos usuários.

## CREDITOS E MAIS:
* [ESSE BOT FOI CRIADO PELO "GabrielRF"](https://github.com/GabrielRF/RegrasRobot)
* [ESSE BOT FOI EDITADO PELO VILHALVA](https://github.com/VILHALVA)
* [VEJA O MANUAL CLICANDO AQUI](./MANUAL.md)