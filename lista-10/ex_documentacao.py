'''
    Arquivo responsavel por operações matematicas
        class: Operacoes
'''
class Operacoes:
    def __init__(self, a, b):
        '''
        Construtor da classe operacoes
            :param self._a: int
                valor do tipo inteiro
            :param self._b: int
                valor do tipo inteiro
        '''
        self._a = a
        self._b = b


    def soma(self):
        '''
        Modulo de soma
            :param self: Operacoes()
                valor do tipo operacoes
            :retorno:
                retorno da soma de a + b
        '''
        return self._a + self._b

    def subtracao(self):
        '''
        Modulo de subtracao
            :param self: Operacoes()
                valor do tipo operacoes
            :retorno:
                retorno da soma de a - b
        '''
        return self._a - self._b

    def multiplicacao(self):
        '''
        Modulo de multiplicacao
            :param self: Operacoes()
                valor do tipo operacoes
            :retorno:
                retorno da soma de a * b
        '''
        return self._a * self._b

    def divisao(self):
        '''
        Modulo de divisao
            :param self: Operacoes()
                valor do tipo operacoes
            :retorno:
                retorno da soma de a / b
        '''
        return self._a / self._b