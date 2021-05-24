from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit

from fattura.controller.ControlloreFattura import ControlloreFattura


class VistaCreaFatturaScarico(QWidget):
    def __init__(self):
        super(VistaCreaFatturaScarico, self).__init__()

        self.v_layout = QVBoxLayout()
        self.h_layout = QHBoxLayout()
        self.controller = ControlloreFattura()

        self.label_numero_fattura = QLabel("Numero: {}".format(self.controller.get_numero_fattura()))
        self.h_layout.addWidget(self.label_numero_fattura)

        self.label_tipo_fattura = QLabel("Tipo: {}".format(self.controller.get_tipo_fattura()))
        self.h_layout.addWidget(self.label_tipo_fattura)

        self.label_data_fattura = QLabel("Data: {}".format(self.controller.get_data_fattura()))
        self.h_layout.addWidget(self.label_data_fattura)

        self.v_layout.addLayout(self.h_layout)

        self.label_search_fornitore = QLabel("Fornitore: ")
        self.search_bar_fornitore = QLineEdit("Inserisci qui la ragione sociale del fornitore")
        self.search_bar_fornitore.returnPressed.connect(self.search_fornitore)

        self.setLayout(self.v_layout)
        self.resize(600, 350)
        self.setFixedSize(self.size())
        self.setWindowTitle("Vista Crea Fattura")


