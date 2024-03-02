# SECRETARIO 2 (VIA CONSOLE)
## DESCRIÇÃO:
- O bot recebe mensagens de texto dos usuários e responde com informações relacionadas aos tópicos especificados.
- Você recebe a mensagem que o usuário enviou no PV do bot dentro do console da sua IDE (Ou servidor). Daí você pode responde-lo diretamente pela IDE.

## EXPLICAÇÃO:
1. **Classe `TelegramBot`:**
   - Inicializa o bot com um token e define a URL base da API do Telegram.

2. **Método `Iniciar`:**
   - Inicia um loop infinito para ler novas mensagens.
   - Obtém as atualizações do Telegram usando o método `ler_novas_mensagens`.
   - Para cada mensagem, extrai o texto, o ID do chat e a ID da mensagem.
   - Gera uma resposta com base no texto da mensagem usando o método `gerar_respostas`.
   - Envia a resposta de volta ao remetente usando o método `responder`.

3. **Método `ler_novas_mensagens`:**
   - Constrói uma solicitação para obter atualizações do Telegram, passando um timeout de 5 segundos.
   - Se houver um ID de atualização fornecido, adiciona esse ID à solicitação para buscar apenas atualizações mais recentes.
   - Envia a solicitação e retorna os dados JSON da resposta.

4. **Método `gerar_respostas`:**
   - Recebe a mensagem do usuário e determina a resposta com base no conteúdo da mensagem.
   - Imprime a mensagem do usuário para registro.
   - Se a mensagem for uma saudação ou uma mensagem específica, retorna uma resposta correspondente sobre Tecnologia, Ciência, Filosofia ou Teologia.
   - Se a mensagem for uma confirmação ou negação, retorna uma resposta correspondente.
   - Se a mensagem não for reconhecida, retorna uma mensagem de erro.

5. **Método `responder`:**
   - Constrói uma solicitação para enviar uma mensagem de volta ao usuário, fornecendo o texto da resposta e o ID do chat.
   - Envia a solicitação ao Telegram para enviar a mensagem de volta ao usuário.

Este bot responderá às mensagens dos usuários com base em padrões predefinidos e fornecerá informações sobre Tecnologia, Ciência, Filosofia e Teologia. 


