# GRUPO PREMIUM
## DESCRIÇÃO:
Este bot Telegram atua como um moderador de grupo premium que impõe um requisito de adicionar 20 contatos aos membros do grupo antes que eles possam enviar mensagens. O bot verifica se os membros já cumpriram esse requisito antes de permitir que eles enviem mensagens no grupo. 

## FUNCIONALIDADES:
1. O bot verifica se um membro já adicionou 20 contatos ao grupo antes de permitir que eles enviem mensagens.
2. Se um membro não cumpriu esse requisito, o bot apaga a mensagem do membro e o silencia por 5 minutos.
3. O bot envia uma mensagem de advertência no grupo informando o membro sobre o requisito não cumprido e a mensagem de advertência é apagada após 5 minutos.
4. O bot permite que os membros adicionem contatos usando um comando `/adicionar_contatos`.
5. O bot armazena os membros que cumpriram o requisito em um banco de dados SQLite.
