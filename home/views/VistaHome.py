
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QAction, QTabWidget, QVBoxLayout, \
    QHBoxLayout, QComboBox, QLabel, QSizePolicy, QFrame, QHeaderView

from listaarticoli.controller.ControlloreListaArticoli import ControlloreListaArticoli
from listaarticoli.view.VistaListaArticoli import VistaListaArticoli
from listaarticoli.view.Vista_lista_articoli_magazzino import Vista_lista_articoli_magazzino
from listaclienti.view.Vista_Lista_clienti import Vista_Lista_clienti
from listaclientiPIva.view.Vista_lista_clientipiva import Vista_lista_clientipiva
from listadipendenti.view.VistaListaDipendenti import VistaListaDipendenti
from listafornitori.view.VistaListaFornitori import VistaListaFornitori
from listafatture.view.VistaListaFatture import VistaListaFatture
from listascontrini.view.VistaListaScontrini import VistaListaScontrini
from listascontrini.view.VistaCreaScontrino import VistaCreaScontrino
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

            self.controller_lista_articoli = ControlloreListaArticoli()
            self.vista_magazzino = Vista_lista_articoli_magazzino(self.controller_lista_articoli)
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
            tabs.addTab(self.Magazzino(), "Magazzino")
            tabs.addTab(self.Fornitori(), "Fornitori")
            tabs.addTab(self.Clienti(), "Clienti")
            tabs.addTab(self.ClientiPIva(), "Clienti PIVA")
            tabs.addTab(self.Fatture(), "Fatture")
            tabs.addTab(self.Scontrini(), "Scontrini")

            layout.addWidget(tabs)




        def prova(self):
            """Create the General page UI."""
            generalTab = QWidget()
            layout = QVBoxLayout()
            layout.addWidget(App())
            generalTab.setLayout(layout)
            return generalTab


        ###################################################
        ###  FUNZIONE CHE RICHIAMA L'INTERFACCIA DELLA  ###
        ###            LISTA DEI DIPENDENTI             ###
        ###################################################
        def Dipendenti(self):
            """Create the General page UI."""
            generalTab = QWidget()
            layout = QVBoxLayout()



            layout.addWidget(VistaListaDipendenti())

            generalTab.setLayout(layout)
            return generalTab


        ###################################################
        ###  FUNZIONE CHE RICHIAMA L'INTERFACCIA DELLA  ###
        ###            LISTA DEGLI ARTICOLI             ###
        ###################################################
        def Articoli(self):
            """Create the General page UI."""
            generalTab = QWidget()
            layout = QVBoxLayout()

            layout.addWidget(VistaListaArticoli(self.controller_lista_articoli, self.vista_magazzino.update_table_view))

            generalTab.setLayout(layout)
            return generalTab

        def Magazzino(self):
            """Create the General page UI."""
            generalTab = QWidget()
            layout = QVBoxLayout()



            layout.addWidget(self.vista_magazzino)


            generalTab.setLayout(layout)
            return generalTab


        ###################################################
        ###  FUNZIONE CHE RICHIAMA L'INTERFACCIA DELLA  ###
        ###             LISTA DEI FORNITORI             ###
        ###################################################
        def Fornitori(self):
            """Create the General page UI."""
            generalTab = QWidget()
            layout = QVBoxLayout()

            layout.addWidget(VistaListaFornitori())

            generalTab.setLayout(layout)
            return generalTab
        
        
        ###################################################
        ###  FUNZIONE CHE RICHIAMA L'INTERFACCIA DELLA  ###
        ###      LISTA DEI CLIENTI CON PARTITA IVA      ###
        ###################################################
        def ClientiPIva(self):
            """Create the General page UI."""
            generalTab = QWidget()
            layout = QVBoxLayout()

            layout.addWidget(Vista_lista_clientipiva())

            generalTab.setLayout(layout)

            return generalTab 
        
        
        ###################################################
        ###  FUNZIONE CHE RICHIAMA L'INTERFACCIA DELLA  ###
        ###         LISTA DEI CLIENTI PRIVATI           ###
        ###################################################
        def Clienti(self):
            """Create the General page UI."""
            generalTab = QWidget()
            layout = QVBoxLayout()

            layout.addWidget(Vista_Lista_clienti())

            generalTab.setLayout(layout)
            return generalTab

        
        ###################################################
        ###  FUNZIONE CHE RICHIAMA L'INTERFACCIA DELLA  ###
        ###             LISTA DELLE FATTURE             ###
        ###################################################
        def Fatture(self):
            generalTab = QWidget()
            layout = QVBoxLayout()

            layout.addWidget(VistaListaFatture(self.controller_lista_articoli, self.vista_magazzino.update_table_view))

            generalTab.setLayout(layout)
            return generalTab


        ###################################################
        ###  FUNZIONE CHE RICHIAMA L'INTERFACCIA DELLA  ###
        ###             LISTA DELLE FATTURE             ###
        ###################################################
        def Scontrini(self):
            generalTab = QWidget()
            layout = QVBoxLayout()

            layout.addWidget(VistaListaScontrini(self.controller_lista_articoli, self.vista_magazzino.update_table_view))

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




