# CONEXÃO COM MYSQL
## DESCRIÇÃO:
Este bot foi desenvolvido para testar a conexão com um banco de dados MySQL. Ele oferece dois comandos principais:

1. **/start**: Ao enviar este comando, o bot envia uma saudação ao usuário, informando que está pronto para testar a conexão com o MySQL.

2. **/test_mysql**: Este comando é usado para testar a conexão com o banco de dados MySQL. Quando o comando é enviado, o bot tenta estabelecer uma conexão com o MySQL usando as informações fornecidas, como o host, usuário, senha e nome do banco de dados. Ele então envia uma mensagem indicando se a conexão foi estabelecida com sucesso ou se ocorreu algum erro durante o processo de conexão.

Este bot é útil para verificar rapidamente se as configurações de conexão com o MySQL estão corretas e se o bot pode se comunicar com o banco de dados sem problemas. Ele fornece uma maneira conveniente de realizar essa verificação diretamente no Telegram, economizando tempo e esforço para os desenvolvedores.

## EXPLICAÇÃO:
1. **Método `start`**:
   - Este método é chamado quando o usuário envia o comando `/start`. Ele responde com uma mensagem de boas-vindas.

2. **Método `test_mysql`**:
   - Este método é chamado quando o usuário envia o comando `/test_mysql`. Ele tenta conectar-se ao banco de dados MySQL usando as credenciais fornecidas. Se a conexão for bem-sucedida, uma mensagem de confirmação é enviada ao usuário. Se ocorrer algum erro durante a conexão, uma mensagem de erro é enviada.

3. **Método `main`**:
   - Este é o ponto de entrada principal do programa. Ele inicializa o bot do Telegram, adiciona os handlers para os comandos `/start` e `/test_mysql` e inicia o bot para começar a receber atualizações do Telegram.

4. **Condição `__name__ == '__main__'`**:
   - Esta condição garante que o código dentro dela só seja executado quando o script for executado diretamente, não quando for importado como um módulo. Isso é comum em scripts Python para garantir que certas partes do código sejam executadas apenas quando o script é executado como o programa principal.

Para usar este bot, você precisa substituir `"TOKEN_DO_SEU_BOT"`, `'seu_host'`, `'seu_usuario'`, `'sua_senha'` e `'seu_banco_de_dados'` pelas informações reais do seu bot do Telegram e do seu banco de dados MySQL. Depois disso, você pode iniciar o bot e testar a conexão com o MySQL usando o comando `/test_mysql`.
