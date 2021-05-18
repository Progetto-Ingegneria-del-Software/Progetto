
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QAction, QTabWidget, QVBoxLayout, QHBoxLayout, QComboBox, QLabel, QSizePolicy, QFrame

from listaarticoli.view.VistaListaArticoli import VistaListaArticoli
from listadipendenti.view.VistaListaDipendenti import VistaListaDipendenti
from listafornitori.view.VistaListaFornitori import VistaListaFornitori
from home.views.logoo import App






'''
class VistaHome(QWidget):
    def __init__(self, parent=None):
        super(VistaHome, self).__init__(parent)


            tabwidget = QTabWidget()
            tabwidget.addTab(label1, "Tab 1")
            tabwidget.addTab(label2, "Tab 2")
            layout.addWidget(tabwidget, 0, 0)


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 tabs - pythonspot.com'
        self.left = 0
        self.top = 0
        self.width = 300
        self.height = 200
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.table_widget = MyTableWidget(self)
        self.setCentralWidget(self.table_widget)

        self.show()


class VistaHome(QWidget):

    def __init__(self):
        super(QWidget, self).__init__()
        self.layout = QVBoxLayout(self)

        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tab1 = QFrame()
        self.tab1.addwidget
        #self.tab2 = QWidget()
        self.tabs.resize(1600, 500)

        # Add tabs
        self.tabs.addTab(self.tab1, "Tab 1")
       # self.tabs.addTab(self.tab2, "Tab 2")

        # Create first tab
        self.tab1.layout = QVBoxLayout(self)
        self.vista_lista_dipendenti = VistaListaDipendenti()
        self.vista_lista_dipendenti.show()
        self.tab1.setLayout(self.tab1.layout)

        # Add tabs to widget
       # self.layout.addWidget(self.tabs)
       # self.setLayout(self.layout)
'''
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




