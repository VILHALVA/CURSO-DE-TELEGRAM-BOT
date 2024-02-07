# DONWLOAD DE AUDIO
Este é um exemplo de um bot simples que permite o download de arquivos de áudio do Telegram. Aqui está uma descrição das principais funcionalidades deste bot:

1. **Configuração Inicial**: O bot é configurado com o seu token, que é obtido ao criar um bot no BotFather do Telegram. Além disso, você precisa especificar o `CHAT_ID` para indicar o chat no qual você deseja que o bot envie mensagens.

2. **Envio de Áudio**: O bot usa o método `send_voice` para enviar uma mensagem de áudio para o chat especificado (`CHAT_ID`). O áudio é lido de um arquivo chamado 'record.ogg', que está localizado em algum diretório (o caminho real do arquivo precisa ser especificado).

3. **Obtenção de Informações do Arquivo de Voz**: Após o envio do áudio, o bot usa o método `get_file` para obter informações sobre o arquivo de áudio que foi enviado. Isso inclui detalhes como o `file_id` do arquivo, que é um identificador exclusivo.

4. **Download do Arquivo de Áudio**: O bot usa o método `download_file` para efetivamente fazer o download do arquivo de áudio. Ele usa o `file_path` obtido nas informações do arquivo de voz para encontrar o arquivo no servidor do Telegram.

5. **Salvar o Arquivo de Áudio**: Após o download, o bot salva o arquivo de áudio no disco local com o nome 'new_file.ogg'. Ele cria um novo arquivo binário ('wb' significa escrita binária) e escreve o conteúdo baixado nesse arquivo.

Em resumo, este bot é projetado para enviar um arquivo de áudio para um chat específico no Telegram, obter informações sobre o arquivo, fazer o download desse arquivo e salvá-lo localmente no sistema de arquivos do bot. Isso pode ser útil para automação de tarefas que envolvem o recebimento e o armazenamento de arquivos de áudio no Telegram. Certifique-se de substituir 'YOUR BOT TOKEN' e 'YOUR CHAT ID' com os valores apropriados antes de usar o bot.

[CÓDIGO FONTE BAIXADO DE PY TLEGRAM BOT API](https://github.com/eternnoir/pyTelegramBotAPI/blob/master/examples/download_file_example.py)