from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QSpacerItem, QSizePolicy, QPushButton, QLabel, QLineEdit, \
    QMessageBox

from fornitore.model.Fornitore import Fornitore


class VistaInserisciFornitore(QWidget):
    def __init__(self, controller, callback):
        super(VistaInserisciFornitore, self).__init__()

        self.controller = controller
        self.callback = callback
        self.info = {}
        self.labels = ["Ragione Sociale:", "Partita IVA:", "Città:", "Indirizzo:", "Telefono:", "Email:"]

        self.v_layout = QVBoxLayout()
        self.grid_layout = QGridLayout()

        self.add_item_view()

        self.v_layout.addLayout(self.grid_layout)

        self.v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_ok = QPushButton("Inserisci")
        btn_ok.clicked.connect(self.add_fornitore)

        self.v_layout.addWidget(btn_ok)

        self.setLayout(self.v_layout)
        self.resize(400, 300)
        self.setFixedSize(self.size())
        self.setWindowTitle("Inserisci Fornitore")

    def add_item_view(self):
        i = 0
        for name in self.labels:
            self.grid_layout.addWidget(QLabel(name), i, 0)
            self.current_text_edit = QLineEdit(self)
            self.current_text_edit.returnPressed.connect(self.add_fornitore)
            self.grid_layout.addWidget(self.current_text_edit, i, 1)
            self.info[name] = self.current_text_edit
            i = i + 1

    def add_fornitore(self):
        ragione_sociale = self.info["Ragione Sociale:"].text()
        partita_iva = self.info["Partita IVA:"].text()
        citta = self.info["Città:"].text()
        indirizzo = self.info["Indirizzo:"].text()
        telefono = self.info["Telefono:"].text()
        email = self.info["Email:"].text()


        if ragione_sociale == "" or partita_iva == "" or citta == "" or indirizzo == "" or telefono == "" or email == "":
            QMessageBox.critical(self, 'Errore di compilazione!', 'Per favore, inserisci tutte le informazioni richieste.',
                                 QMessageBox.Ok, QMessageBox.Ok)

        else:
            self.controller.model.codice_id = self.controller.model.codice_id + 1
            self.controller.aggiungi_fornitore(
                Fornitore(self.controller.model.codice_id, ragione_sociale, partita_iva, citta, indirizzo, telefono, email))
            self.callback()
            self.close()


