# ENTREVISTA
## DESCRIÇÃO:
Este bot de entrevista simples foi desenvolvido em Python usando a biblioteca Telegram Bot API. Sua função principal é coletar informações de membros, como nome e idade, e salvar esses dados em um banco de dados SQLite local. Aqui está uma visão geral das principais características e funcionalidades do bot:

1. **Início da Entrevista:** O bot é ativado com o comando `/start`. Ele cumprimenta o membro e faz perguntas específicas para coletar informações.

2. **Coleta de Dados:** O bot solicita o nome do membro e aguarda a entrada de texto. Em seguida, solicita a idade do membro e registra as respostas em uma conversa.

3. **Armazenamento em Banco de Dados:** Os dados coletados, ou seja, o nome e a idade do membro, são armazenados em um banco de dados SQLite local. Um registro é criado na tabela "entrevistas" para cada entrevistado.

4. **Cancelamento:** O membro pode cancelar a entrevista a qualquer momento, usando o comando `/cancel`. Nesse caso, o bot encerra a conversa e fornece instruções para reiniciar a entrevista.

Este bot é uma demonstração simples de como coletar dados de membro via Telegram e armazená-los em um banco de dados local. É útil para cenários em que você deseja coletar informações de usuários de forma interativa e organizada.

Lembre-se de criar a tabela adequada no banco de dados SQLite para armazenar os dados da entrevista antes de usar o bot.