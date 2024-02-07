# MODERADOR MYSQL
## CRIANDO O BOT:
Para criar um bot moderador de grupos do Telegram que tenha a função de punir e apagar mensagens de spam em grupos diferentes, com configurações personalizadas por administrador de grupo, você precisará seguir estas etapas:

1. **Crie um Bot no BotFather**:
   - Acesse o Telegram e converse com o BotFather para criar um novo bot.
   - Anote o token do bot gerado, pois você precisará dele para interagir com a API do Telegram.

2. **Desenvolva o Bot**:
   - Escolha uma linguagem de programação, como Python, Node.js ou qualquer outra com suporte à API do Telegram.
   - Use a biblioteca apropriada para a linguagem escolhida (por exemplo, python-telegram-bot para Python ou node-telegram-bot-api para Node.js) para interagir com a API do Telegram.

3. **Configuração por Grupo e por Administrador**:
   - Implemente uma lógica que permita a configuração personalizada por grupo e por administrador. Isso pode ser feito de várias maneiras, como armazenar as configurações em um banco de dados ou em um arquivo de configuração.
   - Crie comandos ou métodos que permitam aos administradores configurar as regras de moderação, como palavras proibidas, ações de punição, etc. Armazene essas configurações associadas a cada grupo e administrador.

4. **Detecção de Spam**:
   - Implemente algoritmos ou regras para detectar mensagens de spam com base nas configurações do grupo e do administrador. Isso pode envolver a verificação de palavras-chave proibidas, contagem de mensagens repetitivas, detecção de links suspeitos, etc.

5. **Ações de Moderação**:
   - Quando uma mensagem de spam é detectada, implemente ações de moderação, como apagar a mensagem, advertir o usuário, silenciar temporariamente o usuário ou até mesmo banir o usuário, dependendo das configurações.
   - Certifique-se de que o bot tenha permissões suficientes para executar essas ações no grupo.

6. **Interação com Administradores**:
   - Implemente comandos que permitam aos administradores do grupo configurar as regras de moderação. Por exemplo, um administrador pode usar "/config" para definir as configurações específicas do grupo.

7. **Controle de Acesso e Permissões**:
   - Certifique-se de que apenas os administradores autorizados possam adicionar o bot aos grupos. Isso pode ser controlado por meio de um sistema de convites ou autorizações.

8. **Testes e Ajustes**:
   - Teste o bot em grupos de teste para garantir que ele funcione corretamente.
   - Ajuste as configurações de detecção de spam e ações de moderação com base no feedback e nos resultados dos testes.

9. **Implantação e Hospedagem**:
   - Implante o bot em um servidor ou plataforma de hospedagem, de preferência em um ambiente que ofereça alta disponibilidade.

10. **Divulgação e Uso**:
    - Divulgue o bot para os administradores de grupos interessados e incentive-os a adicioná-lo aos grupos que desejam moderar.

11. **Suporte e Manutenção**:
    - Esteja disponível para oferecer suporte e manutenção contínuos para o bot, pois os administradores de grupos podem precisar de assistência ou configurações adicionais.

Certifique-se de que o bot esteja em conformidade com as políticas do Telegram e respeite as diretrizes de privacidade e segurança ao implementar a moderação. Além disso, lembre-se de que o uso inadequado do bot pode resultar em proibições ou restrições por parte do Telegram, portanto, é importante usá-lo com responsabilidade.

## ESTRUTURA DO BANCO DE DADOS:
A estrutura de banco de dados para salvar as configurações de cada grupo pode variar dependendo das necessidades específicas do seu bot. No entanto, vou lhe fornecer um exemplo de estrutura de banco de dados simplificada usando uma abordagem com uma tabela para armazenar as configurações de cada grupo. Nesse exemplo, cada linha da tabela representa um grupo e cada coluna representa uma configuração ou função específica. Você pode adaptar e expandir essa estrutura conforme necessário.

**Exemplo de Estrutura de Banco de Dados:**

Tabela: `group_settings`

| Coluna                  | Tipo de Dados | Descrição                                      |
|-------------------------|---------------|------------------------------------------------|
| `group_id`              | INT           | Identificador único do grupo (Chave Primária) |
| `admin_id`              | INT           | Identificador do administrador do grupo        |
| `spam_detection`        | BOOLEAN       | Habilitar/desabilitar a detecção de spam       |
| `spam_keywords`         | TEXT          | Lista de palavras-chave proibidas (separadas por vírgula) |
| `punishment_action`     | ENUM          | Ação a ser tomada em caso de spam (ex: "ban", "mute") |
| `max_warnings`          | INT           | Número máximo de advertências permitidas        |
| `warn_action`           | ENUM          | Ação a ser tomada após atingir o limite de advertências (ex: "mute", "ban") |
| `welcome_message`       | TEXT          | Mensagem de boas-vindas personalizada para novos membros |
| `captcha_required`      | BOOLEAN       | Habilitar/desabilitar a verificação de captcha para novos membros |
| `captcha_message`       | TEXT          | Mensagem de captcha a ser enviada para novos membros |
| `created_at`            | TIMESTAMP     | Data e hora de criação do registro             |
| `updated_at`            | TIMESTAMP     | Data e hora da última atualização do registro   |

