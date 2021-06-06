from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtGui import QPixmap

#####################################################
###  QUESTA CLASSE MOSTRA LA FINESTRA DELLA HOME  ###
###             CON IL RELATIVO LOGO              ###
#####################################################
class VistaHome(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 image - pythonspot.com'
        self.left = 0
        self.top = 0
        self.width = 1600
        self.height = 480
        self.show_logo()

    def show_logo(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        label = QLabel(self)
        label.setScaledContents(True)
        pixmap = QPixmap("home/logo/Logo Progetto.png").scaled(1550, 480, QtCore.Qt.KeepAspectRatio)
        label.setPixmap(pixmap)
        label.resize(label.pixmap().size())
        self.resize(pixmap.width(), pixmap.height())
