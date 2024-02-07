# TG-Tube
Bot Telegram Server para descargar música y videos de YouTube y Vimeo (entre otras plataformas platzy, udemy, etc...) además de files de github, Mediafire, archivos en general y archivos googledrive, con registro de eventos de error y registro en base de datos de las entradas.
Ademas con unas pequeñas modificaciones se puede ajustar para almacenar los archivos descargador en el servidor, cambiar la interfaz de usuario, a botones para una mejor experiencia de uso, modificar las descargas para seleccionar el tipo de resolucion o formato de audio y video.

# Plataforma Windows
+ Testeado sobre Windows 10 Pro
+ Proximamente sobre Linux

# Dependencias de TG-Tube
+ pip install pysqlite
+ pip install moviepy
+ pip install pafy
+ pip install youtube_dl
+ pip install sqlite3
+ pip install python-telegram-bot
+ pip install colorama
+ pip install gdown

# Uso de TG-Tube
* 1º Crear un bot por ejemplo BotFather colocar en el API_KEY.HASH la API del bot.
* 2º Ejecutar el DownYotubeBotTelegram.py si la data base file no existe creara una al igual al file logg.
* 3º Los archivos descargados se borran de la carpeta donde se ejecuta el server del bot para no sobre cargarlo (se puede cambiar con un par de lineas).
* 4º Los registros de Errores se guardan en un logger.dat
* 5º Los registros de usuarios que usan el bot se guandan en la database log_telegram_download.sqlite
* 6º Los comandos de usos son: 

+ /start : iniciar el bot
+ /down : download videos de YouTube ex: /down https://youtu.be/Q-ezaxiKe-Y
+ /platf : download videos de Vimeo ex: /platf https://vimeo.com/404133941
+ /downmusic : download musica de YouTube ex: /downmusic https://youtu.be/Q-ezaxiKe-Y
+ /downdrive : download archivos de google drive ex: /downdrive por link o id
+ /downfire : download archivos de mediafire or otra url ex: /downfire o link terminando en .extencion
+ /downgithub : download los paketes de GitHub ex: /downgithub https://github.com/cloudfellows/stuxnet-worm
+ /help : info


# Licencia AGPL

[CÓDIGO FONTE BAIXADO DE JOCKER 404](https://github.com/Jocker404/TG-Tube)
