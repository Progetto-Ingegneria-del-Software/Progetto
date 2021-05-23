from PyQt5.QtWidgets import QWidget, QVBoxLayout, QFormLayout, QLineEdit, QHBoxLayout, QPushButton, QMessageBox


class Vista_modifica_cliente(QWidget):
    def __init__(self, elemento_modifica, controller, callback):
        super(Vista_modifica_cliente, self).__init__()

        self.elemento_modifica = elemento_modifica
        self.controller = controller
        self.callback = callback

        self.v_layout = QVBoxLayout()
        self.layout = QFormLayout()
        #self.info = QLineEdit(self)
        
        if self.elemento_modifica == "Modifica Nome":
            self.info = QLineEdit(self.controller.get_nome_cliente())
        if self.elemento_modifica == "Modifica Cognome":
            self.info = QLineEdit(self.controller.get_cognome_cliente())
        if self.elemento_modifica == "Modifica CF":
            self.info = QLineEdit(self.controller.get_cf_cliente())
        if self.elemento_modifica == "Modifica Email":
            self.info = QLineEdit(self.controller.get_email_cliente())
        if self.elemento_modifica == "Modifica Telefono":
            self.info = QLineEdit(self.controller.get_telefono_cliente())
        if self.elemento_modifica == "Modifica Indirizzo":
            self.info = QLineEdit(self.controller.get_indirizzo_cliente())

        self.layout.addRow(self.elemento_modifica + ':', self.info)

        self.button_layout = QHBoxLayout()
        self.send_button = QPushButton("Ok")
        self.button_layout.addWidget(self.send_button)
        self.button_layout.addStretch()
        self.send_button.clicked.connect(self.completa_modifica)
        self.info.returnPressed.connect(self.completa_modifica)
        self.v_layout.addLayout(self.layout)
        self.v_layout.addLayout(self.button_layout)
        self.setLayout(self.v_layout)

        self.resize(500, 100)
        self.setFixedSize(self.size())
        self.setWindowTitle("Modifica " + self.elemento_modifica)

    def completa_modifica(self):
        if self.info.text() == "":
            QMessageBox.critical(self, 'Errore', 'Per favore, inserisci l\'informazione richiesta',
                                 QMessageBox.Ok, QMessageBox.Ok)
        else:
            if self.elemento_modifica == "Modifica Nome":
                self.controller.set_nome_cliente(self.info.text())
            if self.elemento_modifica == "Modifica Cognome":
                self.controller.set_cognome_cliente(self.info.text())
            if self.elemento_modifica == "Modifica CF":
                self.controller.set_cf_cliente(self.info.text())
            if self.elemento_modifica == "Modifica Email":
                self.controller.set_email_cliente(self.info.text())
            if self.elemento_modifica == "Modifica Telefono":
                self.controller.set_telefono_cliente(self.info.text())
            if self.elemento_modifica == "Modifica Indirizzo":
                self.controller.set_indirizzo_cliente(self.info.text())

            self.callback()
            self.close()
