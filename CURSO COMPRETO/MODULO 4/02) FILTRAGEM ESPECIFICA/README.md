# FILTRAGEM ESPECIFICA
Este é um exemplo de um "Bot de Filtragem de Texto" no Telegram, que demonstra como usar filtros personalizados para processar mensagens com base em padrões de texto específicos. Aqui está uma descrição das principais funcionalidades deste bot:

1. **Filtragem de Texto**: O bot é capaz de responder a mensagens de texto com base em diferentes padrões e critérios de filtragem.

2. **Respostas Simples**: Ele pode responder a mensagens de texto simples que correspondem a um texto específico.

   - Quando alguém envia a mensagem "hello", o bot responde com "hello" no mesmo formato.
   - Ele também pode corresponder ao texto "hello" independentemente de ser em maiúsculas ou minúsculas.

3. **Filtragem de Conteúdo**: O bot pode responder a mensagens que contenham palavras específicas.

   - Quando uma mensagem contém as palavras "good" ou "bad", o bot responde com a própria mensagem.
   - Isso também funciona independentemente das letras maiúsculas ou minúsculas nas palavras.

4. **Filtragem de Início de Texto**: O bot pode responder a mensagens que começam com um prefixo específico.

   - Se uma mensagem começa com "st", o bot responde com a própria mensagem.
   - Isso também funciona independentemente das letras maiúsculas ou minúsculas no prefixo.

5. **Filtragem de Final de Texto**: O bot pode responder a mensagens que terminam com um sufixo específico.

   - Se uma mensagem termina com "ay", o bot responde com a própria mensagem.
   - Isso também funciona independentemente das letras maiúsculas ou minúsculas no sufixo.

6. **Botões de Comando**: O bot responde a comandos específicos:

   - `/callback`: Isso mostra um botão de callback para os usuários.
   - `/poll`: Isso cria uma enquete com uma pergunta específica e opções.

7. **Manipulação de Callback**: O bot é capaz de lidar com callbacks quando os usuários interagem com os botões de callback.

   - Quando um usuário clica no botão de callback com o texto "example" ou "ExAmPLe" (ignorando maiúsculas/minúsculas), o bot responde com um alerta.

8. **Manipulação de Enquete**: O bot também pode lidar com enquetes.

   - Quando uma enquete com a pergunta específica "When do you prefer to work?" é criada, o bot imprime a pergunta.

9. **Filtragem de Padrões Múltiplos**: O bot pode lidar com mensagens que correspondem a múltiplos padrões. Por exemplo:

   - Se uma mensagem contém "hi" ou "привет" ou "salom" (ignorando maiúsculas/minúsculas), o bot responde com a própria mensagem.
   - Se uma mensagem começa com "mi" ou "mea" (ignorando maiúsculas/minúsculas), o bot responde com a própria mensagem.
   - Se uma mensagem termina com "es" ou "on" (ignorando maiúsculas/minúsculas), o bot responde com a própria mensagem.

10. **Filtragem de Comando de Banimento**: O bot pode executar ação de banimento em grupos. Ele banirá o usuário mencionado na resposta a uma mensagem que corresponda a um comando de banimento, como "!ban", "/ban", ".ban", "!бан", "/бан" ou ".бан" (ignorando maiúsculas/minúsculas).

   - Se um comando de banimento for detectado em uma resposta a uma mensagem, o bot banirá o usuário mencionado e responderá com "Banned."

Este bot é um exemplo útil de como criar filtros personalizados para responder a mensagens com base em critérios específicos de texto no Telegram.

[CÓDIGO FONTE BAIXADO DE PY TELEGRAM BOT API](https://github.com/eternnoir/pyTelegramBotAPI/blob/master/examples/custom_filters/advanced_text_filter.py)