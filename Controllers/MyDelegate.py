
from PyQt5 import QtCore, QtGui, QtWidgets
class MyDelegate(QtWidgets.QItemDelegate):

    def createEditor(self, *args):
        return None