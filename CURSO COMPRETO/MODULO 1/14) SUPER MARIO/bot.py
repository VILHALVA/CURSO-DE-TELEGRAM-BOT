#!/usr/bin/env python
# -*- coding: utf-8 -*-
from hack import *
import requests
import json
from Constantes import *
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
                hackMario = hack(processo)           
                if texto == 'pena':
                        bot.sendMessage(chat_id, 'Voce deixou mario com a peninha' , reply_to_message_id=msgid)
                        hackMario.fixarStatusPenaMario()

                if texto == 'moedas':
                        bot.sendMessage(chat_id, 'Voce deixou mario com 99 moedas' , reply_to_message_id=msgid)
                        hackMario.valorfixoMoedas()

                if texto == 'fogo':
                        bot.sendMessage(chat_id, 'Voce deixou mario com flor do fogo' , reply_to_message_id=msgid)
                        hackMario.flordoFogo()       
                if texto == 'pequeno':
                        bot.sendMessage(chat_id, 'Voce deixou o mario pequeno' , reply_to_message_id=msgid)
                        hackMario.pequeno()          
                if texto == 'grande':
                        bot.sendMessage(chat_id, 'Voce deixou o mario grande' , reply_to_message_id=msgid)
                        hackMario.grande()          
                                
                        


























bot.message_loop(handle)
print ('[+] ON')
while 1:
        pass
