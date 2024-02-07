# MODULO 3: BOTS INLINES E BANCO DE DADOS
## DESCRIÇÃO:
Vamos avancar mais um nivel: Você irá aprender a criar seus bots que utilizam BackEnd (Banco de Dados). Desde:
* **1) BOTS INLINES:** Você aprederá a criar bots totalmente inlines (Não precisa adicionar em grupos ou entrar no chat privado para usar), até comandos totalmente inlines.
* **2) BANCO DE DADOS:** O bot poderá salvar, editar e apagar nos registros das tabelas: IDs, Textos, Nomes, Números e Senhas. Além de mídias em diretórios do servidor. 
* **3) BOTS PREMIUM:** Por fim, você aprenderá a criar um bot Premium (Usuários só irão conseguir usar o seu bot somente se pagar uma taxa ou entrar no canal parceiro).

## REQUESITOS:
* [INSTALAR O PYTHON](https://www.python.org/downloads/release/python-3110/)
* [INSTALAR O PY TELEGRAM BOT](https://pypi.org/project/pyTelegramBotAPI/#files)
* [INSTALAR O XAMPP](https://www.apachefriends.org/pt_br/index.html)

## BOTS NA LINGUAGEM PYTHON:
### INSTALAÇÃO DO PYTHON:
1. **Baixar o Python:** Primeiro, você precisa ter o Python instalado no seu sistema. Se você ainda não tem o Python instalado, siga as instruções abaixo para baixá-lo de acordo com seu sistema operacional:

   - **Windows:** Vá para o site oficial do Python em [python.org](https://www.python.org/downloads/windows/) e baixe a versão mais recente do Python para Windows. Execute o instalador e siga as instruções para instalar o Python.

   - **Linux:** A maioria das distribuições Linux já vem com o Python pré-instalado. No entanto, você pode verificar a versão do Python usando o comando `python3 --version`. Se não estiver instalado, você pode instalá-lo usando o gerenciador de pacotes da sua distribuição (por exemplo, `sudo apt-get install python3` no Ubuntu).

   - **macOS:** O macOS também geralmente inclui o Python pré-instalado. Você pode verificar a versão do Python usando o comando `python3 --version`. Se necessário, você pode instalá-lo usando um gerenciador de pacotes como o Homebrew.

### INSTALAÇÃO DA BIBLIOTECA: `pyTelegramBotAPI`:
Depois de ter o Python instalado, você pode instalar a biblioteca `pyTelegramBotAPI` usando o `pip`, que é o gerenciador de pacotes padrão do Python. Abra o terminal ou prompt de comando e execute o seguinte comando:

```bash
pip install pyTelegramBotAPI
```

Isso instalará a biblioteca `pyTelegramBotAPI` no seu ambiente Python.

Agora, você pode começar a criar seu bot em Python e usar a biblioteca `pyTelegramBotAPI` para interagir com a API do Telegram. Certifique-se de obter um token de acesso do BotFather do Telegram antes de criar seu bot e substitua `"SEU_TOKEN_AQUI"` pelo token real do seu bot no código Python.

Com a biblioteca `pyTelegramBotAPI` instalada e o Python configurado, você está pronto para criar e executar seu bot no Telegram.

## BOTS NA LINGUAGEM LUA:
Para criar e rodar um bot do Telegram em Lua, você pode usar a biblioteca `lua-telegram-bot`. Esta biblioteca permite interagir com a API do Telegram usando a linguagem de programação Lua. 

Para instalar a biblioteca `lua-telegram-bot`, você pode usar o gerenciador de pacotes LuaRocks. Se você ainda não tem o LuaRocks instalado, você pode instalá-lo primeiro. Em seguida, você pode usar o LuaRocks para instalar a biblioteca. Aqui estão os comandos:

1. Instale o LuaRocks (caso ainda não tenha):
   
   ```bash
   sudo apt-get install luarocks  # Para sistemas baseados no Debian/Ubuntu
   ```

   ou

   ```bash
   brew install luarocks  # Para macOS (usando Homebrew)
   ```

2. Instale a biblioteca `lua-telegram-bot`:

   ```bash
   luarocks install lua-telegram-bot
   ```

Uma vez que a biblioteca `lua-telegram-bot` esteja instalada, você pode começar a criar seu bot em Lua. Lembre-se de que você precisa registrar seu bot no BotFather do Telegram para obter um token de acesso, que você usará no código Lua para se comunicar com a API do Telegram.

## MANUAL DE INSTRUÇÕES BACK END:
Este manual fornece instruções detalhadas para configurar um bot Python que se conecta a um banco de dados SQLite usando o aplicativo XAMPP. Certifique-se de seguir todas as etapas cuidadosamente.

### Requisitos:
- Python 3.x instalado no seu sistema.
- XAMPP instalado e em execução.

**Configuração do Bot:**
1. Baixe o código-fonte do bot que se conecta a um banco de dados SQLite. Certifique-se de ter o código em mãos.

2. Abra o código-fonte do bot em um editor de texto ou ambiente de desenvolvimento Python de sua escolha.

3. Dentro do código do bot, você encontrará uma variável chamada `DATABASE_PATH`. Defina o caminho para o arquivo de banco de dados SQLite. Por exemplo:
   
   ```python
   DATABASE_PATH = "caminho/para/seu/banco.db"
   ```

4. Defina a variável `OWNER_ID` com o seu ID de usuário Telegram para garantir que você seja reconhecido como o proprietário do bot e tenha permissões de gerenciamento do banco de dados. Você pode obter o seu ID de usuário Telegram com o bot @userinfobot.

5. Acesse o painel de controle do XAMPP no seu navegador. Normalmente, o endereço é `http://localhost/phpmyadmin/`.

6. Crie um novo banco de dados. Clique em "Banco de Dados" na parte superior e forneça um nome para o seu banco de dados. Por exemplo, `database_bot`. Ou use os comandos SQL:
```sql
   CREATE DATABASE IF NOT EXISTS bot_database;
   USE bot_database;
   );
   ```

7. Crie uma nova tabela dentro do banco de dados. Escolha o banco de dados que você criou, clique em "SQL" no topo e cole o seguinte código SQL:

   ```sql
   CREATE TABLE IF NOT EXISTS users (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       nome TEXT NOT NULL,
       idade INTEGER NOT NULL
   );
   ```

8. Agora, você deve configurar o bot para se conectar ao banco de dados SQLite usando o XAMPP. Para isso, você precisa configurar as informações de login do XAMPP no código. Localize as seguintes linhas no código do bot:

   ```python
   DB_USERNAME = "seu_usuario_xampp"
   DB_PASSWORD = "sua_senha_xampp"
   ```

   Substitua `"seu_usuario_xampp"` pelo nome de usuário do XAMPP e `"sua_senha_xampp"` pela senha do XAMPP.

### Executando o Bot:
1. Abra o terminal ou prompt de comando.

2. Navegue até o diretório onde você salvou o código do bot.

3. Execute o bot Python com o seguinte comando:

   ```
   python nome_do_seu_bot.py
   ```

   Certifique-se de que o arquivo Python tenha um nome apropriado (por exemplo, `meu_bot.py`) e que você está no diretório correto.

4. O bot agora está em execução. Você pode interagir com ele no Telegram e usar os comandos que você definiu no código para adicionar e listar usuários no banco de dados.

### Observações Importantes:
- Mantenha suas informações de login do XAMPP em segurança, pois elas concedem acesso ao seu banco de dados.
- Certifique-se de que o XAMPP esteja em execução enquanto o bot estiver em execução para que a conexão com o banco de dados seja estabelecida corretamente.

Este manual oferece uma visão geral básica da configuração do bot com o XAMPP e SQLite. Lembre-se de personalizar o bot e o banco de dados de acordo com suas necessidades específicas.

## COMO UTILIZAR OS BOTS?
1. Siga as instruções no arquivo README de cada exemplo para configurar o ambiente e as dependências.

2. Substitua as chaves de API necessárias, tokens e outras informações relevantes.

3. Execute o bot em um ambiente adequado.

4. Interaja com o bot no Telegram enviando os comandos ou mensagens específicas indicadas no exemplo.

5. Mantenha seu servidor local (XAMPP) bem configurado: Com DATABASE e TABELAS já criadas.


