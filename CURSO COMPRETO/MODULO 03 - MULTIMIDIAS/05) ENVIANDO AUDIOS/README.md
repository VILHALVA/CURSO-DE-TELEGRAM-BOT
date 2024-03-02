# ENVIANDO AUDIO:
## DESCRIÇÃO:
Este bot Telegram foi desenvolvido para permitir aos usuários solicitar e receber arquivos de áudio. Ao iniciar o bot, os usuários recebem uma mensagem de boas-vindas com um botão inline "ENVIAR ÁUDIO". Quando o botão é clicado, o bot envia um arquivo de áudio predefinido para o usuário.

1. **Comando /start**: Ao enviar o comando /start, o bot responde com uma mensagem de boas-vindas e apresenta um botão inline para enviar um áudio.

2. **Botão Inline para Enviar Áudio**: O botão inline "ENVIAR ÁUDIO" permite que os usuários solicitem e recebam um arquivo de áudio predefinido.

3. **Envio de Arquivo de Áudio**: Quando o usuário clica no botão "ENVIAR ÁUDIO", o bot envia o arquivo de áudio correspondente.

4. **Tratamento de Erros**: O bot inclui tratamento de erros para lidar com possíveis problemas ao enviar o arquivo de áudio, garantindo uma experiência de usuário mais suave.

## EXPLICAÇÃO:
1. **Constante MEDIA_DIRECTORY**: Define o diretório onde os arquivos de mídia estão armazenados. Certifique-se de ter os arquivos de mídia (no formato MP3, no caso deste exemplo) neste diretório.

2. **Handler do Comando /start**: Quando o comando `/start` é recebido, o bot responde com uma mensagem que contém um botão inline "ENVIAR ÁUDIO".

3. **Criação do Teclado Inline**: A função `start` cria um teclado inline com um único botão para enviar áudio. Quando o botão é pressionado, ele aciona o callback especificado.

4. **Handler de Callback**: Quando o botão inline é pressionado, o handler de callback é acionado. Ele verifica se o `callback_data` é "send_audio".

5. **Envio do Áudio**: Se o `callback_data` for "send_audio", o bot chama a função `send_media` para enviar o arquivo de áudio para o chat. O caminho do arquivo de áudio é especificado usando o diretório de mídia definido anteriormente.

6. **Envio do Arquivo de Mídia**: A função `send_media` abre o arquivo de áudio e usa `bot.send_audio` para enviar o áudio para o chat especificado.
