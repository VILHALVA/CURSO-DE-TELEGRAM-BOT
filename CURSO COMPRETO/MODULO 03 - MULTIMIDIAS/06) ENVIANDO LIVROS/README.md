# ENVIANDO LIVROS:
## DESCRIÇÃO:
Este bot tem a funcionalidade de enviar um arquivo PDF quando o usuário interage com ele através do comando "/start" e clica em um botão inline chamado "ENVIAR PDF". Quando o botão é pressionado, ele envia um arquivo PDF específico chamado "Python.pdf" localizado no diretório "./MIDIAS" para o usuário que interagiu com o bot. Após o envio do PDF, o bot envia uma mensagem de confirmação indicando que o documento foi enviado com sucesso. O bot é executado continuamente, aguardando interações dos usuários e respondendo de acordo.

## EXPLICAÇÃO:
1. **Handler do Comando /start**: Quando o comando `/start` é recebido, o bot responde com uma mensagem que contém um botão inline "ENVIAR PDF".

2. **Criação do Teclado Inline**: A função `start` cria um teclado inline com um único botão para enviar um PDF. Quando o botão é pressionado, ele aciona o callback especificado.

3. **Handler de Callback**: Quando o botão inline é pressionado, o handler de callback é acionado. Ele verifica se o `callback_data` é "send_pdf".

4. **Envio do Documento**: Se o `callback_data` for "send_pdf", o bot chama a função `send_media` para enviar o arquivo PDF para o chat. O caminho do arquivo PDF é especificado como "./MIDIAS/Python.pdf".

5. **Envio do Arquivo de Mídia**: A função `send_media` abre o arquivo PDF e usa `bot.send_document` para enviar o PDF para o chat especificado. Em seguida, o bot envia uma mensagem indicando que o documento foi enviado com sucesso.

