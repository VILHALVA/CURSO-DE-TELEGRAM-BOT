# BUSCADOR DO GOOGLE
## DESCRIÇÃO:
O bot desenvolvido é um assistente do Telegram que fornece funcionalidades de pesquisa no Google de forma simplificada. Aqui está uma descrição detalhada do que o bot faz e suas principais funcionalidades:

1. **Início e Instruções:**
   - Quando o usuário envia o comando `/start`, o bot saúda o usuário e fornece instruções sobre como usar a funcionalidade de pesquisa no Google.

2. **Pesquisa no Google:**
   - O principal recurso do bot é permitir que os usuários pesquisem no Google diretamente do Telegram. Eles podem fazer isso enviando o comando `/google` seguido do assunto desejado.

3. **Respostas Detalhadas:**
   - Após receber um comando de pesquisa, o bot realiza uma busca no Google para obter resultados relevantes.
   - Caso haja resultados, o bot fornece uma resposta detalhada para cada resultado encontrado, incluindo título, descrição e link.

4. **Manuseio de Erros:**
   - O bot é projetado para lidar com possíveis erros ou situações em que o usuário não fornece um assunto de pesquisa adequado após o comando `/google`.
   - Em caso de nenhum resultado encontrado, o bot informa ao usuário que nenhum resultado foi encontrado.

5. **Interface de Usuário Simples:**
   - O bot utiliza uma interface de usuário simplificada, com comandos claros, a fim de tornar a interação fácil e intuitiva para os usuários.

6. **Integração com Beautiful Soup e Requests:**
   - O bot utiliza as bibliotecas Beautiful Soup e Requests para realizar web scraping e obter resultados da pesquisa no Google.

**Instruções de Uso:**
- Para iniciar a interação, o usuário deve enviar o comando `/start`.
- Em seguida, o bot instrui o usuário a usar o comando `/google` seguido do assunto desejado para realizar uma pesquisa no Google.
- O bot fornece respostas detalhadas com os resultados da pesquisa.

**Nota:** Como o acesso direto aos resultados da pesquisa no Google é limitado, o bot pode não fornecer resultados tão extensos quanto uma pesquisa diretamente no navegador. Além disso, é importante observar que o scraping de resultados do Google pode estar sujeito a restrições e mudanças nas políticas do Google. Este bot foi criado para fins educacionais e de demonstração.
