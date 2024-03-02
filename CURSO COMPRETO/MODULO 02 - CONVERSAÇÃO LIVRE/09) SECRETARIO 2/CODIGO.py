import requests
import json
import os

class TelegramBot:
    def __init__(self):
        TOKEN  = "TOKEN AQUI"
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
        if primeira_mensagem == True or mensagem.lower() in ('/start','oi','ola'):
            return f'''😃Olá! Seja bem vindo ao chatBot.{os.linesep}🌚Eu gosto muito de conversar. Principalmente sobre Tecnologia, Ciência, Filosofia e Teologia.'''
        if mensagem in ("tecnologia", "programação", "android", "robo"):
            return '''🌝Eu gosto muito de falar sobre a tecnologia. Da sua história e evolução até a conquista espacial. Sabia que os robôs vieram para sibstituir os humanos?'''
        elif mensagem in ("Ciência", "ciencia", "astronomia"):
            return '''🌝Diferente da supestição religiosa, a ciência se propoe a provar suas teorias. Pois para ser considerado uma TEORIA, o experimento deve ser reproduzivél. Sabia que na idede média, os cientistas eram chamados de hereges pelas igrejas?'''
        elif mensagem in ("FILOSOFIA", "filosofia", "penso", "pensamento"):
            return '''🌝Embora a Filosofia tenha vindo antes da Ciência e Tecnologia, e depois da religião, ela não ganha os creditos. Pois ela foi, e continua sendo fundamental para nossa civilização. Pois os humanos estão perdendo a capacidade de pensar. Sabia que os primeiros Filosofos não concordavam com seus professores?'''
        elif mensagem in ("TEOLOGIA", "teologia", "religião"):
            return f'''🌝A religião continua perdendo força após o renascimento. Pois ela prega uma coisa e vive outra. Não basta sua reputação manchada; Agora ela está perdendo adeptos devido a internet. Sabia que a Teologia se trata apenas da Filosofia Patristica?'''
        
        elif mensagem.lower() in ("s", "sim"):
            return '''😁Que bom! Estou feliz que você é uma pessoa estudiosa!'''
        elif mensagem.lower() in ("n", "não", "nao"):
            return '''😡Então deixe de ser preguiçoso e vá estudar!'''
        else:
            return f'''🔴SINTO MUITO! NÃO COMPREENDO!{os.linesep}'''

    def responder(self, resposta, chat_id):
        iLINK_REQ = f'{self.iURL}sendMessage?chat_id={chat_id}&text={resposta}'
        requests.get(iLINK_REQ)
        print("=" *100,"\n🤖RESPONDIR:\n>>>" + str(resposta), "\n", "=" *100,)

bot = TelegramBot()
bot.Iniciar() 
