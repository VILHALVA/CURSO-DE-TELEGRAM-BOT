# DESAFIXAR MENSAGEM DE CANAL VINCULADO
## DESCRIÇÃO
Este bot foi projetado para atuar como um moderador de mensagens em um grupo do Telegram que possui um canal vinculado. Seu principal objetivo é desafixar (remover) mensagens que são encaminhadas a partir do canal vinculado, mantendo o grupo organizado e evitando a poluição causada por mensagens indesejadas. Aqui está uma visão geral de suas funcionalidades:

1. **Desafixação de Mensagens:** Quando um membro encaminha uma mensagem de um canal vinculado para o grupo, o bot detecta a origem da mensagem e a desafixa (remove) do canal vinculado. Isso ajuda a manter o grupo limpo e focado em conversas relevantes.

2. **Notificações de Desafixação:** Após remover uma mensagem do canal vinculado, o bot envia uma mensagem de notificação para o grupo, informando que uma mensagem do canal vinculado foi removida. Isso mantém os membros cientes das ações do bot.

3. **Comando /start:** O bot responde ao comando "/start" com uma mensagem de boas-vindas, indicando que está ativo e pronto para moderar o grupo.

4. **Lida com Outras Mensagens:** Além de desafixar mensagens de canais vinculados, o bot também lida com outras mensagens enviadas no grupo. Ele não interfere em mensagens normais e apenas executa ação quando identifica mensagens encaminhadas de canais.

É importante configurar o token do bot (`TOKEN`) e personalizar as mensagens de notificação de acordo com suas preferências. Além disso, você pode ajustar as permissões e configurações de privacidade do grupo para permitir que o bot exclua mensagens.

Lembre-se de que este é um exemplo simplificado e pode ser aprimorado para atender a requisitos específicos do seu grupo ou canal vinculado. A API do Telegram está sujeita a alterações, portanto, verifique a documentação oficial para obter informações atualizadas sobre como trabalhar com mensagens e canais.