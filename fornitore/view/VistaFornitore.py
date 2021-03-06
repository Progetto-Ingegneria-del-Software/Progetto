from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QLabel, QPushButton, QMessageBox

from fornitore.control.ControlloreFornitore import ControlloreFornitore
from fornitore.view.VistaModificaFornitore import VistaModificaFornitore

#####################################################################
###   QUESTA CLASSE SERVE PER MOSTRARE ALL'UTENTE L'INTERFACCIA   ###
###        CON I DATI DI UN FORNITORE PRESENTE NEL SISTEMA        ###
#####################################################################
class VistaFornitore(QWidget):
    def __init__(self, fornitore, controller_fornitore, callback):
        super(VistaFornitore, self).__init__()

        self.controller = ControlloreFornitore(fornitore)
        self.controller_fornitore = controller_fornitore
        self.callback = callback

        v_layout = QVBoxLayout()

        grid_layout = QGridLayout()

        label_codice_id = QLabel("Codice ID: " + str(self.controller.get_codice_id_fornitore()))
        grid_layout.addWidget(label_codice_id, 0, 0)

        self.label_ragione_sociale = QLabel("Ragione Sociale: " + str(self.controller.get_ragione_sociale_fornitore()))
        grid_layout.addWidget(self.label_ragione_sociale, 1, 0)

        button_modifica_ragione_sociale = QPushButton("Modifica Ragione Sociale")
        button_modifica_ragione_sociale.clicked.connect(lambda: self.show_modifica_fornitore("Modifica Ragione Sociale"))
        grid_layout.addWidget(button_modifica_ragione_sociale, 1, 1)

        self.label_partita_iva = QLabel("Partita IVA: " + str(self.controller.get_partita_iva_fornitore()))
        grid_layout.addWidget(self.label_partita_iva, 2, 0)

        button_modifica_partita_iva = QPushButton("Modifica Partita IVA")
        button_modifica_partita_iva.clicked.connect(lambda: self.show_modifica_fornitore("Modifica Partita IVA"))
        grid_layout.addWidget(button_modifica_partita_iva, 2, 1)

        self.label_citta = QLabel("Città: " + str(self.controller.get_citta_fornitore()))
        grid_layout.addWidget(self.label_citta, 3, 0)

        button_modifica_citta = QPushButton("Modifica Città")
        button_modifica_citta.clicked.connect(lambda: self.show_modifica_fornitore("Modifica Città"))
        grid_layout.addWidget(button_modifica_citta, 3, 1)

        self.label_indirizzo = QLabel("Indirizzo: " + str(self.controller.get_indirizzo_fornitore()))
        grid_layout.addWidget(self.label_indirizzo, 4, 0)

        button_modifica_indirizzo = QPushButton("Modifica Indirizzo")
        button_modifica_indirizzo.clicked.connect(lambda: self.show_modifica_fornitore("Modifica Indirizzo"))
        grid_layout.addWidget(button_modifica_indirizzo, 4, 1)

        self.label_telefono = QLabel("Telefono: " + str(self.controller.get_telefono_fornitore()))
        grid_layout.addWidget(self.label_telefono, 5, 0)

        button_modifica_telefono = QPushButton("Modifica Telefono")
        button_modifica_telefono.clicked.connect(lambda: self.show_modifica_fornitore("Modifica Telefono"))
        grid_layout.addWidget(button_modifica_telefono, 5, 1)

        self.label_email = QLabel("Email: " + str(self.controller.get_email_fornitore()))
        grid_layout.addWidget(self.label_email, 6, 0)

        button_modifica_email = QPushButton("Modifica Email")
        button_modifica_email.clicked.connect(lambda: self.show_modifica_fornitore("Modifica Email"))
        grid_layout.addWidget(button_modifica_email, 6, 1)

        v_layout.addLayout(grid_layout)
        button_elimina_fornitore = QPushButton("Elimina Fornitore " + str(self.controller.get_codice_id_fornitore()))
        button_elimina_fornitore.clicked.connect(self.delete_fornitore)
        v_layout.addWidget(button_elimina_fornitore)

        self.setLayout(v_layout)
        self.resize(600, 350)
        self.setFixedSize(self.size())
        self.setWindowTitle("Fornitore " + str(self.controller.get_codice_id_fornitore()))

    ########################################################
    ###    METODO USATO PER FAR CAMBIARE DINAMICAMENTE   ###
    ###   LA VISTA DI UN ARTICOLO, A MODIFICA AVVENUTA   ###
    ########################################################
    def update_info_view(self):
        self.label_ragione_sociale.setText("Ragione Sociale: " + str(self.controller.get_ragione_sociale_fornitore()))
        self.label_partita_iva.setText("Partita IVA: " + str(self.controller.get_partita_iva_fornitore()))
        self.label_citta.setText("Città: " + str(self.controller.get_citta_fornitore()))
        self.label_indirizzo.setText("Indirizzo: " + str(self.controller.get_indirizzo_fornitore()))
        self.label_telefono.setText("Telefono: " + str(self.controller.get_telefono_fornitore()))
        self.label_email.setText("Email: " + str(self.controller.get_email_fornitore()))

    ###################################################
    ###    METODO USATO PER ELIMINARE UN FORNITORE  ###
    ###   PRESENTE NEL SISTEMA DOPO AVER CLICCATO   ###
    ###          SUL CORRISPONDENTE BOTTONE         ###
    ###################################################
    def delete_fornitore(self):
        delete_view = QMessageBox.warning(self, 'Vuoi davvero eliminare il fornitore ' + str(self.controller.get_codice_id_fornitore()) + '?',
                                          'Il fornitore ' + str(self.controller.get_codice_id_fornitore()) + ' sarà permanentemente eliminato dal sistema.\nVuoi continuare?',
                                          QMessageBox.Yes,
                                          QMessageBox.No)
        if delete_view == QMessageBox.Yes:
            self.controller_fornitore.elimina_fornitore_by_id(self.controller.get_codice_id_fornitore())
            self.callback()
            self.close()

    #################################################
    ###    METODO USATO PER MOSTRARE ALL'UTENTE   ###
    ###  L'INTERFACCIA DI MODIFICA DEL FORNITORE  ###
    #################################################
    def show_modifica_fornitore(self, elemento_modifica):
        self.vista_modifica_fornitore= VistaModificaFornitore(elemento_modifica, self.controller, self.controller_fornitore, self.callback, self.update_info_view)
        self.vista_modifica_fornitore.show()
