# coding: utf-8
'''
Created on 2 sep. 2019

@author: Facundo
'''

import os
import time
import random
import json

import asyncio
import logging
import psycopg2

from math import log, log2
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
#from aiogram.dispatcher import webhook
from aiogram.utils.executor import start_webhook

API_TOKEN = os.environ['API_TOKEN']
BOT_USERNAME = os.environ['BOT_USERNAME']
DATABASE_URL = os.environ['DATABASE_URL']

# webhook settings
WEBHOOK_HOST = os.environ['WEBHOOK_HOST']
WEBHOOK_PATH = '/' + API_TOKEN
WEBHOOK_URL = WEBHOOK_HOST+WEBHOOK_PATH

# webserver settings
WEBAPP_HOST = '0.0.0.0' # or ip
WEBAPP_PORT = int(os.environ.get('PORT', '8443'))

logging.basicConfig(level=logging.INFO)

loop = asyncio.get_event_loop()
bot = Bot(token=API_TOKEN, loop=loop)
dp = Dispatcher(bot)

#chat_id, user_id, command, level, new_chat_members, left_chat_member, 

"""
class LevelHandler:
    def __init__(self, user):
        self.user = user
        self.chatId = user.chatId
        self.userId = user.userId
    
    async def changeLevel(self, factor, untilDate=time.time()):
        self.switchLevel(self.user.currentLevel+factor, untilDate)
        if factor > 0:
            bot.send_message(self.chatId,"El usuario ha sido promovido.")
        else:
            bot.send_message(self.chatId,"El usuario ha sido degradado.")

    async def setLevel(self, level, untilDate=time.time()):
        self.switchLevel(level, untilDate)
        bot.send_message(self.chatId,"El nivel del usuario ha cambiado a %d" % level)
        
    async def switchLevel(self, level, untilDate):
        if -4 <= level < 7:
            self.user.currentLevel = self.user.currentLevel%1+level
            switcher = {-4: level_4, -3: level_3, -2: level_2, -1: level_1, 0: level0}
            #Get the function from switcher dictionary
            function = switcher.get(int(level), lambda: rest)
            # Execute the function
            function(untilDate)
        else:
            bot.send_message(self.chatId,"El nivel %d no es vÃ¡lido, abortado." % level)
    
    async def level_4(self, untilDate):
        # Expulsado y sin posibilidad de volver.
        await bot.kick_chat_member(self.chatId, self.userId, untilDate)
        
        await bot.send_message(self.chatId,"El usuario ha sido baneado.")
    
    async def level_3(self, untilDate):
        # Expulsado.
        await bot.kick_chat_member(self.chatId, self.userId)
        await bot.unban_chat_member(self.chatId, self.userId)
        
        await bot.send_message(self.chatId,"El usuario ha sido expulsado.")            
        
    async def level_2(self, untilDate):
        # Restringido completamente.
        await bot.restrict_chat_member(self.chatId, self.userId, untilDate, can_send_messages=0)
        
        await bot.send_message(self.chatId,"El usuario ha sido restringido (texto y multimedia).")

    async def level_1(self, untilDate):
        # Solo texto.
        await bot.restrict_chat_member(self.chatId, self.userId, untilDate, can_send_media_messages=0)
        
        await bot.send_message(self.chatId,"El usuario ha sido restringido (multimedia).")
        
    async def level0(self, untilDate):
        # Quitar restricciones.
        if (bot.get_chat_member(self.chatId, self.userId)).status == "restricted":
            await bot.restrict_chat_member(self.chatId, self.userId, can_send_other_messages=1, can_add_web_page_previews=1)

    async def rest(self, untilDate):
                pass

class CommandHandler:
    async def __init__(self, user):
        self.user = user
        self.chat = user.chat
        self.userId = user.userId
        self.chatId = user.chatId
    
    async def manage(self, message, ignore_mention=True):
        async def getTime(parameters, i):
            try:
                timeString = parameters[i]
            except:
                return 0
            try:
                return abs(int(timeStr[:-1])) * {"s": 1, "m": 60, "h": 60**2, "d": 60**2*24, "M": 60**2*24*30}.get(timeStr[-1:])
            except:
                return await notify("invalidFormatTime", message)

        async def searchUserId(username):
            def createUsernamesList():
                return {user.username: user.id for user in self.chat.active_users.values() if user.username}

            def update():
                updateUsernames()
                usernames = createUsernamesList()
                user_id = usernames.get(username, False)
                
                return user_id
            
            usernames = createUsernamesList()
            user_id = usernames.get(username, update())
            
            return user_id
            
            
                for user_id in chat.active_users.keys():
                    try:
                        username = await bot.get_chat_member(chat.chat_id, user_id).user.username
                    except:
                        continue
        
        def searchUsers():
            users_id = []
            end_of_parameters = None
            
            if message.reply_to_message:
                user_id = message.reply_to_message.from_user.id
                users_id.append(user_id)
            
            for entity in getattr(message, "entities", []):
                if entity.type == "mention":
                    username = message.text[entity.offset:entity.length]
                    user_id = self.searchUserId(username)
                    users_id.append(user_id)
                    
                    if not end_of_parameters:
                        end_of_parameters = entity.offset
                
                elif entity.type == "text_mention":
                    user_id = entity.user.id
                    users_id.append(user_id)
                    
                    if not end_of_parameters:
                        end_of_parameters = entity.offset
            
            users = [self.chat.active_users.get(user_id) for user_id in users_id if user_id]
            
            return users, end_of_parameters
        
        
        text = message.text        
        [command, text] = text.split(" ", 1)
        
        if ignore_mention or BOT_USERNAME in command:
            command.replace(BOT_USERNAME, "")
            users, end_of_parameters = searchUsers()
            
            if text:
                parameters = text[:end_of_parameters]
                
        
        else:
            return
                    
    def dispatch(self, command):
        method_name = 'cmd_' + str(command)
        method = getattr(self, method_name, self.default)
        method()
                
    async def cmd_pin(self, message):
        minLevel = 1
        currentLevel = self.user.currentLevel
        chat = self.chat
        
        if currentLevel < chat.Pin[0] and (time.time() < chat.Pin[1] or currentLevel < minLevel):
            return await notify("noLevel", message)
        
        if not message.reply_to_message:
            return await notify("noMessageReply", message)
        
        disableNotification = 0
        try:
            if message.text[message.entities[0].length:None].split(" ", 2)[1]  == "nonotify":
                disableNotification = 1
        except:
            pass
        
        await bot.pin_chat_message(self.chatId, message.reply_to_message.message_id, disable_notification)
        chat.Pin = [0, 0]
    
    async def cmd_forcepin(self, message):
        minLevel = 1
        currentTime = time.time()
        currentLevel = self.user.currentLevel
        chat = self.chat
        
        if currentLevel < chat.Pin[0] and (time.time() < chat.Pin[1] or currentLevel <                 minLevel):
            return await notify("noLevel", message)
        
        if not message.reply_to_message:
            return await notify("noMessageReply", message)
        
        parameters = message.text[message.entities[0].length:None].split(" ", 3)
        
        seconds = 0
        disableNotification = 0
        try:
            if parameters[1]  == "nonotify":
                disableNotification = 1
            else:
                seconds = self.getTime(parameters, 1)
                try:
                    if parameters[2]  == "nonotify":
                        disableNotification = 1
                except:
                    pass
        except:
            pass
        
        await bot.pin_chat_message(self.chatId, message.reply_to_message.message_id, disableNotification)
        chat.Pin = [self.user.currentLevel, currentTime + seconds]
    
    async def cmd_unpin(self, message):
        minLevel = 1
        chat = self.chat
        currentLevel = self.user.currentLevel
        
        if currentLevel < chat.Pin[0] and (time.time() < chat.Pin[1] or currentLevel <                 minLevel):
            return await notify("noLevel", message)
            
        await bot.unpin_chat_message(self.chatId)
        chat.Pin = [0, 0]
    
    async def cmd_warn(self, message):
        minLevel = 1
        
        async def updateRestWarns(self, user):
            lastWarn, restWarns, cycle, lastTime = user.karma
            currentTime = time.time()
            
            if lastTime > currentTime:
                hours =  0
            else:
                hours =  (currentTime - lastTime)/60**2
            
            limit = 7-int(self.user.currentLevel)
            restWarns += hours//cycle
            lastTime = currentTime - hours%cycle*60**2
            if restWarns > limit:
                restWarns = limit
                lastTime = currentTime
            user.karma = lastWarn, restWarns, cycle, lastTime

        try:
            user, limit = await self.getUser(message)
        except:
            return
        
        try:
            warns = message.text[message.entities[0].length:limit].split(" ", 2)[1]
            if warns in ["1", "2", "3"]: 
                warns = int(warns)
            else:
                return await notify("noValidValue", message)
        except:
            return await notify("noValidValue", message) 
    
        if minLevel > self.user.currentLevel <= user.currentLevel:
            return await notify("noLevel", message)
        
        await updateRestWarns(user)
        
        levelHandler = user.levelHandler
        lastWarn, restWarns, cycle, lastTime = user.karma
        
        restWarns -= warns
        cycle += warns
        lastWarn = warns
        if restWarns < 0: 
            if self.user.currentLevel > -1:
                await levelHandler.changeLvl(-1)
            else:
                lastTime = currentTime+cycle*60**2
                await levelHandler.changeLvl(-1, lastTime)
        
        user.karma = lastWarn, restWarns, cycle, lastTime
        return True
    
    async def cmd_wrm(self, message):
        if self.cmd_warn(message):
            await bot.delete_message(self.chatId, message.reply_to_message.message_id)
    
    async def cmd_unwarn(self, message):
        minLevel = 1
        
        try:
            user, limit = await self.getUser(message)
        except:
            return
        
        if minLevel > self.user.currentLevel <= user.currentLevel:
            return await notify("noLevel", message)
        
        lastWarn, restWarns, cycle, lastTime = user.karma
            
        restWarns += lastWarn
        if restWarns >= 0:
            user.levelHandler.changeLvl(+1)
            lastTime = time.time() - cycle*60**2
        cycle -= lastWarn
        lastWarn = 0
        
        user.karma = lastWarn, restWarns, cycle, lastTime

    async def cmd_nowarns(self, message):
        minLevel = 1
        
        try:
            user, limit = await self.getUser(message)
        except:
            return
        
        if minLevel > self.user.currentLevel <= user.currentLevel:
            return await notify("noLevel", message)

        user.karma[1] = 7-int(user.currentLevel)
    
    async def cmd_getwarns(self, message):
        user = self.user 
        
        if message.reply_to_message:
            user = self.chat.active_users.get(message.reply_to_message.from_user.id)
        else:
            try:
                entity = message.entities[1]
                if entity.type == "text_mention":
                    user = entity.user
                elif entity.type == "mention":
                    userId = self.findUserId(message.text[entity.offset:entity.length])
                    if userId:
                        user = self.chat.active_users.get(userId)
            except:
                pass
        
        #await notify("restWarns", message)
        await bot.send_message(self.chatId, "Warns restantes: %d" % user.karma[1])
    
    async def cmd_unban(self, message):
        await self.cmd_setlevel(message, 0)
    
    async def cmd_unmute(self, message):
        await self.cmd_setlevel(message, 0)
    
    async def cmd_mutemedia(self, message):
        await self.cmd_setlevel(message, -1, 2)
    
    async def cmd_mute(self, message):
        await self.cmd_setlevel(message, -2)
    
    async def cmd_kick(self, message):
        await self.cmd_setlevel(message, -3)
    
    async def cmd_ban(self, message):
        await self.cmd_setlevel(message, -4)
    
    async def cmd_promote(self, message):
        await self.cmd_setlevel(self, message, 1, 7)
    
    async def cmd_degrade(self, message):
        await self.cmd_setlevel(self, message, -1, 7)

    async def cmd_setlevel(self, message, level, minLevel=3):    
        try:
            user, limit = await getUser(message)
        except:
            return
        
        parameters = message.text[message.entities[0].length:limit].split(" ", 3)
        if level == 1:
            try:
                level = int(parameters[1])
                if -4 > level >6: 
                    return await notify("noValidLevel", message)
            except:
                return await notify("noValidLevel", message)
            seconds = 0
        else:
            seconds = self.getTime(parameters, 2)
        
        if minLevel > self.user.currentLevel <= user.currentLevel:
            return await notify("noLevel", message)
        
        user.levelHandler.setLevel(level, time.time() + seconds)
    
    async def cmd_changefaults(self, faults):
        await self.cmd_setfaults(faults, 1)
    
    async def cmd_setfaults(self, faults, change=0):
        minLevel = 7
        try:
            user, limit = await self.getUser(message)
        except:
            return
            
        try:
            faults = int(message.text[message.entities[0].length:limit].split(" ", 2)[1])
        except:
            return await notify("noValidValue", message)
        
        if minLevel > self.user.currentLevel <= user.currentLevel:
            return await notify("noLevel", message)
            
        if change:
            user.karma[2] += faults
        else:
            user.karma[2] = abs(faults)
    
    async def cmd_changescore(self,message):
        minLevel = 7
        try:
            user, limit = await self.getUser(message)
        except:
            return
            
        try:
            score = int(message.text[message.entities[0].length:limit].split(" ", 2)[1])
        except:
            return await notify("noValidValue", message)
        
        if minLevel > self.user.currentLevel <= user.currentLevel:
            return await notify("noLevel", message)
            
        user.levelHandler.setLevel(log2(2**user.currentLevel+score/7))
    
    async def cmd_antiflood(self):
        pass
    
    async def cmd_maxflood(self, time):
        self.user.maxTime = time
    
    async def cmd_delete(self, messsage_id):
        # Eliminar un mensaje.
        bot.delete_message(self.chatId, messsage_id)
    
    async def cmd_muteall(self):
        pass
    
    async def cmd_getinfo(self):
        #get user info
        pass
                
    async def cmd_rules(self):
        pass
    
    async def cmd_modlist(self):
        pass
    
    async def cmd_report(self):
        pass
        
    async def cmd_raidmode(self):
        self.chat.raidHandler = self.chat.RaidHandler()
        
    async def cmd_setwelcome(self):
        # Mensaje de bienvenida.
        pass
    
    async def cmd_setrules(self):
        pass

    async def cmd_settitle(self):
        bot.set_chat_title(self.chatId, title)
    
    async def cmd_setdescription(self):
        # Definir descripción del grupo.
        bot.set_chat_description(self.chatId, description)
    
    async def cmd_setphoto(self, photo):
        bot.set_chat_photo(self.chatId, photo)
    
    async def cmd_default(self, message):
        await bot.send_message(self.chatId, "El comando no existe.")
            
class FloodHandler:
    def __init__(self, user):
        self.user = user
        self.messages = user.messages
        self.antiFloodParameters = user.chat.antiFloodParameters
        
    def checkBotsFlood(self):
        last_message = self.user.chat.last_message
        new_message = [message.message_id, message.date]
        self.user.chat.last_message = new_message

        flood_limit = 10
        group_messages = self.user.chat.group_messages
        
        try:
            step = (new_message[1]-last_message[1])/(new_message[0]-last_message[0])
        except:
            return
        
        messages = []    
        _time = last_message[1] - step
        message_id = last_message[0] + 1
        
        while message_id<new_message[0]:
            if not message_id in group_messages:
                messages.append([message_id, int(_time)])
            
            _time += step
            message_id += 1
        
        self.user.chat.bot_messages.append(messages)
        
        if len(messages) > flood_limit:
            for bot_id in [user.user_id for user in selfuser.chat.active_users if user.is_bot]:
                bot.restrict_chat_member(self.chatId, bot_id, 0, can_send_messages = 0)
                
            self.user.chat.messages_to_delete.extend(self.user.chat.bot_messages)
            self.user.chat.bot_messages.clear()
    
    def manage(self, message):
        self.activity[0] += 1
        
        if self.user.levelHandler.currentLevel < 0:
            self.user.chat.messagesToDelete +=  [message.message_id]
            return
        
        messages = self.messages
        
        messages.append([message.message_id, int(str(message.date)[-2:])])
        if len(messages) > self.antiFloodParameters[-1][1]:
            messages.pop(0)
        
        if self.antiFlood == -1:
            for list in self.antiFloodParameters:
                if len(messages) < list[1]:
                    break
                
                tolerance, listLength = list
                messagesTime = [_time for _, _time in messages[-listLength:]]
                
                if messagesTime[-1] - messagesTime[0] >= tolerance*listLength:
                    list[0] = seconds/listLength
                    
        elif self.antiFlood == 0:
            return
            
        elif self.antiFlood == 1:
            self.checkFlood(self.messages, [1, 6])
            
        elif self.antiFlood == 2:
            for list in self.antiFloodParameters:
                if len(messagesId) < list[1]:
                    break
                
                self.checkFlood(self.messages, list)
    
    def checkFlood(self, messages, list):
        def min(list):
            min = 0
            i = 1
            
            while i < len(list):
                if list[i] < list[min]:
                    min = i
                i += 1
        
            return min
        
        def max(list):
            max = len(list)-1
            i = max-1
            
            while i >= 0:
                if list[i] > list[max]:
                    max = i
                i -= 1
            
            return max

        tolerance, listLength = list
        messagesTime = [time for _, time in messages[-listLength:]]
        
        if messagesTime[-1] - messagesTime[0] < tolerance*listLength:
            self.user.setLevel(-2)
            self.user.chat.messagesToDelete.extend([id for id, _ in messages][-listLength:])
            messages = messages[-listLength:]
            
        elif listLength <= 10:
            messages.insert(1-listLength, messages.pop(min(messagesTime)-listLength))
            messages.append(messages.pop(max(messagesTime)-listLength))

class RaidHandler:
    #commands = {"/deleteall": deleteAll, "/deletemessages": deleteMessages, "/exit": exit}

    async def __init__(self, chat):
        self.chat = chat
        self.chatId = chat.chatId
        self.usersToBan = []
        self.usersRestricted = []
        self.messages_to_delete = chat.messagesToDelete

        notifyAdmins("Raid in process.", "inPrivate")
        
        for user_id in [user.user_id for user in self.chat.active_users if user.is_bot]:
            await bot.restrict_chat_member(self.chatId, user_id, 0, can_send_messages = 0)
            
            self.usersRestricted.append(user_id)
        
    async def manageMessages(self, message):
        user = self.chat.active_users.get(message.from_user.id)
        
        if user.currentLevel < 7:
            self.messages_to_delete.append(message.message_id)
            await bot.restrict_chat_member(self.chat.chatId, user.userId, 0, can_send_messages = 0)
            
            await bot.send_message(self.chatId,"El usuario ha sido restringido momentaneamente.")            
            
            if not user.userId in self.usersRestricted:
                self.usersRestricted.append(user.userId)
        else:
            await self.manageCommand(message)
    
    async def manageCommand(self, message):
        botUsername = "@domador_bot"
        if not message.entities:
            return
        
        entity = message.entities[0]
        if not entity.type == "bot_command":
            return
            
        command = message.text[0:entity.length]
        if "@" in command:
            if  not botUsername in command:
                return
            command = command.replace(botUsername,"")

        await self.commands.get(command, rest)(message)
    
    async def findUserId(self, username, updated=0):
        chat = self.chat
        if not updated:                
            usernames = {user.username: user.id for user in chat.active_users.values()}
        else:
            usernames = {bot.get_chat_member(chat.chatId, userId).user.username: userId for userId in chat.active_users.keys()}
        return await usernames.get(username, False)
    
    async def getUser(self, message):    
        if message.reply_to_message:
            user = self.chat.active_users.get(message.reply_to_message.from_user.id)
            limit = None
        else:
            try:
                entity = message.entities[1]
            except:
                return await notify("noReplyOrFirstName", message)
            
            if not entity.type in ["mention", "text_mention"]:
                return await notify("noReplyOrFirstName", message)
            elif entity.type == "text_mention":
                user = entity.user
            else:
                userId = self.findUserId(message.text[entity.offset:entity.length])
                if not userId:
                    return await notify("unableToFindUser", message) 
                user = self.chat.active_users.get(userId)
                
            limit = message.entities[1].offset
        return user, limit
    
    async def deleteAll(self, message):
        start = message.message_id 
        
        if message.reply_to_message:
            limit = (message.reply_to_message.message_id)
        else:                
            try:
                limit = start - abs(int(message.text[message.entities[0].length:].split(" ", 2)[1]))
            except:
                return await notify("noReplyOrMessageNumber", message)
        
        self.messages_to_delete.extend([x for x in range(start-1, limit-1, -1)])
        
    async def deleteMessages(self, message):
        try:
            user, limit = await getUser(message)
        except:
            return
        
        try:
            riskLevel = abs(int(message.text[message.entities[0].length:limit].split(" ", 2)[1]))
        except:
            riskLevel = 3
        
        user.riskLevel = riskLevel
        self.usersToBan.append(user.user_id)
        
        if user.is_bot:                    
            self.messages_to_delete.extend([message_id for message_id, _ in self.bot_messages])
            self.bot_messages.clear()
        else:
            self.messages_to_delete.extend([message_id for message_id, _ in user.messages])
            self.user.messages.clear()

    async def exit(self, message):
        for user_id in self.usersToBan:
            await bot.kick_chat_member(self.chatId, user_id)
            
            if user_id in self.usersRestricted:
                await self.usersRestricted.remove(user_id)
        
        for user_id in self.usersRestricted:
                await bot.restrict_chat_member(self.chatId, user_id, can_send_other_messages=1, can_add_web_page_previews=1)
        
        await bot.send_message(self.chatId,"Todas las restricciones han sido eliminadas.")
        
        self.chat.raidHandler = None
    
    async def rest(self, message):
        await bot.send_message(self.chatId, "El comando no existe.")
    
class NotifyHandler:
    def __init__(self):
        pass
    
    def notify(self, key, *parameters):
        bot.send_message(self.chatId,"El usuario ha sido restringido momentaneamente.")
        
class Chat:
    def __init__(
            self, 
            chat_id, 
            Pin=[1, 0], 
            active_users={},
            inactive_users={}, 
            bot_messages=[],
            antiFloodParameters=[],
            lastCount=0, 
            lastTime=time.time(),
            commands_prefix="/"
            ):
        
        self.chat_id = chat_id
        self.Pin = Pin
        self.lastCount = lastCount
        self.lastTime = lastTime
        self.bot_messages = bot_messages
        self.commands_prefix = commands_prefix
        self.new_users_rate = [0, 0]

        self.messagesToDelete = []
        self.raidHandler = None
        
        self.active_users = {}
        
        if active_users:
            for user_id, user_dict in active_users.items():
                self.active_users[user_id] = User(self, **user_dict)
                
        self.inactive_users = {}
        if inactive_users:
            for user_id, user_dict in inactive_users.items():
                self.inactive_users[user_id] = User(self, **user_dict)
        
        if antiFloodParameters:
            self.antiFloodParameters = antiFloodParameters
        else:
            definition = 2
            secondsLimit = 24*60**2
            minMessages = 6
            baseTolerance = 1
            self.antiFloodParameters = [[baseTolerance, minMessages-1+definition**x] for x in range(int(log(secondsLimit, definition))+1)] + [[baseTolerance, secondsLimit]] # lista de pares de valores: [tiempo minimo entre mensajes en segundos (tolerancia), longitud de la lista a analizar]
            
    def dict(self):
        dictionary = {
            "chat_id": self.chat_id, 
            "Pin": self.Pin, 
            "lastCount": self.lastCount, 
            "lastTime": self.lastTime, 
            "antiFloodParameters": self.antiFloodParameters,
            "commands_prefix": self.commands_prefix
            }
        
        active_users = {}
        for user_id, user in self.active_users.items():
            active_users[str(user_id)] = user.dict()
        
        inactive_users = {}
        for user_id, user in self.inactive_users.items():
            inactive_users[str(user_id)] = user.dict()
        
        dictionary.update({'active_users':active_users, 'inactive_users': inactive_users})
        return dictionary
    
    async def checkMsgsToDelete(self):
        self.activity #veirficar
    
    
        if  msgsToDelete and time.time() - lastTime > 5:
            count = len(msgsToDelete) 
            if not count > lastCount:
                for msgId in msgsToDelete:
                    DeleteMessage(chatId, msgId)
                lastCount = 0
                msgsToDelete = []
            else:
                lastCount = count
                lastTime = time.time()
    
    def newUsersHandler(self, message: types.Message):
        for user_obj in message.new_chat_members:
            self.new_users_rate += 1
            
            if user_obj.is_bot:
                self.active_users['bot_users'].bot_ids.append(user_obj.id)
                if self.restrict_all_new_bots:
                    bot.restrict_chat_member(self.chatId, user_obj.id, can_send_messages=0)
            
            elif user_obj.id in self.inactive_users:
                self.inactive_users[str(user_obj.id)] = self.inactive_users.pop(str(user_obj.id))

            else:
                user = self.active_users.setdefault(str(user_obj.id), User(self, user_obj.id))            
            
            if 10 >= self.new_users_rate > 5:
                user.setLevel(-1)
                bot.send_message(message.chat.id,"El usuario ha sido restringido (multimedia) por seguridad.")
            
            if self.new_users_rate > 10:
                user.setLevel(-2)
                bot.send_message(message.chat.id,"El usuario ha sido restringido completamente por seguridad.")

    def userLeftHandler(self, message: types.Message):
        user = self.active_users.pop(str(message.left_chat_member.id))
        self.inactive_users[str(message.left_chat_member.id)] = user
        user.messages.clear()

    async def activityHandler(self, message):
        grace_period = 3
        min_messages = 12
        check_frecuence = 24
        
        activity, last_check = user.activity
        
        if time.time() > last_check+check_frecuence*60**2:
            for user in activeusers:
                if activity < 0:
                    activity = activity - (time.time()-last_check)/60**2*(min_messages_rate/check_frecuence)
                    user.activity[0] = activity, time.time()
                
                    if user.activity[0] < -grace_period*(24/check_frecuence*min_messages_rate):
                        user.setLevel(-3)
                else:
                    activity = activity - (time.time()-last_check)/60**2*(min_messages_rate/check_frecuence)
                    user.activity[0] = activity, time.time()
                    
                    if user.activity[0] < 0:
                        await bot.send_message(self.chatId,"El usuario va a ser kickeado en 3 dias por inactividad.")
    
    async def userRateHandler(self, message):
        min_users = 5
        max_users = 1
        min_check_frecuence = 1
        
        rate, last_check = self.new_users_rate
        
        if time.time() > last_check+check_frecuence*60**2:
        
    def messageHandler(self, message):
        user_id = message.from_user.id
        user = self.active_users.setdefault(str(user_id), self.User(chat, user_id, message.from_user.is_bot))
        user.messageHandler(message)
        
        if self.raidHandler:
            self.raidHandler.manageMessages(message)
        else:
            self.checkMsgsToDelete()
            self.newUsersHandler()
            self.userLeftHandler()
"""



