from PyQt5.QtWidgets import QWidget, QFormLayout, QLabel, QLineEdit, QVBoxLayout, QPushButton, QHBoxLayout, QSizePolicy, \
    QSpacerItem, QMessageBox


class Vista_modifica_articolo_magazzino(QWidget):
    def __init__(self, elemento_modifica, controller, callback):
        super(Vista_modifica_articolo_magazzino, self).__init__()

        self.elemento_modifica = elemento_modifica
        self.controller = controller
        self.callback= callback

        self.v_layout = QVBoxLayout()
        self.layout = QFormLayout()

        if self.elemento_modifica == "Modifica Quantità":
           self.info = QLineEdit(str(self.controller.get_stock_articolo()))

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

            if self.elemento_modifica == "Modifica Quantità":
                if self.is_int(self.info.text()) and int(self.info.text())>=0 :
                    self.controller.set_stock_articolo(int(self.info.text()))
                    self.callback()
                    self.close()

                else:
                    QMessageBox.critical(self, 'Errore', 'Per favore, inserisci un valore numerico, intero e positivo',
                                         QMessageBox.Ok, QMessageBox.Ok)

    def is_int(self, val):
        try:
            num = int(val)
        except ValueError:
            return False
        return True