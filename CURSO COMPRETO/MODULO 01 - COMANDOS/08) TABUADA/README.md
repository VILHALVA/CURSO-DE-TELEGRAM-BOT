# TABUADA
## DESCRIÇÃO
Este bot é uma ferramenta útil para obter tabuadas de multiplicação, adição, subtração e divisão. Ele fornece resultados instantâneos para cálculos básicos, permitindo que você visualize facilmente os resultados.

**Comandos Disponíveis:**
- `/start`: Inicia o bot e fornece uma breve descrição de suas funcionalidades, bem como uma lista de comandos disponíveis.
- `/tabuada [número]`: Obtém a tabuada completa de multiplicação, adição, subtração e divisão para o número especificado. Por exemplo, `/tabuada 7`.
- `/tbm [número]`: Obtém a tabuada de multiplicação
- `/tbd [número]`: Obtém a tabuada de divisão
- `/tba [número]`: Obtém a tabuada de adição
- `/tbs [número]`: Obtém a tabuada de subtração

- Para usar, envie o comando desejado seguido do número. Por exemplo: 
```
/tbm 5
```

## EXPLICAÇÃO:
1. **Função `start`**: Esta função é chamada quando o usuário envia o comando `/start`. Ela responde com uma mensagem de boas-vindas e fornece uma breve descrição dos comandos disponíveis.

2. **Funções `tabuada_multiplicacao`, `tabuada_divisao`, `tabuada_adicao` e `tabuada_subtracao`**: Cada uma dessas funções é chamada quando o usuário envia os comandos `/tbm`, `/tbd`, `/tba` e `/tbs`, respectivamente, seguido pelo número para o qual deseja obter a tabuada correspondente. Essas funções calculam a tabuada correspondente e respondem com a mensagem contendo os resultados.

3. **Função `main`**: Esta função é a função principal do programa. Ela cria um objeto `Updater` passando o token do bot. Em seguida, registra os manipuladores de comando para cada comando mencionado acima (`/start`, `/tbm`, `/tbd`, `/tba`, `/tbs`). Por fim, inicia o bot para receber atualizações do Telegram e fica ocioso, mantendo o bot em execução.

