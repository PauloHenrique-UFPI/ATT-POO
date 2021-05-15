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
from cadastro import Cadastro


from conta import Conta
from conta import Cliente
from cadastroConta import Cadastro_Conta


class Ui_Main(QtWidgets.QWidget):
    def setupUi(self, Main):
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
        super(Main, self).__init__(parent)
        self.setupUi(self)
        self.cad = Cadastro()
        self.cadConta = Cadastro_Conta()
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

    def troca_transfere(self):
        self.conta_atual = self.retorna_conta()
        if ( self.conta_atual != None):
            self.controle_de_tela.setCurrentIndex(self.index_Tranferir)

    def tranfere_valor(self):
        num_conta = self.tela_Tranferir.input_conta.text()
        valor = self.tela_Tranferir.input_valor.text()
        retorno = self.cadConta.busca(num_conta)
        if (retorno != None):
            Conta.transfere(self.conta_atual, retorno, float(valor))
            QMessageBox.information(None, 'POOII', 'Transferencia efetuada com sucesso!')
        else:
            QMessageBox.information(None, 'POOII', 'Conta não encontrada! {}'.format(retorno))





    def mostra_extrato(self):
        self.conta_atual = self.retorna_conta()
        if (self.conta_atual != None):
            data = Conta.data(self.conta_atual)
            saldo = Conta.saldo_conta(self.conta_atual)
            self.tela_Extrato.lineEdit_2.setText(data)
            self.tela_Extrato.lineEdit.setText(str(saldo))
            self.controle_de_tela.setCurrentIndex(self.index_Extrato)
    def mostrar_historico(self):
        self.conta_atual = self.retorna_conta()
        if ( self.conta_atual != None ):
            self.tela_Hitorico.input_historico.clear()
            return_historico = Conta.historico(self.conta_atual)
            for operacao in return_historico:
                self.tela_Hitorico.input_historico.addItem(operacao)

            self.controle_de_tela.setCurrentIndex(self.index_Historico)

    def volta_opcoes(self):
        self.controle_de_tela.setCurrentIndex(self.index_Operacoes)

    def troca_cadastra_pessoa(self):
        self.controle_de_tela.setCurrentIndex(self.index_Cadastra)

    def troca_cadastra_conta(self):
        self.controle_de_tela.setCurrentIndex(self.index_Cadastra_Conta)
    
    def troca_operacoes(self):
        self.controle_de_tela.setCurrentIndex(self.index_Operacoes)

    def troca_sacar(self):
        self.conta_atual = self.retorna_conta()
        if ( self.conta_atual != None):
            self.controle_de_tela.setCurrentIndex(self.index_Sacar)

    def troca_deposita(self):
        self.conta_atual = self.retorna_conta()
        if ( self.conta_atual != None):
            self.controle_de_tela.setCurrentIndex(self.index_Depositar)

    def retorna_conta(self):
        numero_atual = self.tela_Operacoes.input_conta.text()
        retorno = self.cadConta.busca(numero_atual)
        if ( retorno == None):
            QMessageBox.information(None, 'POOII', 'Conta não encontrada')
        return retorno

    def saca(self):
        valor = self.tela_Sacar.input_sacar.text()
        if (valor != ''):
            Conta.sacar(self.conta_atual, float(valor))
            QMessageBox.information(None, 'POOII', 'Saque efetuado com sucesso!')
        else:
            QMessageBox.information(None, 'POOII', 'N foi possivel efetuar o saque!')

    def cadastra_pessoa(self):
        nome = self.tela_Cadastra.input_nome.text()
        sobrenome = self.tela_Cadastra.input_sobrenome.text()
        cpf = self.tela_Cadastra.input_cpf.text()
        if not(nome == '' or sobrenome == '' or cpf == '' ):
            p = Cliente(nome, sobrenome, cpf)
            if (self.cad.cadastra(p)):
                QMessageBox.information(None, 'POOII', 'Cadastro realizado com sucesso!')
                self.tela_Cadastra.input_nome.setText('')
                self.tela_Cadastra.input_sobrenome.setText('')
                self.tela_Cadastra.input_cpf.setText('')
            else:
                QMessageBox.information(None, 'POOII', 'cpf ja cadastrado!')
    
    def deposita(self):
        valor = self.tela_Depositar.input_deposito.text()
        if (valor != ''):
            Conta.depositar(self.conta_atual,float(valor))
            QMessageBox.information(None, 'POOII', 'Valor depositado!')
        else:
            QMessageBox.information(None, 'POOII', 'Digite um valor para deposito!')

    def cadastra_Conta(self):
        
        cpf = self.tela_Cadastra_Conta.lineEdit.text()
        if not(cpf == ''):
            p = self.cad.busca(cpf)
            if ( p != None):
                self.cout += 1
                c = Conta(p,str(self.cout),0,10000)#ainda n esta completo, numero da conta aleatorio
                if (self.cadConta.cadastra(c)):
                    QMessageBox.information(None, 'POOII', 'Cadastro realizado com sucesso!\n Numero da conta:{}'.format(self.cout))
                    self.tela_Cadastra_Conta.lineEdit.setText('')

                else:
                    QMessageBox.information(None, 'POOII', 'conta ja cadastrado!')
            else:
                QMessageBox.information(None, 'POOII', 'cpf não encontrado!')
        else:
            QMessageBox.information(None, 'POOII', 'Todos os valor devem ser preenxidos!')
        self.controle_de_tela.setCurrentIndex(self.index_Inicial)
        
    
    def troca_inicial(self):
        self.controle_de_tela.setCurrentIndex(self.index_Inicial)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())
