# UPLOAD E DONWLOAD DE AUDIO
## DESCRIÇÃO:
- Este é um exemplo de um bot simples que permite o download de arquivos de áudio do Telegram. Ele é projetado para enviar um arquivo de áudio para um chat específico no Telegram, obter informações sobre o arquivo, fazer o download desse arquivo e salvá-lo localmente no sistema de arquivos do bot. Isso pode ser útil para automação de tarefas que envolvem o recebimento e o armazenamento de arquivos de áudio no Telegram. 

## EXPLICAÇÃO:
1. **Configuração Inicial**: O bot é configurado com o seu token, que é obtido ao criar um bot no BotFather do Telegram. Além disso, você precisa especificar o `CHAT_ID` para indicar o chat no qual você deseja que o bot envie mensagens.

2. **Envio de Áudio**: O bot usa o método `send_voice` para enviar uma mensagem de áudio para o chat especificado (`CHAT_ID`). O áudio é lido de um arquivo chamado 'audio.ogg', que está localizado em [AUDIO](CODIGO/AUDIO/audio.ogg)

3. **Obtenção de Informações do Arquivo de Voz**: Após o envio do áudio, o bot usa o método `get_file` para obter informações sobre o arquivo de áudio que foi enviado. Isso inclui detalhes como o `file_id` do arquivo, que é um identificador exclusivo.

4. **Download do Arquivo de Áudio**: O bot usa o método `download_file` para efetivamente fazer o download do arquivo de áudio. Ele usa o `file_path` obtido nas informações do arquivo de voz para encontrar o arquivo no servidor do Telegram.

5. **Salvar o Arquivo de Áudio**: Após o download, o bot salva o arquivo de áudio no disco local com o nome 'audio.ogg'. Ele cria um novo arquivo binário ('wb' significa escrita binária) e escreve o conteúdo baixado nesse arquivo.

## COMO USAR?
Para usar este script, você precisa substituir `'YOUR BOT TOKEN'` pelo token do seu bot e `'YOUR CHAT ID'` pelo ID do chat para o qual você deseja enviar a mensagem de voz. Além disso, você precisa ter um arquivo de voz (`'tests/test_data/record.ogg'` no exemplo) que deseja enviar.

Aqui está uma explicação passo a passo do que o script faz:

1. **Importações e Configurações**: O script começa importando a biblioteca `telebot` e define o token do bot e o ID do chat. Certifique-se de substituir esses valores pelos seus.

2. **Inicialização do Bot**: O bot é inicializado com o token fornecido.

3. **Envio da Mensagem de Voz**: O bot envia a mensagem de voz para o chat especificado usando `bot.send_voice`. Ele lê o arquivo de voz especificado (`'CODIGO/AUDIO/audio.ogg'` no exemplo) e envia-o para o chat.

4. **Obtenção do Arquivo de Voz**: Em seguida, o script obtém informações sobre o arquivo de voz enviado usando `bot.get_file`. Isso retorna um objeto `File` com detalhes sobre o arquivo de voz.

5. **Download do Arquivo de Voz**: O script usa `bot.download_file` para baixar o arquivo de voz. Ele passa o caminho do arquivo obtido anteriormente (`file_info.file_path`) para fazer o download do arquivo.

6. **Salvar o Arquivo**: Por fim, o arquivo de voz baixado é salvo no disco com o nome `'audio.ogg'`.

Certifique-se de que seu bot tenha permissão para enviar mensagens de voz e que o caminho do arquivo de voz esteja correto.


