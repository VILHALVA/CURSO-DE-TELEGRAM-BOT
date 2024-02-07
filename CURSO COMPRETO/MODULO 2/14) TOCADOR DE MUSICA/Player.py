from os import mkdir as create
from os.path import exists
from time import sleep
import pafy
import vlc


path_queue = 'files/queue.txt'
path_command = 'files/command.txt'
path_communication = 'files/communication.txt'

if not exists('files'):
    create('files')

Instance = vlc.Instance()
player = Instance.media_player_new()
command_file = open(path_command, 'w')
command_file.write('')
command_file.close()

try:
    communication_file = open(path_communication, 'r')
    communication_file.close()
except:
    communication_file = open(path_communication, 'w')
    communication_file.close()


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

            user_id = link.split(' ')[0]
            user_name = link.split(' ')[2]
            link = link.split(' ')[1]

            return user_id,user_name,link

        else:
            return None,None,None

    except:
        queue_file = open(path_queue, 'w')
        queue_file.close()

    return None,None,None


def play_music(link):
    video = pafy.new(link,ydl_opts={
        'ignoreerrors': True,
        'quiet': True,
        'no_warnings': True,
        'nocheckcertificate': True,
    })

    playurl = video.getbestaudio().url

    Media = Instance.media_new(playurl)
    player.set_media(Media)
    player.play()

    return video.title


def set_communication(telegram_id,msg):
    communication_file = open(path_communication, 'a')
    communication_file.write(telegram_id+' '+msg+'\n')
    communication_file.close()


def main():
    user_id,user_name,link = None,None,None
    print('Player iniciado!\n')
    while True:
        if player.get_state() == vlc.State.NothingSpecial or player.get_state() == vlc.State.Ended:
            user_id,user_name,link = get_link()

            if link:
                music_title = play_music(link)
                set_communication('allow_users','Tocando no momento: '+str(music_title)+'<cut>Adicionado por: '+user_name)

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
                    if user_id and user_id != telegram_id:
                        set_communication(telegram_id,'Um pedido foi enviado a '+user_name+' para pular esta música.')
                        set_communication(user_id,telegram_name+' gostaria de pular sua música: '+str(music_title)+'<cut>digite /skip para pular')
                    else:
                        user_id,user_name,link = get_link()
                        if link:
                            music_title = play_music(link)
                            set_communication('allow_users','Tocando no momento: '+str(music_title)+'<cut>Adicionado por: '+user_name)
                        else:
                            set_communication(telegram_id,'Não há músicas na fila')

                elif command == 'volume':
                    msg = 'Volume atual: '+str(player.audio_get_volume())+'%'
                    set_communication(telegram_id,msg)
                elif 'volume' in command:
                    player.audio_set_volume(int(command[6:]))
                elif command == 'nowplaying':
                    if player.get_state() == vlc.State.Playing:
                        if user_name:
                            msg = 'Tocando no momento: '+str(music_title)+'<cut>Adicionado por: '+user_name
                        else:
                            msg = 'Nenhuma música está sendo reproduzida no momento'
                    elif player.get_state() == vlc.State.Paused:
                        if user_name:
                            msg = 'Música pausada: '+str(music_title)+'<cut>Adicionado por: '+user_name
                        else:
                            msg = 'Nenhuma música está sendo reproduzida no momento'
                    else:
                        msg = 'Nenhuma música está sendo reproduzida no momento'
                    
                    set_communication(telegram_id,msg)

                command_file = open(path_command, 'w')
                command_file.write('')
                command_file.close()
        sleep(0.3)

main()
