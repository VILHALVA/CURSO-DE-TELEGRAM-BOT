# PROJETO FINAL: ANTI-SPAM MYSQL
## DESCRIÇÃO:
Este bot implementa uma funcionalidade de configuração de punições para um grupo de Telegram. Ele permite que administradores do grupo configurem diferentes tipos de punições para usuários que enviam spam, como banimento, silenciamento temporário, expulsão do grupo, ou desativar a punição.

O bot possui os seguintes recursos:

1. **Comando /settings**: Este comando pode ser usado pelos administradores do grupo para configurar as punições. Quando acionado, o bot exibe o status atual das punições no grupo e apresenta opções de botões para selecionar a punição desejada.

2. **Configuração de punições**: Ao clicar em um dos botões apresentados pelo comando /settings, os administradores podem configurar a punição desejada. Essas punições são então salvas no banco de dados MySQL.

3. **Aplicação de punições**: Quando um usuário envia uma mensagem contendo um link, o bot verifica se a punição correspondente está configurada para o grupo. Se uma punição estiver configurada, o bot aplica a punição ao usuário que enviou a mensagem de spam.

4. **Notificação de punição**: Após aplicar uma punição, o bot envia uma mensagem ao grupo mencionando o nome do usuário punido e o tipo de punição aplicada.

5. **Persistência de configurações**: As configurações de punição são armazenadas no banco de dados MySQL, permitindo que persistam entre reinicializações do bot.

6. **Manuseio de erros**: O bot está equipado para lidar com erros, como a falta de permissões para editar mensagens ou ao acessar o banco de dados.

## PROPOSITO:
Este bot é uma ferramenta útil para administradores de grupos do Telegram que desejam automatizar o processo de aplicação de punições a usuários que enviam spam. Ele oferece uma maneira conveniente de configurar e gerenciar diferentes tipos de punições para manter a ordem e a qualidade da comunidade do grupo.

## EXPLICAÇÃO:
```python
import telebot
from DB_CONNECTION import db_connection
from TOKEN import TOKEN
from telebot import types
import re
```

1. `import telebot`: Importa a biblioteca Telebot, que é usada para interagir com a API do Telegram.
2. `from DB_CONNECTION import db_connection`: Importa a conexão com o banco de dados MySQL.
3. `from TOKEN import TOKEN`: Importa o token do bot a partir de um arquivo separado para garantir segurança.
4. `from telebot import types`: Importa tipos específicos do Telebot, como `InlineKeyboardMarkup`.
5. `import re`: Importa o módulo `re` para realizar operações com expressões regulares.

```python
bot = telebot.TeleBot(TOKEN)
```

Cria uma instância do bot Telebot usando o token importado.

```python
connection = db_connection
cursor = connection.cursor()
```

Estabelece uma conexão com o banco de dados MySQL e cria um cursor para executar consultas SQL.

```python
@bot.message_handler(commands=['settings'])
def handle_settings(message):
    ...
```

Define um handler para lidar com o comando "/settings". Quando o comando "/settings" é enviado, esta função é chamada.

```python
def handle_settings(message):
    ...
```

Esta função é chamada quando o comando "/settings" é enviado. Ela verifica se o remetente é um administrador do grupo, busca a punição atual do grupo no MySQL e envia uma mensagem com o status atual e um painel de botões para configurar as punições.

```python
@bot.callback_query_handler(func=lambda call: True)
def handle_callback_query(call):
    ...
```

Define um handler para lidar com as callback queries dos botões. Quando um botão é pressionado, esta função é chamada.

```python
def handle_callback_query(call):
    ...
```

Esta função é chamada quando um botão é pressionado. Ela verifica se o remetente é um administrador do grupo, salva a punição selecionada no banco de dados, aplica a punição ao membro e envia uma nova mensagem com o status atualizado.

```python
def save_punishment(group_id, punishment):
    ...
```

Esta função salva a punição selecionada para o grupo no banco de dados MySQL.

```python
def get_punishment(group_id):
    ...
```

Esta função obtém a punição atual do grupo a partir do banco de dados MySQL.

```python
def apply_punishment(message, punishment):
    ...
```

Esta função aplica a punição selecionada ao membro.

```python
@bot.message_handler(func=lambda message: True)
def anti_spam(message):
    ...
```

Define um handler para mensagens de texto. Quando uma mensagem de texto é enviada, esta função é chamada.

```python
def anti_spam(message):
    ...
```

Esta função é chamada quando uma mensagem de texto é enviada. Ela verifica se o remetente não é um bot, se o remetente é um administrador do grupo e se a mensagem contém links. Se a mensagem contiver links, ela remove a mensagem do usuário e aplica a punição configurada.

```python
if __name__ == '__main__':
    ...
```

Esta parte do código verifica se o script está sendo executado diretamente e, se for o caso, inicia o bot.

