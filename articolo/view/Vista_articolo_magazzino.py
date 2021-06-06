from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QGridLayout

from articolo.controller.ControlloreArticolo import ControlloreArticolo
from articolo.view.VistaDescrizioneArticolo import VistaDescrizioneArticolo
from articolo.view.Vista_modifica_articolo_magazzino import Vista_modifica_articolo_magazzino

#####################################################################
###   QUESTA CLASSE SERVE PER MOSTRARE ALL'UTENTE L'INTERFACCIA   ###
###        CON I DATI DI UN ARTICOLO PRESENTE IN MAGAZZINO        ###
#####################################################################
class Vista_articolo_magazzino(QWidget):
    def __init__(self, articolo, callback):
        super(Vista_articolo_magazzino, self).__init__()

        self.controller = ControlloreArticolo(articolo)
        self.callback = callback

        v_layout = QVBoxLayout()

        grid_layout = QGridLayout()

        label_stock = QLabel("Quantità: " + str(self.controller.get_stock_articolo()))
        grid_layout.addWidget(label_stock, 0, 0)

        button_stock = QPushButton("Modifica Quantità")
        button_stock.clicked.connect(lambda: self.show_modifica_articolo("Modifica Quantità"))
        grid_layout.addWidget(button_stock, 0, 1)

        button_descrizione = QPushButton("Visualizza Descrizione")
        button_descrizione.clicked.connect(self.show_descrizione_articolo)

        v_layout.addLayout(grid_layout)
        v_layout.addWidget(button_descrizione)
        self.setLayout(v_layout)
        self.resize(400, 100)
        self.setFixedSize(self.size())
        self.setWindowTitle("Articolo " + str(self.controller.get_codice_articolo()))

    #################################################
    ###    METODO USATO PER MOSTRARE ALL'UTENTE   ###
    ###  L'INTERFACCIA DI MODIFICA DELL'ARTICOLO  ###
    #################################################
    def show_modifica_articolo(self, elemento_modifica):
        self.vista_modifica_articolo = Vista_modifica_articolo_magazzino(elemento_modifica, self.controller, self.callback)
        self.vista_modifica_articolo.show()

    #########################################################
    ###       METODO USATO PER MOSTRARE ALL'UTENTE        ###
    ###  L'INTERFACCIA CON LA DESCRIZIONE DELL' ARTICOLO  ###
    #########################################################
    def show_descrizione_articolo(self):
        self.vista_descrizione_articolo = VistaDescrizioneArticolo(self.controller)
        self.vista_descrizione_articolo.show()