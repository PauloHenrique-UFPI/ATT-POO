import sys
import os

from PyQt5 import  QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from PyQt5.QtCore import QCoreApplication

from telaInicia import Tela_Inicial
from telaCadastra import Tela_Cadastra
from telaOperacoes import Tela_Operacoes
from telaHistorico import Tela_Historico
from telaExtrato import Tela_Extrato
from telaTranferir import Tela_Transferir
from telaSacar import Tela_Sacar
from telaDeposita import Tela_Depositar
from telaCadastraConta import Tela_CadastraConta
from cliente import Cliente_connect




class Ui_Main(QtWidgets.QWidget):
    def setupUi(self, Main):
        '''
            Modulo que troca para a tela inicial
            :param self: Main(), Main feito altomaticamente
                valor do tipo Main
               
        '''
        Main.setObjectName('Main')
        Main.resize(640,480)

        self.controle_de_tela = QtWidgets.QStackedLayout()

        self.stack_Inicial = QtWidgets.QMainWindow()
        self.stack_Cadastra = QtWidgets.QMainWindow()
        self.stack_Extrato = QtWidgets.QMainWindow()
        self.stack_Sacar = QtWidgets.QMainWindow()
        self.stack_Operacoes = QtWidgets.QMainWindow()
        self.stack_Tranferir = QtWidgets.QMainWindow()
        self.stack_Depositar = QtWidgets.QMainWindow()
        self.stack_Historico = QtWidgets.QMainWindow()
        self.stack_Cadastra_Conta = QtWidgets.QMainWindow()

        self.tela_Inicial = Tela_Inicial()
        self.tela_Inicial.setupUi(self.stack_Inicial)

        self.tela_Cadastra = Tela_Cadastra()
        self.tela_Cadastra.setupUi(self.stack_Cadastra)

        self.tela_Extrato = Tela_Extrato()
        self.tela_Extrato.setupUi(self.stack_Extrato)

        self.tela_Sacar = Tela_Sacar()
        self.tela_Sacar.setupUi(self.stack_Sacar)

        self.tela_Operacoes = Tela_Operacoes()
        self.tela_Operacoes.setupUi(self.stack_Operacoes)

        self.tela_Tranferir = Tela_Transferir()
        self.tela_Tranferir.setupUi(self.stack_Tranferir)

        self.tela_Depositar = Tela_Depositar()
        self.tela_Depositar.setupUi(self.stack_Depositar)

        self.tela_Hitorico = Tela_Historico()
        self.tela_Hitorico.setupUi(self.stack_Historico)

        self.tela_Cadastra_Conta = Tela_CadastraConta()
        self.tela_Cadastra_Conta.setupUi(self.stack_Cadastra_Conta)

        self.controle_de_tela.addWidget(self.stack_Inicial)
        self.controle_de_tela.addWidget(self.stack_Cadastra)
        self.controle_de_tela.addWidget(self.stack_Extrato)
        self.controle_de_tela.addWidget(self.stack_Operacoes)
        self.controle_de_tela.addWidget(self.stack_Sacar)
        self.controle_de_tela.addWidget(self.stack_Tranferir)
        self.controle_de_tela.addWidget(self.stack_Depositar)
        self.controle_de_tela.addWidget(self.stack_Historico)
        self.controle_de_tela.addWidget(self.stack_Cadastra_Conta)

        self.index_Inicial = 0
        self.index_Cadastra = 1
        self.index_Extrato = 2
        self.index_Operacoes = 3
        self.index_Sacar = 4
        self.index_Tranferir = 5
        self.index_Depositar = 6
        self.index_Historico = 7
        self.index_Cadastra_Conta = 8


