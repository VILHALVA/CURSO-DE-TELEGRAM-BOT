# ENTREVISTADOR EM MYSQL
## DESCRIÇÃO:
Este bot do Telegram oferece uma variedade de recursos para gerenciar uma lista de usuários de forma eficiente e conveniente. Aqui estão os principais recursos:

1. **Adicionar Usuário**: Os usuários podem adicionar novos usuários à lista fornecendo seus nomes e idades. O bot guia por meio de uma série de mensagens interativas, solicitando o nome e a idade do novo usuário a ser adicionado.

2. **Listar Usuários**: O bot permite que as pessoas visualizem todos os usuários cadastrados na lista. Ao selecionar essa opção no menu, ele exibe uma lista detalhada de todos os usuários, incluindo seus nomes e idades.

3. **Atualizar Usuário**: Os usuários têm a capacidade de atualizar as informações de um usuário existente na lista. O bot solicita o nome do usuário a ser atualizado, seguido pelo novo nome e idade a serem atualizados. Isso permite que as pessoas mantenham a lista de usuários atualizada com as informações mais recentes.

4. **Excluir Usuário**: O bot permite que as pessoas excluam um usuário específico da lista. Ao selecionar essa opção no menu e fornecer o nome do usuário a ser excluído, o bot remove o usuário da lista, garantindo que apenas usuários válidos sejam mantidos na lista.

5. **Interface Amigável**: O bot oferece uma interface de usuário amigável, apresentando um menu inicial com botões inline que facilitam a navegação e a interação. Os usuários podem acessar facilmente as diferentes opções do bot e seguir as instruções fornecidas para realizar as operações desejadas.

6. **Feedback de Ações**: O bot fornece feedback claro e informativo após a conclusão de cada ação. Os usuários recebem mensagens de confirmação ou feedback de erro, garantindo uma experiência de usuário suave e sem problemas.

7. **Operações CRUD**: Este bot segue o paradigma CRUD (Create, Read, Update, Delete), permitindo que as pessoas realizem todas as operações básicas de manipulação de dados em uma lista de usuários diretamente do Telegram.

## PROPOSITO:
- No `Módulo 02`, nós criamos o bot `O6) ENTREVISTADOR`, no entanto, os registros eram armazenados apenas em variáveis temporárias na memória do programa. Isso significa que, se o bot fosse desligado ou reiniciado, todos os dados seriam perdidos. 

- Ao integrar um banco de dados, como MySQL, seremos capazes de salvar, recuperar, editar e apagar registros de forma confiável e duradoura. Essa abordagem oferecerá uma solução escalável e robusta para o armazenamento de dados do bot, garantindo que as informações dos usuários sejam preservadas ao longo do tempo e em diferentes sessões de uso do bot.

## EXPLICAÇÃO:
1. **Classe `GerenciadorUsuarios`**: Esta classe é responsável por todas as operações relacionadas aos usuários no banco de dados MySQL.

   - **Método `__init__`**: Estabelece a conexão com o banco de dados MySQL usando as credenciais fornecidas e inicializa o cursor para executar consultas SQL.

   - **Método `adicionar_usuario`**: Adiciona um novo usuário ao banco de dados. Recebe o nome e a idade do usuário como parâmetros e executa uma instrução SQL de inserção.

   - **Método `listar_usuarios`**: Retorna todos os usuários cadastrados no banco de dados. Executa uma consulta SQL de seleção para obter os nomes e idades dos usuários.

   - **Método `atualizar_usuario`**: Atualiza as informações de um usuário existente no banco de dados. Recebe o nome antigo, o novo nome e a nova idade como parâmetros e executa uma instrução SQL de atualização.

   - **Método `excluir_usuario`**: Exclui um usuário do banco de dados. Recebe o nome do usuário como parâmetro e executa uma instrução SQL de exclusão.

2. **Funções de manipulação de comandos e mensagens**: O bot utiliza as funções `start`, `button` e `message` para lidar com os comandos e mensagens enviadas pelos usuários.

   - **Método `start`**: Inicia a conversa com o usuário, exibindo um teclado inline com opções para adicionar, listar, atualizar ou excluir usuários.

   - **Método `button`**: É chamado quando o usuário pressiona um dos botões do teclado inline. Dependendo da opção selecionada, executa a ação correspondente.

   - **Método `message`**: É chamado quando o usuário envia uma mensagem de texto. Processa a mensagem de acordo com a ação que está sendo executada (por exemplo, adicionar nome, idade, atualizar nome, idade etc.).

3. **Inicialização do Bot**: O método `main` inicializa o bot, define os manipuladores de comandos e mensagens e inicia o polling para receber atualizações do Telegram.

4. **MySQL**: Os dados dos usuários são armazenados em um banco de dados MySQL chamado `cadastro`, na tabela `usuarios`. Cada linha na tabela representa um usuário com os campos `nome` e `idade`.

