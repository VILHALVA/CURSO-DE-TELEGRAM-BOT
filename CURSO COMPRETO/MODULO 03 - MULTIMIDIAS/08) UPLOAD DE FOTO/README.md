# UPLOAD DE FOTO
## DESCRIÇÃO:
Este bot foi desenvolvido para receber fotos enviadas pelos usuários e salvá-las localmente em um diretório chamado "FOTOS". Ele é capaz de lidar com diferentes formatos de fotos, incluindo JPG, PNG e outros formatos suportados pelo Telegram. Além disso, fornece feedback aos usuários informando se a foto foi recebida e salva com sucesso ou se ocorreu algum erro durante o processamento.

## EXPLICAÇÃO:
1. **Handler de Mensagens de Fotos**: O decorador `@bot.message_handler(content_types=['photo'])` define uma função chamada `handle_photos` para lidar com mensagens contendo fotos.

2. **Obtenção do ID da Conversa**: O ID da conversa (chat_id) é obtido da mensagem para que o bot saiba para onde enviar o feedback após processar a foto.

3. **Verificação e Criação do Diretório de Fotos**: O código verifica se o diretório "./FOTOS" existe. Se não existir, o código cria o diretório usando `os.makedirs("./FOTOS")`.

4. **Download e Salvamento da Foto**: A função tenta baixar a foto enviada usando o ID do arquivo da foto. A última foto enviada é escolhida para garantir a maior resolução possível. Em seguida, a foto é salva no diretório "./FOTOS" com o nome do arquivo sendo o ID do arquivo da foto seguido da extensão ".jpg".

5. **Feedback ao Usuário**: Após salvar a foto com sucesso, o bot envia uma mensagem de feedback para o usuário informando que a foto foi recebida e salva com sucesso.

6. **Tratamento de Exceções**: Se ocorrer algum erro durante o processamento da foto, uma mensagem de erro é enviada para o usuário informando sobre o problema encontrado.

## COMO USAR?
1. Adicione o bot ao seu Telegram e inicie uma conversa com ele.
2. Envie a foto que deseja salvar para o bot.
3. Aguarde o feedback do bot, que informará se a foto foi recebida e salva com sucesso ou se ocorreu algum erro durante o processamento.
4. Caso ocorra algum erro, verifique se a foto está em um formato suportado e tente enviar novamente.