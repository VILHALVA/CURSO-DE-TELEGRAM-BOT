# APROVAÇÃO DE ADM
## DESCRIÇÃO:
- Este bot gerencia a aprovação de usuários como administradores (ADM) para acessar recursos específicos.
- Quando um usuário inicia o bot pela primeira vez, ele verifica se o usuário está aprovado pelo ADM no banco de dados MySQL. Se não estiver aprovado, o bot oferece a opção de solicitar aprovação.
- Os usuários não aprovados podem solicitar aprovação clicando em um botão inline. A solicitação é enviada ao administrador do bot.
- O administrador do bot pode aprovar os usuários enviando o comando `/approve` seguido do ID do usuário.
- Após a aprovação, o usuário recebe uma mensagem confirmando sua aprovação pelo ADM e pode acessar os recursos específicos do bot.

## CARACTERISTICAS:
- Gerenciamento de Aprovação: O bot mantém um registro de usuários aprovados pelo ADM em um banco de dados MySQL.
- Interação com Usuário: O bot fornece uma interface interativa para solicitar aprovação e gerenciar usuários aprovados.
- Controle de Acesso: Apenas usuários aprovados pelo ADM têm acesso aos recursos específicos do bot.

## FAÇA MELHORIAS:
- Melhorias na Interface do Usuário: Pode-se aprimorar a interface do usuário para fornecer feedback mais claro durante o processo de solicitação e aprovação.
- Funcionalidades Adicionais: Podem ser adicionadas funcionalidades adicionais, como revogar aprovações de usuários ou enviar notificações aos administradores sobre novas solicitações de aprovação.

