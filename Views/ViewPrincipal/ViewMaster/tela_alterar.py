# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_alterar.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from Controllers.CriarUsuarioController import CriarUsuarioController


class Ui_TelaAlterarMaster(object):
    
    def __init__(self):
        self.usuario_criar_controller = CriarUsuarioController(self)
               
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(523, 488)
        MainWindow.setStyleSheet("background-color: rgb(0, 80, 121);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.table_product = QtWidgets.QTableWidget(self.centralwidget)
        self.table_product.setGeometry(QtCore.QRect(40, 40, 441, 335))
        self.table_product.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.table_product.setRowCount(10)
        self.table_product.setObjectName("table_product")
        self.table_product.setColumnCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.table_product.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_product.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_product.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_product.setHorizontalHeaderItem(3, item)
        self.btn_voltar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_voltar.setGeometry(QtCore.QRect(390, 400, 91, 31))
        self.btn_voltar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_voltar.setStyleSheet("QPushButton{color: rgb(255, 255, 255); border-radius: 10px; font-size: 16px; background-color:rgb(0, 0, 10);;}\n"
"\n"
"QPushButton:hover{background-color: #fff; color:black}\n"
"\n"
"")
        self.btn_voltar.setObjectName("btn_voltar")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 0, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.btn_atualizar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_atualizar.setGeometry(QtCore.QRect(60, 390, 91, 31))
        self.btn_atualizar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_atualizar.setStyleSheet("QPushButton{color: rgb(255, 255, 255); border-radius: 10px; font-size: 16px; background-color:rgb(0, 0, 10);;}\n"
"\n"
"QPushButton:hover{background-color: #fff; color:black}\n"
"\n"
"")
        self.btn_atualizar.setObjectName("btn_atualizar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 523, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
  
        self.usuario_criar_controller.listar_todos()
        self.btn_atualizar.clicked.connect(lambda:self.usuario_criar_controller.atualizar_usuario_master())
        self.btn_voltar.clicked.connect(lambda:self.usuario_criar_controller.sair(MainWindow))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.table_product.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.table_product.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "LOGIN"))
        item = self.table_product.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "SENHA"))
        item = self.table_product.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "PERMISS??O"))
        self.btn_voltar.setText(_translate("MainWindow", "Voltar"))
        self.label.setText(_translate("MainWindow", "Alterar Usu??rio"))
        self.btn_atualizar.setText(_translate("MainWindow", "Atualizar"))
