# UPLOAD DE ARQUIVOS
## DESCRIÇÃO:
Este bot é um utilitário para receber e salvar diferentes tipos de arquivos, incluindo áudio, foto, vídeo e documentos. Ele foi projetado para ser usado em conversas privadas, onde os usuários podem enviar os arquivos diretamente para o bot.

Ao iniciar uma conversa com o bot através do comando /start, os usuários receberão instruções sobre como usar o bot. Eles serão informados de que podem enviar qualquer tipo de arquivo desejado e o bot cuidará do resto.

Quando um usuário envia um arquivo, o bot salva o arquivo recebido em um diretório especificado no código. Após salvar o arquivo com sucesso, o bot fornece um feedback ao usuário informando que o arquivo foi salvo com sucesso.

Se ocorrer algum erro durante o processo de salvamento do arquivo, o bot também fornecerá um feedback ao usuário indicando que ocorreu um erro e fornecendo detalhes sobre o problema encontrado.

## EXPLICAÇÃO:
1. **Diretório de Salvamento de Arquivos**: O código define a variável `SAVE_DIR` para armazenar o diretório onde os arquivos recebidos serão salvos. Ele verifica se o diretório existe e, se não existir, o cria usando `os.makedirs(SAVE_DIR)`.

2. **Instruções de Uso**: Quando o usuário inicia a conversa com o bot através do comando `/start`, o bot responde com instruções sobre como usar o bot para enviar e salvar arquivos de diferentes tipos, como áudio, foto, vídeo ou documento.

3. **Manipulador de Mensagens para Arquivos**: O decorador `@bot.message_handler(content_types=["audio", "photo", "video", "document"])` define uma função chamada `save_media` para lidar com mensagens contendo qualquer um desses tipos de conteúdo.

4. **Salvar e Enviar Arquivo Recebido**: Na função `save_media`, o código identifica o tipo de conteúdo do arquivo recebido e obtém o ID do arquivo correspondente. Em seguida, ele faz o download do arquivo usando o ID do arquivo e o salva no diretório especificado, adicionando um carimbo de data e hora ao nome do arquivo para evitar substituições. Após salvar o arquivo com sucesso, o bot envia uma mensagem de confirmação para o usuário.

5. **Tratamento de Exceções**: Se ocorrer algum erro durante o processo de salvamento do arquivo, o bot envia uma mensagem de erro para o usuário informando sobre o problema encontrado.

