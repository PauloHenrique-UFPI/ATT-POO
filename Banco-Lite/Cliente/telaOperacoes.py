# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'telaOperacoes.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Tela_Operacoes(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(335, 287)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 10, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.botao_sacar = QtWidgets.QPushButton(self.centralwidget)
        self.botao_sacar.setGeometry(QtCore.QRect(170, 100, 75, 23))
        self.botao_sacar.setObjectName("botao_sacar")
        self.botao_depositar = QtWidgets.QPushButton(self.centralwidget)
        self.botao_depositar.setGeometry(QtCore.QRect(90, 100, 75, 23))
        self.botao_depositar.setObjectName("botao_depositar")
        self.botao_transferir = QtWidgets.QPushButton(self.centralwidget)
        self.botao_transferir.setGeometry(QtCore.QRect(90, 130, 75, 23))
        self.botao_transferir.setObjectName("botao_transferir")
        self.botao_historico = QtWidgets.QPushButton(self.centralwidget)
        self.botao_historico.setGeometry(QtCore.QRect(130, 160, 75, 23))
        self.botao_historico.setObjectName("botao_historico")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(260, 240, 75, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.input_conta = QtWidgets.QLineEdit(self.centralwidget)
        self.input_conta.setGeometry(QtCore.QRect(110, 60, 113, 20))
        self.input_conta.setObjectName("input_conta")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(170, 130, 75, 23))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Operacoes"))
        self.botao_sacar.setText(_translate("MainWindow", "Sacar"))
        self.botao_depositar.setText(_translate("MainWindow", "Depositar"))
        self.botao_transferir.setText(_translate("MainWindow", "Trasferir"))
        self.botao_historico.setText(_translate("MainWindow", "Historico"))
        self.pushButton_5.setText(_translate("MainWindow", "Voltar"))
        self.input_conta.setPlaceholderText(_translate("MainWindow", "Id da conta"))
        self.pushButton.setText(_translate("MainWindow", "Extrato"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Tela_Operacoes()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
