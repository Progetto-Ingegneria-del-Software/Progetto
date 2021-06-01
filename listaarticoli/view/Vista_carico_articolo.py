from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QSpacerItem, QSizePolicy, QPushButton, \
    QMessageBox, QGridLayout

#from articolo.model.Articolo import Articolo


class Vista_carico_articolo(QWidget):
    def __init__(self, controller, callback):
        super(Vista_carico_articolo, self).__init__()

        self.controller = controller
        self.callback = callback
        self.info = {}
        self.labels = ["Codice a barre:", "Quantità da incrementare:"]

        self.v_layout = QVBoxLayout()
        self.grid_layout = QGridLayout()

        self.load_item_view()

        self.v_layout.addLayout(self.grid_layout)

        self.v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_ok = QPushButton("Carica articolo")
        btn_ok.clicked.connect(self.load_articolo)

        self.v_layout.addWidget(btn_ok)

        self.setLayout(self.v_layout)
        self.resize(400, 250)
        self.setFixedSize(self.size())
        self.setWindowTitle("Carico articolo in magazzino")

    def load_item_view(self):
        i=0
        for name in self.labels:
            self.grid_layout.addWidget(QLabel(name), i, 0)
            self.current_text_edit = QLineEdit(self)
            self.current_text_edit.returnPressed.connect(self.load_articolo)
            self.grid_layout.addWidget(self.current_text_edit, i, 1)
            self.info[name] = self.current_text_edit
            i = i+1

    def load_articolo(self):
        codice_immesso = self.info["Codice a barre:"].text()
        stock = self.info["Quantità da incrementare:"].text()

        if codice_immesso == "" or stock == "":
            QMessageBox.critical(self, 'Errore di compilazione!', 'Per favore, inserisci tutte le informazioni richieste.',
                                 QMessageBox.Ok, QMessageBox.Ok)
        elif self.is_int(stock) and int(stock)>0:
            articolo_cercato = self.controller.inserimento_carico(codice_immesso, stock)
            if articolo_cercato == True:
                self.callback()
                self.close()
            else:
                QMessageBox.critical(self, 'Errore',
                                     'Articolo inserito non presente in anagrafica articolo, aggiungere articolo e informazioni in anagrafica articolo.',
                                     QMessageBox.Ok, QMessageBox.Ok)
        else:
            QMessageBox.critical(self, 'Errore',
                                 'Per favore, inserisci un valore numerico, intero e positivo per incrementare la quantità.',
                                 QMessageBox.Ok, QMessageBox.Ok)

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

