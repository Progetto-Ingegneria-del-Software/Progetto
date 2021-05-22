from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QLabel, QPushButton, QMessageBox

from clientePIva.control.Controllore_clientepiva import Controllore_clientepiva

from clientePIva.view.Vista_modifica_clientepiva import Vista_modifica_clientepiva

class Vista_clientepiva(QWidget):
    def __init__(self, clientepiva, elimina_clientepiva, callback):
        super(Vista_clientepiva, self).__init__()

        self.controller = Controllore_clientepiva(clientepiva)
        self.elimina_clientepiva = elimina_clientepiva
        self.callback = callback

        v_layout = QVBoxLayout()

        grid_layout = QGridLayout()

        label_codice_id = QLabel("Codice ID: " + str(self.controller.get_codice_id_clientepiva()))
        grid_layout.addWidget(label_codice_id, 0, 0)


        label_ragione_sociale = QLabel("Ragione Sociale: " + str(self.controller.get_ragione_sociale_clientepiva()))
        grid_layout.addWidget(label_ragione_sociale, 1, 0)

        button_modifica_ragione_sociale = QPushButton("Modifica Ragione Sociale")
        button_modifica_ragione_sociale.clicked.connect(lambda: self.show_modifica_clientepiva("Modifica Ragione Sociale"))
        grid_layout.addWidget(button_modifica_ragione_sociale, 1, 1)

        label_partita_iva = QLabel("Partita IVA: " + str(self.controller.get_partita_iva_clientepiva()))
        grid_layout.addWidget(label_partita_iva, 2, 0)

        button_modifica_partita_iva = QPushButton("Modifica Partita IVA")
        button_modifica_partita_iva.clicked.connect(lambda: self.show_modifica_clientepiva("Modifica Partita IVA"))
        grid_layout.addWidget(button_modifica_partita_iva, 2, 1)

        label_citta = QLabel("Città: " + str(self.controller.get_citta_clientepiva()))
        grid_layout.addWidget(label_citta, 3, 0)

        button_modifica_citta = QPushButton("Modifica Città")
        button_modifica_citta.clicked.connect(lambda: self.show_modifica_clientepiva("Modifica Città"))
        grid_layout.addWidget(button_modifica_citta, 3, 1)

        label_indirizzo = QLabel("Indirizzo: " + str(self.controller.get_indirizzo_clientepiva()))
        grid_layout.addWidget(label_indirizzo, 4, 0)

        button_modifica_indirizzo = QPushButton("Modifica Indirizzo")
        button_modifica_indirizzo.clicked.connect(lambda: self.show_modifica_clientepiva("Modifica Indirizzo"))
        grid_layout.addWidget(button_modifica_indirizzo, 4, 1)

        label_telefono = QLabel("Telefono: " + str(self.controller.get_telefono_clientepiva()))
        grid_layout.addWidget(label_telefono, 5, 0)

        button_modifica_telefono = QPushButton("Modifica Telefono")
        button_modifica_telefono.clicked.connect(lambda: self.show_modifica_clientepiva("Modifica Telefono"))
        grid_layout.addWidget(button_modifica_telefono, 5, 1)

        label_email = QLabel("Email: " + str(self.controller.get_email_clientepiva()))
        grid_layout.addWidget(label_email, 6, 0)

        button_modifica_email = QPushButton("Modifica Email")
        button_modifica_email.clicked.connect(lambda: self.show_modifica_clientepiva("Modifica Email"))
        grid_layout.addWidget(button_modifica_email, 6, 1)

        v_layout.addLayout(grid_layout)
        button_elimina_clientepiva = QPushButton("Elimina Cliente PIva " + str(self.controller.get_codice_id_clientepiva()))
        button_elimina_clientepiva.clicked.connect(self.delete_clientepiva)
        v_layout.addWidget(button_elimina_clientepiva)

        self.setLayout(v_layout)
        self.resize(500, 400)
        self.setFixedSize(self.size())
        self.setWindowTitle("Cliente PIva " + str(self.controller.get_codice_id_clientepiva()))

    def delete_clientepiva(self):
        delete_view = QMessageBox.warning(self, 'Vuoi davvero eliminare il Cliente PIva ' + str(self.controller.get_codice_id_clientepiva()) + '?',
                                          'Il Cliente PIva ' + str(self.controller.get_codice_id_clientepiva()) + ' sarà permanentemente eliminato dal sistema.\nVuoi continuare?',
                                          QMessageBox.Yes,
                                          QMessageBox.No)
        if delete_view == QMessageBox.Yes:
            self.elimina_clientepiva(self.controller.get_codice_id_clientepiva())
            self.callback()
            self.close()

    def show_modifica_clientepiva(self, elemento_modifica):
        self.vista_modifica_clientepiva= Vista_modifica_clientepiva(elemento_modifica, self.controller, self.callback)
        self.vista_modifica_clientepiva.show()
