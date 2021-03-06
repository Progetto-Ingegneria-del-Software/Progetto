from listafatture.view.VistaCreaFatturaCarico import VistaCreaFatturaCarico
from PyQt5 import QtGui
from PyQt5.QtWidgets import QVBoxLayout, QWidget, QLabel, QHBoxLayout, QPushButton

from listafatture.view.VistaCreaFatturaScarico import VistaCreaFatturaScarico

#####################################################################
###   QUESTA CLASSE SERVE PER MOSTRARE ALL'UTENTE L'INTERFACCIA   ###
###        DI SCELTA PER IL TIPO DI FATTURA DA EFFETTUARE         ###
#####################################################################
class VistaScegliFattura(QWidget):
    def __init__(self, controller_articoli, controller, callback, callback_magazzino):
        super(VistaScegliFattura, self).__init__()

        self.callback_magazzino = callback_magazzino
        self.callback = callback
        self.controller_articoli = controller_articoli
        self.controller = controller

        self.v_layout = QVBoxLayout()

        self.testo = QLabel("Che tipo di fattura vuoi creare?")
        self.v_layout.addWidget(self.testo)

        font = QtGui.QFont()
        font.setPixelSize(20)

        self.testo.setFont(font)

        # Font dei bottoni
        btn_font = QtGui.QFont()
        btn_font.setPixelSize(15)

        self.buttons_layout = QHBoxLayout()
        self.carico_btn = QPushButton("Carico")    # Bottone per impostare il tipo Carico
        self.carico_btn.setFont(btn_font)
        self.carico_btn.clicked.connect(self.funzione_carico_btn)  # Al click sul bottone Carico, viene chiamata la funzione apposita
        
        self.scarico_btn = QPushButton("Scarico")  # Bottone per impostare il tipo Scarico
        self.scarico_btn.setFont(btn_font)
        self.scarico_btn.clicked.connect(self.funzione_scarico_btn)  # Al click sul bottone Scarico, viene chiamata la funzione apposita

        self.buttons_layout.addWidget(self.carico_btn)
        self.buttons_layout.addWidget(self.scarico_btn)

        self.v_layout.addLayout(self.buttons_layout)

        self.setLayout(self.v_layout)
        self.resize(350, 150)
        self.setFixedSize(self.size())
        self.setWindowTitle("Scegli fattura")

    #########################################
    ###  FUNZIONE CHE IMPOSTA IL TIPO DI  ### 
    ###        FATTURA SU "CARICO"        ###
    #########################################
    def funzione_carico_btn(self):
        self.vista_crea_fattura_carico = VistaCreaFatturaCarico(self.controller_articoli, self.controller, self.callback, self.callback_magazzino)
        self.vista_crea_fattura_carico.show()
        self.close()

    #########################################
    ###  FUNZIONE CHE IMPOSTA IL TIPO DI  ### 
    ###       FATTURA SU "SCARICO"        ###
    #########################################
    def funzione_scarico_btn(self):
        self.vista_crea_fattura_scarico = VistaCreaFatturaScarico(self.controller_articoli, self.controller, self.callback, self.callback_magazzino)
        self.vista_crea_fattura_scarico.show()
        self.close()