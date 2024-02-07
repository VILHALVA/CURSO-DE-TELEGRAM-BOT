import telepot
from telepot.delegate import per_from_id, create_open

from enigma import Enigma
import resposta

teste = Enigma ('teste')
teste.setMsg ('Oi, como vai?')

class SaBOTagem (telepot.helper.UserHandler):
    def __init__ (self, *args, **kwargs):
        """Construtor =P"""
        super (SaBOTagem, self).__init__ (*args, **kwargs)

    def on_message (self, msg):
        """Recebeu msg, testa resposta"""
        print (msg)

    def open (self, initMsg, seed):
        """Hora que abrir canal, Enigma 1"""
        bot.sendMessage (seed, teste.msg)


TOKEN = input ()
bot = telepot.DelegatorBot (TOKEN, [
    (per_from_id (), create_open (SaBOTagem, timeout = 3600)),
])
bot.message_loop (run_forever = True)
