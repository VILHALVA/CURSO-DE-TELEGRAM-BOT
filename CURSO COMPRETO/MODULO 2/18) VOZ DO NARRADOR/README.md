# VOZ DO NARRADOR
## DESCRIÇÃO:
Esse é um bot que permite enviar um texto e receber um áudio com a voz do Ricardo ou Felipe.

## REQUERIMENTOS:
- Antes de começar, é necessário criar uma conta no Google Cloud e configurar as credenciais de acesso à API.

- Para utilizar a voz do Felipe, basta alterar o segundo parâmetro da função text_to_speech para 'pt-BR-Wavenet-F'.

## EXECUÇÃO:
Vamos utilizar a biblioteca python-telegram-bot para criar o bot e receber as mensagens dos usuários.

A função text_to_speech recebe um texto e o nome da voz que deve ser usada na conversão para fala. Neste exemplo, estamos utilizando as vozes "pt-BR-Wavenet-B" e "pt-BR-Wavenet-F", que correspondem às vozes do Ricardo e do Felipe, respectivamente. Você pode conferir outras vozes disponíveis na documentação da API do Google Cloud Text-to-Speech.

A função handle_message é registrada como um handler para mensagens de texto e é executada sempre que o bot recebe uma mensagem de texto de um usuário. Essa função converte o texto em fala usando a voz do Ricardo e envia o áudio como mensagem de voz para o usuário.




