# ANTIPORNOGRAFIA
## DESCRIÇÃO:
Esse é um bot que apaga mensagens contendo conteúdo pornográfico e bane os usuários que as enviaram em um grupo.

## INSTRUÇÕES:
Vamos criar um manipulador de mensagens para o bot que será executado sempre que uma mensagem for enviada para o grupo em que o bot está. Dentro desse manipulador, vamos verificar se a mensagem contém pornografia e, caso positivo, apagá-la e banir o usuário que a enviou.

Para verificar se uma mensagem contém pornografia, podemos usar a biblioteca pyporn. É necessário instalá-la usando o seguinte comando: 
````bash
pip install pyporn
````

## CÓDIGO:
No código, a função handle_message é registrada como manipulador de mensagens do bot. Essa função recebe a mensagem enviada pelo usuário e o contexto da mensagem. Dentro da função, verificamos se a mensagem contém pornografia usando a função pyporn.contains_porn. Se a mensagem contiver pornografia, a função remove a mensagem usando context.bot.delete_message e bane o usuário usando context.bot.kick_chat_member.

Por fim, registramos o manipulador de mensagens usando dispatcher.add_handler e iniciamos o bot usando updater.start_polling().

## OBSERVAÇÃO:
Com esse código, o bot irá remover mensagens contendo pornografia e banir usuários que as enviaram em um grupo. Note que essa implementação é baseada em uma biblioteca externa e pode não ser 100% eficaz na detecção de pornografia. Além disso, é importante lembrar que o uso de um bot anti-pornografia pode ser sensível a questões culturais e étnicas, por isso é importante considerar cuidadosamente o seu uso e implementação.

