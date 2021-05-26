from PyQt5.QtWidgets import QVBoxLayout, QGridLayout, QWidget, QLabel, QHBoxLayout, QPushButton

from fattura.controller.ControlloreFattura import ControlloreFattura

class VistaScegliFattura(QWidget):
    def __init__(self, callback):
        super(VistaScegliFattura, self).__init__()

        self.controller = ControlloreFattura
        self.callback = callback
        self.info = {}

        self.v_layout = QVBoxLayout()
        self.grid_layout = QGridLayout()

        self.testo = QLabel("Che tipo di fattura vuoi creare?")

        self.v_layout.addLayout(self.grid_layout)

        self.button_layout = QHBoxLayout()
        self.carico_btn = QPushButton("Carico")
        self.scarico_btn = QPushButton("Scarico")
        self.v_layout.addLayout(self.button_layout)

        self.carico_btn.clicked.connect(self.controller.set_tipo_fattura('Carico'))
        self.scarico_btn.clicked.connect(self.controller.set_tipo_fattura('Scarico'))

        self.setLayout(self.v_layout)
        self.resize(400, 500)
        self.setFixedSize(self.size())
        self.setWindowTitle("Scegli il tipo di fattura")