# MODULO 01: PRIMEIROS COMANDOS

<img src="FOTO.jpg" align="center" width="400"> <br>

## DESCRIÇÃO: 
- Neste `MODULO 01`, você será introduzido aos recursos avançados de interação com seu bot no Telegram. Aqui está uma visão geral do que você aprenderá em cada tópico:

    - **Comandos via barra de texto:**
      - Exploraremos como os usuários podem interagir com seu bot através de comandos inseridos na barra de texto do Telegram. Você aprenderá a definir e processar comandos específicos para realizar ações dentro do seu bot, como exibir informações e executar funções.

    - **Utilização de botões de teclado:**
      - Veremos como criar e implementar botões de teclado, fornecendo aos usuários uma interface mais intuitiva e amigável para interagir com seu bot. Você aprenderá a criar diferentes tipos de teclados, como teclados de resposta única e teclados personalizados, e como processar as respostas dos usuários.

    - **Implementação de botões inline:**
      - Abordaremos a utilização de botões inline, que permitem aos usuários realizar ações específicas diretamente nas conversas, como enviar consultas de pesquisa, acionar ações ou fornecer feedback. Você aprenderá a criar e processar botões inline para proporcionar uma experiência de usuário mais dinâmica e interativa.

    - **Integração de bots inline:**
      - Exploraremos estratégias avançadas para a integração de bots inline em conversas individuais e em grupos. Você aprenderá a desenvolver bots inline que oferecem funcionalidades úteis e relevantes em resposta às consultas dos usuários, aumentando assim a usabilidade e a utilidade do seu bot no Telegram.

   - **Comandos Matemáticos (Tabuada/Calculadora):**
      - Através de bots matemáticos utilizando comandos, os usuários aprenderão a interagir de forma direta com o bot para realizar cálculos matemáticos específicos. Eles serão capazes de enviar comandos para executar diversas operações, como adição, subtração, multiplicação, divisão, entre outras. Além disso, os usuários podem solicitar funcionalidades específicas, como exibir a tabuada de um número ou resolver expressões matemáticas mais complexas. Esse tipo de interação proporciona aos usuários uma maneira conveniente e direta de obter resultados matemáticos, tornando o aprendizado e a prática desses conceitos mais acessíveis e interativos.

## PROPOSITO:
O propósito principal deste módulo é capacitar os alunos a implementar recursos avançados de interação com bots no Telegram, visando melhorar a experiência do usuário e expandir as funcionalidades do bot. Ao compreender e dominar os conceitos de comandos via barra de texto, botões de teclado e botões inline, os alunos serão capazes de criar bots mais interativos, intuitivos e úteis, capazes de atender às necessidades e expectativas dos usuários de forma mais eficaz.

## CARACTERISTICAS:
1. **Via Comandos (/comandos):**
   - Nesse modo de interação, o usuário envia comandos específicos precedidos por uma barra ("/") para o bot. O bot é configurado para reconhecer esses comandos e executar ações correspondentes a cada comando específico. Por exemplo, um usuário pode enviar "/start" para iniciar a interação com o bot ou "/help" para receber instruções de ajuda.

2. **Botões Inline:**
   - Com os botões inline, o bot envia opções ou botões interativos como parte de suas respostas às mensagens dos usuários. Esses botões geralmente aparecem abaixo da mensagem do bot e permitem que o usuário selecione uma opção com apenas um toque. O bot pode ser configurado para responder de maneira diferente com base no botão selecionado pelo usuário.

3. **Botões de Teclado:**
   - Os botões de teclado são semelhantes aos botões inline, mas em vez de aparecerem como parte da mensagem, eles são exibidos permanentemente na interface de chat do usuário. O bot pode enviar um teclado com várias opções, e o usuário pode selecionar uma delas clicando nos botões. Essa abordagem proporciona uma maneira conveniente e fácil de interagir com o bot, especialmente em dispositivos móveis.

4. **Bots Inline:**
   - Os bots inline são bots especiais que podem ser acionados a partir de qualquer conversa no Telegram, mesmo que o usuário não esteja interagindo diretamente com o bot. Quando o usuário digita "@" seguido do nome do bot em qualquer conversa, o bot inline é ativado e pode fornecer respostas ou realizar ações diretamente naquela conversa. Isso permite uma interação rápida e eficiente com os bots sem a necessidade de iniciar uma conversa separada.

