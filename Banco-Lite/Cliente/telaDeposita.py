# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'telaDeposita.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Tela_Depositar(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(352, 314)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 30, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.botao_depositar = QtWidgets.QPushButton(self.centralwidget)
        self.botao_depositar.setGeometry(QtCore.QRect(230, 130, 75, 23))
        self.botao_depositar.setObjectName("botao_depositar")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(260, 250, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.input_deposito = QtWidgets.QLineEdit(self.centralwidget)
        self.input_deposito.setGeometry(QtCore.QRect(20, 130, 201, 20))
        self.input_deposito.setObjectName("input_deposito")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Depositar"))
        self.botao_depositar.setText(_translate("MainWindow", "Depositar"))
        self.pushButton.setText(_translate("MainWindow", "Voltar"))
        self.input_deposito.setPlaceholderText(_translate("MainWindow", "Valor do deposito"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Tela_Depositar()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
