from PyQt5.QtWidgets import QWidget, QFormLayout, QLabel, QLineEdit, QVBoxLayout, QPushButton, QHBoxLayout, QSizePolicy, \
    QSpacerItem, QMessageBox


class VistaModificaArticolo(QWidget):
    def __init__(self, elemento_modifica, controller, callback_articoli, callback_magazzino):
        super(VistaModificaArticolo, self).__init__()

        self.elemento_modifica = elemento_modifica
        self.controller = controller
        self.callback_articoli = callback_articoli
        self.callback_magazzino = callback_magazzino

        self.v_layout = QVBoxLayout()
        self.layout = QFormLayout()

        if self.elemento_modifica == "Modifica Codice":
            self.info = QLineEdit(self.controller.get_codice_articolo())
        if self.elemento_modifica == "Modifica Gruppo Merceologico":
            self.info = QLineEdit(self.controller.get_gruppo_merceologico_articolo())
        if self.elemento_modifica == "Modifica Categoria":
            self.info = QLineEdit(self.controller.get_categoria_articolo())
        if self.elemento_modifica == "Modifica Marca":
            self.info = QLineEdit(self.controller.get_marca_articolo())
        if self.elemento_modifica == "Modifica Prezzo Unitario":
            self.info = QLineEdit(str(self.controller.get_prezzo_unitario_articolo()))
        if self.elemento_modifica == "Modifica Sconto":
            self.info = QLineEdit(str(self.controller.get_sconto_perc_articolo()))
        if self.elemento_modifica == "Modifica Descrizione":
            self.info = QLineEdit(self.controller.get_descrizione_articolo())

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
            if self.elemento_modifica == "Modifica Codice":
                self.controller.set_codice_articolo(self.info.text())
            if self.elemento_modifica == "Modifica Gruppo Merceologico":
                self.controller.set_gruppo_merceologico_articolo(self.info.text())
            if self.elemento_modifica == "Modifica Categoria":
                self.controller.set_categoria_articolo(self.info.text())
            if self.elemento_modifica == "Modifica Marca":
                self.controller.set_marca_articolo(self.info.text())
            if self.elemento_modifica == "Modifica Prezzo Unitario":
                if self.is_int(self.info.text()):
                    self.controller.set_prezzo_unitario_articolo(int(self.info.text()))
                elif self.is_float(self.info.text()):
                    self.controller.set_prezzo_unitario_articolo(float(self.info.text()))
                else:
                    QMessageBox.critical(self, 'Errore', 'Per favore, inserisci un valore numerico',
                                         QMessageBox.Ok, QMessageBox.Ok)
            if self.elemento_modifica == "Modifica Sconto":
                if self.is_int(self.info.text()):
                    self.controller.set_prezzo_unitario_articolo(int(self.info.text()))
                elif self.is_float(self.info.text()):
                    self.controller.set_prezzo_unitario_articolo(float(self.info.text()))
                else:
                    QMessageBox.critical(self, 'Errore', 'Per favore, inserisci un valore numerico',
                                         QMessageBox.Ok, QMessageBox.Ok)
            if self.elemento_modifica == "Modifica Descrizione":
                self.controller.set_descrizione_articolo(self.info.text())
            self.callback_articoli()
            self.callback_magazzino()
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