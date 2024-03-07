# BLOQUEIO DE MIDIAS
## DESCRIÇÃO:
Este bot do Telegram foi projetado para ajudar administradores de grupos a controlar o envio de mídias indesejadas, como fotos, vídeos, gifs e áudios. Abaixo está uma descrição detalhada das funcionalidades e do comportamento do bot:

1. **Configuração de Bloqueio de Mídias**: Os administradores podem usar o comando "/settings" para acessar as configurações de bloqueio de mídias do grupo. Eles são apresentados com opções para bloquear ou permitir o envio de diferentes tipos de mídias, como fotos, vídeos, gifs e áudios.

2. **Interface de Configuração Intuitiva**: O bot fornece uma interface amigável com botões que representam cada tipo de mídia. Os administradores podem selecionar os tipos de mídias que desejam bloquear ou permitir no grupo.

3. **Armazenamento de Configurações por Grupo**: As configurações de bloqueio de mídias são armazenadas no banco de dados MySQL, garantindo que as preferências de cada grupo sejam mantidas e aplicadas consistentemente.

4. **Aplicação Automática de Punições**: Quando um usuário tenta enviar uma mídia que está bloqueada de acordo com as configurações do grupo, o bot automaticamente impede o envio da mídia e, se configurado para isso, pode aplicar uma punição adicional, como restringir o usuário de enviar mensagens temporariamente.

5. **Feedback de Configuração Atual**: Após alterar as configurações, o bot envia uma mensagem confirmando as novas configurações de bloqueio de mídias para garantir que os administradores estejam cientes das mudanças.

6. **Gestão de Erros Robusta**: O bot é projetado para lidar com erros de forma adequada, garantindo que as configurações sejam aplicadas corretamente e que os administradores recebam feedback adequado em caso de problemas.

## EXPLICAÇÃO:
1. **Configuração Inicial:**
   - Importa os módulos necessários.
   - Estabelece a conexão com o banco de dados MySQL.
   - Cria um objeto `telebot.TeleBot` com o token fornecido.

2. **Handlers de Mensagem:**
   - `handle_settings`: Lida com o comando `/settings`, permitindo que administradores de grupo configurem o bloqueio de mídia.
   - `handle_callback_query`: Lida com as respostas dos botões de configuração.
   - `handle_media`: Lida com mensagens de mídia recebidas no grupo e aplica o bloqueio conforme configurado.

3. **Funções Auxiliares:**
   - `save_punishment`: Salva a configuração de bloqueio de mídia no banco de dados.
   - `get_punishment`: Obtém a configuração atual de bloqueio de mídia do banco de dados.
   - `apply_punishment`: Aplica o bloqueio de mídia com base na configuração.

4. **Execução do Bot:**
   - Inicia o bot, começando a receber atualizações do Telegram com `bot.polling()`.