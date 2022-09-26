from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

class Alerta:
    def alertaLoginCerto():
        msg = QMessageBox()
        msg.setWindowTitle('Cadastro de usuario')
        msg.setText('Login efetuado ! ')
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setDefaultButton(QMessageBox.Ok) 
        x = msg.exec_()
        
    def alertaLoginErrado():
        msg = QMessageBox()
        msg.setWindowTitle('Cadastro de usuario')
        msg.setText('Login e/ou senha inválido !')
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setDefaultButton(QMessageBox.Ok)
        msg.setInformativeText('Operacão inválida !')
        x = msg.exec_()
        
    def alertaLoginVazio():
        msg = QMessageBox()
        msg.setWindowTitle('Cadastro de usuario')
        msg.setText('Login e/ou senha vazia !')
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setDefaultButton(QMessageBox.Ok)
        msg.setInformativeText('Operacão inválida !')
        x = msg.exec_()    
        
    def alertaExcluir():
        msg = QMessageBox()
        msg.setWindowTitle('Cadastro de usuario')
        msg.setText('Excluido com sucesso !')
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setDefaultButton(QMessageBox.Ok)
        msg.setInformativeText('Excluido !')
        x = msg.exec_()     
        
    def alertaLoginInvalido():
        msg = QMessageBox()
        msg.setWindowTitle('Cadastro de usuario')
        msg.setText('Login e/ou senha inválido !')
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setDefaultButton(QMessageBox.Ok)
        msg.setInformativeText('Operacão inválida !')
        x = msg.exec_()
        
    def alertaLoginExcluido():
        msg = QMessageBox()
        msg.setWindowTitle('Cadastro de usuario')
        msg.setText('Usuário Excluido !')
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setDefaultButton(QMessageBox.Ok)
        msg.setInformativeText('Operacão Efetuada !')
        x = msg.exec_()
        
    def alertaLoginErroExcluir():
        msg = QMessageBox()
        msg.setWindowTitle('Cadastro de usuario')
        msg.setText('Usuário não Excluído !')
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setDefaultButton(QMessageBox.Ok)
        msg.setInformativeText('Operacão inválida !')
        x = msg.exec_()    
        
        
    def alertaLoginCadastrado():
        msg = QMessageBox()
        msg.setWindowTitle('Cadastro de usuario')
        msg.setText('Usuário Cadastrado !')
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setDefaultButton(QMessageBox.Ok)
        x = msg.exec_()     
           
           
    def alertaLoginNaoCadastrado():
        msg = QMessageBox()
        msg.setWindowTitle('Cadastro de usuario')
        msg.setText('Usuário Não Cadastrado !')
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setDefaultButton(QMessageBox.Ok)
        x = msg.exec_()      
        
        
    def alertaLoginCadastradoVazio():
        msg = QMessageBox()
        msg.setWindowTitle('Cadastro de usuario')
        msg.setText('Nao pode vázio !')
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setDefaultButton(QMessageBox.Ok)
       
        x = msg.exec_() 
        
    def alertaConsultaLogin():
        msg = QMessageBox()
        msg.setWindowTitle('Cadastro de usuario')
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setDefaultButton(QMessageBox.Ok)
        msg.setInformativeText('Usuario Existe')
        x = msg.exec_()
        
          
    def alertaConsultaErro():
        msg = QMessageBox()
        msg.setWindowTitle('Cadastro de usuario')
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setDefaultButton(QMessageBox.Ok)
        msg.setInformativeText('Usuario não existe')
        x = msg.exec_()
        
        
    def alertaErro():
        msg = QMessageBox()
        msg.setWindowTitle('Cadastro de usuario')
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setDefaultButton(QMessageBox.Ok)
        msg.setInformativeText('Erro')
        x = msg.exec_()    
        
    def alertaAtualizado():
        msg = QMessageBox()
        msg.setWindowTitle('Cadastro de usuario')
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setDefaultButton(QMessageBox.Ok)
        msg.setInformativeText('Atualizado com sucesso ')
        x = msg.exec_()        
          