class CommandHandler:
    async def __init__(self, user):
        self.user = user
        self.chat = user.chat
        self.userId = user.userId
        self.chatId = user.chatId
        self.message = None
        
        self.warn_reasons = {5: "spam", 
                                        10: "flood", 
                                        25: "cp"
                                        }
    
    async def manage(self, message, ignore_mention=True):
        async def searchUserId(username):
            def createUsernamesList():
                return {user.username: user.id for user in active_users.values() if user.username}
            
            def updateUsernames():
                for user_id in active_users.keys():
                    try:
                        username = bot.get_chat_member(self.chat_id, user_id).user.username
                        
                        user = active_users[str(user_id)]
                        user.username = username

                    except:
                        #pasar usuario inexistente en el grupo a la lista de usuarios inactivos del grupo
                        continue

            def update():
                updateUsernames()
                usernames = createUsernamesList()
                user_id = usernames.get(username, False)
                
                return user_id
            
            self.message = message
            usernames = createUsernamesList()
            user_id = usernames.get(username, update())
            
            return user_id
                
        def searchUsers():
            users_id = []
            end_of_parameters = None
            
            if message.reply_to_message:
                user_id = message.reply_to_message.from_user.id
                users_id.append(user_id)
            
            for entity in getattr(message, "entities", []):
                if entity.type == "mention":
                    username = message.text[entity.offset:entity.length]
                    user_id = self.searchUserId(username)
                    users_id.append(user_id)
                    
                    if not end_of_parameters:
                        end_of_parameters = entity.offset
                
                elif entity.type == "text_mention":
                    user_id = entity.user.id
                    users_id.append(user_id)
                    
                    if not end_of_parameters:
                        end_of_parameters = entity.offset
            
            users = [active_users.get(user_id) for user_id in users_id if user_id]
            
            return users, end_of_parameters
        
        text = message.text
        
        if text:     
            [command, text] = text.split(" ", 1)
            
            if ignore_mention or BOT_USERNAME in command:
                command.replace(BOT_USERNAME, "")
                users, end_of_parameters = searchUsers()
                parameters = text[:end_of_parameters]
                
                self.dispatch(command, users, parameters)
        
        else:
            return
                    
    def dispatch(self, command, users, parameters):
        method_name = 'cmd_' + str(command)
        method = getattr(self, method_name, self.default)
        method(users, parameters)
    
    async def cmd_warn(self, users, parameters):
        """
            fault_score = puntaje de falta, se reduce con el tiempo (esto depende de calming_factor)
            patience_exponent = exponente que determina el aumento exponencial de mute_time. Es acumulativo.
             
            non_penalizable_limit = máximo fault_score sin que se aplique mute
            patience_factor = determina el porcentaje de los puntos de fault que se almacena permanentemente como patience_exponent
            severity_factor = determina a cuántos segundos de muteo equivale 1 punto de fault_score
            calming_factor = velocidad a la que desaparece 1 punto de fault_score, en segundos
        """
        
        def updateFaultScore():            
            time_lapsed = time.time() - last_update
            score_lapsed = (0 if time_lapsed <0 else time_lapsed) / calming_factor
            fault_score = fault_score - score_lapsed
            fault_score = 0 if fault_score < 0 else fault_score
            
            last_update = time.time()
                                
        try:
            fault = parameters.split(" ", 1)[0]
            fault = int(fault)
        except:
            return await self.notifyHandler(None, "noValidFormat")
        
        non_penalizable_limit, severity_factor, patience_factor, calming_factor = self.user.karma_parameters
        
        for user in users:
            last_fault, fault_score, patience_exponent, last_update = user.karma
            
            updateFaultScore()
            
            fault_score += fault
            patience_exponent = patience_exponent + fault * patience_factor
            warn_reason = self.warn_reasons[fault]
            
            if fault_score > non_penalizable_limit:
                    mute_time = fault_score**patience_exponent * severity_factor
                    last_update = time.time() + mute_time
                    user.levelHandler.changeLvl(-1, mute_time)
                    self.notifyHandler(user, "mute", warn_reason)
            elif user.level > 0:
                    user.levelHandler.changeLvl(-1)
                    self.notifyHandler(user, "degrade", "Límite de Warns sobrepasado")
            else:
                    self.notifyHandler(user, "warn", warn_reason)
            
            last_fault = fault
            
            user.karma = [last_fault, fault_score, patience_exponent, last_update]
    
    async def cmd_wrm(self, users, parameters):
            await bot.delete_message(self.chat_id, self.message.reply_to_message.message_id)
            await self.cmd_warn(users, parameters)
    
    async def cmd_unwarn(self, users, parameters):
        def updateFaultScore():            
            time_lapsed = time.time() - last_update
            score_lapsed = (0 if time_lapsed <0 else time_lapsed) / calming_factor
            fault_score = fault_score - score_lapsed
            fault_score = 0 if fault_score < 0 else fault_score
            
            last_update = time.time()

        try:
            fault = parameters.split(" ", 1)[0]
            fault = int(fault)
        except:
            fault = None
        
        non_penalizable_limit, severity_factor, patience_factor, calming_factor = self.user.karma_parameters
        
        for user in users:
            last_fault, fault_score, patience_exponent, last_update = user.karma
            
            updateFaultScore()
            
            if not fault:
                fault = last_fault
            
            fault_score -= fault
            patience_exponent = patience_exponent - fault * patience_factor
            
            if fault_score > non_penalizable_limit:
                user.levelHandler.changeLvl(+1)
                self.notifyHandler(user, "unmute")
            elif 0 <=  user.level <= self.level:
                user.levelHandler.changeLvl(+1)
                self.notifyHandler(user, "promote")
            else:
                self.notifyHandler(user, "unwarn")
            
            user.karma = [0, fault_score, patience_exponent, last_update]
    
    async def cmd_clfaults(self, users, _):
        for user in users:
            user.karma[1] = 0
            self.notifyHandler(user, "faultsCleared")
    
    async def cmd_getfaults(self, users, _):
        for user in users:
            faults = user.karma[1]
            self.notifyHandler(user, "showFaults", faults)

