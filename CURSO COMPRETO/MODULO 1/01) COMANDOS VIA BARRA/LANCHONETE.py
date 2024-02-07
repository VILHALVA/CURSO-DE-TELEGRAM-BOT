import requests
import time
import json
import os

class TelegramBot:
    def __init__(self):
        TOKEN  = "TOKEN_AQUI"
        self.iURL = f'https://api.telegram.org/bot{TOKEN}/'
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
        print("🤡CLIENTE >>>" + str(mensagem))
        if primeira_mensagem == True or mensagem.lower() in ('menu','cardapio'):
            return f'''Olá seja bem vindo a Pizzaria MammaMia, informe o codigo do item que deseja pedir:{os.linesep}1 - Pizza Calabresa{os.linesep}2 - Pizza Napolitana{os.linesep}3 - Pizza 4 Queijos'''
        if mensagem == '1':
            return f'''Pizza Calabresa - R$25,00{os.linesep}Confirmar pedido?(s/n)
            '''
        elif mensagem == '2':
            return f'''Pizza Napolitana - R$27,00{os.linesep}Confirmar pedido?(s/n)
            '''
        elif mensagem == '3':
            return f'''Pizza 4 Queijos - R$30,00{os.linesep}Confirmar pedido?(s/n)'''

        elif mensagem.lower() in ('s', 'sim'):
            return '''Pedido Confirmado! '''
        elif mensagem.lower() in ('n', 'não'):
            return '''Item não incluso! Informe o codigo do item: '''
        else:
            return 'Para acessar o cardapio digite "menu"'

    def responder(self, resposta, chat_id):
        iLINK_REQ = f'{self.iURL}sendMessage?chat_id={chat_id}&text={resposta}'
        requests.get(iLINK_REQ)
        print("🤖RESPOSTA: >>>" + str(resposta))

bot = TelegramBot()
bot.Iniciar() 
