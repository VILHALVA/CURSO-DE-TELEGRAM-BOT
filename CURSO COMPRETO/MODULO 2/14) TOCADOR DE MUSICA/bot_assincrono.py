from telegram.ext import CommandHandler, Filters, MessageHandler, Updater
from multiprocessing import Process
from os import mkdir as create
from datetime import datetime
from bs4 import BeautifulSoup
from os.path import exists
from time import sleep
import urllib.request
import pafy
import vlc


path_communication = 'files/communication.txt'
path_command = 'files/command.txt'
path_whitelist = 'files/users.txt'
path_history = 'files/history.txt'
path_token = 'files/token.txt'
path_queue = 'files/queue.txt'

if not exists('files'):
    create('files')

try:
    command_file = open(path_command, 'r')
    command_file.close()
except:
    command_file = open(path_command, 'w')
    command_file.close()

try:
    path_file = open(path_queue, 'r')
    path_file.close()
except:
    path_file = open(path_queue, 'w')
    path_file.close()

try:
    history_file = open(path_history, 'r')
    history_file.close()
except:
    history_file = open(path_history, 'w')
    history_file.close()

try:
    communication_file = open(path_communication, 'r')
    communication_file.close()
except:
    communication_file = open(path_communication, 'w')
    communication_file.close()

try:
    token_file = open(path_token, 'r')
    token = token_file.read()
    token_file.close()
except:
    token = input('Token do telegram não encontrado, cole o Token de seu Bot aqui: ')

    token_file = open(path_token, 'w')
    token_file.write(str(token))
    token_file.close()


password = input('Digite uma senha: ')
help_message = '''/play nome_da_música ou url.
/pause Pausa a faixa atualmente sendo reproduzida.
/resume Retomar a música pausada.
/volume Verifique ou altere o volume atual.
/skip Ignora a música atual e reproduz a próxima música da fila'''

Instance = vlc.Instance()
player = Instance.media_player_new()


def get_link():
    try:
        queue_file = open(path_queue, 'r')
        queue = queue_file.read()
        queue_file.close()

        cut = queue.find('\n')

        if cut != -1:
            link = queue[0:cut]
            queue = queue[cut+1:]

            queue_file = open(path_queue, 'w')
            queue_file.write(queue)
            queue_file.close()

            return link

        else:
            return ''

    except:
        queue_file = open(path_queue, 'w')
        queue_file.close()
        link = ''

    return link


def play_music(link):
    video = pafy.new(link,ydl_opts={
        'ignoreerrors': True,
        'quiet': True,
        'no_warnings': True,
        'nocheckcertificate': True,
        'age_limit': 50,
    })

    playurl = video.getbestaudio().url

    Media = Instance.media_new(playurl)
    player.set_media(Media)
    player.play()


def set_communication(telegram_id,msg):
    communication_file = open(path_communication, 'a')
    communication_file.write(telegram_id+' '+msg+'\n')
    communication_file.close()

    

def history(msg):
    history_file = open(path_history, 'a')
    history_file.write(msg+'\n')
    history_file.close()
    print(msg)



def set_command(update,command_player):
    command_file = open(path_command, 'w')
    command_file.write(str(update.message.chat_id)+' '+command_player+' '+update.message.chat['first_name'])
    command_file.close()



def getWhiteList():
    try:
        whitelist_file = open(path_whitelist, 'r')
        whitelist = whitelist_file.read()
        whitelist_file.close()
    except:
        whitelist_file = open(path_whitelist, 'w')
        whitelist_file.close()
        whitelist = ''
    
    return whitelist



def logger(update):
    if update:
        log = datetime.strftime(datetime.now(), '%H:%M:%S %d/%m/%Y')
        log += ' '+str(update.message.chat_id)+' '+update.message.chat['first_name']+': '+update.message.text
        return log
    else:
        return 'Erro: objeto vazio'



def start(bot, update):
    history(logger(update))
    whitelist = getWhiteList()

    if str(update.message.chat_id) in whitelist:
        response_message = help_message
    else:
        response_message = 'Digite /password <senha> para utilizar este bot'

    bot.send_message(
        chat_id=update.message.chat_id,
        text=response_message
    )


def verifyPassword(bot, update):
    history(logger(update))

    whitelist = getWhiteList()

    if str(update.message.chat_id) in whitelist:
        response_message = 'Você já está cadastrado, digite /help para ver os comandos.'
    else:
        try:
            text = update.message.text.split(' ',1)[1]
        except:
            text = None

        if text == None:
            response_message = 'Digite uma senha para usar o bot.'
        elif text == password:
            whitelist_file = open(path_whitelist, 'a')
            whitelist_file.write(str(update.message.chat_id)+'\n')
            whitelist_file.close()

            response_message = 'Senha correta, digite /help para ver os comandos.'
        else:
            response_message = 'Senha incorreta, tente novamente.'

    bot.send_message(
        chat_id=update.message.chat_id,
        text=response_message
    )


def getHelp(bot, update):
    history(logger(update))
    whitelist = getWhiteList()

    if str(update.message.chat_id) in whitelist:
        response_message = help_message
    else:
        response_message = 'Você não tem permissão para usar este comando, digite /password <senha>'

    bot.send_message(
        chat_id=update.message.chat_id,
        text=response_message
    )


