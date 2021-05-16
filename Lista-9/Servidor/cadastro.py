
class Cadastro:
    
    __slots__ = ['_lista_pessoas']

    def __init__(self):
        self._lista_pessoas = []
    
    def cadastra(self, cliente):
        existe = self.busca(cliente.cpf)
        if(existe == None):
            self._lista_pessoas.append(cliente)
            return True
        else:
            return False

    def busca(self, cpf):
        for lp in self._lista_pessoas:
            if lp.cpf == cpf:
                return lp
        return None