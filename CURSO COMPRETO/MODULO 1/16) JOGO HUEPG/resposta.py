# Resposta para enigmas

class Resposta:
    """Resposta para enigmas, que sabem qual próximo enigma"""
    def __init__ (self, resposta, proximo):
        self.resposta = resposta
        self.proximo = proximo

    def check (self, txt):
        """Checa se texto é a resposta. Padrão: compara strings literalmente"""
        return txt == self.resposta
