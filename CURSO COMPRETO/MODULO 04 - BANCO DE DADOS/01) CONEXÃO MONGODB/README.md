# CONEXÃO COM MONGODB
## DESCRIÇÃO
Este bot é um exemplo simples de como testar a conexão com um banco de dados MongoDB utilizando a API do Telegram. Ele oferece dois comandos:

1. `/start`: Ao iniciar o bot, ele envia uma mensagem de boas-vindas ao usuário.
2. `/test_db`: Este comando é utilizado para testar a conexão com o MongoDB. Quando acionado, o bot tenta conectar-se ao banco de dados especificado na URI fornecida e inserir um documento de teste na coleção `test_collection` do banco de dados `test_database`. Se a operação for bem-sucedida, uma mensagem de confirmação é enviada; caso contrário, uma mensagem de erro é enviada ao usuário.

É importante configurar o token do bot do Telegram e a URI de conexão do MongoDB antes de iniciar o bot. Este bot pode ser útil para verificar se a conexão com o MongoDB está funcionando corretamente antes de implementar recursos mais avançados que dependem do banco de dados.

## EXPLICAÇÃO:
1. **Classe `Bot`**:
   - O construtor `__init__` recebe o token do bot e a URI de conexão do MongoDB como parâmetros. Ele inicializa o `Updater` do Telegram e o `dispatcher`.
   - Dois manipuladores de comando são adicionados ao `dispatcher`: um para o comando `/start` e outro para o comando `/test_db`.
   
2. **Método `start`**:
   - Este método é chamado quando o usuário envia o comando `/start`. Ele responde com uma mensagem de boas-vindas e instrui o usuário a usar o comando `/test_db` para verificar a conexão com o MongoDB.
   
3. **Método `test_db`**:
   - Este método é chamado quando o usuário envia o comando `/test_db`. Ele tenta conectar-se ao banco de dados MongoDB usando a URI fornecida. Se a conexão for bem-sucedida, uma mensagem de confirmação é enviada ao usuário. Se ocorrer algum erro durante a conexão, uma mensagem de erro é enviada.
   
4. **Método `start_bot`**:
   - Este método inicia o bot, iniciando o processo de polling para receber atualizações do Telegram.

5. **Condição `__name__ == "__main__"`**:
   - Essa condição garante que o código dentro dela só seja executado quando o script for executado diretamente, não quando for importado como um módulo. Isso é comum em scripts Python para garantir que certas partes do código sejam executadas apenas quando o script é executado como o programa principal.

