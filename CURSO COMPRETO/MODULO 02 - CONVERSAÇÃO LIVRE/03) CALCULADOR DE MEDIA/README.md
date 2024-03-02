# CALCULAR MEDIA
## DESCRIÇÃO:
O "Bot da Média de Notas" é um assistente virtual desenvolvido em Python para a plataforma Telegram. Sua principal função é calcular a média de notas inseridas pelo usuário. Este bot oferece uma maneira simples e eficaz de calcular a média de quatro notas escolares.

- **Início Saudável**: Ao iniciar uma conversa com o bot enviando o comando `/start`, você será recebido com uma saudação amigável e instruções sobre como inserir suas notas.

- **Validação de Entrada**: O bot verifica se as notas inseridas estão no formato correto e se estão dentro da faixa de 0 a 10. Se algo estiver fora desses critérios, o bot fornecerá uma mensagem de erro e pedirá que você insira as notas novamente.

- **Cálculo da Média**: Depois de inserir as quatro notas válidas, o bot calculará automaticamente a média das notas e a exibirá com duas casas decimais.

## EXPLICAÇÃO:
1. **`notas = {}`**: Este dicionário será usado para armazenar as notas dos usuários, mas atualmente está vazio.

2. **Handler do Comando `/start`**:
   - Quando o usuário inicia o bot com o comando `/start`, a função `start` é chamada.
   - A função `start` envia uma mensagem de boas-vindas ao usuário, solicitando que eles digitem suas 4 notas separadas por espaços.
   - Em seguida, `bot.register_next_step_handler` é usado para registrar a próxima etapa de processamento da mensagem do usuário, que é a função `validar_notas`.

3. **Função `validar_notas`**:
   - Esta função é chamada após o usuário enviar suas notas.
   - Ele tenta processar as notas fornecidas pelo usuário.
   - Primeiro, verifica se o número de notas fornecidas é exatamente 4. Se não for, ele lança um erro.
   - Em seguida, converte as notas de strings para floats e verifica se todas as notas estão entre 0 e 10. Se não estiverem, ele lança um erro.
   - Calcula a média das notas e a envia de volta ao usuário com duas casas decimais de precisão.
   - Se ocorrer um erro durante o processamento das notas, ele envia uma mensagem de erro ao usuário e chama a função `start` novamente para reiniciar o processo.

