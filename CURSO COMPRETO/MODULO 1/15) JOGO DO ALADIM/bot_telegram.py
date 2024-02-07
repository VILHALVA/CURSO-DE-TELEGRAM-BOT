#!/usr/bin/env python
# -*- coding: utf-8 -*-
from hack import *
import requests
import json
import telepot
import math
import time
import re
import os
#api do bot
api = ''
bot = telepot.Bot(api)
# função handle
def handle(msg):
        uid = msg['from']['id']
        firstname = msg['from']['first_name']
        chat_id = msg['chat']['id']
        chat_type = msg['chat']['type']
        try:
                user = '@' + msg['from']['username']
        except:
                print ('')
        msgid = msg['message_id']

        content_type, chat_type, chat_id = telepot.glance(msg)
        if msg.get('text'):
                texto = msg['text'].split()[0]
                


                #inicio dos comandos ------------------------------------>>>>     
                processo = "zsnesw.exe"
                hacked = hack(processo)  
                if texto == 'vida':
                        bot.sendMessage(chat_id, 'Voce deixou aladin com a vida full.' , reply_to_message_id=msgid)
                        hacked.vidaAladin()

                if texto == 'diamante':
                        bot.sendMessage(chat_id, 'Voce deixou aladin com altos diamante' , reply_to_message_id=msgid)
                        hacked.diamanteAladin()      
                if texto == 'maça':
                        bot.sendMessage(chat_id, 'Voce deixou aladin com mais maças' , reply_to_message_id=msgid)
                        hacked.macaAladin()        
              






















bot.message_loop(handle)
print ('[+] ON')
while 1:
        pass