class NotifyHandler:
    def __init__(self):
        pass
    
    def func(self):
        pass
    
class LevelHandler:
    def __init__(self):
        pass
    
    def func(self):
        pass


"""

class User:
    def __init__(
            self, 
            chat,
            chat_id,
            user_id, 
            level=0,
            karma=[1, 0, 1, 0] #[last_fault, fault_score, patience_exponent, last_update]
            ):
        
        self.level = 0
        
        self.chat = chat
        self.user_id = user_id
        self.chat_id = chat. chat_id
        self.karma = karma
        self.karma_parameters = chat.karma_parameters        
        self.username = getattr(bot.get_chat_member(chat_id, user_id).user, 'username', None)
        
        #tools
        self.levelHandler = LevelHandler(self)
        self.notifyHandler = NotifyHandler(self)
        self.commandHandler = CommandHandler(self)
    
    def dict(self):
        dictionary = {
            "user_id": self.user_id, 
            "karma": self.karma
            }

        return dictionary
    
    def messageHandler(self, message):
        self.commandHandler.manage(message)


class Chat:
    def __init__(
            self, 
            chat_id, 
            active_users={},
            inactive_users={}, 
            commands_prefix="/",
            karma_parameters=[1, 0, 1, 0]
            ):
        
        self.chat_id = chat_id
        self.commands_prefix = commands_prefix

        self.active_users = {}
        if active_users:
            for user_id, user_dict in active_users.items():
                self.active_users[user_id] = User(self, **user_dict)
                
        self.inactive_users = {}
        if inactive_users:
            for user_id, user_dict in inactive_users.items():
                self.inactive_users[user_id] = User(self, **user_dict)
                
    def dict(self):
        dictionary = {
            "chat_id": self.chat_id, 
            "Pin": self.Pin, 
            "lastCount": self.lastCount, 
            "lastTime": self.lastTime, 
            "antiFloodParameters": self.antiFloodParameters,
            "commands_prefix": self.commands_prefix
            }
        
        active_users = {}
        for user_id, user in self.active_users.items():
            active_users[str(user_id)] = user.dict()
        
        inactive_users = {}
        for user_id, user in self.inactive_users.items():
            inactive_users[str(user_id)] = user.dict()
        
        dictionary.update({'active_users':active_users, 'inactive_users': inactive_users})
        return dictionary
        
    def newUsersHandler(self, message: types.Message):
        for user_obj in message.new_chat_members:
            self.new_users_rate += 1
            
            if user_obj.is_bot:
                self.active_users['bot_users'].bot_ids.append(user_obj.id)
                if self.restrict_all_new_bots:
                    bot.restrict_chat_member(self.chatId, user_obj.id, can_send_messages=0)
            
            elif user_obj.id in self.inactive_users:
                self.inactive_users[str(user_obj.id)] = self.inactive_users.pop(str(user_obj.id))

            else:
                user = self.active_users.setdefault(str(user_obj.id), User(self, user_obj.id))            
            
            if 10 >= self.new_users_rate > 5:
                user.setLevel(-1)
                bot.send_message(message.chat.id,"El usuario ha sido restringido (multimedia) por seguridad.")
            
            if self.new_users_rate > 10:
                user.setLevel(-2)
                bot.send_message(message.chat.id,"El usuario ha sido restringido completamente por seguridad.")

    def userLeftHandler(self, message: types.Message):
        user = self.active_users.pop(str(message.left_chat_member.id))
        self.inactive_users[str(message.left_chat_member.id)] = user
        user.messages.clear()
        
    def messageHandler(self, message):
        user_id = message.from_user.id
        user = self.active_users.setdefault(str(user_id), self.User(self.chat, user_id, message.from_user.is_bot))
        user.messageHandler(message)
        
        if self.raidHandler:
            self.raidHandler.manageMessages(message)
        else:
            self.checkMsgsToDelete()
            self.newUsersHandler()
            self.userLeftHandler()

"""





