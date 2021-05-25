import datetime
'''
    DESCRIPTION

        Class - Cliente
            Classe criada para cadastro de clientes que podem ter 1 ou mais contas no Banco
        Classs - Conta
            Classe conta para cadastro de contas para clientes do banco
        Classs - Historico
            Classe historico para obtenção do historico de transações de uma conta no banco
'''

class Cliente:
    __slots__ = ['_nome','_sobrenome','_cpf']
    def __init__(self, nome, sobrenome, cpf):
        '''
        Função do construtor da classe Cliente
            :param self._nome: str
                valor do tipo string
            
            :param self._sobrenome: str
                valor do tipo string

            param self._cpf: str
                valor do tipo string
        '''
        self._nome = nome
        self._sobrenome = sobrenome
        self._cpf = cpf

    @property
    def nome(self):
        '''
            Função Get do paramentro nome

            :param self: Cliente()
                variavel do tipo Cliente 

            :return:
                vai retornar o parametro 'nome' da classe
        '''
        return self._nome
        

    @property
    def sobrenome(self):
        '''
            Função Get do paramentro sobrenome

            :param self: Cliente()
                variavel do tipo Cliente 

            :return:
                vai retornar o parametro 'sobrenome' da classe
        '''
        return self._sobrenome
       

    @property
    def cpf(self):
        '''
        Função Get do paramentro cpf
            :param self: Cliente()
                variavel do tipo Cliente 

            :return:
                vai retornar o parametro 'cpf' da classe
        '''
        return self._cpf
   
        
    

class Conta:

    __slots__ = ['_cliente','_numero','_saldo','_limite','_historico','_data']
    _cont_contas = 0
    def __init__(self, cliente, numero, saldo, limite):
        '''
        Função do construtor da classe Conta

            :param self._numero: str
                valor do tipo string
            
            :param self._saldo: int
                valor do tipo inteiro

            :param self._limite: int
                valor do tipo inteiro
            
            :param self._historico: Historico()
                valor do tipo Historico
            
            :param self._data: str
                valor do tipo string

            :param self._cont_contas: int
                valor do tipo inteiro
        '''
        self._numero = numero
        self._saldo = saldo
        self._limite = limite
        self._historico = Historico()
        self._data = str(datetime.datetime.today())
        Conta._cont_contas +=1

    
    def data(self):
        '''
        Função Get do parametro data

            :param self: Conta()
                valor do tipo Conta

            :retorno:
                retorna o parametro 'data' da classe
        '''
        return self._data

    def saldo_conta(self):
        '''
        Função Get do parametro data

            :param self: Conta()
                valor do tipo Conta

            :retorno:
                retorna o parametro 'data' da classe
        '''
        return self._saldo

    @staticmethod
    def total_contas():
        '''
        Função Get do parametro total_contas

            :param self: Conta()
                valor do tipo Conta

            :retorno:
                retorna o parametro 'total_conta' da classe
        '''
        return Conta._cont_contas


    @property
    def numero(self):
        '''
        Função Get do parametro numero

            :param self: Conta()
                valor do tipo Conta

            :retorno:
                retorna o parametro 'numero' da classe
        '''
        return self._numero

    def historico(self):
        '''
        Função Get do parametro historico

            :param self: Conta()
                valor do tipo Conta

            :retorno:
                retorna uma lista 'historico._transacoes' da classe
        '''
        return self._historico._transacoes


    def depositar(self, valor):
        '''
        Função operação de deposito na conta

            :param self: Conta()
                valor do tipo Conta
            
            :param valor: int
                valor inteiro

            :retorno:
                retorna um boleano 'True' caso tenho sucesso 'False' caso contrario
        '''
        if self._saldo+valor > self._limite:
            print('\nSaldo excede limite, impossivel depositar\n')
            return False
        else:
            self._historico._transacoes.append('Deposito de {}'.format(valor))
            self._saldo += valor
            return True

    def sacar(self,valor):
        '''
        Função operação de saque na conta

            :param self: Conta()
                valor do tipo Conta
            
            :param valor: int
                valor inteiro

            :retorno:
                retorna um boleano 'True' caso tenho sucesso 'False' caso contrario
        '''
        if self._saldo >= valor:
            self._historico._transacoes.append('saque de {}'.format(valor))
            self._saldo-=valor
            return True
        else:
            print('\nImpossivel sacar a quantia!!\n')
            return False
    
    def transfere(self, contax, valor):
        '''
        Função operação de transferencia na conta

            :param self: Conta()
                valor do tipo Conta
            
            :param contax: Conta()
                valor do tipo Conta
            
            :param valor: int
                valor inteiro

            :retorno:
                retorna um boleano 'True' caso tenho sucesso 'False' caso contrario
        '''
        if self.sacar(valor) == False:
            return False
        else:
            self._historico._transacoes.append('transferencia de {}'.format(valor))
            contax.depositar(valor)
            return True

    def extrato(self):
        '''
        Função operação de extrato da conta

            :param self: Conta()
                valor do tipo Conta
        '''
        self._historico._transacoes.append('Acesso ao extrato')
        print('Numero da conta: ',self._numero)
        print('Saldo: ',self._saldo)

    def mostra_historico(self):
        '''
        Função operação de historico da conta

            :param self: Conta()
                valor do tipo Conta
        '''
        print('\nNumero da conta: ',self._numero)
        self._historico.imprime()
  

class Historico:
    def __init__(self):
        '''
        Função do construtor da classe Cliente
            :param self._data_abertura: str
                valor do tipo string
            
            :param self._transacoes str
                valor do tipo string
        '''
        self._data_abertura = datetime.datetime.today()
        self._transacoes = []
    
    @property
    def transacoes(self):
        '''
        Função Get do atributo 'transacoes'

            :param self: Historico
                valor tipo Historico
            :retorno:
                retorna atributo transacoes.
        '''
        return self._transacoes

print(__doc__)