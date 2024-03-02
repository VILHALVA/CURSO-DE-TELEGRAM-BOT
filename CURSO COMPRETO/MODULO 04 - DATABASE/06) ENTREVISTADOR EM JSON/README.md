# ENTREVISTADOR EM JSON
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

- Ao integrar um banco de dados, com arquivos JSON, seremos capazes de salvar, recuperar, editar e apagar registros de forma confiável e duradoura. Essa abordagem oferecerá uma solução escalável e robusta para o armazenamento de dados do bot, garantindo que as informações dos usuários sejam preservadas ao longo do tempo e em diferentes sessões de uso do bot.

## EXPLICAÇÃO:
1. **Classe `Usuario`**: Esta classe representa um usuário com os atributos `nome` e `idade`. Será utilizada para criar instâncias de usuários.

2. **Classe `GerenciadorUsuarios`**: Esta classe é responsável por gerenciar as operações de adicionar, listar, atualizar e excluir usuários no arquivo JSON. Ela utiliza métodos para realizar essas operações.

3. **Método `start`**: Este método é chamado quando o usuário inicia a conversa com o bot. Ele exibe um teclado inline com opções para adicionar, listar, atualizar ou excluir usuários.

4. **Método `button`**: Este método é chamado quando o usuário pressiona um dos botões do teclado inline. Dependendo da opção selecionada, ele executa a ação correspondente.

5. **Método `message`**: Este método é chamado quando o usuário envia uma mensagem de texto. Ele processa a mensagem de acordo com a ação que está sendo executada (por exemplo, adicionar nome, idade, atualizar nome, idade etc.).

6. **Funcionalidades do CRUD**: O bot permite adicionar usuários fornecendo nome e idade, listar todos os usuários cadastrados, atualizar o nome e a idade de um usuário existente e excluir um usuário pelo nome.

7. **Inicialização do Bot**: O método `main` inicializa o bot, define os manipuladores de comandos e mensagens e inicia o polling para receber atualizações do Telegram.

8. **Persistência dos Dados**: Os dados dos usuários são armazenados em um arquivo JSON chamado `usuarios.json`. Cada vez que uma operação de CRUD é realizada, o arquivo é lido, atualizado conforme necessário e gravado de volta no disco.

