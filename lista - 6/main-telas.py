import sys
import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from PyQt5.QtCore import QCoreApplication 

from telaMenu import Tela_Menu
from telaCadastra import Tela_Cadastra
from telaBusca import Tela_Busca
from pessoa import Pessoa
from cadastro import Cadastro

class Ui_Main(QtWidgets.QWidget):
    def setupUi(self, Main):
        Main.setObjectName('Main')
        Main.resize(640, 480)

        self.QtStack = QtWidgets.QStackedLayout()

        self.stack0 = QtWidgets.QMainWindow()
        self.stack1 = QtWidgets.QMainWindow()
        self.stack2 = QtWidgets.QMainWindow()

        self.tela_Menu = Tela_Menu()
        self.tela_Menu.setupUi(self.stack0)

        self.tela_Cadastra = Tela_Cadastra()
        self.tela_Cadastra.setupUi(self.stack1)

        self.tela_Busca = Tela_Busca()
        self.tela_Busca.setupUi(self.stack2)

        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)
    


class Main(QMainWindow, Ui_Main):
    def __init__(self, parent = None):
        super(Main, self).__init__(parent)
        self.setupUi(self)

        self.cad = Cadastro()
        self.tela_Menu.pushButton.clicked.connect(self.abrirTelaCadastro)
        self.tela_Menu.pushButton_2.clicked.connect(self.abrirTelaBusca)

        self.tela_Cadastra.pushButton.clicked.connect(self.botaoCadastra)
        self.tela_Buscar.pushButton.clicked.connect(self.botaoBusca)
    
    def botaoCadastra(self):
        nome = self.tela_Cadastro.lineEdit.text()
        endereco = self.tecla_Cadastro.lineEdit_2.text()
        cpf = self.tela_Cadastra.lineEdit_3.text()
        nascimento = self.tecla_Cadastro.lineEdit_4.text()
        if not(nome == '' or endereco == '' or cpf == '' or nascimento == ''):
            p = Pessoa(nome, endereco, cpf, nascimento)
            if (self.cad.cadastra(p)):
                QMessageBox.information(nome, 'POOII', 'Cadastro realizado com sucesso!')
                self.tela_Cadastra.lineEdit.setText('')
                self.tela_Cadastra.lineEdit_2.setText('')
                self.tela_Cadastra.lineEdit_3.setText('')
                self.tela_Cadastra.lineEdit_4.setText('')
            else:
                QMessageBox.information(None, 'POOII', 'cpf ja cadastrado!')
        else:
            QMessageBox.information(None, 'POOII', 'Todos os valor devem ser preenxidos!')
        
        self.QtStack.setCurrenIndex(0)

    def botaoBusca(self):
        cpf = self.tela_Busca.lineEdit_4.text()
        pessoa = self.cad.busca(cpf)
        if (pessoa != None):
            self.tela_Busca.label.setText(pessoa.nome)
            self.tela_Busca.lineEdit_2.setText(pessoa.endereco)
            self.tela_Busca.lineEdit_3.setText(pessoa.nascimento)
        else:
            QMessageBox.information(None, 'POOII', 'cpf não encontrado!')
        
        self.tela_Busca.pushButton_2.clicked.connect(self.QtStack.setCurrenIndex(0))

    def abrirTelaCadastro(self):
        self.QtStack.setCurrenIndex(1)
    
    def abrirTelaBusca(self):
        self.QtStack.setCurrenIndex(2)

if __name__ == '__main__':
    app =QApplication(sys.argv)
    show_main = Main
    sys.exit(app.exec_())