from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QLabel, QPushButton, QMessageBox

from dipendente.controller.ControlloreDipendente import ControlloreDipendente
from dipendente.view.VistaModificaDipendente import VistaModificaDipendente


class VistaDipendente(QWidget):
    def __init__(self, dipendente, elimina_dipendente, callback):
        super(VistaDipendente, self).__init__()

        self.controller = ControlloreDipendente(dipendente)
        self.elimina_dipendente = elimina_dipendente
        self.callback = callback

        v_layout = QVBoxLayout()

        grid_layout = QGridLayout()

        label_codice_id = QLabel("Codice ID: " + str(self.controller.get_codice_id_dipendente()))
        grid_layout.addWidget(label_codice_id, 0, 0)

        label_nome = QLabel("Nome: " + str(self.controller.get_nome_dipendente()))
        grid_layout.addWidget(label_nome, 1, 0)

        button_modifica_nome = QPushButton("Modifica Nome")
        button_modifica_nome.clicked.connect(lambda: self.show_modifica_dipendente("Modifica Nome"))
        grid_layout.addWidget(button_modifica_nome, 1, 1)

        label_cognome = QLabel("Cognome: " + str(self.controller.get_cognome_dipendente()))
        grid_layout.addWidget(label_cognome, 2, 0)

        button_modifica_cognome = QPushButton("Modifica Cognome")
        button_modifica_cognome.clicked.connect(lambda: self.show_modifica_dipendente("Modifica Cognome"))
        grid_layout.addWidget(button_modifica_cognome, 2, 1)

        label_cf = QLabel("CF: " + str(self.controller.get_cf_dipendente()))
        grid_layout.addWidget(label_cf, 3, 0)

        button_modifica_cf = QPushButton("Modifica CF")
        button_modifica_cf.clicked.connect(lambda: self.show_modifica_dipendente("Modifica CF"))
        grid_layout.addWidget(button_modifica_cf, 3, 1)

        label_email = QLabel("Email: " + str(self.controller.get_email_dipendente()))
        grid_layout.addWidget(label_email, 4, 0)

        button_modifica_email = QPushButton("Modifica Email")
        button_modifica_email.clicked.connect(lambda: self.show_modifica_dipendente("Modifica Email"))
        grid_layout.addWidget(button_modifica_email, 4, 1)

        label_telefono = QLabel("Telefono: " + str(self.controller.get_telefono_dipendente()))
        grid_layout.addWidget(label_telefono, 5, 0)

        button_modifica_telefono = QPushButton("Modifica Telefono")
        button_modifica_telefono.clicked.connect(lambda: self.show_modifica_dipendente("Modifica Telefono"))
        grid_layout.addWidget(button_modifica_telefono, 5, 1)

        label_mansione = QLabel("Mansione: " + str(self.controller.get_mansione_dipendente()))
        grid_layout.addWidget(label_mansione, 6, 0)

        button_modifica_mansione = QPushButton("Modifica Mansione")
        button_modifica_mansione.clicked.connect(lambda: self.show_modifica_dipendente("Modifica Mansione"))
        grid_layout.addWidget(button_modifica_mansione, 6, 1)

        label_stipendio = QLabel("Stipendio: " + str(self.controller.get_stipendio_dipendente()))
        grid_layout.addWidget(label_stipendio, 7, 0)

        button_modifica_stipendio = QPushButton("Modifica Stipendio")
        button_modifica_stipendio.clicked.connect(lambda: self.show_modifica_dipendente("Modifica Stipendio"))
        grid_layout.addWidget(button_modifica_stipendio, 7, 1)

        v_layout.addLayout(grid_layout)
        button_elimina_dipendente = QPushButton("Elimina Dipendente " + str(self.controller.get_codice_id_dipendente()))
        button_elimina_dipendente.clicked.connect(self.delete_dipendente)
        v_layout.addWidget(button_elimina_dipendente)

        self.setLayout(v_layout)
        self.resize(500, 350)
        self.setFixedSize(self.size())
        self.setWindowTitle("Dipendente " + str(self.controller.get_codice_id_dipendente()))

    def delete_dipendente(self):
        delete_view = QMessageBox.warning(self, 'Vuoi davvero eliminare il dipendente ' + str(self.controller.get_codice_id_dipendente()) + '?',
                                          'Il dipendente ' + str(self.controller.get_codice_id_dipendente()) + ' sarà permanentemente eliminato dal sistema.\nVuoi continuare?',
                                          QMessageBox.Yes,
                                          QMessageBox.No)
        if delete_view == QMessageBox.Yes:
            self.elimina_dipendente(self.controller.get_codice_id_dipendente())
            self.callback()
            self.close()

    def show_modifica_dipendente(self, elemento_modifica):
        self.vista_modifica_dipendente = VistaModificaDipendente(elemento_modifica, self.controller, self.callback)
        self.vista_modifica_dipendente.show()
