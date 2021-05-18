from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QLabel, QPushButton, QMessageBox

from fornitore.control.ControlloreFornitore import ControlloreFornitore
from fornitore.view.VistaModificaFornitore import VistaModificaFornitore


class VistaFornitore(QWidget):
    def __init__(self, fornitore, elimina_fornitore, callback):
        super(VistaFornitore, self).__init__()

        self.controller = ControlloreFornitore(fornitore)
        self.elimina_fornitore = elimina_fornitore
        self.callback = callback

        v_layout = QVBoxLayout()

        grid_layout = QGridLayout()

        label_codice_id = QLabel("Codice ID: " + str(self.controller.get_codice_id_fornitore()))
        grid_layout.addWidget(label_codice_id, 0, 0)

        label_ragione_sociale = QLabel("Ragione Sociale: " + str(self.controller.get_ragione_sociale_fornitore()))
        grid_layout.addWidget(label_ragione_sociale, 1, 0)

        button_modifica_ragione_sociale = QPushButton("Modifica Ragione Sociale")
        button_modifica_ragione_sociale.clicked.connect(lambda: self.show_modifica_fornitore("Modifica Ragione Sociale"))
        grid_layout.addWidget(button_modifica_ragione_sociale, 1, 1)

        label_partita_iva = QLabel("Partita IVA: " + str(self.controller.get_partita_iva_fornitore()))
        grid_layout.addWidget(label_partita_iva, 2, 0)

        button_modifica_partita_iva = QPushButton("Modifica Partita IVA")
        button_modifica_partita_iva.clicked.connect(lambda: self.show_modifica_fornitore("Modifica Partita IVA"))
        grid_layout.addWidget(button_modifica_partita_iva, 2, 1)

        label_citta = QLabel("Città: " + str(self.controller.get_citta_fornitore()))
        grid_layout.addWidget(label_citta, 3, 0)

        button_modifica_citta = QPushButton("Modifica Città")
        button_modifica_citta.clicked.connect(lambda: self.show_modifica_fornitore("Modifica Città"))
        grid_layout.addWidget(button_modifica_citta, 3, 1)

        label_indirizzo = QLabel("Indirizzo: " + str(self.controller.get_indirizzo_fornitore()))
        grid_layout.addWidget(label_indirizzo, 4, 0)

        button_modifica_indirizzo = QPushButton("Modifica Indirizzo")
        button_modifica_indirizzo.clicked.connect(lambda: self.show_modifica_fornitore("Modifica Indirizzo"))
        grid_layout.addWidget(button_modifica_indirizzo, 4, 1)

        label_telefono = QLabel("Telefono: " + str(self.controller.get_telefono_fornitore()))
        grid_layout.addWidget(label_telefono, 5, 0)

        button_modifica_telefono = QPushButton("Modifica Telefono")
        button_modifica_telefono.clicked.connect(lambda: self.show_modifica_fornitore("Modifica Telefono"))
        grid_layout.addWidget(button_modifica_telefono, 5, 1)

        label_email = QLabel("Email: " + str(self.controller.get_email_fornitore()))
        grid_layout.addWidget(label_email, 6, 0)

        button_modifica_email = QPushButton("Modifica Email")
        button_modifica_email.clicked.connect(lambda: self.show_modifica_fornitore("Modifica Email"))
        grid_layout.addWidget(button_modifica_email, 6, 1)

        v_layout.addLayout(grid_layout)
        button_elimina_fornitore = QPushButton("Elimina Fornitore " + str(self.controller.get_codice_id_fornitore()))
        button_elimina_fornitore.clicked.connect(self.delete_fornitore)
        v_layout.addWidget(button_elimina_fornitore)

        self.setLayout(v_layout)
        self.resize(500, 400)
        self.setFixedSize(self.size())
        self.setWindowTitle("Fornitore " + str(self.controller.get_codice_id_fornitore()))

    def delete_fornitore(self):
        delete_view = QMessageBox.warning(self, 'Vuoi davvero eliminare il fornitore ' + str(self.controller.get_codice_id_fornitore()) + '?',
                                          'Il fornitore ' + str(self.controller.get_codice_id_fornitore()) + ' sarà permanentemente eliminato dal sistema.\nVuoi continuare?',
                                          QMessageBox.Yes,
                                          QMessageBox.No)
        if delete_view == QMessageBox.Yes:
            self.elimina_fornitore(self.controller.get_codice_id_fornitore())
            self.callback()
            self.close()

    def show_modifica_fornitore(self, elemento_modifica):
        self.vista_modifica_fornitore= VistaModificaFornitore(elemento_modifica, self.controller, self.callback)
        self.vista_modifica_fornitore.show()
