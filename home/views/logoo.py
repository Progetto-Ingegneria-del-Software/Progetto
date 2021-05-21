import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QSizePolicy
from PyQt5.QtGui import QIcon, QPixmap


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 image - pythonspot.com'
        self.left = 0
        self.top = 0
        self.width = 1600
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create widget
        label = QLabel(self)
        label.setScaledContents(True)
        pixmap = QPixmap("home/logo/logo.png").scaled(1600, 480, QtCore.Qt.KeepAspectRatio)
        label.setPixmap(pixmap)
        label.resize(label.pixmap().size())
        self.resize(pixmap.width(), pixmap.height())