class User:
    def __init__(
            self, 
            chat,
            chat_id,
            user_id, 
            level=0,
            karma=[1, 0, 1, 0] #[last_fault, fault_score, patience_exponent, last_update]
            ):
        
        self.level = 0
        
        self.chat = chat
        self.user_id = user_id
        self.chat_id = chat_id
        self.level = level
        self.karma = karma
        self.karma_parameters = chat.karma_parameters  
        
        self.username = "".join([random.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(10)])

    def dict(self):
        dictionary = {
            "user_id": self.user_id, 
            "level": self.level,
            "karma": str(self.karma)
            }
        
        return dictionary
    
class Chat:
    def __init__(
            self, 
            chat_id, 
            users={},
            commands_prefix="/",
            karma_parameters=[1, 0, 1, 0],
            is_active=True
            ):
        
        self.chat_id = chat_id
        
        self.commands_prefix = commands_prefix
        self.karma_parameters = karma_parameters
        self.is_active = is_active
        
        self.users = {}
        if users:
            for user_id, user_dict in users.items():
                self.users[user_id] = User(self, **user_dict)
                                
    def dict(self):
        chat_data = {
            "chat_id": self.chat_id, 
            "commands_prefix": self.commands_prefix,
            "karma_parameters": str(self.karma_parameters),
            "is_active": self.is_active
            }
        
        chat_users = []
        for _, user in self.users.items():
            user_dict = user.dict()
            user_dict["is_active"] = True
            chat_users.append(user_dict)
        
        return chat_data, chat_users


