from PyQt5.QtWidgets import QWidget, QVBoxLayout, QFormLayout, QLineEdit, QHBoxLayout, QPushButton, QMessageBox


class VistaModificaFornitore(QWidget):
    def __init__(self, elemento_modifica, controller, callback):
        super(VistaModificaFornitore, self).__init__()

        self.elemento_modifica = elemento_modifica
        self.controller = controller
        self.callback = callback

        self.v_layout = QVBoxLayout()
        self.layout = QFormLayout()

        if self.elemento_modifica == "Modifica Ragione Sociale":
            self.info = QLineEdit(self.controller.get_ragione_sociale_fornitore())
        if self.elemento_modifica == "Modifica Partita IVA":
            self.info = QLineEdit(self.controller.get_partita_iva_fornitore())
        if self.elemento_modifica == "Modifica Città":
            self.info = QLineEdit(self.controller.get_citta_fornitore())
        if self.elemento_modifica == "Modifica Indirizzo":
            self.info = QLineEdit(self.controller.get_indirizzo_fornitore())
        if self.elemento_modifica == "Modifica Telefono":
            self.info = QLineEdit(str(self.controller.get_telefono_fornitore()))
        if self.elemento_modifica == "Modifica Email":
            self.info = QLineEdit(self.controller.get_email_fornitore())

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
            if self.elemento_modifica == "Modifica Ragione Sociale":
                self.controller.set_ragione_sociale_fornitore(self.info.text())
            if self.elemento_modifica == "Modifica Partita IVA":
                self.controller.set_partita_iva_fornitore(self.info.text())
            if self.elemento_modifica == "Modifica Città":
                self.controller.set_citta_fornitore(self.info.text())
            if self.elemento_modifica == "Modifica Indirizzo":
                self.controller.set_indirizzo_fornitore(self.info.text())
            if self.elemento_modifica == "Modifica Telefono":
                self.controller.set_telefono_fornitore(self.info.text())
            if self.elemento_modifica == "Modifica Email":
                self.controller.set_email_fornitore(self.info.text())
            self.callback()
            self.close()