from PyQt5.QtWidgets import QWidget, QFormLayout, QLabel, QLineEdit, QVBoxLayout, QPushButton, QHBoxLayout, QSizePolicy, \
    QSpacerItem, QMessageBox


class VistaModificaArticolo(QWidget):
    def __init__(self, elemento_modifica, controller, callback):
        super(VistaModificaArticolo, self).__init__()

        self.elemento_modifica = elemento_modifica
        self.controller = controller
        self.callback= callback

        self.v_layout = QVBoxLayout()
        self.layout = QFormLayout()
        self.info = QLineEdit(self)

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
            if self.elemento_modifica == "Modifica Gruppo Merceologico":
                self.controller.set_gruppo_merceologico_articolo(self.info.text())
            if self.elemento_modifica == "Modifica Categoria":
                self.controller.set_categoria_articolo(self.info.text())
            if self.elemento_modifica == "Modifica Marca":
                self.controller.set_marca_articolo(self.info.text())
            if self.elemento_modifica == "Modifica Prezzo Unitario":
                self.controller.set_prezzo_unitario_articolo(self.info.text())
            if self.elemento_modifica == "Modifica Sconto":
                self.controller.set_sconto_perc_articolo(self.info.text())
            self.callback()
            self.close()