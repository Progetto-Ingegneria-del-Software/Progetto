from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QAction, QTabWidget, QVBoxLayout, \
    QHBoxLayout, QComboBox, QLabel, QSizePolicy, QFrame, QHeaderView

from listaarticoli.view.VistaListaArticoli import VistaListaArticoli
from listadipendenti.view.VistaListaDipendenti import VistaListaDipendenti
from listafornitori.view.VistaListaFornitori import VistaListaFornitori
from home.views.logoo import App

class VistaHome(QWidget):
        def __init__(self, parent=None):
            super(VistaHome, self).__init__(parent)
            self.setWindowTitle("VistaHome")
            self.resize(1600, 600)
            # Create a top-level layout
            layout = QVBoxLayout()
            self.setLayout(layout)

            # Create the tab widget with two tabs
            tabs = QTabWidget()
           # tabs.addTab(self.Bellaraga(), "Bella Raga")
            tabs.addTab(self.prova(), "Logo")
            tabs.addTab(self.Dipendenti(), "Dipendenti")
            tabs.addTab(self.Articoli(), "Articoli")
            tabs.addTab(self.Fornitori(), "Forinitori")

            layout.addWidget(tabs)




        def prova(self):
            """Create the General page UI."""
            generalTab = QWidget()
            layout = QVBoxLayout()
            layout.addWidget(App())
            generalTab.setLayout(layout)
            return generalTab


        def Dipendenti(self):
            """Create the General page UI."""
            generalTab = QWidget()
            layout = QVBoxLayout()



            layout.addWidget(VistaListaDipendenti())

            generalTab.setLayout(layout)
            return generalTab

        def Articoli(self):
            """Create the General page UI."""
            generalTab = QWidget()
            layout = QVBoxLayout()

            layout.addWidget(VistaListaArticoli())

            generalTab.setLayout(layout)
            return generalTab

        def Fornitori(self):
            """Create the General page UI."""
            generalTab = QWidget()
            layout = QVBoxLayout()

            layout.addWidget(VistaListaFornitori())

            generalTab.setLayout(layout)
            return generalTab

'''
class Window(QWidget):
        def __init__(self):
                super().__init__()
                self.title = "PyQt5 Adding Image To Label"
                self.top = 0
                self.left = 0
                self.width = 1600
                self.height = 480
                self.InitWindow()
'''




