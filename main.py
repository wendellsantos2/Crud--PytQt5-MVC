import  sys
from PyQt5 import QtWidgets

from Views.ViewPrincipal.viewLogin.tela_login import Ui_LogIn

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LogIn = QtWidgets.QMainWindow()
    ui = Ui_LogIn()
    ui.setupUi(LogIn) 
    LogIn.show()
    sys.exit(app.exec_())
