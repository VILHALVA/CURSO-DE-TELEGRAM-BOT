from gerenciadorDeMemoria import *
from Enderecos import *
class hack(object):
    gerenciadorDeMemoria = None
    def __init__(self,nomeProcesso):
        self.gerenciadorDeMemoria = gerenciadorDeMemoria(nomeProcesso)
        pass

    def injetarStatusAladin(self, status):
        self.gerenciadorDeMemoria.escreverByte(status_aladin, status.to_bytes(1, byteorder='little'))

    def vidaAladin(self):
        statusaladinAgora = self.gerenciadorDeMemoria.lerByte(status_aladin)
        print(statusaladinAgora)
        if (statusaladinAgora != energia_aladin):
            self.gerenciadorDeMemoria.escreverByte(status_aladin,energia_aladin.to_bytes(1,byteorder='little'))

    def diamanteAladin(self):
        statusaladinAgora1 = self.gerenciadorDeMemoria.lerByte(status_diamante_aladin)
        print(statusaladinAgora1)
        if (statusaladinAgora1 != quantidade_diamante_aladin):
            self.gerenciadorDeMemoria.escreverByte(status_diamante_aladin,quantidade_diamante_aladin.to_bytes(1,byteorder='little'))

    def macaAladin(self):
        statusaladinAgora2 = self.gerenciadorDeMemoria.lerByte(status_maca_aladin)
        print(statusaladinAgora2)
        if (statusaladinAgora2 != quantidade_maca_aladin):
            self.gerenciadorDeMemoria.escreverByte(status_maca_aladin,quantidade_maca_aladin.to_bytes(1,byteorder='little'))

