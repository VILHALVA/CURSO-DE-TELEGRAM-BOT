# GERENCIADOR DE DATABASE
## DESCRIÇÃO:
Este bot foi projetado para gerenciar um banco de dados SQLite por meio do aplicativo XAMPP. Aqui estão as principais funcionalidades e características deste bot:

**1. Adicionar Usuários:**
   - Apenas o proprietário do bot pode adicionar novos usuários ao banco de dados.
   - Use o comando `/adduser Nome Idade` para adicionar um novo usuário com seu nome e idade ao banco de dados.

**2. Listar Usuários:**
   - O proprietário do bot pode listar todos os usuários no banco de dados.
   - Use o comando `/listusers` para obter uma lista de todos os usuários registrados no banco de dados.

**3. Banco de Dados SQLite:**
   - O bot está conectado a um banco de dados SQLite por meio do XAMPP.
   - Os dados dos usuários são armazenados no banco de dados com os campos "nome" e "idade".

**4. Segurança:**
   - Apenas o proprietário do bot (com base no ID de usuário do Telegram) pode executar comandos que afetam o banco de dados.
   - O acesso ao banco de dados é protegido por um nome de usuário e senha configurados no XAMPP.

## ISNTRUÇÕES:
   - Certifique-se de definir o `OWNER_ID` com o seu ID de usuário Telegram para ser reconhecido como o proprietário do bot.
   - Configure as informações de login do XAMPP (nome de usuário e senha) e o nome do banco de dados no código.
   - Execute o bot Python e use os comandos `/adduser` e `/listusers` para gerenciar o banco de dados SQLite.

## ATENÇÃO:
Lembre-se de manter as informações de login e senha do XAMPP em segurança, pois elas concedem acesso ao seu banco de dados. Este é um exemplo básico que pode ser expandido de acordo com suas necessidades específicas de gerenciamento de banco de dados. Certifique-se de ajustar as configurações para corresponder ao seu ambiente.