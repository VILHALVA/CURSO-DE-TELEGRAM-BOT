# CANAL PARCEIRO
## DESCRIÇÃO
Este bot foi desenvolvido para garantir que apenas membros inscritos em um canal parceiro específico no Telegram possam usá-lo.

- Ao receber o comando '/start', o bot verifica se o usuário que enviou a mensagem é um membro do canal parceiro especificado.
- Se o usuário for membro do canal parceiro, o bot responde permitindo o uso normal do bot.
- Se o usuário não for membro do canal parceiro, o bot informa que ele precisa ser membro do canal para usar o bot.
- O bot usa a API do Telegram para verificar o status de associação do usuário ao canal.

## CARACTERISTICAS:
- Verificação de associação ao canal: O bot usa a função `get_chat_member` da API do Telegram para verificar se o usuário é membro do canal parceiro.
- Resposta interativa: O bot responde de forma interativa, informando ao usuário se ele é membro do canal parceiro ou não.
- Compatibilidade multiplataforma: O bot pode ser implantado em qualquer plataforma que suporte a API do Telegram, como servidores locais ou em nuvem.



