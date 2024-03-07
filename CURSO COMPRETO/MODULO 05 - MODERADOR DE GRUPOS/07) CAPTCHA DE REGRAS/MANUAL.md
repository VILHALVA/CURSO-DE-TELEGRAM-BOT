<img align="right" alt="RegrasRobot Logo" width="30%" height="auto" src="https://github.com/GabrielRF/RegrasRobot/blob/main/utils/logo.jpg?raw=true">

# RegrasRobot
[![Deploy](https://github.com/GabrielRF/RegrasRobot/actions/workflows/deploy.yml/badge.svg)](https://github.com/GabrielRF/RegrasRobot/actions/workflows/deploy.yml)
## Sobre

Este é um bot para ser usado em grupos públicos ou privados do Telegram que possuem a opção de aprovar a entrada de novos membros ligada.

Em grupos públicos, a opção pode ser ligada e funcionará sempre.

Em grupos privados, a opção está disponível na criação dos links de convite.

Assim que a pessoa tentar entrar no grupo, o bot enviará uma mensagem e exigirá que a pessoa clique no botão correto, confirmando que leu e entendeu as regras.

## Executar

Crie o arquivo `utils/token.conf`, colocando em seu conteúdo o token do bot. 

Renomeie o arquivo `RegrasRobot.db_sample` para `RegrasRobot.db`.

Garanta que o `redis` esteja rodando e disponível para `localhost`.

Instale os requisitos:

```shell
pip install requirements -r
```

Execute o bot:

```shell
python bot.py
```
