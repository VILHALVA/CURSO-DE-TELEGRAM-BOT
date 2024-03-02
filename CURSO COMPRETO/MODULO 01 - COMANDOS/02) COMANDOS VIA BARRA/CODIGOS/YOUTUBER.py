import requests
import time
import json
import os

class TelegramBot:
    def __init__(self):
        TOKEN  = "TOKEN_AQUI"
        self.iURL = f"https://api.telegram.org/bot{TOKEN}/"
    def Iniciar(self):
        iUPDATE_ID = None
        while True:
            ATUALIZACAO = self.ler_novas_mensagens(iUPDATE_ID)
            IDADOS = ATUALIZACAO["result"]
            if IDADOS:
                for dado in IDADOS:
                    iUPDATE_ID = dado['update_id']
                    mensagem = str(dado["message"]["text"])
                    chat_id = dado["message"]["from"]["id"]
                    primeira_mensagem = int(dado["message"]["message_id"]) == 1
                    resposta = self.gerar_respostas(mensagem, primeira_mensagem)
                    self.responder(resposta, chat_id)
                    
    def ler_novas_mensagens(self, iUPDATE_ID):
        iLINK_REQ = f'{self.iURL}getUpdates?timeout=5'
        if iUPDATE_ID:
            iLINK_REQ = f'{iLINK_REQ}&offset={iUPDATE_ID + 1}'
        iRESULT = requests.get(iLINK_REQ)
        return json.loads(iRESULT.content)

    def gerar_respostas(self, mensagem, primeira_mensagem):
        print("=" *100,"\n🤡USUÁRIO:\n>>>" + str(mensagem), "\n", "=" *100)
        if primeira_mensagem == True or mensagem.lower() in ('menu','cardapio'):
            return f'''😃Olá! Seja bem vindo ao chatBot.{os.linesep}🌚Eu tenho sugestões dos melhores canais do YouTube para você conhecer.{os.linesep}😒Envie o número correspodente ao canal sugerido:{os.linesep} 1️⃣ > CURIOSO NEWS{os.linesep} 2️⃣ > FALA DE TUDO{os.linesep} 3️⃣ > UNIVERSO ASTRONÔMICO{os.linesep} 4️⃣ > SUPER OITO{os.linesep} 5️⃣ > DEVEDIA.'''
        if mensagem == "1":
            return f'''https://www.youtube.com/c/CuriosoNewsvideos/videos{os.linesep}🌝Gostou do canal?'''
        elif mensagem == "2":
            return f'''https://www.youtube.com/c/FaladeTudo/videos{os.linesep}🌝Gostou do canal?'''
        elif mensagem == "3":
            return f'''https://www.youtube.com/c/UniversoAstronomico/videos{os.linesep}🌝Gostou do canal?'''
        elif mensagem == "4":
            return f'''https://www.youtube.com/user/otaviouga/videos{os.linesep}🌝Gostou do canal?'''
        elif mensagem == "5":
            return f'''https://www.youtube.com/c/DevmediaBrasil/videos{os.linesep}🌝Gostou do canal?'''
        
        elif mensagem.lower() in ("s", "sim"):
            return '''😁OK! Muito obrigado pelo FadBack!'''
        elif mensagem.lower() in ("n", "não"):
            return '''😡Sinto muito! Não é possivel agradar a todo mundo!'''
        else:
            return f'''🔴SINTO MUITO! NÃO COMPREENDO!{os.linesep}😊Para acessar o painel digite "menu"!'''

    def responder(self, resposta, chat_id):
        iLINK_REQ = f'{self.iURL}sendMessage?chat_id={chat_id}&text={resposta}'
        requests.get(iLINK_REQ)
        print("=" *100,"\n🤖RESPONDIR:\n>>>" + str(resposta), "\n", "=" *100,)

bot = TelegramBot()
bot.Iniciar() 
