from fattura.controller.ControlloreFattura import ControlloreFattura
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QSpacerItem, QSizePolicy, QPushButton, \
    QMessageBox, QGridLayout

from fattura.model.Fattura import Fattura


class VistaCreaFattura(QWidget):
    def __init__(self, controller, callback):
        super(VistaCreaFattura, self).__init__()

        self.messaggio_tipo_fattura(ControlloreFattura.get_tipo_fattura)  # Viene stabilito il tipo di fattura Carico/Scarico
        

        self.controller = controller
        self.callback = callback
        self.info = {}
        self.labels = ["Numero:", "Tipo:", "Data:"]

        self.v_layout = QVBoxLayout()
        self.grid_layout = QGridLayout()

        self.add_item_view()

        self.v_layout.addLayout(self.grid_layout)

        self.v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        

        btn_ok = QPushButton("Crea")
        btn_ok.clicked.connect(self.add_fattura)

        self.v_layout.addWidget(btn_ok)

        self.setLayout(self.v_layout)
        self.resize(400, 250)
        self.setFixedSize(self.size())
        self.setWindowTitle("Crea Fattura")

    def add_item_view(self):
        i=0
        for name in self.labels:
            self.grid_layout.addWidget(QLabel(name), i, 0)
            self.current_text_edit = QLineEdit(self)
            self.current_text_edit.returnPressed.connect(self.add_fattura)
            self.grid_layout.addWidget(self.current_text_edit, i, 1)
            self.info[name] = self.current_text_edit
            i = i+1

    def add_fattura(self):
        gruppo_merciologico = self.info["Gruppo Merciologico:"].text()
        categoria = self.info["Categoria:"].text()
        marca = self.info["Marca:"].text()
        prezzo_unitario = self.info["Prezzo Unitario:"].text()

        if gruppo_merciologico == "" or categoria == "" or marca == "" or prezzo_unitario == "":
            QMessageBox.critical(self, 'Errore di compilazione!', 'Per favore, inserisci tutte le informazioni richieste.',
                                 QMessageBox.Ok, QMessageBox.Ok)
        else:
            self.controller.model.codice_id = self.controller.model.codice_id+1
            self.controller.aggiungi_articolo(Fattura(self.controller.model.codice_id, gruppo_merciologico, categoria, marca, prezzo_unitario, None, None))
            self.callback()
            self.close()

    def messaggio_tipo_fattura(self, tipo):
        message_tipo = QMessageBox.warning(self, 'Che tipo di fattura vuoi creare?', 'Carico o Scarico?', QMessageBox.Carico, QMessageBox.Scarico)
        if message_tipo == QMessageBox.Carico:
            tipo = 'Carico'
        else:
            tipo = 'Scarico'