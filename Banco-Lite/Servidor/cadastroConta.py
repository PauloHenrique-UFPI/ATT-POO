'''
    DESCRIPTION

        Class - Cadastro_Conta
            Classe criada para criar lista de 'Conta()'
'''
class Cadastro_Conta:
    
    __slots__ = ['_lista_contas']

    def __init__(self):
        '''
        Modulo que cria o  'construtor' da Classe'
            :param  self._lista_contas: Conta()
                valor do tipo Conta
        '''
        self._lista_contas = []
    
    def cadastra(self, conta):
        '''
        Modulo que cadastra a 'conta' no parametro self._lista_contas 
            :param  self: Conta()
                valor do tipo Conta
            :param conta: Conta()
                valor do tipo Conta
            :retorno:
              retorno do tipo boleano 'True' se consegue adicionar na lista 'False' caso contrario
        '''
        existe = self.busca(conta.numero)
        if(existe == None):
            self._lista_contas.append(conta)
            return True
        else:
            return False

    def busca(self, numero):
        '''
        Modulo que busca a 'conta' no parametro self._lista_contas 
            :param  self: Conta()
                valor do tipo Conta
            :param numero: str
                valor do tipo string
            :retorno:
                retorno do tipo Conta(), retona 'None' caso nao encontre a conta retorna a 'conta' procurada
        '''
        for lp in self._lista_contas:
            if lp.numero() == numero:
                return lp
        return None



