# JOGO DE ADIVINHAÇÃO
## DESCRIÇÃO:
Este é um simples bot do Telegram que permite aos usuários jogarem um jogo de adivinhação. O bot escolhe um número aleatório entre 1 e 10 através de botões inline, e o usuário deve tentar adivinhar qual é o número correto.

## COMO USAR?
1. Execute o código Python para iniciar o bot.

2. Inicie uma conversa com o bot no Telegram.

3. Use o comando `/start` para iniciar o jogo.

4. O bot apresentará um teclado inline com números de 1 a 10.

5. Clique no número que você acha que é o correto.

6. O bot responderá com uma mensagem indicando se você acertou ou errou.

7. O jogo pode ser reiniciado a qualquer momento usando o comando `/start`.

## ESTRUTURA:
- `start_game`: Esta função é acionada quando o usuário envia o comando `/start`. Ela cria um teclado inline com os números de 1 a 10 e inicia o jogo.

- `guess_number`: Esta função é acionada quando o usuário clica em um dos números no teclado inline. Ela verifica se o número escolhido pelo usuário é igual ao número correto escolhido pelo bot e envia uma mensagem com o resultado.

- `game_states`: Um dicionário para armazenar o estado do jogo para cada usuário.

- O bot utiliza a biblioteca `python-telegram-bot` para se comunicar com a API do Telegram e interagir com os usuários.

