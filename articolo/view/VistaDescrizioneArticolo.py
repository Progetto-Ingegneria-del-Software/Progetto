from PyQt5.QtWidgets import QWidget, QLabel, QHBoxLayout

#############################################################################
###       QUESTA CLASSE SERVE PER MOSTRARE ALL'UTENTE L'INTERFACCIA       ###
###  CON ALL'INTERNO LA DESCRIZIONE DI UN ARTICOLO PRESENTE IN MAGAZZINO  ###
#############################################################################
class VistaDescrizioneArticolo(QWidget):
    def __init__(self, controller):
        super(VistaDescrizioneArticolo, self).__init__()

        self.controller = controller

        layout = QHBoxLayout()
        descrizione_label = QLabel("Descrizione:\n\n" + self.controller.get_descrizione_articolo())
        layout.addWidget(descrizione_label)
        self.setLayout(layout)
        self.resize(450, 100)
        self.setFixedSize(self.size())
        self.setWindowTitle("Descrizione Articolo " + str(controller.get_codice_articolo()))