# MODULO 4: MODERADOR DE GRUPOS
## DESCRIÇÃO:
Você irá aprender a criar seus bots de Moderação dos grupos do Telegram. Desde:
* **1) COMANDOS BÁSICOS:** Os bots poderão Banir, Kink e Silenciar membros via comandos de Admin.  
* **2) AUTONOMIA:** Bastando o bot está como ADMIN, ele irá filtrar e Administrar seu grupo automáticamente com funções pré programadas no código.
* **3) BANCO DE DADOS:** Você irá criar um grande bot em que os usuários possam adicionar e configurar individualmente suas funções em cada grupo.

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

## COMO UTILIZAR OS BOTS?
1. Escolha um dos exemplos de bot.

2. Siga as instruções no arquivo README de cada exemplo para configurar o ambiente e as dependências.

3. Substitua as chaves de API necessárias, tokens e outras informações relevantes.

4. Execute o bot em um ambiente adequado.

5. Interaja com o bot no Telegram enviando os comandos ou mensagens específicas indicadas no exemplo.