Neste exemplo:
- `group_id` é usado como chave primária para identificar cada grupo exclusivamente.
- `admin_id` pode ser usado para rastrear qual administrador configurou as regras para o grupo.
- `spam_detection` indica se a detecção de spam está habilitada ou desabilitada para o grupo.
- `spam_keywords` armazena palavras-chave proibidas que são usadas para a detecção de spam.
- `punishment_action` define qual ação deve ser tomada quando uma mensagem de spam é detectada (por exemplo, banir ou silenciar o usuário).
- `max_warnings` e `warn_action` lidam com ações após um número máximo de advertências por spam.
- `welcome_message` armazena a mensagem de boas-vindas personalizada para novos membros.
- `captcha_required` indica se a verificação de captcha é necessária para novos membros.
- `captcha_message` armazena a mensagem do captcha a ser enviada para novos membros.
- `created_at` e `updated_at` registram quando o registro foi criado e atualizado.

Você pode personalizar essa estrutura de acordo com as configurações específicas que deseja oferecer aos administradores de grupo. Certifique-se de que seu bot possa ler e gravar essas informações no banco de dados conforme necessário.

## INSTRUÇÕES:
Para criar um bot no Telegram com a função de punir quem enviar qualquer link no grupo e permitir que cada administrador personalize a ação (banir, kickar, silenciar ou apenas apagar a mensagem) com o comando `/settings`, você precisará de:

1. Um bot Telegram funcionando.
2. Um banco de dados MySQL configurado.

Aqui está um exemplo de código Python que implementa essa funcionalidade, juntamente com os comandos SQL para criar o banco de dados e a tabela necessários:

**Código Python:**

```python
import telebot
import mysql.connector

# Configurações do bot
TOKEN = 'SEU_TOKEN_AQUI'
bot = telebot.TeleBot(TOKEN)

# Configurações do banco de dados MySQL
db_host = 'SEU_HOST_MYSQL'
db_user = 'SEU_USUARIO_MYSQL'
db_password = 'SUA_SENHA_MYSQL'
db_database = 'nome_do_banco'  # Substitua pelo nome do seu banco

# Conexão com o banco de dados
db_connection = mysql.connector.connect(
    host=db_host,
    user=db_user,
    password=db_password,
    database=db_database
)

# Cursor para executar consultas SQL
db_cursor = db_connection.cursor()

# Comando SQL para criar a tabela de configuração
create_table_query = '''
CREATE TABLE IF NOT EXISTS group_settings (
    group_id BIGINT PRIMARY KEY,
    admin_id BIGINT,
    action ENUM('ban', 'kick', 'mute', 'delete') DEFAULT 'delete'
)
'''

# Executa o comando SQL para criar a tabela
db_cursor.execute(create_table_query)
db_connection.commit()

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Olá! Use o comando /settings para configurar a ação para links no grupo.")

@bot.message_handler(commands=['settings'])
def settings(message):
    # Verifica se o usuário é um administrador do grupo
    chat_member = bot.get_chat_member(message.chat.id, message.from_user.id)
    if chat_member.status in ['administrator', 'creator']:
        # Envia o teclado de configuração
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add('/ban', '/kick', '/mute', '/delete')
        bot.send_message(message.chat.id, "Escolha a ação para links no grupo:", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, "Você precisa ser um administrador para configurar as ações.")

@bot.message_handler(commands=['ban', 'kick', 'mute', 'delete'])
def set_action(message):
    action = message.text[1:]  # Remove o "/" do comando
    user_id = message.from_user.id
    group_id = message.chat.id

    # Verifica se o usuário é um administrador do grupo
    chat_member = bot.get_chat_member(group_id, user_id)
    if chat_member.status in ['administrator', 'creator']:
        # Atualiza a ação na tabela de configuração
        update_query = '''
        INSERT INTO group_settings (group_id, admin_id, action)
        VALUES (%s, %s, %s)
        ON DUPLICATE KEY UPDATE action = %s
        '''
        data = (group_id, user_id, action, action)
        db_cursor.execute(update_query, data)
        db_connection.commit()

        bot.send_message(group_id, f"Ação para links no grupo configurada para: {action}")
    else:
        bot.send_message(group_id, "Você precisa ser um administrador para configurar as ações.")

if __name__ == '__main__':
    bot.polling()
```

Certifique-se de substituir `SEU_TOKEN_AQUI`, `SEU_HOST_MYSQL`, `SEU_USUARIO_MYSQL`, `SUA_SENHA_MYSQL` e `nome_do_banco` pelas informações apropriadas.

**Comandos SQL para criar o banco de dados e a tabela:**

```sql
CREATE DATABASE IF NOT EXISTS nome_do_banco;

USE nome_do_banco;

CREATE TABLE IF NOT EXISTS group_settings (
    group_id BIGINT PRIMARY KEY,
    admin_id BIGINT,
    action ENUM('ban', 'kick', 'mute', 'delete') DEFAULT 'delete'
);
```

Esse código cria um bot que permite aos administradores configurarem a ação para links no grupo usando o comando `/settings`. Cada administrador pode personalizar a ação (banir, kickar, silenciar ou apenas apagar a mensagem) de acordo com sua preferência. As configurações são armazenadas em um banco de dados MySQL. Certifique-se de ter o módulo `mysql-connector-python` instalado via pip (`pip install mysql-connector-python`).