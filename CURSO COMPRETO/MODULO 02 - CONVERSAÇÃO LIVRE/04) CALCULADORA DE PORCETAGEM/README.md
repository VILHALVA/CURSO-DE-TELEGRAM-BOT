# CALCULADORA DE PORCETAGEM
## DESCRIÇÃO:
O bot Calculadora de Porcentagem é uma ferramenta útil para calcular tanto aumentos quanto descontos percentuais em valores numéricos. Com este bot, os usuários podem facilmente calcular o valor resultante após um aumento ou desconto em um valor específico. Basta enviar uma mensagem contendo o valor original seguido por um espaço e o percentual de aumento ou desconto desejado, e o bot fornecerá o resultado calculado. Esta calculadora é ideal para situações em que é necessário calcular rapidamente o valor após uma alteração percentual.

## COMO USAR?
1. Inicie o bot clicando no comando `/start`.

2. Após iniciar o bot, envie uma mensagem contendo o valor original seguido por um espaço e o percentual de aumento ou desconto desejado.

Por exemplo:
- Para calcular um aumento de 10% em um valor de 100, você pode enviar a mensagem `100 10`.
- Para calcular um desconto de 20% em um valor de 50, você pode enviar a mensagem `50 20`.

O bot calculará o resultado e responderá com o valor resultante após o aumento ou desconto.

Lembre-se de fornecer os valores separados por um espaço e garantir que o valor e a porcentagem sejam numéricos válidos para obter o resultado correto. Se você seguir estas etapas, poderá usar o bot de calculadora de porcentagem para calcular aumentos e descontos com facilidade.

## EXPLICAÇÃO:
1. **Configuração básica de logging**: Configura o logger para registrar possíveis erros ou mensagens informativas.

2. **Função `start`**: Este é o handler para o comando `/start`. Quando o usuário envia este comando, o bot responde com uma mensagem de boas-vindas e instruções sobre como usar o bot para calcular aumentos ou descontos percentuais.

3. **Função `calculate_percentage`**: Este é o handler para lidar com mensagens que contêm valores e porcentagens. Ele verifica se a mensagem contém um valor seguido por uma porcentagem, separados por um espaço. Em seguida, converte o valor para um número de ponto flutuante e a porcentagem para um número inteiro. Depois, calcula o resultado do aumento ou desconto e envia a resposta ao usuário.

4. **Função `main`**: Esta é a função principal do programa. Ela configura o `Updater` para receber atualizações do bot, registra os handlers para comandos e mensagens e inicia o bot para começar a receber e processar mensagens.

