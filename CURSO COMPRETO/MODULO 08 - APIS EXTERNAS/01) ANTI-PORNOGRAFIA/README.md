# ANTI-PORNOGRAFIA
## DESCRIÇÃO:
Esse é um bot que utiliza a API WebPurify para verificar e banir imagens pornográficas em um grupo do Telegram.

## INSTRUÇÕES:
### Passo 1: Obtendo a Chave de API:
1. Acesse o site da WebPurify e inscreva-se para obter uma chave de API gratuita: [WebPurify - Signup](https://www.webpurify.com/signup/).
2. Após se inscrever, você receberá sua chave de API por e-mail.

### Passo 2: Instalando Pacotes:
Você precisará instalar a biblioteca `requests` para fazer solicitações HTTP à API da WebPurify. Você pode fazer isso executando o seguinte comando no seu terminal:

```
pip install requests
```

### Passo 3: Execução do Bot
Abra código, `CODIGO.py`, e execute-o no seu terminal. Certifique-se de substituir `'SUA_CHAVE_DE_API_AQUI'` pela sua chave de API da WebPurify e `'SEU_TOKEN_AQUI'` pelo token do seu bot.

### Nota Importante:
- Certifique-se de conceder ao seu bot permissões de administrador no grupo onde ele estará ativo para que ele possa banir usuários quando necessário.
- A detecção de conteúdo pornográfico não é perfeita e pode retornar falsos positivos ou falsos negativos. Portanto, use com cautela e revise os resultados conforme necessário.

## EXPLICAÇÃO:
1. ```python
   import telebot
   import requests
   ```
   - Importa os módulos necessários: `telebot` para interagir com a API do Telegram e `requests` para fazer solicitações HTTP.

2. ```python
   WEBPURIFY_API_KEY = 'SUA_CHAVE_DE_API_AQUI'
   ```
   - Define a chave de API da WebPurify. Você precisa substituir `'SUA_CHAVE_DE_API_AQUI'` pela sua chave de API real.

3. ```python
   TOKEN = 'SEU_TOKEN_AQUI'
   bot = telebot.TeleBot(TOKEN)
   ```
   - Define o token do bot do Telegram. Você precisa substituir `'SEU_TOKEN_AQUI'` pelo token real do seu bot.

4. ```python
   def check_and_ban_porn(message):
       ...
   ```
   - Define a função `check_and_ban_porn` que verifica se uma mensagem contém uma foto e, em seguida, usa a API WebPurify para determinar se a imagem é pornográfica. Se for, a mensagem é excluída e o usuário é banido do grupo.

5. ```python
   @bot.message_handler(func=lambda message: True)
   def handle_text(message):
       check_and_ban_porn(message)
   ```
   - Define um manipulador de mensagens para lidar com mensagens de texto. Ele chama a função `check_and_ban_porn` para verificar se há conteúdo pornográfico na mensagem.

6. ```python
   @bot.message_handler(content_types=['photo'])
   def handle_photo(message):
       check_and_ban_porn(message)
   ```
   - Define um manipulador de mensagens para lidar com mensagens de mídia (especificamente fotos). Ele também chama a função `check_and_ban_porn` para verificar se há conteúdo pornográfico na foto.

7. ```python
   bot.polling()
   ```
   - Inicia o bot, aguardando novas atualizações do Telegram.

Este script monitorará todas as mensagens de texto e fotos enviadas ao grupo e, se houver conteúdo pornográfico detectado pela API WebPurify, o bot excluirá a mensagem e banirá o remetente do grupo.