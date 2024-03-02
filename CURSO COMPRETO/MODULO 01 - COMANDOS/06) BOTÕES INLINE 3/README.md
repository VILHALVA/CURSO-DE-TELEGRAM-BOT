# BOTÕES INLINE 3 (URL)
## DESCRIÇÃO:
O bot apresenta botões inline que, quando clicados, abrem URLs específicas.
Primeiramente ele enviará uma mensagem com os botões inline para acessar as URLs fornecidas. Ao clicar em um dos botões, o usuário será redirecionado para a URL correspondente.

## EXPLICAÇÃO DO [CODIGO 1](CODIGOS/CODIGO_1.py):
* **Handler para o comando "/start":**
   ```python
   @bot.message_handler(commands=["start"])
   def start(message):
       markup = InlineKeyboardMarkup(row_width=2)
       button1 = InlineKeyboardButton("Botão 1", url="https://t.me/CODIGOGP")
       button2 = InlineKeyboardButton("Botão 2", url="https://t.me/CODIGOCN")
       markup.add(button1, button2)
       bot.send_message(message.chat.id, "Use os botões inline para acessar os links!", reply_markup=markup)
   ```
   - Este código cria um handler para mensagens que começam com o comando "/start".
   - Quando o bot recebe o comando "/start", ele executa a função `start`.
   - Dentro da função `start`, é criado um teclado inline (`InlineKeyboardMarkup`) com uma largura de linha de 2 (`row_width=2`).
   - Dois botões inline são adicionados ao teclado (`button1` e `button2`), cada um com um texto e um URL associado.
   - Em seguida, uma mensagem é enviada para o chat do usuário com o texto "Use os botões inline para acessar os links!" e o teclado inline adicionado como reply_markup.

Essa abordagem permite que os usuários do bot iniciem a interação clicando no comando "/start" e, em seguida, possam acessar os links associados aos botões inline fornecidos.

## EXPLICAÇÃO DO [CODIGO 2](CODIGOS/CODIGO_2.py):
1. **Definindo a estrutura dos botões:**
   ```python
   keyboard = [
       [
           InlineKeyboardButton("Botão 1", url="https://www.exemplo.com"),
           InlineKeyboardButton("Botão 2", url="https://www.exemplo.com"),
           InlineKeyboardButton("Botão 3", url="https://www.exemplo.com")
       ],
       [
           InlineKeyboardButton("Botão 4", url="https://www.exemplo.com"),
           InlineKeyboardButton("Botão 5", url="https://www.exemplo.com")
       ],
       [
           InlineKeyboardButton("Botão 6", url="https://www.exemplo.com")
       ]
   ]
   ```
   - Aqui, uma estrutura de teclado é definida como uma lista de listas. Cada lista interna representa uma linha de botões.
   - Cada botão é um objeto `InlineKeyboardButton`. Eles têm um texto visível pelo usuário e um URL associado.

2. **Criando o `InlineKeyboardMarkup`:**
   ```python
   reply_markup = InlineKeyboardMarkup(keyboard)
   ```
   - O `InlineKeyboardMarkup` é inicializado com a estrutura do teclado definida acima.

3. **Registrando os handlers:**
   ```python
   dp.add_handler(CommandHandler("start", start))
   dp.add_handler(CallbackQueryHandler(button_click))
   ```
   - Aqui, os handlers são registrados para lidar com comandos e callbacks.
   - `CommandHandler("start", start)` registra a função `start` para lidar com o comando "/start".
   - `CallbackQueryHandler(button_click)` registra a função `button_click` para lidar com cliques nos botões inline.

No contexto geral do código, este trecho cria um conjunto de botões inline organizados em linhas diferentes e tamanhos diferentes. Quando o comando "/start" é enviado ao bot, ele responde com uma mensagem contendo esses botões inline. Se um desses botões for clicado pelo usuário, o `CallbackQueryHandler` irá direcionar o processamento para a função `button_click`.

## POSIÇÕES DOS BOTÕES:
Para definir a posição de um botão em um teclado inline no Telegram, você pode usar os métodos `row()` e `add()` disponíveis na classe `InlineKeyboardMarkup` do módulo `telebot.types`.

- O método `row()` permite adicionar um ou mais botões em uma mesma linha. Os botões adicionados por meio deste método serão exibidos lado a lado.
- O método `add()` permite adicionar botões em uma nova linha. Os botões adicionados por meio deste método serão exibidos em uma nova linha abaixo dos botões adicionados anteriormente.

Ao usar esses métodos, você pode controlar a disposição e a posição dos botões no teclado inline, organizando-os conforme sua preferência. Por exemplo, se você quiser que dois botões estejam na mesma linha e outros dois abaixo deles, você os adicionará em duas chamadas separadas ao método `row()`, e se desejar adicionar mais botões em outra linha, você usará o método `add()`. Assim, você pode criar layouts personalizados para atender às suas necessidades específicas de design e usabilidade.