def setPause(bot, update):
    history(logger(update))
    whitelist = getWhiteList()

    if str(update.message.chat_id) in whitelist:
        set_command(update,'pause')
        response_message = 'Música pausada!'
    else:
        response_message = 'Você não tem permissão para usar este comando, digite /password <senha>'

    bot.send_message(
        chat_id=update.message.chat_id,
        text=response_message
    )


def setResume(bot, update):
    history(logger(update))
    whitelist = getWhiteList()

    if str(update.message.chat_id) in whitelist:
        set_command(update,'resume')
        response_message = 'Reproduzindo música!'
    else:
        response_message = 'Você não tem permissão para usar este comando, digite /password <senha>'

    bot.send_message(
        chat_id=update.message.chat_id,
        text=response_message
    )


def skipMusic(bot, update):
    history(logger(update))
    whitelist = getWhiteList()

    if str(update.message.chat_id) in whitelist:
        set_command(update,'skip')
        response_message = 'Reproduzindo próxima música!'
    else:
        response_message = 'Você não tem permissão para usar este comando, digite /password <senha>'

    bot.send_message(
        chat_id=update.message.chat_id,
        text=response_message
    )


def setVolume(bot, update):
    history(logger(update))
    whitelist = getWhiteList()

    if str(update.message.chat_id) in whitelist:
        if update.message.text == '/volume':
            set_command(update,'volume')
        else:
            try:
                text = int(update.message.text.split(' ',1)[1])

                if text < 0:
                    text = 0
                elif text > 100:
                    text = 100
            except:
                text = None

            if text == None:
                response_message = 'Digite um valor entre 0 a 100'
            else:
                set_command(update,'volume'+str(text))
                response_message = 'Volume alterado: %s%' % str(text)
    else:
        response_message = 'Você não tem permissão para usar este comando, digite /password <senha>'

    bot.send_message(
        chat_id=update.message.chat_id,
        text=response_message
    )
        

def playMusic(bot, update):
    history(logger(update))
    whitelist = getWhiteList()

    if str(update.message.chat_id) in whitelist:
        try:
            textToSearch = update.message.text.split(' ',1)[1]
        except:
            textToSearch = None
        
        if textToSearch == None:
            response_message = 'Oops, digite o nome de uma música ou envie a url'
        elif ('youtube.com' in textToSearch or 'youtu.be' in textToSearch) and ' ' not in textToSearch:
            link = textToSearch
        else:
            query = urllib.parse.quote(textToSearch)
            url = 'https://www.youtube.com/results?search_query=' + query
            response = urllib.request.urlopen(url)
            html = response.read()
            soup = BeautifulSoup(html, 'html.parser')
            for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
                link = 'https://www.youtube.com' + vid['href']
                break

    
        queue_file = open(path_queue, 'a')
        queue_file.write(link+'\n')
        queue_file.close()
        response_message = 'Música adicionada na fila!'
    else:
        response_message = 'Você não tem permissão para usar este comando, digite /password <senha>'

    bot.send_message(
        chat_id=update.message.chat_id,
        text=response_message
    )



def main_player():
    while True:
        if player.get_state() == vlc.State.NothingSpecial or player.get_state() == vlc.State.Ended:
            link = get_link()

            if link:
                play_music(link)

        else:
            command_file = open(path_command, 'r')
            command = command_file.read()
            command_file.close()


            if command != '':
                telegram_id = command.split(' ',2)[0]
                telegram_name = command.split(' ',2)[2]
                command = command.split(' ',2)[1]

                if command == 'pause':
                    player.set_pause(1)
                elif command == 'resume':
                    player.set_pause(0)
                elif command == 'skip':
                    link = get_link()
                    if link:
                        play_music(link)
                elif command == 'volume':
                    msg = 'Volume atual: '+str(player.audio_get_volume())
                    set_communication(telegram_id,msg)
                elif 'volume' in command:
                    player.audio_set_volume(int(command[6:]))

                command_file = open(path_command, 'w')
                command_file.write('')
                command_file.close()

        sleep(0.3)



def main_telegram():
    updater = Updater(token)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler(['password', 'pw'], verifyPassword))
    dispatcher.add_handler(CommandHandler(['skip', 's', 'next'], skipMusic))
    dispatcher.add_handler(CommandHandler(['play', 'p'], playMusic))
    dispatcher.add_handler(CommandHandler(['resume'], setResume))
    dispatcher.add_handler(CommandHandler(['volume'], setVolume))
    dispatcher.add_handler(CommandHandler(['pause'], setPause))
    dispatcher.add_handler(CommandHandler(['stop'], setPause))
    dispatcher.add_handler(CommandHandler(['help'], getHelp))
    dispatcher.add_handler(CommandHandler(['start'], start))

    updater.start_polling()
    updater.idle()



if __name__ == "__main__":
    telegram_process = Process(target=main_telegram)
    player_process = Process(target=main_player)

    telegram_process.start()
    player_process.start()

    telegram_process.join()

    print('teste')
    player_process.join()