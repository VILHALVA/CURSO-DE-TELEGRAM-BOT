# ENTREVISTA
## DESCRIÇÃO:
Este bot do Telegram é um pequeno projeto para coletar dados de usuários e salvar no dicionário. 

* O usuário envia um comando `/start` ou `/ayuda` ou `/help` para iniciar o bot.
* O bot solicita o nome do usuário.
* O usuário envia seu nome.
* O bot solicita a idade do usuário.
* O usuário envia sua idade.
* O bot solicita o sexo do usuário.
* O usuário envia seu sexo.
* O bot envia uma mensagem com os dados do usuário.

## EXECUÇÃO:
```
Usuário: /start

Bot: QUAL É O SEU NOME?

Usuário: João

Bot: OLÁ, João! QUAL É A SUA IDADE?

Usuário: 20

Bot: QUAL É O SEU SEXO?

Usuário: HOMEM

Bot: DADOS INTRODUZIDOS:

NOME..: João
IDADE..: 20
SEXO..: HOMEM
```

## EXPLICAÇÃO:
1. **Dicionário `usuarios`**: É usado para armazenar informações dos usuários, como nome, idade e sexo, indexados pelo ID do chat.

2. **Função `cmd_start`**: Esta função é chamada quando o usuário envia um dos comandos `/start`, `/ayuda` ou `/help`. Ela responde solicitando ao usuário que envie seu nome usando `ForceReply()`. Em seguida, registra a próxima etapa para lidar com a resposta do usuário.

3. **Função `perguntar_nome`**: Esta função é chamada para processar a resposta do usuário ao solicitar o nome. Ela armazena o nome do usuário no dicionário `usuarios` e solicita a idade do usuário usando `ForceReply()`. Novamente, registra a próxima etapa para lidar com a resposta do usuário.

4. **Função `perguntar_idade`**: Esta função é chamada para processar a resposta do usuário à solicitação de idade. Primeiro, verifica se a entrada é um número. Se não for, solicita novamente. Se for um número, armazena a idade do usuário no dicionário `usuarios` e solicita o sexo do usuário usando um teclado personalizado (`ReplyKeyboardMarkup`). Novamente, registra a próxima etapa para lidar com a resposta do usuário.

5. **Função `dados_usuario`**: Esta função é chamada para processar a resposta do usuário à solicitação de sexo. Primeiro, verifica se o usuário selecionou uma das opções fornecidas. Se não tiver, solicita novamente. Se tiver, armazena o sexo do usuário no dicionário `usuarios` e envia uma mensagem com os dados introduzidos pelo usuário.

6. **Saída dos dados**: Após todas as informações serem coletadas, uma mensagem contendo o nome, idade e sexo do usuário é enviada para o chat do usuário.

## AVISO: OS REGISTROS NÃO SÃO PERMANENTES:
- Este bot não utiliza um banco de dados para armazenar informações dos usuários permanentemente. Em vez disso, ele salva temporariamente os dados nas variáveis durante a execução do programa. Se o bot for reiniciado ou desligado, todas as informações armazenadas serão perdidas.

- Só no `MODULO 04` do nosso curso, será possível aprender a integrar um banco de dados ao bot para armazenar as informações dos usuários permanentemente, garantindo que os dados não sejam perdidos mesmo após reinicializações ou desligamentos do bot.

