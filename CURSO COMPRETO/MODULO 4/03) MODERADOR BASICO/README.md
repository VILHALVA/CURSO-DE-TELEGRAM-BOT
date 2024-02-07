# MODERADOR BÁSICO
## DESCRIÇÃO:
Este é um exemplo de bot capaz de moderar um grupo. Ele executa as seguintes funções:

1. **Comando /start**: Quando um usuário envia o comando /start para o bot, ele responde com uma mensagem de boas-vindas.

2. **Monitoramento de Mensagens**: O bot monitora as mensagens enviadas ao grupo. Se a mensagem contiver a palavra "palavrão", o bot remove a mensagem, envia uma mensagem de aviso ao usuário e remove o usuário do grupo.

3. **Bem-vindo a Novos Membros**: O bot envia uma mensagem de boas-vindas sempre que um novo membro ingressa no grupo.

4. **Adeus a Membros Removidos**: Quando um membro é removido do grupo, seja pelo próprio membro ou pelo administrador, o bot envia uma mensagem de despedida.

## PROGRAMANDO:
O código utiliza a biblioteca `python-telegram-bot` para interagir com a API do Telegram e implementar as funcionalidades mencionadas acima. Abaixo está uma breve explicação das principais partes do código:

1. **Configuração Inicial e Token**: Substitua `'TOKEN_AQUI'` pelo token do seu bot, obtido ao criar o bot com o BotFather no Telegram.

2. **Criação do Updater**: O Updater é responsável por receber as atualizações do Telegram.

3. **Handlers de Comando e Mensagem**: O código define três handlers principais:
   - `start_handler`: Responde ao comando /start com uma mensagem de boas-vindas.
   - `message_handler`: Monitora as mensagens do grupo, verifica se contêm palavras ofensivas e toma ações apropriadas.
   - `new_member_handler`: Envia uma mensagem de boas-vindas sempre que um novo membro ingressa no grupo.

4. **Funções de Callback**: As funções como `start`, `handle_message`, `new_member`, `bot_removed`, e `member_left` são chamadas quando o bot recebe as respectivas atualizações do Telegram.

5. **Adição de Handlers**: Os handlers são adicionados ao Dispatcher do Updater, que direciona as atualizações para as funções apropriadas.

6. **Inicialização do Bot**: O `updater.start_polling()` inicia o processo de busca por novas atualizações do Telegram.

## OBSERVAÇÃO:
Este é apenas um exemplo básico, e você pode personalizá-lo para atender às suas necessidades específicas de moderação e interação com o grupo.