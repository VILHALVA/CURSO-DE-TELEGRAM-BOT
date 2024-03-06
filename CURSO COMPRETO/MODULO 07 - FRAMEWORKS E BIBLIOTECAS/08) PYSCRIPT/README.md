# PYSCRIPT
## EXPLICAÇÃO:
```python
from telebot import TeleBot
from pyscript import Script

# Crie uma instância do bot
bot = TeleBot("SEU_TOKEN_DO_BOT")

# Defina o script PyScript que será executado quando o comando "/start" for recebido
start_script = Script("""
function onMessage(message) {
  // Envie uma mensagem de saudação ao usuário
  bot.sendMessage(message.chat.id, "Olá, " + message.from.username + "!");
}
""")

# Adicione o manipulador de comando para "/start"
bot.on_command("/start", start_script.run)

# Inicie o bot
bot.polling()
```

**Explicação:**

1. Importamos as bibliotecas TeleBot e PyScript.
2. Criamos uma instância do bot usando nosso token do Telegram.
3. Definimos um script PyScript que será executado quando o comando "/start" for recebido. O script envia uma mensagem de saudação ao usuário.
4. Adicionamos o manipulador de comando para "/start" usando o método `bot.on_command()`.
5. Iniciamos o bot usando o método `bot.polling()`.

**Observações:**

* Substitua `SEU_TOKEN_DO_BOT` pelo seu token do Telegram.
* Este é um exemplo simples. Você pode adicionar mais comandos e funcionalidades ao seu bot.
* Para mais informações sobre o PyScript, consulte a [documentação](https://pyscript.net/).
