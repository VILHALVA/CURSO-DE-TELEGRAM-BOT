# CONVERSADOR LIVRE:
## DESCRIÇÃO:
Este bot é um assistente virtual básico projetado para interagir com os usuários de forma eficiente. Ao ser iniciado, o bot carrega automaticamente dois arquivos essenciais: "WORD.json" e "CONFIG.json". O arquivo "WORD.json" contém uma lista de palavras-chave e suas respostas correspondentes, permitindo que o bot responda a uma variedade de perguntas comuns e forneça informações úteis aos usuários. 

Por sua vez, o arquivo "CONFIG.json" define o comportamento do bot. Nele, as configurações podem ser ajustadas conforme necessário para personalizar a interação. 

O bot é capaz de compreender palavras-chave em uma frase completa, o que significa que não é necessário que a mensagem do usuário consista apenas na palavra-chave, mas pode ser uma parte dela dentro de uma frase. 

1. **Respostas a Perguntas Básicas:**
   - O bot pode responder a uma variedade de perguntas básicas, como nome, como está, o que pode fazer, entre outras.
   - Ele também pode fornecer piadas, curiosidades e recomendações sobre uma variedade de tópicos.

2. **Gerenciamento de Respostas:**
   - Se uma mensagem do usuário não corresponder a nenhuma resposta pré-definida, o bot pode solicitar ao usuário que forneça uma resposta para ser adicionada ao banco de dados.
   - Essa funcionalidade é controlada pelas configurações no arquivo "CONFIG.json".

3. **Erro de Mensagem não Compreendida:**
   - Se o bot não entender a mensagem do usuário, ele enviará uma mensagem indicando que não compreendeu e oferecerá orientações para reenviar a mensagem seguindo um formato específico.

## `CONFIG.json`:
Aqui está uma descrição do que acontece quando cada chave no arquivo "CONFIG.json" está definida como "ON" ou "OFF":

| Chave   | Descrição                                 | Comportamento quando "ON"                            | Comportamento quando "OFF"                           |
|---------|-------------------------------------------|-------------------------------------------------------|-------------------------------------------------------|
| SEMPRE  | Sempre Responder                          | O bot responderá a todas as mensagens, independentemente se for mencionado via user (@). | O bot responderá apenas se for mencionado via user (@). |
| CRIAR   | Permitir Adicionar Respostas              | Os usuários poderão adicionar novas respostas ao banco de dados do bot. | Os usuários não poderão adicionar novas respostas.    |
| ERRO    | Ativar Mensagem de Erro                   | Se o bot não entender a mensagem do usuário, ele enviará uma mensagem indicando que não compreendeu e oferecerá orientações sobre como reenviar a mensagem seguindo um formato específico. | Se o bot não entender a mensagem do usuário, ele não enviará uma mensagem de erro e não oferecerá orientações para reenviar a mensagem. |

## PROPOSITO:
- No `Módulo 02`, nós criamos o bot `O5) CONVERSADOR`, no entanto, os registros eram armazenados apenas em variáveis temporárias na memória do programa. Isso significa que, se o bot fosse desligado ou reiniciado, todos os dados seriam perdidos. 

- Ao integrar um banco de dados, como MySQL, MongoDB ou utilizar arquivos JSON, seremos capazes de salvar, recuperar, editar e apagar registros de forma confiável e duradoura. Essa abordagem oferecerá uma solução escalável e robusta para o armazenamento de dados do bot, garantindo que as informações dos usuários sejam preservadas ao longo do tempo e em diferentes sessões de uso do bot.