# MIDIAS MYSQL
## ATENÇÃO:
- Antes de executar esse bot, você deve importar o arquivo `DATABASE.sql` para dentro do seu banco de dados.

- Após isso, coloque o nome da `host de conexão`, `seu user`, `sua senha` e `seu token` dentro de `CODIGO.py`.

## DESCRIÇÃO:
Este bot do Telegram é projetado para interagir com os usuários de forma a exibir uma lista de arquivos disponíveis em um banco de dados MySQL e permitir que os usuários selecionem um desses arquivos. Ele segue uma estrutura modular, onde cada ação ou comando tem seu próprio manipulador dedicado.

1. **Inicialização e Conexão ao Banco de Dados**: O bot é inicializado usando a biblioteca `telebot` e conecta-se a um banco de dados MySQL por meio do módulo `mysql.connector`, permitindo acessar os nomes dos arquivos armazenados.

2. **Comando `/start`**: Quando um usuário inicia uma conversa ou envia o comando `/start`, o bot responde enviando uma lista de botões inline contendo os nomes dos arquivos disponíveis no banco de dados.

3. **Manipulador de Botões Inline**: Cada botão inline corresponde a um arquivo disponível. Quando o usuário clica em um desses botões, o bot responde com uma mensagem contendo o nome do arquivo selecionado.

4. **Manipuladores de Callback**: Os manipuladores de callback são acionados quando um botão inline é pressionado. Eles são responsáveis por processar a seleção do usuário e responder adequadamente.

5. **Encerramento e Execução do Bot**: O código principal verifica se o script está sendo executado como o programa principal e inicia o polling do bot. Isso garante que o bot esteja pronto para receber mensagens.

## PROPOSITO:
O propósito desse bot do Telegram é fornecer aos usuários uma maneira conveniente de visualizar e selecionar arquivos armazenados em um banco de dados MySQL diretamente através da interface do Telegram. Ele é útil em cenários onde os usuários precisam acessar uma lista de arquivos disponíveis e interagir com eles de forma rápida e fácil, sem a necessidade de acessar diretamente o banco de dados ou usar interfaces mais complexas.

Alguns possíveis casos de uso incluem:

1. **Gerenciamento de Mídias**: Permite que os usuários acessem e escolham entre várias mídias armazenadas, como imagens, vídeos ou documentos.

2. **Catálogo de Produtos**: Em um contexto de comércio eletrônico, o bot pode oferecer aos usuários uma seleção de produtos disponíveis para visualização e compra.

3. **Recursos Educacionais**: Pode ser utilizado em plataformas de ensino a distância para fornecer acesso a materiais educacionais, como PDFs, apresentações ou vídeos.

4. **Sistema de Arquivos**: Em sistemas internos de gerenciamento de documentos de uma empresa, o bot pode permitir que os funcionários acessem e compartilhem documentos relevantes de forma eficiente.

## EXPLICAÇÃO:
1. `@bot.message_handler(commands=["start"])`:
   - Este é um decorador que informa ao bot que a função seguinte (`start`) será acionada quando um comando `/start` for enviado pelo usuário.

2. `def start(message):`:
   - Aqui começa a definição da função `start`. Ela recebe um parâmetro `message`, que é a mensagem enviada pelo usuário que acionou o comando `/start`.

3. `filenames = get_filenames()`:
   - Esta linha chama a função `get_filenames()` para obter os nomes dos arquivos do banco de dados.

4. `markup = InlineKeyboardMarkup(row_width=1)`:
   - Cria um novo objeto `InlineKeyboardMarkup` com uma largura de linha de 1, o que significa que os botões serão organizados em uma única coluna.

5. `for filename in filenames:`:
   - Inicia um loop sobre cada nome de arquivo obtido da função `get_filenames()`.

6. `markup.add(InlineKeyboardButton(filename, callback_data=filename))`:
   - Adiciona um botão inline para cada nome de arquivo à `markup`. Cada botão será rotulado com o nome do arquivo e terá seu `callback_data` definido como o nome do arquivo.

7. `bot.send_message(message.chat.id, "Escolha um arquivo:", reply_markup=markup)`:
   - Envia uma mensagem para o chat de onde veio a mensagem original (`message`), apresentando a mensagem "Escolha um arquivo:" e incluindo os botões inline contidos em `markup`.

8. `@bot.callback_query_handler(func=lambda call: True)`:
   - Este é um decorador que informa ao bot que a função seguinte (`callback_query`) será acionada sempre que houver uma resposta de callback.

9. `def callback_query(call):`:
   - Aqui começa a definição da função `callback_query`. Ela recebe um parâmetro `call`, que representa a resposta de callback do usuário.

10. `query = call.data`:
    - Extrai os dados do callback, que neste caso é o nome do arquivo selecionado pelo usuário.

11. `bot.send_message(call.message.chat.id, f'Você selecionou: {query}')`:
    - Envia uma mensagem para o chat de onde veio a mensagem de callback (`call.message.chat.id`), informando ao usuário qual arquivo foi selecionado.


