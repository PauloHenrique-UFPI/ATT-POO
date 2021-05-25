'''
    DESCRIPTION

        Class - Cadastro_Conta
            Classe criada para criar lista de 'Conta()'
'''
class Cadastro:
    '''
        Modulo que cria o  'construtor' da Classe'
            :param  self._lista_contas: Conta()
                valor do tipo Conta
    '''
   
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
        '''
            Modulo que busca a 'Pessoa' no parametro self._lista_pessoas
                :param  self: Pessoa()
                    valor do tipo pessoa
                :param cpf: str
                    valor do tipo string
                :retorno:
                    retorno do tipo Conta(), retona 'None' caso nao encontre a pessoa retorna a 'Pessoa' procurada
        '''
        for lp in self._lista_pessoas:
            if lp.cpf == cpf:
                return lp
        return None