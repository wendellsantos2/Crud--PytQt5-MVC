 

from PyQt5 import QtCore, QtGui, QtWidgets

from Controllers.CriarUsuarioController import CriarUsuarioController
from Controllers.MyDelegate import MyDelegate


class Ui_TelaListarUsuario(object):
    
    def __init__(self):
        self.usuario_criar_controller = CriarUsuarioController(self)
          
                     
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(465, 491)
        MainWindow.setStyleSheet("background-color: rgb(0, 80, 121);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 0, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.table_product = QtWidgets.QTableWidget(self.centralwidget)
        self.table_product.setGeometry(QtCore.QRect(70, 40, 331, 335))
        self.table_product.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.table_product.setRowCount(10)
        self.table_product.setObjectName("table_product")
        self.table_product.setColumnCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.table_product.setItemDelegateForColumn(0,MyDelegate())
        self.table_product.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_product.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_product.setHorizontalHeaderItem(2, item)
        self.btn_sair = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sair.setGeometry(QtCore.QRect(300, 400, 91, 31))
        self.btn_sair.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_sair.setStyleSheet("QPushButton{color: rgb(255, 255, 255); border-radius: 10px; font-size: 16px; background-color:rgb(0, 0, 10);;}\n"
"\n"
"QPushButton:hover{background-color: #fff; color:black}\n"
"\n"
"")
        self.btn_sair.setObjectName("btn_sair")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 465, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
         
        self.usuario_criar_controller.listar_usuarios()
        self.btn_sair.clicked.connect(lambda:self.usuario_criar_controller.sair(MainWindow))
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Tela do Usuario"))
        item = self.table_product.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.table_product.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "LOGIN"))
        item = self.table_product.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "PERMISSÃO"))
        self.btn_sair.setText(_translate("MainWindow", "Sair"))
