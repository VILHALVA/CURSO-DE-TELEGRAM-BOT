# RSS DO YOUTUBE
## DESCRIÇÃO:
Esse é um bot que se conecta à sua conta do YouTube e envia novos vídeos para um canal do Telegram.
Este exemplo usa a biblioteca googleapiclient para se conectar à API do YouTube e buscar os vídeos mais recentes dos canais inscritos. Ele também usa a biblioteca python-telegram-bot para enviar mensagens para o canal do Telegram.

## REQUERIMENTOS:
Para usar este código, você precisará definir suas credenciais do YouTube e do Telegram, bem como o ID do chat do Telegram em que deseja enviar as mensagens. Em seguida, execute o script para iniciar o job que verifica os vídeos a cada 10 minutos e o bot do Telegram. Quando um novo vídeo é detectado, o bot enviará uma mensagem para o canal do Telegram especificado.

Segue abaixo um exemplo de como implementar isso:
* 1- Obter as credenciais da API do YouTube seguindo os passos descritos na [documentação](https://developers.google.com/youtube/registering_an_application).
* 2- Instalar os pacotes google-auth e google-api-nodejs-client usando o npm.

## OBSERVAÇÃO:
É importante notar que o código acima apenas busca pelos últimos vídeos dos canais do YouTube a cada hora. É possível ajustar a frequência da verificação alterando o intervalo de tempo passado para a função setInterval.