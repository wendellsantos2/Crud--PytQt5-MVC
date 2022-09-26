from PyQt5 import QtCore, QtGui, QtWidgets
from Controllers.AbrirTelas import AbrirTelaController
from Controllers.CriarUsuarioController import CriarUsuarioController
from Views.ViewPrincipal.ViewMaster.tela_alterar import Ui_TelaAlterarMaster
 
from Views.ViewPrincipal.ViewMaster.tela_alterar_adm import Ui_TelaAlterarAdm
 
from Views.ViewPrincipal.ViewMaster.tela_consultar import Ui_TelaConsultar
 
from Views.ViewPrincipal.ViewMaster.tela_criar_usuario import Ui_TelaCadastroUsuario
 
from Views.ViewPrincipal.ViewMaster.tela_excluir_adm import Ui_TelaExcluirAdmin

from PyQt5 import QtCore, QtGui, QtWidgets

from Views.ViewPrincipal.ViewMaster.tela_listar_usuario import Ui_TelaListarUsuario
 


class Ui_TelaAdm(object):
        
        
    def __init__(self):
        self.abrir_tela = AbrirTelaController(self)
        self.abrir_login = CriarUsuarioController(self)
               
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(478, 508)
        MainWindow.setStyleSheet("background-color: rgb(0, 80, 121);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(150, 40, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(40, 80, 381, 321))
        self.frame.setStyleSheet("background-color: rgba(0,0,0,0.2)")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.btn_criar = QtWidgets.QPushButton(self.frame)
        self.btn_criar.setGeometry(QtCore.QRect(100, 70, 181, 31))
        self.btn_criar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_criar.setStyleSheet("QPushButton{color: rgb(255, 255, 255); border-radius: 10px; font-size: 16px; background-color:rgb(0, 0, 10);;}\n"
"\n"
"QPushButton:hover{background-color: #fff; color:black}\n"
"\n"
"")
        self.btn_criar.setObjectName("btn_criar")
        self.btn_consultar = QtWidgets.QPushButton(self.frame)
        self.btn_consultar.setGeometry(QtCore.QRect(100, 110, 181, 31))
        self.btn_consultar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_consultar.setStyleSheet("QPushButton{color: rgb(255, 255, 255); border-radius: 10px; font-size: 16px; background-color:rgb(0, 0, 10);;}\n"
"\n"
"QPushButton:hover{background-color: #fff; color:black}\n"
"\n"
"")
        self.btn_consultar.setObjectName("btn_consultar")
        self.btn_listar = QtWidgets.QPushButton(self.frame)
        self.btn_listar.setGeometry(QtCore.QRect(100, 150, 181, 31))
        self.btn_listar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_listar.setStyleSheet("QPushButton{color: rgb(255, 255, 255); border-radius: 10px; font-size: 16px; background-color:rgb(0, 0, 10);;}\n"
"\n"
"QPushButton:hover{background-color: #fff; color:black}\n"
"\n"
"")
        self.btn_listar.setObjectName("btn_listar")
        self.btn_deletar = QtWidgets.QPushButton(self.frame)
        self.btn_deletar.setGeometry(QtCore.QRect(100, 190, 181, 31))
        self.btn_deletar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_deletar.setStyleSheet("QPushButton{color: rgb(255, 255, 255); border-radius: 10px; font-size: 16px; background-color:rgb(0, 0, 10);;}\n"
"\n"
"QPushButton:hover{background-color: #fff; color:black}\n"
"\n"
"")
        self.btn_deletar.setObjectName("btn_deletar")
        self.btn_alterar = QtWidgets.QPushButton(self.frame)
        self.btn_alterar.setGeometry(QtCore.QRect(100, 230, 181, 31))
        self.btn_alterar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_alterar.setStyleSheet("QPushButton{color: rgb(255, 255, 255); border-radius: 10px; font-size: 16px; background-color:rgb(0, 0, 10);;}\n"
"\n"
"QPushButton:hover{background-color: #fff; color:black}\n"
"\n"
"")
        self.btn_alterar.setObjectName("btn_alterar")
        self.btn_sair = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sair.setGeometry(QtCore.QRect(360, 420, 61, 31))
        self.btn_sair.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_sair.setStyleSheet("QPushButton{color: rgb(255, 255, 255); border-radius: 10px; font-size: 16px; background-color:rgb(0, 0, 10);;}\n"
"\n"
"QPushButton:hover{background-color: #fff; color:black}\n"
"\n"
"")
        self.btn_sair.setObjectName("btn_sair")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 478, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.btn_criar.clicked.connect(lambda:self.abrir_tela.abrir_cadastro(Ui_TelaCadastroUsuario))
        self.btn_consultar.clicked.connect(lambda:self.abrir_tela.abrir_consulta(Ui_TelaConsultar))
        self.btn_deletar.clicked.connect(lambda:self.abrir_tela.abrir_deletar_adm(Ui_TelaExcluirAdmin))
        self.btn_alterar.clicked.connect(lambda:self.abrir_tela.abrir_alterar_adm(Ui_TelaAlterarAdm))
        self.btn_listar.clicked.connect(lambda:self.abrir_tela.abrir_listagem_usuario(Ui_TelaListarUsuario))
        self.btn_sair.clicked.connect(lambda:self.abrir_login.sair(MainWindow))
  
      
      
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Tela do Adm"))
        self.btn_criar.setText(_translate("MainWindow", "Criar Usuario"))
        self.btn_consultar.setText(_translate("MainWindow", "Consultar Usuario "))
        self.btn_listar.setText(_translate("MainWindow", "Listar Usuario"))
        self.btn_deletar.setText(_translate("MainWindow", "Deletar Usuario "))
        self.btn_alterar.setText(_translate("MainWindow", "Alterar Usuario "))
        self.btn_sair.setText(_translate("MainWindow", "Logout"))
