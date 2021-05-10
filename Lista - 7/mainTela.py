import sys
import os

from PyQt5 import  QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from PyQt5.QtCore import QCoreApplication

from telaInicial import Tela_Inicial
from telaCadastra import Tela_Cadastra
from telaOperacoes import Tela_Operacoes
from telaHistorico import Tela_Historico

from conta import Conta
from conta import Cliente


class Ui_Main(QtWidgets.QWidget):
    def setupUi(self, Main):
        Main.setObjectName('Main')
        Main.resize(640,480)

        self.QtStack = QtWidgets.QStackedLayout()

        self.stack0 = QtWidgets.QMainWindow()
        self.stack1 = QtWidgets.QMainWindow()
        self.stack2 = QtWidgets.QMainWindow()

        self.tela_inicial = Tela_Inicial()
        self.tela_inicial.setupUi(self.stack0)

        self.tela_cadastra = Tela_Cadastra()
        self.tela_cadastra.setupUi(self.stack1)

        self.tela_operacoes = Tela_Operacoes()
        self.tela_operacoes.setupUi(self.stack2)

        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)



class Main(QMainWindow, Ui_Main):
    def __init__(self, parent = None):
        super(Main, self).__init__(parent)
        self.setupUi(self)

        self.cadPessoa = Pessoa()
        self.cadConta = Conta
        self.tela_inicial.pushButton.clicked.connect(self.abrirTelaCadastra)
        self.tela_inicial.pushButton_2.clicked.connect(self.abrirTelaOperacoes)

    def abrirTelaCadastra(self):
        self.QtStack.setCurrentIndex(1)
        self.tela_cadastra.pushButton.clicked.connect(self.botaoCadastra)
        self.tela_cadastra.pushButton_2.clicked.connect(self.volta)
            

    def volta(self):
        self.QtStack.setCurrentIndex(0)
        

    def abrirTelaOperacoes(self):
        self.QtStack.setCurrentIndex(2)
        self.tela_operacoes.pushButton_5.clicked.connect(self.volta)

    def botaoCadastra(self):



if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())
