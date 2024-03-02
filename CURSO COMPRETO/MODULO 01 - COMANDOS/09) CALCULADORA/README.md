# BOT DE CALCULADORA
## DESCRIÇÃO:
O bot de calculadora é uma aplicação desenvolvida para o aplicativo de mensagens Telegram que permite aos usuários realizar operações matemáticas simples diretamente dentro da plataforma. Aqui está uma descrição do que o bot faz:

1. **Inicia a interação**: Quando um usuário inicia uma conversa com o bot, ele recebe uma mensagem de boas-vindas e uma breve saudação.

2. **Fornece ajuda**: Os usuários podem solicitar ajuda digitando o comando `/ajuda`. O bot responde com uma mensagem explicando os comandos disponíveis e como usá-los.

3. **Realiza cálculos**: Os usuários podem realizar cálculos matemáticos básicos utilizando os comandos disponíveis:
   - `somar {valor1} e {valor2}`: Calcula a soma de dois valores.
   - `subtrair {valor1} e {valor2}`: Calcula a subtração de dois valores.
   - `multiplicar {valor1} e {valor2}`: Calcula a multiplicação de dois valores.
   - `dividir {valor1} e {valor2}`: Calcula a divisão de dois valores.

4. **Responde aos comandos**: Após receber um comando válido, o bot realiza o cálculo correspondente e responde ao usuário com o resultado.

5. **Lida com entradas inválidas**: Se um usuário envia um comando inválido ou uma mensagem que o bot não consegue entender, o bot responde informando que não entendeu a mensagem.

## COMO USAR?
1. Inicie uma conversa com o bot no Telegram. Você pode encontrá-lo pesquisando pelo nome de usuário do bot na barra de pesquisa do Telegram.

2. Uma vez que a conversa tenha sido iniciada, você pode usar os seguintes comandos:

   - `/start`: Este comando inicia a interação com o bot e cumprimenta você.
   
   - `/ajuda`: Este comando mostra uma mensagem de ajuda com os comandos disponíveis.

   - `somar {valor1} e {valor2}`: Este comando calcula a soma dos dois valores especificados. Por exemplo, se você quiser somar 5 e 3, você digitaria: `somar 5 e 3`.

   - `subtrair {valor1} e {valor2}`: Este comando calcula a subtração dos dois valores especificados. Por exemplo, se você quiser subtrair 10 de 7, você digitaria: `subtrair 10 e 7`.

   - `multiplicar {valor1} e {valor2}`: Este comando calcula a multiplicação dos dois valores especificados. Por exemplo, se você quiser multiplicar 4 por 6, você digitaria: `multiplicar 4 e 6`.

   - `dividir {valor1} e {valor2}`: Este comando calcula a divisão dos dois valores especificados. Por exemplo, se você quiser dividir 15 por 3, você digitaria: `dividir 15 e 3`.

3. Após enviar um comando válido, o bot responderá com o resultado do cálculo. Se você enviar um comando inválido ou uma mensagem que o bot não entenda, ele responderá informando que não entendeu o que foi enviado.

## EXPLICAÇÃO:
### **CONFIG.py**:
1. **Configuração do Bot:**
   - É importada a biblioteca `telebot` para interagir com a API do Telegram.
   - É definido o token do bot, que deve ser substituído pelo token real fornecido pelo BotFather.
   - O objeto `bot` é criado usando o token fornecido.

### **MAIN.py**:
1. **Importações:**
   - São importados os módulos necessários, como `telebot`, `time`, e `re`.

2. **Handlers de Comando:**
   - `@bot.message_handler(commands=['ajuda'])`: Responde ao comando `/ajuda` fornecendo uma mensagem de ajuda com os comandos disponíveis.
   - `@bot.message_handler(commands=['start'])`: Responde ao comando `/start` iniciando a interação com o bot.

3. **Handlers de Mensagem:**
   - `@bot.message_handler(regexp=r"^somar ([+-]?([0-9]*[.])?[0-9]+) e ([+-]?([0-9]*[.])?[0-9]+)$")`: Responde a mensagens que correspondem ao padrão para soma. Extrai os valores da mensagem, calcula a soma e envia a resposta.
   - `@bot.message_handler(regexp=r"^subtrair ([+-]?([0-9]*[.])?[0-9]+) e ([+-]?([0-9]*[.])?[0-9]+)$")`: Responde a mensagens que correspondem ao padrão para subtração. Extrai os valores da mensagem, calcula a subtração e envia a resposta.
   - `@bot.message_handler(regexp=r"^multiplicar ([+-]?([0-9]*[.])?[0-9]+) e ([+-]?([0-9]*[.])?[0-9]+)$")`: Responde a mensagens que correspondem ao padrão para multiplicação. Extrai os valores da mensagem, calcula a multiplicação e envia a resposta.
   - `@bot.message_handler(regexp=r"^dividir ([+-]?([0-9]*[.])?[0-9]+) e ([+-]?([0-9]*[.])?[0-9]+)$")`: Responde a mensagens que correspondem ao padrão para divisão. Extrai os valores da mensagem, verifica se o denominador não é zero, calcula a divisão e envia a resposta.
   - `@bot.message_handler(func=lambda message: True)`: Responde a todas as outras mensagens com uma mensagem padrão de "não compreendi".

4. **Função `extrair_valores`:**
   - Esta função é responsável por extrair os valores numéricos de uma mensagem que corresponde a um padrão específico usando expressões regulares.

5. **Execução do Bot:**
   - O bot é iniciado para receber atualizações com um timeout de 20 segundos.

Este bot é capaz de realizar cálculos matemáticos simples e fornecer ajuda sobre os comandos disponíveis. Certifique-se de substituir `"AQUI_VAI_O_TOKEN_DO_SEU_BOT_TELEGRAM"` pelo token real do seu bot.

