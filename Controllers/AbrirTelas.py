from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5 import QtCore, QtGui, QtWidgets
from Database.Connection import Conexao

from Models.User import User
 
 

class AbrirTelaController:
    def __init__(self, criar_usuario):
        self.usuario = User(Conexao())
        self.criar_usuario = criar_usuario
    
    def abrir_cadastro(self, Ui_TelaCriarMaster):
        self.criar_usuario.Form = QtWidgets.QMainWindow()
        self.criar_usuario.ui = Ui_TelaCriarMaster()
        self.criar_usuario.ui.setupUi(self.criar_usuario.Form)
        self.criar_usuario.Form.show()
        
        
    def abrir_consulta(self, Ui_TelaConsultar):
        self.criar_usuario.Form = QtWidgets.QMainWindow()
        self.criar_usuario.ui = Ui_TelaConsultar()
        self.criar_usuario.ui.setupUi(self.criar_usuario.Form)
        self.criar_usuario.Form.show()
        
    def abrir_deletar_adm(self, Ui_TelaExcluirAdm):
        self.criar_usuario.Form = QtWidgets.QMainWindow()
        self.criar_usuario.ui = Ui_TelaExcluirAdm()
        self.criar_usuario.ui.setupUi(self.criar_usuario.Form)
        self.criar_usuario.Form.show()  
        
        
    def abrir_deletar_master(self, Ui_TelaExcluir):
        self.criar_usuario.Form = QtWidgets.QMainWindow()
        self.criar_usuario.ui = Ui_TelaExcluir()
        self.criar_usuario.ui.setupUi(self.criar_usuario.Form)
        self.criar_usuario.Form.show()  
        
   
        
    def abrir_alterar(self, Ui_TelaAlterarMaster):
        self.criar_usuario.Form = QtWidgets.QMainWindow()
        self.criar_usuario.ui = Ui_TelaAlterarMaster()
        self.criar_usuario.ui.setupUi(self.criar_usuario.Form)
        self.criar_usuario.Form.show()  
        
    def abrir_alterar_adm(self, Ui_TelaAlterar):
        self.criar_usuario.Form = QtWidgets.QMainWindow()
        self.criar_usuario.ui = Ui_TelaAlterar()
        self.criar_usuario.ui.setupUi(self.criar_usuario.Form)
        self.criar_usuario.Form.show()      
   
    def abrir_listagem(self, Ui_TelaListarMaster):
        self.criar_usuario.Form = QtWidgets.QMainWindow()
        self.criar_usuario.ui = Ui_TelaListarMaster()
        self.criar_usuario.ui.setupUi(self.criar_usuario.Form)
        self.criar_usuario.Form.show()   
    
    def abrir_listagem_usuario(self, Ui_TelaListarUsuario ):
        self.criar_usuario.Form = QtWidgets.QMainWindow()
        self.criar_usuario.ui = Ui_TelaListarUsuario()
        self.criar_usuario.ui.setupUi(self.criar_usuario.Form)
        self.criar_usuario.Form.show()            
           
     
    def abrir_tela_adm(self, Ui_TelaAdm):
        self.criar_usuario.Form = QtWidgets.QMainWindow()
        self.criar_usuario.ui = Ui_TelaAdm()
        self.criar_usuario.ui.setupUi(self.criar_usuario.Form)
        self.criar_usuario.Form.show()
        
    def abrir_tela_alterar_adm(self, Ui_TelaAlterarAdm):
        self.criar_usuario.Form = QtWidgets.QMainWindow()
        self.criar_usuario.ui = Ui_TelaAlterarAdm()
        self.criar_usuario.ui.setupUi(self.criar_usuario.Form)
        self.criar_usuario.Form.show()
        
    def abrir_tela_alterar_adm(self, Ui_TelaAlterarAdm):
        self.criar_usuario.Form = QtWidgets.QMainWindow()
        self.criar_usuario.ui = Ui_TelaAlterarAdm()
        self.criar_usuario.ui.setupUi(self.criar_usuario.Form)
        self.criar_usuario.Form.show()         