## REQUESITOS:
### INSTALANDO O PYTHON:
1. **Baixe o Python:**
   Acesse o site oficial do Python em [python.org](https://www.python.org/downloads/) e faça o download da versão mais recente para o seu sistema operacional. Certifique-se de selecionar a opção que inclui o instalador para facilitar o processo.

2. **Execute o Instalador:**
   Após o download, execute o instalador. Certifique-se de marcar a opção "Adicionar o Python ao PATH" durante o processo de instalação. Isso facilitará a execução do Python a partir do terminal ou prompt de comando.

3. **Verifique a Instalação:**
   Após a instalação, abra o terminal ou prompt de comando e digite o seguinte comando para verificar se o Python foi instalado corretamente:
   ```
   python --version
   ```
   Isso deve exibir a versão do Python que você instalou.

4. Antes de iniciar a criação do seu bot, é fundamental possuir conhecimentos prévios em programação utilizando Python. Se ainda não possui essa habilidade, recomendamos que você faça um dos nossos cursos de Python para iniciantes, disponíveis nos seguintes links:
- [CURSO DE PYTHON](https://github.com/VILHALVA/CURSO-DE-PYTHON)
- [CURSO DE PYTHON POO](https://github.com/VILHALVA/CURSO-DE-PYTHON-POO)
- [CURSO DE LOGICA COM PYTHON](https://github.com/VILHALVA/CURSO-DE-LOGICA-COM-PYTHON)
- [MESTRE DO PYTHON](https://github.com/VILHALVA/MESTRE-DO-PYTHON)

### INSTALANDO O TELEBOT:
#### [PYTELEGRAMBOTAPI:](https://github.com/eternnoir/pyTelegramBotAPI#documentation)
1. **Abra o Terminal ou Prompt de Comando:**
   Abra o terminal ou prompt de comando no seu sistema operacional.

2. **Instale o Telebot usando o pip:**
   Execute o seguinte comando para instalar a biblioteca Telebot usando o pip, que é o gerenciador de pacotes padrão do Python:
   ```
   pip install pyTelegramBotAPI
   ```

3. **Verifique a Instalação:**
   Para verificar se a biblioteca foi instalada corretamente, você pode criar um arquivo Python e importar a biblioteca Telebot. Se não houver erros ao importar, significa que a instalação foi bem-sucedida.
   ```python
   import telebot
   ```

#### [PY-TELEGRAM-BOT:](https://python-telegram-bot.readthedocs.io/en/stable/)
1. **Abra o Terminal ou Prompt de Comando:**
   Abra o terminal ou prompt de comando no seu sistema operacional.

2. **Instale o py-telegram-bot usando o pip:**
   Execute o seguinte comando para instalar a biblioteca py-telegram-bot usando o pip, que é o gerenciador de pacotes padrão do Python:
   ```
   pip install python-telegram-bot
   ```

3. **Verifique a Instalação:**
   Para verificar se a biblioteca foi instalada corretamente, você pode criar um arquivo Python e importar a biblioteca py-telegram-bot. Se não houver erros ao importar, significa que a instalação foi bem-sucedida.
   ```python
   import telegram
   ```

## QUAL É DIFERENÇA?
Ambas "pyTelegramBotAPI" e "py-telegram-bot" são bibliotecas Python para criar bots no Telegram. Aqui está uma breve comparação entre elas:

1. **pyTelegramBotAPI**:
   - Esta biblioteca é mais antiga e amplamente utilizada.
   - É conhecida por ser simples e fácil de usar.
   - Oferece uma API bem documentada e possui uma comunidade ativa de desenvolvedores.
   - Fornecer recursos básicos e avançados para criar bots no Telegram.
   - Documentação clara e exemplos disponíveis para facilitar o aprendizado e uso.

2. **py-telegram-bot**:
   - Esta é uma biblioteca relativamente nova e crescente.
   - É considerada mais poderosa e flexível em comparação com pyTelegramBotAPI.
   - Possui uma arquitetura mais modular, permitindo maior personalização e extensibilidade.
   - Oferece suporte a funcionalidades avançadas do Telegram, como bots inline e bots de pagamento.
   - Tende a ser preferida por desenvolvedores que buscam uma solução mais avançada e têm requisitos mais complexos para seus bots.