#chats_list = [{chat_id, commands_prefix, karma_parameters}, {chat_id, commands_prefix, karma_parameters})
#chats_tables_list = [{chat_id, user_json}, {chat_id, user_json}]

class DataBaseSession:
    def __init__(self):
        self.create_types_function =  """               
            CREATE TYPE chats_list_type AS (
                chat_id INT,
                commands_prefix VARCHAR,
                karma_parameters TEXT,
                is_active BOOL
            );
            
            CREATE TYPE chats_tables_list_type AS (
                chat_id INT,
                chat_users JSON
            );
            
            CREATE TYPE chats_table_list_type AS (
                user_id INT,
                level INT,
                karma TEXT
            );
        """
                
        self.update_tables_function = """
            CREATE OR REPLACE FUNCTION update_tables(chats_list JSON, chats_tables_list JSON) RETURNS bool AS $$
                DECLARE
                    rec chats_tables_list_type;
                    table_A RECORD;
                BEGIN                                        
                    table_A := (SELECT to_regclass('public.groups'));
                    
                    IF table_A IS NULL THEN
                        CREATE TABLE groups
                        AS (SELECT * FROM json_populate_recordset(null::chats_list_type, chats_list));
                    ELSE
                        INSERT INTO table_A(chat_id, commands_prefix, karma_parameters, is_active)
                            SELECT chat_id, commands_prefix, karma_parameters, is_active
                            FROM json_populate_recordset(null::chats_list_type, chats_list) AS table_B
                        ON CONFLICT (chat_id) 
                        DO
                            UPDATE
                            SET
                                commands_prefix = table_B.commands_prefix,
                                karma_parameters = table_B.karma_parameters,
                                is_active = table_B.is_active;
                    END IF;
                    
                    FOR rec IN (SELECT * FROM json_populate_recordset(null::chats_tables_list_type, chats_tables_list))
                    LOOP
                        table_A := (SELECT to_regclass('public.' || TO_CHAR(rec.chat_id, '000000')));
                        IF table_A IS NULL THEN
                            EXECUTE format('CREATE TABLE %L AS (SELECT * FROM json_populate_recordset(null::chats_table_list_type, rec.chat_users));', rec.chat_id::INTEGER);
                        ELSE
                            INSERT INTO table_A (user_id, level, karma)
                                SELECT user_id, level, karma 
                                FROM json_populate_recordset(null::chats_table_list_type, rec.chat_users) AS table_B
                            ON CONFLICT (user_id) 
                            DO
                                UPDATE
                                SET
                                    level = table_B.level,
                                    karma = table_B.karma;
                        END IF;
                    END LOOP;
                    RETURN TRUE;
                END; $$
            LANGUAGE plpgsql;
        """
        
        self.get_tables_function = """
            CREATE OR REPLACE FUNCTION get_tables(OUT chats_list JSON, OUT chats_tables_list JSON) AS $$
                DECLARE
                    rec RECORD;
                BEGIN
                    CREATE TEMP TABLE temp_chats_list(chat_id INT, chat_json JSON);
                    FOR rec IN (SELECT * FROM groups WHERE is_active IS TRUE)
                    LOOP
                        EXECUTE format('INSERT INTO temp_chats_list(chat_id, chat_json) VALUES(rec.chat_id, SELECT json_agg(%I));', TO_CHAR(rec));
                    END LOOP;
                    
                    chats_list := (SELECT json_agg(groups));
                    chats_tables_list := (SELECT json_agg(temp_chats_list));
                END; $$
            LANGUAGE plpgsql;
        """
    
    def updateFunctions(self):
        self.execute(self.create_types_function)
        self.execute(self.update_tables_function)
        self.execute(self.get_tables_function)
    
    def execute(self, sql):
        connection = None
        try:
            print('Connecting to the PostgreSQL database...')
            connection = psycopg2.connect(DATABASE_URL, sslmode='require')
            cursor = connection.cursor()
            
            cursor.execute(sql)
            result = cursor.fetchall()
            print("Result: {}".format(result))
           
            cursor.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if connection is not None:
                connection.commit()
                connection.close()
                print('Database connection closed.')
    
    def callFunction(self, proc, parameters):
        connection = None
        result = False
        try:
            print('Connecting to the PostgreSQL database...')
            connection = psycopg2.connect(DATABASE_URL, sslmode='require')
            cursor = connection.cursor()
            
            result = cursor.callproc(proc, parameters)
            print("Result: {}".format(result))
           
            cursor.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if connection is not None:
                connection.commit()
                connection.close()
                print('Database connection closed.')
                
            return result

    
    
    
    def updateTables(self, chats_list, chats_tables_list):
        result = self.callFunction("update_tables", [chats_list, chats_tables_list])
        return result        
        
    def getTables(self):
        result = self.execute("get_tables")
        return result





