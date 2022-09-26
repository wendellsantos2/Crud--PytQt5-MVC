import sys
import os


myDir = os.getcwd()
sys.path.append(myDir)


from PyQt5 import QtCore, QtGui, QtWidgets
from Controllers.LoginController import LoginController
from Views.ViewPrincipal.ViewMaster.tela_master import Ui_TelaMaster


class Ui_LogIn(object):
    
    def __init__(self):
        self.login_controller = LoginController(self)
    
    def setupUi(self, LogIn):
        LogIn.setObjectName("LogIn")
        LogIn.resize(449, 428)
        LogIn.setStyleSheet("background-color: rgb(0, 80, 121);")
        self.label = QtWidgets.QLabel(LogIn)
        self.label.setGeometry(QtCore.QRect(150, 0, 151, 141))
        self.label.setStyleSheet("background-color:None;")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("c:\\Users\\Fadami\\Desktop\\ProjetoCrudOficial\\View\\ui\\../../../../Projetos/Empresas/Transtellini/Icons/icon_title.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(LogIn)
        self.frame.setGeometry(QtCore.QRect(50, 90, 381, 321))
        self.frame.setStyleSheet("background-color: rgba(0,0,0,0.2)")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.btn_login = QtWidgets.QPushButton(self.frame)
        self.btn_login.setGeometry(QtCore.QRect(100, 230, 181, 41))
        self.btn_login.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_login.setStyleSheet("QPushButton{color: rgb(255, 255, 255); border-radius: 10px; font-size: 16px; background-color:rgb(0, 0, 10);;}\n"
"\n"
"QPushButton:hover{background-color: #fff; color:black}\n"
"\n"
"")
        self.btn_login.setObjectName("btn_login")
        self.inpt_senha = QtWidgets.QLineEdit(self.frame)
        self.inpt_senha.setGeometry(QtCore.QRect(60, 140, 251, 31))
        self.inpt_senha.setStyleSheet("color:#fff; font-size: 16px;")
        self.inpt_senha.setText("")
        self.inpt_senha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.inpt_senha.setAlignment(QtCore.Qt.AlignCenter)
        self.inpt_senha.setObjectName("inpt_senha")
        self.inpt_login = QtWidgets.QLineEdit(self.frame)
        self.inpt_login.setGeometry(QtCore.QRect(60, 80, 251, 31))
        self.inpt_login.setStyleSheet("color:#fff; font-size: 16px;")
        self.inpt_login.setText("")
        self.inpt_login.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.inpt_login.setAlignment(QtCore.Qt.AlignCenter)
        self.inpt_login.setObjectName("inpt_login")
        self.label_2 = QtWidgets.QLabel(LogIn)
        self.label_2.setGeometry(QtCore.QRect(50, 40, 381, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(LogIn)
        QtCore.QMetaObject.connectSlotsByName(LogIn)
        LogIn.setTabOrder(self.inpt_senha, self.btn_login)


        self.x = self.btn_login.clicked.connect(lambda:self.login_controller.logIn(self.inpt_login.text(),self.inpt_senha.text(),Ui_TelaMaster,LogIn))

    def retranslateUi(self, LogIn):
        _translate = QtCore.QCoreApplication.translate
        LogIn.setWindowTitle(_translate("Login", "Form"))
        self.btn_login.setText(_translate("Login", "LOGIN"))
        self.inpt_senha.setPlaceholderText(_translate("Login", "Senha"))
        self.inpt_login.setPlaceholderText(_translate("Login", "login"))
        self.label_2.setText(_translate("Login", "Sistema de cadastro e permissao"))
        
 