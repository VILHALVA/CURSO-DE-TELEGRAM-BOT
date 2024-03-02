# PROJETO FINAL - CONVERSADOR COM DICIONÁRIO DE PERGUNTAS E RESPOSTAS:
## DESCRIÇÃO:
Este bot é um assistente virtual básico. Ele foi projetado para interagir com os usuários respondendo a uma variedade de perguntas comuns e fornecendo informações úteis. Ele é capaz de responder a perguntas simples sobre sua identidade, suas habilidades e oferecer algumas funcionalidades, como contar piadas e fornecer informações básicas sobre diversos tópicos.

O bot é iniciado com uma saudação padrão quando o comando /start é enviado pelo usuário, e ele está programado para responder a uma série de perguntas frequentes, como "Qual é o seu nome?", "Como você está?" e "O que você pode fazer?".

Além disso, ele é capaz de fornecer respostas engraçadas, como contar piadas, além de oferecer assistência em algumas áreas específicas, como matemática e recomendações de restaurantes.

Este bot serve como uma introdução simples à interação com bots de bate-papo e pode ser expandido com mais perguntas e funcionalidades conforme necessário para atender às necessidades dos usuários.

## COMO USAR?
1. **Coloque O TOKEN:** Dentro do arquivo ´[CODIGO.py](CODIGO/CODIGO.py)´ coloque o seu TOKEN e der `RUN`.

2. **Iniciar o Bot**: Envie o comando /start para iniciar uma conversa.

3. **Perguntas Comuns**: Você pode fazer perguntas comuns, como "Olá", "Qual é o seu nome?" e "Como você está?". Ele responderá de acordo.

4. **Explorar Habilidades**: Experimente perguntar "O que você pode fazer?" para descobrir as habilidades. Ele está programado para fornecer informações básicas, contar piadas e muito mais!

5. **Adicionar mais Dialogo**: Dentro do arquivo `[CONVERSA.py](CODIGO/CONVERSA.py)` Adicione mais Perguntas e Respostas.

## EXPLICAÇÃO:
1. **CODIGO.py**:
   - `@bot.message_handler(func=lambda message: True)`: Define um manipulador de mensagem que é acionado para todas as mensagens recebidas pelo bot.
   - `handle_message(message)`: Esta função é chamada sempre que uma mensagem é recebida. Ela extrai o texto da mensagem, gera uma resposta com base no texto usando o método `generate_response` da classe `ConversationHandler` e responde ao remetente da mensagem com a resposta gerada.

2. **CONVERSA.py**:
   - `class ConversationHandler`: Define uma classe que contém métodos estáticos relacionados ao processamento de conversas.
   - `generate_response(input_text)`: Este método estático recebe o texto de entrada da mensagem e retorna uma resposta com base no texto. Ele contém um dicionário de perguntas e respostas predefinidas. Se a entrada corresponder a uma pergunta no dicionário, a resposta correspondente é retornada. Caso contrário, uma mensagem padrão de "Desculpe, não entendi. Tente outra pergunta!" é retornada.

## PORQUE É MELHOR USAR DICIONÁRIO DO QUE IF/ELSE NESSE CASO?
Usar um dicionário para mapear perguntas e respostas, como é feito neste código, é uma abordagem muito mais eficiente e escalável do que usar uma série de declarações if/else para verificar cada possível pergunta individualmente. Aqui estão algumas razões pelas quais o uso de um dicionário é preferível:

1. **Eficiência**:
   - Um dicionário permite o acesso direto aos valores com base em suas chaves, enquanto uma série de if/else requer verificações sequenciais até encontrar uma correspondência. Isso significa que, em média, a busca em um dicionário é mais rápida do que uma série de if/else, especialmente em casos onde há um grande número de perguntas e respostas.

2. **Facilidade de Manutenção**:
   - Manter uma lista de perguntas e respostas em um dicionário é muito mais fácil do que adicionar ou modificar várias declarações if/else. Com um dicionário, você pode adicionar ou alterar pares pergunta-resposta simplesmente atualizando o dicionário, sem a necessidade de alterar a estrutura do código.

3. **Escalabilidade**:
   - À medida que o número de perguntas e respostas aumenta, a manutenção de uma série de if/else se torna cada vez mais complicada e propensa a erros. Um dicionário, por outro lado, pode facilmente acomodar um número ilimitado de perguntas e respostas sem afetar significativamente a complexidade do código.

4. **Legibilidade do Código**:
   - O uso de um dicionário para mapear perguntas e respostas resulta em um código mais limpo e legível. A lógica de correspondência entre perguntas e respostas é encapsulada de forma concisa no dicionário, tornando mais fácil entender o propósito e o funcionamento do código.



