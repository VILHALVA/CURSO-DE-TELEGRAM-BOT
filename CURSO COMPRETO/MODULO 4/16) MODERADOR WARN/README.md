# bot-moderador-para-telegram
Bot moderador de grupos para la aplicación de mensajería Telegram.

El proposito de este bot es facilitar la moderación de grupos de la aplicación Telegram, proveyendo herramientas que permitan aplacar la mala conducta de integrantes de dichos grupos. A diferencia de otros bots de este tipo que utilizan un sistema muy simple de 3 avisos antes de expulsar al usuario en cuestión, este bot busca emular simplificadamente la paciencia humana, utilizando un puntaje de "enojo" que se reduce solo con tiempo de ausencia de mala conducta, y un puntaje no reducible de "paciencia" que permite ajustar la severidad del castigo en base a lo problemático que resulte el usuario en cuestión. Más adelante tengo pensado diseñar otros sistemas que faciliten también la moderación. La app está desarrollada en lenguaje Python, asimismo se emplea el servidor HEROKU para desplegarla, y también la base de datos PostgreSQL para guardar la información de cada usuario y grupo.

Nota: Actualmente estoy intentando implementar lenguaje procedural en PostgreSQL para agilizar el respaldo y recuperación de los datos necesarios, por lo que el bot no se encuentra operativo.

[CODIGO FONTE BAIXADO DE ](https://github.com/facujc/bot-moderador-para-telegram)

