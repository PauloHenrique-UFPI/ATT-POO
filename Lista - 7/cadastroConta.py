
class Cadastro_Conta:
    
    __slots__ = ['_lista_contas']

    def __init__(self):
        self._lista_contas = []
    
    def cadastra(self, conta):
        existe = self.busca(conta.numero)
        if(existe == None):
            self._lista_contas.append(conta)
            return True
        else:
            return False

    def busca(self, numero):
        for lp in self._lista_contas:
            if lp.numero == numero:
                return lp
        return None



