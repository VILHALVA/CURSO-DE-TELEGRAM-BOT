# LikeBot para o Telegram
## Design do Sistema
1. Propósito do projeto:
Este projeto é um bot simples para o Telegram que permite que você curta mensagens em um chat em grupo. É útil para chats em grupo onde você deseja curtir mensagens, mas não deseja usar o botão "like" porque é muito grande e ocupa muito espaço.

1. Declaração do problema:

O Telegram possui um botão "like", no entanto, ele não fornece estatísticas sobre o número de curtidas que uma mensagem recebeu. Isso é um problema porque você não pode saber se uma mensagem é popular ou não.

1. Solução:

A solução é criar um bot que permita curtir mensagens em um chat em grupo. O bot irá armazenar o número de curtidas que uma mensagem recebeu e irá mostrar o número de curtidas que uma mensagem recebeu.

1. Requisitos do sistema:

Os requisitos do sistema são:

- O bot deve ser capaz de curtir mensagens em um chat em grupo.

- O bot deve ser capaz de mostrar o número de curtidas que uma mensagem recebeu.

- O bot deve ser capaz de mostrar o número de curtidas que uma mensagem recebeu em um intervalo de tempo específico.

- O bot deve ser capaz de mostrar o número de curtidas que uma mensagem recebeu em um intervalo de tempo específico para um usuário específico.

1. Arquitetura do sistema:

A arquitetura do sistema é:

- O bot é escrito em Python.
- O bot usa a biblioteca [python-telegram-bot](https://python-telegram-bot.org/).

- O bot usa um arquivo JSON para armazenar o número de curtidas que uma mensagem recebeu.

- O bot usa um arquivo JSON para armazenar o número de curtidas que uma mensagem recebeu em um intervalo de tempo específico.

## Design do Banco de Dados
1. Esquema do banco de dados:
|User_id|Message_id|Likes|Data|
|---|---|---|---|
|123456789|123456789|1|2020-01-01 00:00:00|

```json
{
    "likes": {
        "message_id_0": {
            "user_id": {
                "like": 1,
                "date": "2020-01-01 00:00:00"
            },
            "message_id_1": {
            "user_id": {
                "like": 1,
                "date": "2020-01-01 00:00:00"
            },
        }
    }
}
```

## Estrutura do bot
O bot terá os seguintes manipuladores:

- /start: Este manipulador será usado para iniciar o bot.
- /help: Este manipulador será usado para mostrar a mensagem de ajuda.
- like: Este manipulador será usado para curtir uma mensagem.

## Lista de tarefas
### Tarefa 1: Criar uma Classe para o banco de dados de curtidas
1. Criar uma classe para o banco de dados de curtidas.

Atributos:

- likes: Este atributo será usado para armazenar o número de curtidas que uma mensagem recebeu.
- dislikes: Este atributo será usado para armazenar o número de descurtidas que uma mensagem recebeu.
- data: Este atributo será usado para armazenar o arquivo JSON.

Métodos:

- __init__: Este método será usado para inicializar a classe e carregar o arquivo JSON, se ele não existir, ele será criado.
- add_like: Este método será usado para adicionar uma curtida a uma mensagem no banco de dados.
- add_dislike: Este método será usado para adicionar uma descurtida a uma mensagem no banco de dados.
- remove_like: Este método será usado para remover uma curtida de uma mensagem no banco de dados.
- remove_dislike: Este método será usado para remover uma descurtida de uma mensagem no banco de dados.
- get_likes: Este método será usado para obter o número de curtidas que uma mensagem recebeu.
- get_dislikes: Este método será usado para obter o número de descurtidas que uma mensagem recebeu.
- add_image: Este método será usado para adicionar uma imagem a uma mensagem no banco de dados.