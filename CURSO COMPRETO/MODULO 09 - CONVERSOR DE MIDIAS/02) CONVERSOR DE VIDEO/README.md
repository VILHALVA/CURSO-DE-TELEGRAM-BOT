# CONVERSOR DE VIDEO: QUALQUER VIDEO PARA MP4
## DESCRIÇÃO:
Este bot responderá a qualquer mensagem de vídeo enviada com um arquivo MP4 convertido. Ele utiliza a biblioteca python-telegram-bot e o ffmpeg para a conversão.

## INSTRUÇÃO:
Veja o exemplo no [MAIN.PY](./CODIGO/MAIN.py). Além disso, você precisará ter o ffmpeg instalado em seu sistema para este bot funcionar.

## COMO INSTALAR O FFMPEG?
**No Windows:**

1. Baixe o FFmpeg do site oficial: [FFmpeg Download](https://ffmpeg.org/download.html).
2. Extraia o arquivo zip para uma pasta de sua escolha.
3. Adicione o diretório binário do FFmpeg ao seu PATH do sistema:
   - Clique com o botão direito do mouse em "Este PC" ou "Meu Computador" e selecione "Propriedades".
   - Clique em "Configurações avançadas do sistema" e, em seguida, em "Variáveis de ambiente".
   - Na seção "Variáveis do sistema", encontre a variável "Path" e clique em "Editar".
   - Adicione o caminho para a pasta bin do FFmpeg (por exemplo, `C:\caminho\para\ffmpeg\bin`) ao final da lista de valores separados por ponto e vírgula.
4. Verifique se o FFmpeg está instalado corretamente abrindo um prompt de comando e digitando `ffmpeg -version`. Se a instalação foi bem-sucedida, você deverá ver a versão do FFmpeg instalada.

**No Linux:**

1. Instale o FFmpeg usando o gerenciador de pacotes do seu sistema. Por exemplo, no Ubuntu, você pode executar o seguinte comando no terminal:
   ```bash
   sudo apt-get install ffmpeg
   ```
2. Verifique se o FFmpeg está instalado corretamente digitando `ffmpeg -version` no terminal. Se a instalação foi bem-sucedida, você deverá ver a versão do FFmpeg instalada.
