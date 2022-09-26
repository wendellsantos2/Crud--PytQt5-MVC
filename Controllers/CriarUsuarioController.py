import sys
import os

 
 
myDir = os.getcwd()
sys.path.append(myDir)
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5 import QtCore, QtGui, QtWidgets
from Database.Connection import Conexao
from Models.User import User
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from Database.Connection import Conexao
from Models.User import User
from QMessageBox.Alerta import Alerta 

class CriarUsuarioController():
    def __init__(self, criar_usuario):
        self.usuario = User(Conexao())
        self.criar_usuario = criar_usuario
         
         
    def criar_usuario_adm(self,login,c_senha,senha, MainWindow):
            if len(login)==0 or len(senha)==0  :
             Alerta.alertaLoginVazio()
            elif senha != c_senha:
               Alerta.alertaLoginInvalido()
            else:
                self.usuario.inserir_usuario(login,senha) 
                Alerta.alertaLoginCadastrado()
                MainWindow.hide()
                
                
    def criar_usuario_master(self,login,c_senha,senha,permissao, MainWindow):
            if len(login)==0 or len(senha)==0  :
                Alerta.alertaLoginCadastradoVazio()
            elif senha != c_senha:
                Alerta.alertaLoginInvalido()
            else:
                self.usuario.inserir_usuario_master(login,senha,permissao) 
                Alerta.alertaLoginCadastrado()
                MainWindow.hide()
    
    def consultar_usuario(self,login,MainWindow):
            try:
                if login:
                    user = self.usuario.consultar_usuario(login)
                    if user[1] == login :
                        Alerta.alertaConsultaLogin() 
            except:
                    Alerta.alertaConsultaErro()
            
    def listar_adm(self):
        tela = self.criar_usuario.table_product
        usuarios = self.usuario.listar_adm()
        tela.setRowCount(0)
        for linha, coluna in enumerate(usuarios):
            tela.insertRow(linha)
            for numero_coluna, dado in enumerate(coluna):
                tela.setItem(linha, numero_coluna, QtWidgets.QTableWidgetItem(str(dado)))        
                
    def listar_todos(self):
        tela = self.criar_usuario.table_product
        usuarios = self.usuario.listar_todos()
        tela.setRowCount(0)
        for linha, coluna in enumerate(usuarios):
            tela.insertRow(linha)
            for numero_coluna, dado in enumerate(coluna):
                tela.setItem(linha, numero_coluna, QtWidgets.QTableWidgetItem(str(dado)))
                    
                
    def listar_usuarios(self):
        tela = self.criar_usuario.table_product
        usuarios = self.usuario.listar_usuario()
        tela.setRowCount(0)
        for linha, coluna in enumerate(usuarios):
            tela.insertRow(linha)
            for numero_coluna, dado in enumerate(coluna):
                tela.setItem(linha, numero_coluna, QtWidgets.QTableWidgetItem(str(dado)))            
    
    def listar_usuario_permissao(self):
        tela = self.criar_usuario.table_product
        usuarios = self.usuario.listar_usuario_permissao()
        tela.setRowCount(0)
        for linha, coluna in enumerate(usuarios):
            tela.insertRow(linha)
            for numero_coluna, dado in enumerate(coluna):
                tela.setItem(linha, numero_coluna, QtWidgets.QTableWidgetItem(str(dado))) 
    
    
    
    def excluir_adm(self):
        try:  
            tela = self.criar_usuario.table_product
            if tela.currentItem() != None: 
                usuario = tela.currentItem().text()
                self.usuario.deletar_usuario(usuario)
                Alerta.alertaExcluir()
                self.listar_adm()
          
        except:  
                Alerta.alertaErro()
        
    def atualizar_usuario(self):
        table = self.criar_usuario.table_product
        usuarios = []
        fila = []
        for row_number in range(table.rowCount()):
            for column_number in range(table.columnCount()):
                if table.item(row_number,column_number) != None:
                    fila.append(table.item(row_number,column_number).text())
            if len(fila)>0:
                usuarios.append(fila)
            fila = []
        
        if len(usuarios)>0:
            for usuario in usuarios:
                self.usuario.atualizar_tela_adm(usuario[0],usuario[1],usuario[2])
                Alerta.alertaAtualizado()
              
             
    def atualizar_usuario_master(self):
        table = self.criar_usuario.table_product
        usuarios = []
        fila = []
        for row_number in range(table.rowCount()):
            for column_number in range(table.columnCount()):
                if table.item(row_number,column_number) != None:
                    fila.append(table.item(row_number,column_number).text())
            if len(fila)>0:
                usuarios.append(fila)
            fila = []
        if len(usuarios)>0:
            for usuario in usuarios:
                self.usuario.atualizar_usuario_master(usuario[0],usuario[1],usuario[2],usuario[3])
            Alerta.alertaAtualizado()
 
    def sair(self,MainWindow):
        MainWindow.close()
        
 