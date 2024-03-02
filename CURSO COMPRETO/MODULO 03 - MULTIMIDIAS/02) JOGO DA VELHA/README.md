# JOGO DA VELHA
## DESCRIÇÃO:
Este bot implementa o clássico jogo da velha (também conhecido como jogo do galo), onde dois jogadores alternam entre marcar espaços em uma grade 3x3. Aqui está uma breve descrição do que o bot faz:

1. **Controle do Jogo**:
   - O bot permite que os jogadores joguem o jogo da velha diretamente no Telegram.
   - Ele mantém o controle do estado do jogo para cada jogador, identificado pelo seu user_id no Telegram.
   - Cada partida é gerenciada individualmente.

2. **Interface do Usuário**:
   - O bot fornece uma interface de teclado embutida para os jogadores selecionarem suas opções.
   - Os jogadores podem escolher o nível de dificuldade do jogo (Fácil, Médio ou Difícil).
   - Eles também escolhem se querem jogar com "X" ou "O".

3. **Lógica do Jogo**:
   - O bot implementa a lógica do jogo da velha, garantindo que as regras sejam seguidas.
   - Ele calcula as jogadas do computador em níveis de dificuldade variáveis.
   - As jogadas do computador são determinadas usando um algoritmo que avalia as possibilidades futuras e escolhe a melhor jogada disponível.

4. **Feedback ao Usuário**:
   - O bot fornece feedback adequado ao usuário durante o jogo, informando sobre as jogadas feitas e o estado atual do jogo.
   - Ele atualiza dinamicamente a grade do jogo no Telegram para refletir as jogadas feitas.

5. **Controle de Tempo**:
   - O bot controla o tempo entre as jogadas, garantindo que o jogo não expire se um jogador demorar muito para fazer sua jogada.
   - Se um jogador não jogar dentro de um determinado período, a partida é encerrada e o bot limpa o estado do jogo.

## REQUIREMENTOS:
```bash
pip install -r requirements.txt
export BOT_TOKEN=TELEGRAM_TOKEN
python3.6 JOGO DA VELHA.py
```

O comando `pip install -r requirements.txt` é uma forma eficiente de instalar todas as dependências de um projeto Python a partir de um arquivo de requisitos chamado `requirements.txt`. Este arquivo é comumente usado para listar todas as bibliotecas e suas versões necessárias para executar um projeto Python específico.

Aqui está uma explicação passo a passo do que esse comando faz:

1. **Identificação do arquivo de requisitos**: O comando espera encontrar um arquivo chamado `requirements.txt` no diretório atual ou no caminho especificado.

2. **Leitura do arquivo de requisitos**: Ele lê o arquivo `requirements.txt` e analisa cada linha em busca de especificações de pacotes Python e suas versões.

3. **Resolução de dependências**: O comando utiliza as informações do arquivo `requirements.txt` para resolver dependências. Isso significa que ele verifica se todas as bibliotecas e suas versões especificadas são compatíveis entre si e podem ser instaladas juntas.

4. **Instalação das dependências**: Após resolver as dependências, o comando utiliza o pip (gerenciador de pacotes Python) para instalar cada uma das bibliotecas listadas no arquivo `requirements.txt`. Ele faz isso automaticamente e de forma recursiva, ou seja, ele também instala quaisquer dependências das bibliotecas listadas.

5. **Finalização da instalação**: Após a instalação de todas as dependências com sucesso, o comando exibe uma mensagem indicando que a instalação foi concluída.

Usar um arquivo `requirements.txt` e o comando `pip install -r requirements.txt` é uma prática recomendada em projetos Python porque simplifica o processo de gerenciamento de dependências e facilita a reprodução do ambiente de desenvolvimento em diferentes máquinas. Isso garante que todos os colaboradores do projeto estejam usando as mesmas versões das bibliotecas, evitando problemas de compatibilidade.

## EXPLICAÇÃO:
- **Classe `Velhus`**: Esta classe representa o jogo da velha e permite calcular jogadas possíveis, verificar se alguém ganhou e determinar o resultado do jogo.

- **Classe `Velha`**: Esta classe controla o estado de cada jogador, incluindo o estado atual do jogo, a última jogada feita, a mensagem a ser enviada ao usuário, o estado da tela (para determinar em qual tela o usuário está), o nível de dificuldade, os jogadores (humano e computador) e o ID do usuário do Telegram.

- **Classe `Partidas`**: Esta classe mantém uma lista de partidas ativas, indexadas pelo ID do usuário do Telegram. Ela também tem métodos para criar, remover e limpar partidas.

- **Classe `JogoDaVelha`**: Esta classe é a classe controladora do jogo. Ela recebe mensagens do usuário, processa-as e responde de acordo. Ela também gerencia o fluxo do jogo, como escolher o nível de dificuldade, selecionar quem joga primeiro e processar as jogadas do jogador e do computador.

- **Função `configuracao_log`**: Esta função configura o registro para exibir mensagens de depuração.

- **Função `main`**: Esta é a função principal do programa. Ela configura o registro, inicializa o bot do Telegram, cria uma instância da classe `JogoDaVelha` e inicia o loop de eventos asyncio para lidar com as mensagens do Telegram.


