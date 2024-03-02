# ENVIANDO FOTOS:
## DESCRIÇÃO:
Este bot é um exemplo simples de um bot do Telegram que permite aos usuários enviar uma foto. Quando um usuário inicia uma conversa com o bot ou envia o comando "/start", o bot responde com uma mensagem que contém um botão inline. Ao clicar no botão "ENVIAR FOTO", o usuário pode selecionar uma foto para enviar ao bot.

## EXPLICAÇÃO:
1. **Handler do Comando /start**: Quando o comando `/start` é recebido, o bot responde com uma mensagem que contém um botão inline "ENVIAR FOTO".

2. **Criação do Teclado Inline**: A função `start` cria um teclado inline com um único botão para enviar uma foto. Quando o botão é pressionado, ele aciona o callback especificado.

3. **Handler de Callback**: Quando o botão inline é pressionado, o handler de callback é acionado. Ele verifica se o `callback_data` é "send_photo".

4. **Envio da Foto**: Se o `callback_data` for "send_photo", o bot chama a função `send_media` para enviar o arquivo de foto para o chat. O caminho do arquivo de foto é especificado como "./MIDIAS/telegram.jpg".

5. **Envio do Arquivo de Mídia**: A função `send_media` abre o arquivo de foto e usa `bot.send_photo` para enviar a foto para o chat especificado.


