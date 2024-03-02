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

## EXPLICAÇÃO:
1. **Dicionário `game_states`**: Este dicionário é usado para armazenar o estado do jogo para cada usuário. O estado do jogo inclui se o usuário está aguardando para adivinhar um número ou não, e o número correto que o usuário precisa adivinhar.

2. **Handler `start_game`**: Este é o handler para o comando `/start`. Quando o usuário inicia o jogo, o bot cria um teclado inline com botões numerados de 1 a 10 e envia uma mensagem de boas-vindas pedindo ao usuário para escolher um número. O estado do jogo é atualizado para "waiting_for_guess" e o número correto é escolhido aleatoriamente e armazenado.

3. **Handler `guess_number`**: Este é o handler para os callbacks dos botões numerados. Quando o usuário clica em um botão, este handler é acionado. Ele verifica se o número escolhido pelo usuário é igual ao número correto armazenado no estado do jogo. Se o número estiver correto, o bot envia uma mensagem de parabéns. Se estiver incorreto, o bot envia o número correto. O estado do jogo é então redefinido e os botões são removidos da mensagem.


