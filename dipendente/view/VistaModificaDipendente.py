from PyQt5.QtWidgets import QWidget, QVBoxLayout, QFormLayout, QLineEdit, QHBoxLayout, QPushButton, QMessageBox


class VistaModificaDipendente(QWidget):
    def __init__(self, elemento_modifica, controller, callback):
        super(VistaModificaDipendente, self).__init__()

        self.elemento_modifica = elemento_modifica
        self.controller = controller
        self.callback = callback

        self.v_layout = QVBoxLayout()
        self.layout = QFormLayout()

        if self.elemento_modifica == "Modifica Nome":
            self.info = QLineEdit(self.controller.get_nome_dipendente())
        if self.elemento_modifica == "Modifica Cognome":
            self.info = QLineEdit(self.controller.get_cognome_dipendente())
        if self.elemento_modifica == "Modifica CF":
            self.info = QLineEdit(self.controller.get_cf_dipendente())
        if self.elemento_modifica == "Modifica Email":
            self.info = QLineEdit(str(self.controller.get_email_dipendente()))
        if self.elemento_modifica == "Modifica Telefono":
            self.info = QLineEdit(str(self.controller.get_telefono_dipendente()))
        if self.elemento_modifica == "Modifica Mansione":
            self.info = QLineEdit(self.controller.get_mansione_dipendente())
        if self.elemento_modifica == "Modifica Stipendio":
            self.info = QLineEdit(self.controller.get_stipendio_dipendente())

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
        self.setWindowTitle(self.elemento_modifica)

    def completa_modifica(self):
        if self.info.text() == "":
            QMessageBox.critical(self, 'Errore', 'Per favore, inserisci l\'informazione richiesta',
                                 QMessageBox.Ok, QMessageBox.Ok)
        else:
            if self.elemento_modifica == "Modifica Nome":
                self.controller.set_nome_dipendente(self.info.text())
            if self.elemento_modifica == "Modifica Cognome":
                self.controller.set_cognome_dipendente(self.info.text())
            if self.elemento_modifica == "Modifica CF":
                self.controller.set_cf_dipendente(self.info.text())
            if self.elemento_modifica == "Modifica Email":
                self.controller.set_email_dipendente(self.info.text())
            if self.elemento_modifica == "Modifica Telefono":
                self.controller.set_telefono_dipendente(self.info.text())
            if self.elemento_modifica == "Modifica Mansione":
                self.controller.set_mansione_dipendente(self.info.text())
            if self.elemento_modifica == "Modifica Stipendio":
                if self.is_int(self.info.text()):
                    self.controller.set_stipendio_dipendente(int(self.info.text()))
                    print(int(self.info.text()))
                elif self.is_float(self.info.text()):
                    self.controller.set_stipendio_dipendente(float(self.info.text()))
                else:
                    QMessageBox.critical(self, 'Errore', 'Per favore, inserisci un valore numerico',
                                         QMessageBox.Ok, QMessageBox.Ok)
            self.callback()
            self.close()

    def is_float(self, val):
        try:
            num = float(val)
        except ValueError:
            return False
        return True

    def is_int(self, val):
        try:
            num = int(val)
        except ValueError:
            return False
        return True