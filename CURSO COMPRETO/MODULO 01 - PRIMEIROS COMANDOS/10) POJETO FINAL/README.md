# PROJETO FINAL: MENU E SUBMENUS DE BOTÕES INLINES
## DESCRIÇÃO:
Esse é um bot do Telegram que oferece opções de menu sobre diferentes tópicos (Astronomia, Ciência, Tecnologia e Telegram) e fornece informações sobre esses tópicos quando o usuário seleciona uma opção.

1. **Criação de botões inline**: Cada bot possui funções para criar botões inline, que são botões interativos que aparecem nas mensagens e permitem que os usuários interajam com o bot de maneira mais dinâmica.

2. **Callbacks para botões**: Os bots têm handlers de callback para processar as seleções dos usuários quando eles interagem com os botões inline. Esses callbacks são acionados quando um usuário clica em um botão e executam ações com base na seleção feita.

3. **Organização em submenus**: Cada bot organiza suas funcionalidades em submenus, com botões que representam diferentes categorias ou opções de interação. Isso ajuda a manter o código organizado e facilita a navegação para os usuários.

4. **Respostas às seleções dos usuários**: Cada código tem funções para responder às seleções dos usuários com mensagens relevantes ou ações apropriadas, com base nos botões que foram pressionados.

## CARACTERISTICAS:
1. **MAIN.py**:
   - Importações: O código importa os módulos `telebot` e os módulos personalizados `ASTRONOMIA`, `CIENCIA`, `TECNOLOGIA` e `TELEGRAM`.
   - Definição do token: O token do bot é definido na variável `TOKEN`.
   - Handlers de mensagem e callback: São definidos um handler para o comando `/start` ou `/menu` que exibe o menu principal e um handler para os callbacks dos botões que foram pressionados no menu.
   - Iniciar o bot: O bot é inicializado chamando `bot.polling()`, que faz com que o bot comece a buscar atualizações do Telegram.

2. **EXEMPLO: ASTRONOMIA.py**:
   - Função `submenu_astronomia()`: Essa função retorna um objeto `InlineKeyboardMarkup` que representa o submenu de Astronomia com botões para diferentes planetas.
   - Função `callback_query()`: Essa função é responsável por lidar com os callbacks dos botões do submenu de Astronomia. Dependendo do botão pressionado, ela envia uma mensagem com informações sobre o planeta correspondente.

## OBJETIVO:
Separar os submenus em arquivos separados e manter o menu principal em um arquivo dedicado, como "MAIN.py", é uma prática importante em projetos de desenvolvimento de software, incluindo bots. Isso ajuda a organizar o código de forma mais modular, facilitando a manutenção, a colaboração e a escalabilidade do projeto. Aqui estão algumas razões pelas quais essa abordagem é benéfica:

1. **Organização do Código:** Dividir o código em arquivos separados com responsabilidades específicas ajuda a manter a estrutura do projeto mais organizada e compreensível. Cada arquivo pode conter o código relacionado a uma parte específica do bot, como um submenu ou uma funcionalidade específica, facilitando a navegação e a localização de código relevante.

2. **Reutilização de Código:** Ao separar os submenus em arquivos individuais, você pode reutilizar facilmente esses componentes em outros projetos ou partes do mesmo projeto. Isso promove uma abordagem mais modular e facilita a manutenção e atualização de funcionalidades compartilhadas entre diferentes partes do bot.

3. **Escalabilidade:** Conforme o bot cresce e novas funcionalidades são adicionadas, manter o código organizado em arquivos separados torna mais fácil gerenciar o crescimento do projeto. Novos submenus ou funcionalidades podem ser facilmente adicionados sem afetar o código existente, desde que sigam a mesma estrutura modular.

4. **Colaboração:** Em projetos colaborativos, dividir o código em arquivos separados permite que diferentes membros da equipe trabalhem em partes específicas do bot de forma independente. Isso reduz conflitos de código e facilita a colaboração entre desenvolvedores.

## COMO FAZER?
1. Crie um arquivo "MAIN.py" que contenha o menu principal do bot e as importações necessárias para os submenus.
2. Crie arquivos separados para cada submenu ou funcionalidade do bot, nomeando-os de forma descritiva para facilitar a identificação.
3. No arquivo "MAIN.py", importe os submenus usando declarações de importação Python.
4. No arquivo de cada submenu, defina as funções e lógicas necessárias para essa parte específica do bot.
5. Certifique-se de que cada submenu seja acessível a partir do menu principal, definindo as opções de menu correspondentes e chamando as funções apropriadas de cada submenu.


