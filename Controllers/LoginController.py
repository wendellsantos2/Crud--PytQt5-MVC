import sys
import os




myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5 import QtWidgets
from Database.Connection import Conexao
from Models.User import User
from Views.ViewPrincipal.ViewUsuario.tela_usuario import Ui_TelaUsuario
from Views.ViewPrincipal.ViewMaster.tela_adm import Ui_TelaAdm
from QMessageBox.Alerta import Alerta 
class LoginController():
    
    def __init__(self, log_in):
        self.user = User(Conexao())
        self.log_in = log_in
    def logIn(self,login,senha, Ui_TelaMaster, LogIn):
        try:    
            if login and senha:
                user = self.user.getUser(login,senha)       
            elif user[3] == 4:
                LogIn.hide()
                self.log_in.Form = QtWidgets.QMainWindow()
                self.log_in.ui = Ui_TelaMaster()
                self.log_in.ui.setupUi(self.log_in.Form)
                self.log_in.Form.show()
                Alerta.alertaLoginCerto()
                return
            elif user[3] == 3:
                LogIn.hide()
                self.log_in.Form = QtWidgets.QMainWindow()
                self.log_in.ui = Ui_TelaAdm()
                self.log_in.ui.setupUi(self.log_in.Form)
                self.log_in.Form.show()
                Alerta.alertaLoginCerto()
                return
            elif user[3] == 5:
                LogIn.hide()
                self.log_in.Form = QtWidgets.QMainWindow()
                self.log_in.ui = Ui_TelaUsuario()
                self.log_in.ui.setupUi(self.log_in.Form)
                self.log_in.Form.show()
                Alerta.alertaLoginCerto()
                return
        except:
                Alerta.alertaLoginErrado()
