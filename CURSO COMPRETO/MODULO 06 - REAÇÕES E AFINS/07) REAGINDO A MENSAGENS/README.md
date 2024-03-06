# REAGINDO A MENSAGENS
## DESCRIÇÃO:
Este bot foi desenvolvido para reagir a todas as mensagens recebidas em um grupo do Telegram com uma reação de coração. Ele utiliza a função `setMessageReaction` da API do Telegram para definir a reação de coração em cada mensagem recebida no grupo.

## [DETALHES:](https://t.me/BotNews/86)
* API de bot 7.0
* Reações:
• Apresentando suporte completo de reação para bots.
• Os bots agora podem reagir a mensagens com setMessageReaction .
• As reações às mensagens agora geram atualizações para os bots.
• Adicionado o campo `available_reactions` à classe Chat.

Para atualizar a biblioteca Telebot, você pode usar o seguinte comando pip:

```
pip install --upgrade pyTelegramBotAPI
```

Isso garantirá que você tenha a versão mais recente da biblioteca, que deve incluir suporte para a API de bot 7.0 e reações às mensagens. Certifique-se de executar esse comando em seu terminal ou prompt de comando.

* [SAIBA MAIS CLICANDO AQUI](https://core.telegram.org/bots/api#setmessagereaction)

## EXPLICAÇÃO:
1. **Importações:**
```python
from telebot import TeleBot
from TOKEN import *
```
   - `TeleBot`: É a classe principal da biblioteca Telebot, que é usada para criar e gerenciar o bot do Telegram.
   - `TOKEN`: É importado de um arquivo chamado `TOKEN.py`, que contém o token de acesso do bot. Isso é feito para proteger o token e evitar que seja compartilhado diretamente no código.

2. **Criação do objeto bot:**
```python
bot = TeleBot(TOKEN)
```
   - Cria uma instância do bot Telebot utilizando o token de acesso.

3. **Manipulador de mensagens:**
```python
@bot.message_handler(func=lambda mensagem: True)
def responder(mensagem):
    # Definir uma reação de coração na mensagem
    reaction = [{"type": "heart"}]  # Reação de coração
    bot.set_message_reaction(mensagem.chat.id, mensagem.message_id, reaction)
```
   - Define um manipulador de mensagens que será acionado para todas as mensagens recebidas.
   - Quando uma mensagem é recebida, a função `responder()` é chamada.
   - Dentro desta função, uma reação de coração é definida utilizando a função `set_message_reaction()` do bot Telebot. Esta função recebe o ID do chat, o ID da mensagem e a reação a ser definida.

4. **Iniciar o polling:**
```python
bot.polling()
```
   - Inicia o processo de polling para receber e responder às mensagens. O bot continuará a rodar e responder às mensagens indefinidamente.

