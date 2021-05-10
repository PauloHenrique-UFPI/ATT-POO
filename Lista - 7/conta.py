import datetime


class Cliente:

    __slots__ = ['_nome','_sobrenome','_cpf'] 
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf

    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    @property
    def sobrenome(self):
        return self._sobrenome
    @sobrenome.setter
    def sobrenome(self, novo_sobrenome):
        self._sobrenome = novo_sobrenome

    @property
    def cpf(self):
        return self._cpf
    @cpf.setter
    def cpf(self,novo_cpf):
        self._cpf = novo_cpf


class Conta:

    __slots__ = ['_cliente','_numero','_saldo','_limite','_historico']
    _cont_contas = 0
    def __init__(self, cliente, numero, saldo, limite):
        self._numero = numero
        self._saldo = saldo
        self._limite = limite
        self._historico = Historico()
        Conta._cont_contas +=1

    @staticmethod
    def total_contas():
        return Conta._cont_contas


    @property
    def numero(self):
        return self._numero
    @numero.setter
    def numero(self, novo_numero):
        self._numero = novo_numero

    @property
    def limite(self):
        return self._limite
    @limite.setter
    def limite(self, novo_limite):
        self._limite = novo_limite



    @property
    def historico(self):
        return self._historico


    def depositar(self, valor):
        if self._saldo+valor > self._limite:
            print('\nSaldo excede limite, impossivel depositar\n')
            return False
        else:
            self._historico._transacoes.append('Deposito de {}'.format(valor))
            self._saldo += valor
            return True

    def sacar(self,valor):
        if self._saldo >= valor:
            self._historico._transacoes.append('saque de {}'.format(valor))
            self._saldo-=valor
            return True
        else:
            print('\nImpossivel sacar a quantia!!\n')
            return False
    
    def transfere(self, contax, valor):
        if self.sacar(valor) == False:
            return False
        else:
            self._historico._transacoes.append('transferencia de {}'.format(valor))
            contax.depositar(valor)
            return True

    def extrato(self):
        self._historico._transacoes.append('Acesso ao extrato')
        print('Numero da conta: ',self._numero)
        print('Saldo: ',self._saldo)

    def mostra_historico(self):
        print('\nNumero da conta: ',self._numero)
        self._historico.imprime()
  

class Historico:
    def __init__(self):
        self._data_abertura = datetime.datetime.today()
        self._transacoes = []

    def imprime(self):
        print('Data de criação:',self._data_abertura)
        print('Historico de trasações:')
        for t in self._transacoes:
            print('-',t)
