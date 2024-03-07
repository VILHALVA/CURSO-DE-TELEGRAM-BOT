# LISTA DE COMPRAS
## DESCRIÇÃO:
- O bot permite interações básicas para adicionar, remover e visualizar itens em uma planilha do Google Sheets.
- Os comandos disponíveis são `/add`, `/remove` e `/view`, que são utilizados para adicionar, remover e visualizar itens na planilha, respectivamente.
- As operações de adicionar, remover e visualizar são realizadas por meio de uma integração com uma planilha do Google Sheets, utilizando a biblioteca `sheet.py`.
- Apenas usuários autorizados, cujos nomes de usuário estão listados na configuração `settings.ALLOWED_USERS`, têm permissão para utilizar os comandos do bot.
- O bot pode ser executado em dois modos: `poll` (consulta regular) ou `web` (utilizando webhook). O modo é especificado como um argumento ao iniciar o script.
- O bot requer a instalação da biblioteca `telegram` e `settings.py` configurado corretamente com o token do bot Telegram e as configurações do webhook (se necessário).
- Para utilizar o bot, o usuário deve adicionar o bot ao chat e iniciar uma conversa com ele. Em seguida, pode usar os comandos `/add`, `/remove` e `/view` para interagir com a planilha.

## CREDITOS E MAIS:
* [ESSE BOT FOI CRIADO PELO "cuducos"](https://github.com/cuducos/lista-de-compras)
* [ESSE BOT FOI EDITADO PELO VILHALVA](https://github.com/VILHALVA)
* [VEJA O MANUAL CLICANDO AQUI](./MANUAL.md)