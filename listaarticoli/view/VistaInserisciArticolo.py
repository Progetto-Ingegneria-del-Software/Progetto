from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QSpacerItem, QSizePolicy, QPushButton, \
    QMessageBox, QGridLayout

from articolo.model.Articolo import Articolo
from listaarticoli.view.Vista_lista_articoli_magazzino import Vista_lista_articoli_magazzino

class VistaInserisciArticolo(QWidget):
    def __init__(self, controller, callback_articoli, callback_magazzino):
        super(VistaInserisciArticolo, self).__init__()

        self.controller = controller
        self.callback_articoli = callback_articoli
        self.callback_magazzino = callback_magazzino
        self.info = {}
        self.labels = ["Codice a Barre:", "Gruppo Merceologico:", "Categoria:", "Marca:", "Prezzo Unitario:", "Descrizione:"]

        self.v_layout = QVBoxLayout()
        self.grid_layout = QGridLayout()

        self.add_item_view()

        self.v_layout.addLayout(self.grid_layout)

        self.v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_ok = QPushButton("Inserisci")
        btn_ok.clicked.connect(self.add_articolo)

        self.v_layout.addWidget(btn_ok)

        self.setLayout(self.v_layout)
        self.resize(400, 250)
        self.setFixedSize(self.size())
        self.setWindowTitle("Inserisci Articolo")

    def add_item_view(self):
        i=0
        for name in self.labels:
            self.grid_layout.addWidget(QLabel(name), i, 0)
            self.current_text_edit = QLineEdit(self)
            self.current_text_edit.returnPressed.connect(self.add_articolo)
            self.grid_layout.addWidget(self.current_text_edit, i, 1)
            self.info[name] = self.current_text_edit
            i = i+1

    def add_articolo(self):
        codice = self.info["Codice a Barre:"].text()
        gruppo_merciologico = self.info["Gruppo Merceologico:"].text()
        categoria = self.info["Categoria:"].text()
        marca = self.info["Marca:"].text()
        prezzo_unitario = self.info["Prezzo Unitario:"].text()
        descrizione = self.info["Descrizione:"].text()

        if codice == "" or gruppo_merciologico == "" or categoria == "" or marca == "" or prezzo_unitario == "":
            QMessageBox.critical(self, 'Errore di compilazione!', 'Per favore, inserisci tutte le informazioni richieste.',
                                 QMessageBox.Ok, QMessageBox.Ok)
            return
        if not self.is_float(prezzo_unitario) and not self.is_int(prezzo_unitario):
            QMessageBox.critical(self, 'Errore', 'Per favore, inserisci un valore numerico nel campo Prezzo Unitario.',
                                 QMessageBox.Ok, QMessageBox.Ok)
            return
        for articolo in self.controller.get_lista_articoli():
            if articolo.codice == codice:
                QMessageBox.critical(self, 'Errore',
                                     'Il codice a barre è già presente nel sistema.',
                                     QMessageBox.Ok, QMessageBox.Ok)
                return
        self.controller.aggiungi_articolo(Articolo(codice, gruppo_merciologico, categoria, marca, prezzo_unitario, 0, descrizione, 0))
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
