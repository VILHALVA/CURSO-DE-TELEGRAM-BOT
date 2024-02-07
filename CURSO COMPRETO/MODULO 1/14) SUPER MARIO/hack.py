from gerenciadorDeMemoria import *
from Enderecos import *
class hack(object):

    gerenciadorDeMemoria = None
    vidaAoPegarMoeda = None
    def __init__(self,nomeProcesso):
        self.gerenciadorDeMemoria = gerenciadorDeMemoria(nomeProcesso)
        self.vidaAoPegarMoeda = False
        self.fixarStatusMario = False
        pass


    def injetarStatusMario(self,status):
        self.gerenciadorDeMemoria.escreverByte(STATUSMARIO,status.to_bytes(1,byteorder='little'))

    def fixarStatusPenaMario(self):

        statusMarioAgora = self.gerenciadorDeMemoria.lerByte(STATUSMARIO)
        print(statusMarioAgora)
        if (statusMarioAgora != MARIO_PENINHA):
            self.gerenciadorDeMemoria.escreverByte(STATUSMARIO,MARIO_PENINHA.to_bytes(1,byteorder='little'))
        if (statusMarioAgora == MARIO_PENINHA):  #aumentei isto no codigo pra n fz nada se tiver peninha kajsdkasjd
            print('ja tem peninha')

        pass

    def valorfixoMoedas(self):
        valorPadraoDeMoedas = 99
        quantidadeAtualDemoedas = self.gerenciadorDeMemoria.lerByte(MOEDAS)
        if (quantidadeAtualDemoedas!=99):
            self.gerenciadorDeMemoria.escreverByte(MOEDAS,valorPadraoDeMoedas.to_bytes(1,byteorder='little'))
            print('moedas fixadas')
    def flordoFogo(self):
        statusMarioAgora = self.gerenciadorDeMemoria.lerByte(STATUSMARIO)
        print(statusMarioAgora)
        if (statusMarioAgora != MARIO_FLOR_DE_FOGO):
            self.gerenciadorDeMemoria.escreverByte(STATUSMARIO,MARIO_FLOR_DE_FOGO.to_bytes(1,byteorder='little'))
        if (statusMarioAgora == MARIO_FLOR_DE_FOGO):  #aumentei isto no codigo pra n fz nada se tiver peninha kajsdkasjd
            print('ja esta grande')

    def pequeno(self):
        statusMarioAgora = self.gerenciadorDeMemoria.lerByte(STATUSMARIO)
        print(statusMarioAgora)
        if (statusMarioAgora != MARIO_PEQUENO):
            self.gerenciadorDeMemoria.escreverByte(STATUSMARIO,MARIO_PEQUENO.to_bytes(1,byteorder='little'))
        if (statusMarioAgora == MARIO_PEQUENO):  #aumentei isto no codigo pra n fz nada se tiver peninha kajsdkasjd
            print('ja esta grande')     
    def grande(self):
        statusMarioAgora = self.gerenciadorDeMemoria.lerByte(STATUSMARIO)
        print(statusMarioAgora)
        if (statusMarioAgora != MARIO_GRANDE):
            self.gerenciadorDeMemoria.escreverByte(STATUSMARIO,MARIO_GRANDE.to_bytes(1,byteorder='little'))
        if (statusMarioAgora == MARIO_GRANDE):  #aumentei isto no codigo pra n fz nada se tiver peninha kajsdkasjd
            print('ja esta pequeno')            

                