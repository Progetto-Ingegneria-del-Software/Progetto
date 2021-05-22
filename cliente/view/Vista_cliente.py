from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QLabel, QPushButton, QMessageBox

from cliente.controller.Controllore_cliente import Controllore_cliente
from cliente.view.Vista_modifica_cliente import Vista_modifica_cliente


class Vista_cliente(QWidget):
    def __init__(self, cliente, elimina_cliente, callback):
        super(Vista_cliente, self).__init__()

        self.controller = Controllore_cliente(cliente)
        self.elimina_cliente = elimina_cliente
        self.callback = callback

        v_layout = QVBoxLayout()

        grid_layout = QGridLayout()

        label_codice_id = QLabel("Codice ID: " + str(self.controller.get_codice_id_cliente()))
        grid_layout.addWidget(label_codice_id, 0, 0)

        label_nome = QLabel("Nome: " + str(self.controller.get_nome_cliente()))
        grid_layout.addWidget(label_nome, 1, 0)

        button_modifica_nome = QPushButton("Modifica Nome")
        button_modifica_nome.clicked.connect(lambda: self.show_modifica_cliente("Modifica Nome"))
        grid_layout.addWidget(button_modifica_nome, 1, 1)

        label_cognome = QLabel("Cognome: " + str(self.controller.get_cognome_cliente()))
        grid_layout.addWidget(label_cognome, 2, 0)

        button_modifica_cognome = QPushButton("Modifica Cognome")
        button_modifica_cognome.clicked.connect(lambda: self.show_modifica_cliente("Modifica Cognome"))
        grid_layout.addWidget(button_modifica_cognome, 2, 1)

        label_cf = QLabel("CF: " + str(self.controller.get_cf_cliente()))
        grid_layout.addWidget(label_cf, 3, 0)

        button_modifica_cf = QPushButton("Modifica CF")
        button_modifica_cf.clicked.connect(lambda: self.show_modifica_cliente("Modifica CF"))
        grid_layout.addWidget(button_modifica_cf, 3, 1)

        label_email = QLabel("Email: " + str(self.controller.get_email_cliente()))
        grid_layout.addWidget(label_email, 4, 0)

        button_modifica_email = QPushButton("Modifica Email")
        button_modifica_email.clicked.connect(lambda: self.show_modifica_cliente("Modifica Email"))
        grid_layout.addWidget(button_modifica_email, 4, 1)

        label_telefono = QLabel("Telefono: " + str(self.controller.get_telefono_cliente()))
        grid_layout.addWidget(label_telefono, 5, 0)

        button_modifica_telefono = QPushButton("Modifica Telefono")
        button_modifica_telefono.clicked.connect(lambda: self.show_modifica_cliente("Modifica Telefono"))
        grid_layout.addWidget(button_modifica_telefono, 5, 1)

        label_indirizzo = QLabel("Indirizzo: " + str(self.controller.get_indirizzo_cliente()))
        grid_layout.addWidget(label_indirizzo, 6, 0)

        button_modifica_indirizzo = QPushButton("Modifica Indirizzo")
        button_modifica_indirizzo.clicked.connect(lambda: self.show_modifica_cliente("Modifica Indirizzo"))
        grid_layout.addWidget(button_modifica_indirizzo, 6, 1)





        v_layout.addLayout(grid_layout)
        button_elimina_cliente = QPushButton("Elimina cliente " + str(self.controller.get_codice_id_cliente()))
        button_elimina_cliente.clicked.connect(self.delete_cliente)
        v_layout.addWidget(button_elimina_cliente)

        self.setLayout(v_layout)
        self.resize(500, 400)
        self.setFixedSize(self.size())
        self.setWindowTitle("cliente " + str(self.controller.get_codice_id_cliente()))

    def delete_cliente(self):
        delete_view = QMessageBox.warning(self, 'Vuoi davvero eliminare il cliente ' + str(self.controller.get_codice_id_cliente()) + '?',
                                          'Il cliente ' + str(self.controller.get_codice_id_cliente()) + ' sarà permanentemente eliminato dal sistema.\nVuoi continuare?',
                                          QMessageBox.Yes,
                                          QMessageBox.No)
        if delete_view == QMessageBox.Yes:
            self.elimina_cliente(self.controller.get_codice_id_cliente())
            self.callback()
            self.close()

    def show_modifica_cliente(self, elemento_modifica):
        self.vista_modifica_cliente = Vista_modifica_cliente(elemento_modifica, self.controller, self.callback)
        self.vista_modifica_cliente.show()
