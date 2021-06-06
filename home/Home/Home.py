
from PyQt5.QtWidgets import QWidget,QTabWidget, QVBoxLayout

from listaarticoli.controller.ControlloreListaArticoli import ControlloreListaArticoli
from listaarticoli.view.VistaListaArticoli import VistaListaArticoli
from listaarticoli.view.Vista_lista_articoli_magazzino import Vista_lista_articoli_magazzino
from listaclienti.view.Vista_Lista_clienti import Vista_Lista_clienti
from listaclientiPIva.view.Vista_lista_clientipiva import Vista_lista_clientipiva
from listadipendenti.view.VistaListaDipendenti import VistaListaDipendenti
from listafornitori.view.VistaListaFornitori import VistaListaFornitori
from listafatture.view.VistaListaFatture import VistaListaFatture
from listascontrini.view.VistaListaScontrini import VistaListaScontrini
from home.views.VistaHome import VistaHome


##############################################################################
###  QUESTA CLASSE SUDDIVIDE IN TAB LE PRINCIPALI VISTE DELL'APPLICAZIONE  ###
###                   MOSTRANDONE LA HOME ALL'AVVIO                        ###
##############################################################################
class Home(QWidget):
        def __init__(self):
            super(Home, self).__init__()

            self.controller_lista_articoli = ControlloreListaArticoli()
            self.vista_magazzino = Vista_lista_articoli_magazzino(self.controller_lista_articoli)
            self.setWindowTitle("Home")
            self.resize(1600, 600)

            layout = QVBoxLayout()
            self.setLayout(layout)

            tabs = QTabWidget()
            tabs.addTab(self.Home(), "Home")
            tabs.addTab(self.Scontrini(), "Scontrini")
            tabs.addTab(self.Fatture(), "Fatture")
            tabs.addTab(self.Magazzino(), "Magazzino")
            tabs.addTab(self.Articoli(), "Articoli")
            tabs.addTab(self.Clienti(), "Clienti")
            tabs.addTab(self.ClientiPIva(), "Clienti PIVA")
            tabs.addTab(self.Fornitori(), "Fornitori")
            tabs.addTab(self.Dipendenti(), "Dipendenti")


            layout.addWidget(tabs)

        ###################################################
        ###  FUNZIONE CHE RICHIAMA L'IMMAGINE DEL LOGO  ###
        ###                  NELLA HOME                 ###
        ###################################################
        def Home(self):
            """Create the General page UI."""
            generalTab = QWidget()
            layout = QVBoxLayout()
            layout.addWidget(VistaHome())
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


        ###################################################
        ###  FUNZIONE CHE RICHIAMA L'INTERFACCIA DELLA  ###
        ###      LISTA DEGLI ARTICOLI IN MAGAZZINO      ###
        ###################################################
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




