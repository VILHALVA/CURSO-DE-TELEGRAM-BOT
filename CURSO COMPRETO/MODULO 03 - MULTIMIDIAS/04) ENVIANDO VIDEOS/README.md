# ENVIANDO VIDEO:
## DESCRIÇÃO:
Este bot é um simples bot do Telegram que permite aos usuários enviar vídeos quando solicitados. Ao iniciar o bot, os usuários recebem uma mensagem com um botão inline "ENVIAR VÍDEO". Quando o botão é clicado, o bot envia um vídeo predefinido para o usuário.

1. **Comando /start**: Quando os usuários iniciam o bot ou enviam o comando /start, recebem uma mensagem inicial com um botão inline para enviar um vídeo.
   
2. **Botão Inline para Enviar Vídeo**: O bot oferece um botão inline "ENVIAR VÍDEO" que os usuários podem clicar para receber um vídeo.

3. **Envio de Vídeo**: Quando o botão "ENVIAR VÍDEO" é clicado, o bot envia um vídeo predefinido para o usuário.

## EXPLICAÇÃO:
1. **Handler do Comando /start**: Quando o comando `/start` é recebido, o bot responde com uma mensagem que contém um botão inline. O botão é criado usando a função `create_inline_keyboard` e tem o texto "ENVIAR VIDEO".

2. **Criação do Teclado Inline**: A função `create_inline_keyboard` é usada para criar um teclado inline com o botão especificado. Esta função recebe uma lista de listas, onde cada lista interna contém o texto do botão e o `callback_data` associado a ele. O teclado inline é então enviado como parte da mensagem de resposta.

3. **Handler de Callback**: Quando o botão inline é pressionado, o handler de callback é acionado. Ele verifica se o `callback_data` é "send_video".

4. **Envio do Vídeo**: Se o `callback_data` for "send_video", o bot chama a função `send_media` para enviar o vídeo para o chat. O caminho do arquivo de vídeo é especificado como `"./MIDIAS/sol.mp4"`. Certifique-se de ter o arquivo de vídeo nesse local.

5. **Envio do Arquivo de Mídia**: A função `send_media` abre o arquivo de vídeo e usa `bot.send_video` para enviar o vídeo para o chat especificado.

