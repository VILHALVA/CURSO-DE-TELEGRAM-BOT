# Enigma básico

class Enigma:
    """Enigma, com mensagem inicial e respostas"""
    def __init__ (self, nome):
        self.nome = nome
        self.respostas = []

    def addResposta (self, resposta):
        """Adiciona uma resposta como válida. Respostas são do tipo 'Resposta'"""
        self.respostas.append (resposta)

    def checkResposta (self, txt):
        """Checa se um texto é uma resposta válida"""
        for res in self.respostas:
            if res.check (txt):
                return res.proximo
        
        return False

    def setMsg (self, mensagemInicial):
        self.msg = mensagemInicial