class Main(QMainWindow, Ui_Main):
    def __init__(self, parent = None):
        '''
            Modulo que troca para a tela inicial
            :param self: Main(),parent
                valor do tipo class Main
                valor do tipo none
        '''
        super(Main, self).__init__(parent)
        self.cliente = Cliente_connect()
        Cliente_connect.connect(self.cliente)
        self.setupUi(self)
        self.tela_Inicial.botao_cadpessoa.clicked.connect(self.troca_cadastra_pessoa)
        self.tela_Cadastra.botao_cadastra.clicked.connect(self.cadastra_pessoa)
        self.tela_Cadastra.pushButton_2.clicked.connect(self.troca_inicial)
        self.tela_Inicial.botao_cadconta.clicked.connect(self.troca_cadastra_conta)
        self.tela_Cadastra_Conta.pushButton.clicked.connect(self.cadastra_Conta)
        self.tela_Inicial.botao_singin.clicked.connect(self.troca_operacoes)
        self.tela_Operacoes.botao_depositar.clicked.connect(self.troca_deposita)
        self.tela_Depositar.botao_depositar.clicked.connect(self.deposita)
        self.tela_Depositar.pushButton.clicked.connect(self.volta_opcoes)
        self.tela_Operacoes.botao_sacar.clicked.connect(self.troca_sacar)
        self.tela_Sacar.botao_sacar.clicked.connect(self.saca)
        self.tela_Sacar.botao_voltar.clicked.connect(self.volta_opcoes)
        self.tela_Operacoes.botao_historico.clicked.connect(self.mostrar_historico)
        self.tela_Operacoes.pushButton_5.clicked.connect(self.troca_inicial)
        self.tela_Hitorico.pushButton.clicked.connect(self.volta_opcoes)
        self.tela_Operacoes.pushButton.clicked.connect(self.mostra_extrato)
        self.tela_Extrato.botao_voltar.clicked.connect(self.volta_opcoes)
        self.tela_Operacoes.botao_transferir.clicked.connect(self.troca_transfere)
        self.tela_Tranferir.botao_transferir.clicked.connect(self.tranfere_valor)
        self.tela_Tranferir.botao_voltar.clicked.connect(self.volta_opcoes)
        self.cout = 0
        self.conta_atual = None
    
    def troca_inicial(self):
        '''
            Modulo que troca para a tela inicial
            :param self: Main()
                valor do tipo class Main
        '''
        self.controle_de_tela.setCurrentIndex(self.index_Inicial)

    def troca_transfere(self):
        '''
            Modulo que troca de tela de tranferencia
            :param self: Main()
                valor do tipo class Main
        '''
        self.conta_atual = self.retorna_conta()
        if ( self.conta_atual != None):
            self.controle_de_tela.setCurrentIndex(self.index_Tranferir)

    def volta_opcoes(self):
        '''
            Modulo que troca de tela de opcoes: saca, tranfere...
            :param self: Main()
                valor do tipo class Main
        '''
        self.controle_de_tela.setCurrentIndex(self.index_Operacoes)

    def troca_cadastra_pessoa(self):
        '''
            Modulo que troca para a tela de cadastrar pessoas
            :param self: Main()
                valor do tipo class Main
        '''
        self.controle_de_tela.setCurrentIndex(self.index_Cadastra)

    def troca_cadastra_conta(self):
        '''
            Modulo que troca para a tela de cadastrar pessoas
            :param self: Main()
                valor do tipo class Main
        '''
        self.controle_de_tela.setCurrentIndex(self.index_Cadastra_Conta)
    
    def troca_operacoes(self):
        '''
            Modulo que troca de tela de opcoes: saca, tranfere...
            :param self: Main()
                valor do tipo class Main
        '''
        self.controle_de_tela.setCurrentIndex(self.index_Operacoes)

    def troca_sacar(self):
        '''
            Modulo que troca para a tela de sacar
            :param self: Main()
                valor do tipo class Main
        '''
        self.conta_atual = self.retorna_conta()
        if ( self.conta_atual != None):
            self.controle_de_tela.setCurrentIndex(self.index_Sacar)

    def troca_deposita(self):
        '''
            Modulo que troca para a tela de depositar
            :param self: Main()
                valor do tipo class Main
        '''
        self.conta_atual = self.retorna_conta()
        if ( self.conta_atual != None):
            self.controle_de_tela.setCurrentIndex(self.index_Depositar)

    def retorna_conta(self):
        '''
            Retorna a conta atual, da tela de opcões
            :param self: Main()
                valor do tipo class Main
        '''
        numero_atual = self.tela_Operacoes.input_conta.text()
        
        if ( numero_atual == ''):
            QMessageBox.information(None, 'POOII', 'Todos os campos devem ser preenchidos')
            return None
        return numero_atual

    def mostra_extrato(self):
        '''
            Modulo que mostra o extrato quandoa tela extrato é chamada
            :param self: Main()
                valor do tipo class Main
        '''
        self.conta_atual = self.retorna_conta()
        Cliente_connect.passa_mensagem(self.cliente,'extrato')
        flag = Cliente_connect.passa_mensagem(self.cliente, str(self.conta_atual))
        if (flag != None):
            data = Cliente_connect.passa_mensagem(self.cliente, 'data')
            saldo = Cliente_connect.passa_mensagem(self.cliente, 'saldo')
            self.tela_Extrato.lineEdit_2.setText(data)
            self.tela_Extrato.lineEdit.setText(str(saldo))
            self.controle_de_tela.setCurrentIndex(self.index_Extrato)
        else:
             QMessageBox.information(None, 'POOII', 'conta!!')

    def mostrar_historico(self):
        '''
            Modulo que mostra o histórico quandoa tela extrato é chamada
            :param self: Main()
                valor do tipo class Main
        '''
        self.conta_atual = self.retorna_conta()
        Cliente_connect.passa_mensagem(self.cliente,'historico')
        flag = Cliente_connect.passa_mensagem(self.cliente, str(self.conta_atual))
        if ( flag != None ):
            self.tela_Hitorico.input_historico.clear()
            arrayHistorico = []
            condParada = 'True'
            while condParada != 'False':
                condParada = Cliente_connect.passa_mensagem(self.cliente, 'historico')
                if condParada != 'False':
                    arrayHistorico.append(condParada)
                else:
                    break
            for operacao in arrayHistorico:
                self.tela_Hitorico.input_historico.addItem(operacao)

            self.controle_de_tela.setCurrentIndex(self.index_Historico)
    
    def saca(self):
        '''
            Modulo que gerencia os dados para saque e envia para o servidor
            :param self: Main()
                valor do tipo class Main
        '''
        valor = self.tela_Sacar.input_sacar.text()
        if (valor != ''):
            Cliente_connect.passa_mensagem(self.cliente,'sacar')
            flag = Cliente_connect.passa_mensagem(self.cliente, str(self.conta_atual))
            if flag == 'True':
                
                flag = Cliente_connect.passa_mensagem(self.cliente, str(valor))
                if flag =='True':
                    QMessageBox.information(None, 'POOII', 'Saque efetuado com sucesso!')
                else:
                    QMessageBox.information(None, 'POOII', 'Impossivel sacar a quantia!!')

            else:
                QMessageBox.information(None, 'POOII', 'Essa conta não existe! ')
        else:
            QMessageBox.information(None, 'POOII', 'Todos os campos devem ser preenchidos! ')
    
    def deposita(self):
        '''
            Modulo que gerencia os dados para depósito e envia para o servidor
            :param self: Main()
                valor do tipo class Main
        '''
        valor = self.tela_Depositar.input_deposito.text()
        if (valor != ''):
            Cliente_connect.passa_mensagem(self.cliente, 'depositar')
            flag = Cliente_connect.passa_mensagem(self.cliente,self.conta_atual)
            if flag == 'True':
                flag = Cliente_connect.passa_mensagem(self.cliente, valor)
                
                if flag == 'True':
                    QMessageBox.information(None, 'POOII', 'Valor depositado!')
                else:
                    QMessageBox.information(None, 'POOII', 'Valor exedeu o limite!')
            else:
                QMessageBox.information(None, 'POOII', 'Conta não encontrada')
                   
                        
        else:
            QMessageBox.information(None, 'POOII', 'Digite um valor para deposito!')
    
    def tranfere_valor(self):
        '''
            Modulo que gerencia os dados para tranferência e envia para o servidor
            :param self: Main()
                valor do tipo class Main
        '''
        num_conta = self.tela_Tranferir.input_conta.text()
        valor = self.tela_Tranferir.input_valor.text()
        
        Cliente_connect.passa_mensagem(self.cliente,'tranferir')
        retorno = Cliente_connect.passa_mensagem(self.cliente,self.conta_atual)
        print('retorno conta atual: ',retorno)

        if retorno == 'True':
            retorno =  Cliente_connect.passa_mensagem(self.cliente,num_conta)
            print('retorno segunda: ',retorno)
            
            if retorno == 'True':
                retorno = Cliente_connect.passa_mensagem(self.cliente,str(valor))
                
                if retorno == 'True':
                    QMessageBox.information(None, 'POOII', 'Transferencia efetuada com sucesso!')
                else:
                    QMessageBox.information(None, 'POOII', 'Nao foi possivel transferir')
            else:
                QMessageBox.information(None, 'POOII', 'Conta2 não encontrada!')
        else:
            QMessageBox.information(None, 'POOII', 'Conta não encontrada!')


    def cadastra_pessoa(self):
        '''
            Modulo que gerencia os dados para cadastrar uma pessoa e envia para o servidor
            :param self: Main()
                valor do tipo class Main
        '''
        nome = self.tela_Cadastra.input_nome.text()
        sobrenome = self.tela_Cadastra.input_sobrenome.text()
        cpf = self.tela_Cadastra.input_cpf.text()
        if not(nome == '' or sobrenome == '' or cpf == '' ):
            
            Cliente_connect.passa_mensagem(self.cliente,'cad_pessoa')
            Cliente_connect.passa_mensagem(self.cliente, nome)
            Cliente_connect.passa_mensagem(self.cliente, sobrenome)
            returno = Cliente_connect.passa_mensagem(self.cliente, cpf)
            if ( returno == 'True'):
                QMessageBox.information(None, 'POOII', 'Cadastro realizado com sucesso!')
                self.tela_Cadastra.input_nome.setText('')
                self.tela_Cadastra.input_sobrenome.setText('')
                self.tela_Cadastra.input_cpf.setText('')
            else:
                QMessageBox.information(None, 'POOII', 'cpf ja cadastrado!')
    

    def cadastra_Conta(self):
        '''
            Modulo que gerencia os dados para cadastrar uma pessoa e envia para o servidor
            :param self: Main()
                valor do tipo class Main
        '''
        
        cpf = self.tela_Cadastra_Conta.lineEdit.text()
        str(cpf)
        if not(cpf == ''):
            Cliente_connect.passa_mensagem(self.cliente,'cad_conta')
            info = Cliente_connect.passa_mensagem(self.cliente, 'none')
            self.cout = int(info)
            retorno = Cliente_connect.passa_mensagem(self.cliente, cpf)
            print("retorno de cpf: ",retorno)
            if ( retorno == 'True'):
                self.cout += 1
                retorno2 = Cliente_connect.passa_mensagem(self.cliente,str(self.cout))
                print("retorno da conta: ",retorno2)
                if (retorno2 == 'True'):
                    QMessageBox.information(None, 'POOII', 'Cadastro realizado com sucesso!\n Numero da conta:{}'.format(self.cout))
                    self.tela_Cadastra_Conta.lineEdit.setText('')

                else:
                    QMessageBox.information(None, 'POOII', 'nao foi possivel cadastrar!')
            else:
                QMessageBox.information(None, 'POOII', 'cpf não encontrado!')
        else:
            QMessageBox.information(None, 'POOII', 'Todos os valor devem ser preenxidos!')
        self.controle_de_tela.setCurrentIndex(self.index_Inicial)
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())