async def on_startup(dp):
    await bot.set_webhook(WEBHOOK_URL)


@dp.message_handler()
async def messageHandler(message: types.Message):
    chat_id = message.chat.id
    print("Chat ID: {}, From: {}".format(chat_id, message.from_user.first_name))
    
    if chat_id == 927039296:
        users_num = 20
        chats_num = 10
            
        chats = {}
        
        for _ in range(chats_num):
            users = {}
            chat_id = random.randrange(100000, 999999)
            commands_prefix = random.choice(["/", "!", ".", "-"])
            karma_parameters = [random.randrange(1, 99), random.random(), random.randrange(1, 99), random.randrange(1, 99)]
            chat = Chat(chat_id, users, commands_prefix, karma_parameters)
            
            for _ in range(users_num):
                user_id = random.randrange(10000, 99999)
                level = random.randrange(-2, 7)
                karma = [random.randrange(1, 99), random.random(), random.randrange(1, 99), random.randrange(1, 99)]
                user = User(chat, chat_id, user_id, level, karma)
                
                users[user_id] = user
        
            chat.users = users
            chats[chat_id] = chat
        
        chats_list = []
        chats_tables_list = []
        
        for chat_id, chat in chats.items():
            chat_data, chat_users = chat.dict()
            chats_list.append(chat_data)
            print(chat_id)
            chats_tables_list.append({"chat_id": chat_id, "chat_users": chat_users})
        
        session = DataBaseSession()
        
        session.updateFunctions()
        session.updateTables(json.dumps(chats_list), json.dumps(chats_tables_list))
        
        
    """
        chats_tables_list
        {123984: [{user_id: 123515, level: 1, karma = [1, 0, 1, 1]},
                            {user_id: 123515, level: 1, karma = [1, 0, 1, 1]},
                            {user_id: 123515, level: 1, karma = [1, 0, 1, 1]},
                            ],
        123984: [{user_id: 123515, level: 1, karma = [1, 0, 1, 1]},
                            {user_id: 123515, level: 1, karma = [1, 0, 1, 1]},
                            {user_id: 123515, level: 1, karma = [1, 0, 1, 1]},
                            ],
        123984: [{user_id: 123515, level: 1, karma = [1, 0, 1, 1]},
                            {user_id: 123515, level: 1, karma = [1, 0, 1, 1]},
                            {user_id: 123515, level: 1, karma = [1, 0, 1, 1]},
                            ]
        }
        
        chat_data
        [{chat_id: 1234134, commands_prefix: "/", karma_parameters: [0,1,2,3]},
         {chat_id: 1234134, commands_prefix: "/", karma_parameters: [0,1,2,3]},
         {chat_id: 1234134, commands_prefix: "/", karma_parameters: [0,1,2,3]},
         {chat_id: 1234134, commands_prefix: "/", karma_parameters: [0,1,2,3]},
        ]
    """

        
    """
        chat_id = message.chat.id
        if chat_id == 1234134:
            user_id = message.from_user.id        
            user = active_users.setdefault(user_id, inactive_users.pop(user_id, User(chat_id, user_id)))
            user.state = True
            user.messageHandler(message)
            
            await bot.send_message(chat_id, chat_id)
            
    """





async def on_shutdown(dp):
    # insert code here to run it before shutdown
    pass

active_users = {}
inactive_users = {}

if __name__ == '__main__':
    start_webhook(dispatcher=dp, webhook_path=WEBHOOK_PATH, on_startup=on_startup, on_shutdown=on_shutdown, skip_updates=False, host=WEBAPP_HOST, port=WEBAPP_PORT)
