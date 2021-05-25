from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, \
    QAbstractItemView, QHeaderView, QMessageBox, QLineEdit, QLabel


class VistaScegliFattura(QtWidgets):
    def __init__(self, controller, callback):
        super(VistaScegliFattura, self).__init__()

        self.controller = controller
        self.callback = callback
        self.info = {}

        self.v_layout = QVBoxLayout()
        self.grid_layout = QGridLayout()

        self.testo = QLabel

        self.v_layout.addLayout(self.grid_layout)

        self.v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        

        btn_ok = QPushButton("Crea")
        btn_ok.clicked.connect(lambda: self.add_fattura(tipo_cliente))

        self.v_layout.addWidget(btn_ok)

        self.setLayout(self.v_layout)
        self.resize(400, 300)
        self.setFixedSize(self.size())
        self.setWindowTitle("Crea Fattura")