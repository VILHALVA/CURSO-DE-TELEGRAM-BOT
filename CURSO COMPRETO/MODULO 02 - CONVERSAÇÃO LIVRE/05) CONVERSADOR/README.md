# CONVERSADOR
## [CODIGO 1](./CODIGOS/CODIGO_1.py):
Este script Python utiliza a biblioteca `telebot` para criar um bot do Telegram com diferentes comandos e handlers para processar mensagens recebidas.

1. **Função de verificação:**
   ```python
   def verificar(mensagem):
       return True
   ```
   - Define uma função `verificar` que retorna sempre `True`. Esta função será usada para verificar se uma mensagem deve ser processada.

2. **Handlers para comandos:**
   - Handlers para comandos `/start` e `/help` que enviam mensagens de boas-vindas e instruções, respectivamente.
   - Handlers usam a função `verificar` para verificar se a mensagem deve ser processada.

3. **Handler para mensagens contendo a palavra "TOP":**
   - Este handler responde às mensagens que contêm a palavra "TOP" (independentemente da caixa).
   - Se a palavra "TOP" estiver presente na mensagem, o bot responde com "Sim, é muito top!".

4. **Handler padrão para mensagens não reconhecidas:**
   - Este handler é acionado quando nenhuma outra função de handler é correspondente à mensagem recebida.
   - Ele responde com uma mensagem padrão indicando que não entendeu a mensagem do usuário e sugere digitar `/help` para obter ajuda.

5. **Handler de tratamento de erros:**
   - Este handler é acionado sempre que ocorre um erro durante o processamento de uma mensagem.
   - Ele responde à mensagem original indicando que ocorreu um erro e exibe o erro específico.

## [CODIGO 2](./CODIGOS/CODIGO_2.py):
Esse é um bot que responde a mensagens do usuário com respostas específicas, dependendo do conteúdo da mensagem. 

1. **Handler para o Comando "/start":**
   ```python
   @bot.message_handler(func=verificar, commands=["start"])
   def start(mensagem):
       bot.send_message(mensagem.chat.id, "Olá usuário!")
   ```
   - Este handler responde ao comando "/start" com a mensagem "Olá usuário!".

2. **Handler para Todas as Mensagens:**
   ```python
   @bot.message_handler(func=verificar)
   def sample_responses(input_text):
       user_message = str(input_text).lower()
       if user_message in ("ola", "hi", "oi"):
           return "Iai! Beleza? Como está?"
       elif user_message in ("bem", "otimo", "top"):
           return "Que Bom!"
       elif user_message in ("mal", "mau", "ruim"):
           return "O problema não é meu!"
       elif user_message in ("time", "horas", "dia", "data"):
           now = datetime.now()
           date_time = now.strftime("%d/%m/%y, %H:%M:%S")
           return str(date_time)
       else:
           return "Sinto muito! Não compreendir o que você disse"
   ```
   - Este handler processa todas as mensagens de texto recebidas pelo bot.
   - Dependendo do conteúdo da mensagem, o bot responde com respostas predefinidas:
     - Se a mensagem contiver "ola", "hi" ou "oi", o bot responde com "Iai! Beleza? Como está?".
     - Se a mensagem contiver "bem", "otimo" ou "top", o bot responde com "Que Bom!".
     - Se a mensagem contiver "mal", "mau" ou "ruim", o bot responde com "O problema não é meu!".
     - Se a mensagem contiver "time", "horas", "dia" ou "data", o bot responde com a data e hora atuais.
     - Se a mensagem não corresponder a nenhum dos padrões acima, o bot responde com "Sinto muito! Não compreendi o que você disse".

3. **Tratamento de Mensagens e Erros:**
   ```python
   def handle_message(update, context):
       text = str(update.message.text).lower()
       response = sample_responses(text)
       update.message.reply_to(response)

   def error(update, context):
       print(f"Update {update} Causa do error: {context.error}")
   ```
   - `handle_message` é uma função que lida com as mensagens recebidas pelo bot e envia a resposta correspondente usando a função `sample_responses`.
   - `error` é uma função de callback para lidar com erros que possam ocorrer durante a execução do bot.

## [CODIGO 3](./CODIGOS/CODIGO_3.py):
Este é um bot do Telegram que responde a mensagens de texto com respostas predefinidas, dependendo do conteúdo da mensagem. Vamos analisar o código em detalhes:

1. **Funções de Resposta:**
   - `reply_to_message(update, context)`: Esta função é chamada sempre que o bot recebe uma mensagem de texto. Ela extrai o texto da mensagem, gera uma resposta usando a função `generate_response` e envia a resposta de volta ao remetente.
   - `generate_response(message)`: Esta função gera uma resposta com base no texto da mensagem recebida. Ela verifica se a mensagem começa com determinadas palavras-chave e retorna uma resposta correspondente.

2. **Configuração do Logger:**
   - `logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)`: Isso configura o formato e o nível de logging para o programa.

3. **Criação do Updater e Dispatcher:**
   - `updater = Updater('TOKEN AQUI')`: Isso cria um objeto Updater com o token do bot fornecido.
   - `dispatcher = updater.dispatcher`: Isso cria um dispatcher que gerenciará os handlers do bot.

4. **Criação dos Handlers:**
   - `start_handler = CommandHandler('start', reply_to_message)`: Este handler responde ao comando "/start" com a função `reply_to_message`.
   - `message_handler = MessageHandler(Filters.text & (~Filters.command), reply_to_message)`: Este handler responde a todas as mensagens de texto (exceto comandos) com a função `reply_to_message`.

5. **Adição dos Handlers ao Dispatcher:**
   - Os handlers criados são adicionados ao dispatcher para que o bot possa processar os comandos e mensagens recebidos.

No geral, este código cria um bot do Telegram que responde a mensagens de texto com respostas predefinidas. Ele pode ser estendido para lidar com uma variedade de interações com o usuário.

## AVISO: OS REGISTROS NÃO SÃO PERMANENTES:
- Este bot não utiliza um banco de dados para armazenar informações dos usuários permanentemente. Em vez disso, ele salva temporariamente os dados nas variáveis durante a execução do programa. Se o bot for reiniciado ou desligado, todas as informações armazenadas serão perdidas.

- Só no `MODULO 04` do nosso curso, será possível aprender a integrar um banco de dados ao bot para armazenar as informações dos usuários permanentemente, garantindo que os dados não sejam perdidos mesmo após reinicializações ou desligamentos do bot.

