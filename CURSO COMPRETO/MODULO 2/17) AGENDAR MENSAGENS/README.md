# AGENDAR MENSAGENS
## DESCRIÇÃO:
Com ele você pode programar mensagens para serem enviadas em momentos específicos, útil para lembretes, anúncios e outras finalidades.

## COMANDOS DISPONIVEIS:
- `/schedule <mensagem>`: Inicia o processo de agendamento. Substitua `<mensagem>` pela mensagem que você deseja agendar.

**Instruções de Agendamento:**

1. Use o comando `/schedule` para iniciar o agendamento.

2. O bot solicitará que você insira a data e hora para enviar a mensagem. Use o formato "dd/mm/yyyy hh:mm".

3. Confirme o agendamento com o comando `/confirm_schedule`.

## FUNCIONAMENTO:
O bot utiliza a biblioteca `python-telegram-bot` para interagir com a API do Telegram e a funcionalidade de agendamento do módulo `schedule` para programar as mensagens. Com este bot, você pode facilmente agendar mensagens para serem enviadas em momentos específicos, como lembretes, anúncios e outras finalidades.

## OBSERVAÇÕES:
- Certifique-se de adicionar o bot ao grupo onde você deseja agendar as mensagens.

- Certifique-se de que o arquivo `.env` esteja configurado corretamente com o token do seu bot.

- Certifique-se de que o seu bot tenha permissões suficientes para enviar mensagens no grupo.

