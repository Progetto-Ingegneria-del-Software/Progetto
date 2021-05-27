from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QTableWidget, QAbstractItemView, \
    QHeaderView, QPushButton

from listafatture.controller.ControlloreListaFatture import ControlloreListaFatture
from listafornitori.control.ControlloreListaFornitori import ControlloreListaFornitori


class VistaCreaFatturaCarico(QWidget):
    def __init__(self, tipo_fattura):
        super(VistaCreaFatturaCarico, self).__init__()

        self.tipo_fattura = tipo_fattura

        self.controller = ControlloreListaFatture()

        bold_font = QtGui.QFont()
        bold_font.setBold(True)

        self.v_layout = QVBoxLayout()
        self.h_layout = QHBoxLayout()

        self.label_tipo_fattura = QLabel("Tipo: {}".format(self.tipo_fattura))
        self.h_layout.addWidget(self.label_tipo_fattura)

        self.label_data_fattura = QLabel("Data: ")
        self.h_layout.addWidget(self.label_data_fattura)
        self.edit_data_fattura = QLineEdit("gg/mm/aaaa")
        self.edit_data_fattura.setFixedWidth(100)
        self.h_layout.addWidget(self.edit_data_fattura)

        self.h_layout.addStretch()

        self.v_layout.addLayout(self.h_layout)

        self.label_search_fornitore = QLabel("Dati Fornitore:")
        self.label_search_fornitore.setFont(bold_font)
        self.v_layout.addWidget(self.label_search_fornitore)
        self.search_bar_fornitore = QLineEdit("Inserisci la ragione sociale del fornitore")
        self.search_bar_fornitore.setFixedWidth(300)
        self.v_layout.addWidget(self.search_bar_fornitore)
        self.search_bar_fornitore.returnPressed.connect(self.search_fornitore)

        self.h_layout2 = QHBoxLayout()

        self.label_riga1_fornitore = QLabel("Codice ID:   Ragione Sociale:   Partita IVA:")
        self.h_layout2.addWidget(self.label_riga1_fornitore)

        self.v_layout.addLayout(self.h_layout2)

        self.h_layout3 = QHBoxLayout()

        self.label_riga2_fornitore = QLabel("Città:   Indirizzo:   Telefono:   Email:")
        self.h_layout3.addWidget(self.label_riga2_fornitore)

        self.v_layout.addLayout(self.h_layout3)

        self.h_layout4 = QHBoxLayout()

        self.label_search_articolo = QLabel("Dati Articolo/i:")
        self.label_search_articolo.setFont(bold_font)
        self.h_layout4.addWidget(self.label_search_articolo)
        self.search_bar_articolo = QLineEdit("Inserisci il codice a barre dell'articolo")
        self.search_bar_articolo.setFixedWidth(300)
        self.h_layout4.addWidget(self.search_bar_articolo)
        self.search_bar_quantita = QLineEdit()
        self.search_bar_quantita.setFixedWidth(50)
        self.h_layout4.addWidget(self.search_bar_quantita)
        self.search_button = QPushButton("Aggiungi Articolo")
        self.h_layout4.addWidget(self.search_button)
        # self.search_button.pressed.connect(self.add_articolo_in_fattura)
        self.h_layout4.addStretch()

        self.v_layout.addLayout(self.h_layout4)

        self.table_articoli = QTableWidget()
        self.table_articoli.setColumnCount(5)
        self.table_articoli.setRowCount(0)
        self.table_articoli.setHorizontalHeaderLabels(["Codice", "Descrizione", "Prezzo Unitario", "Sconto", "Totale Riga"])
        self.table_articoli.verticalHeader().setVisible(False)
        self.table_articoli.setAlternatingRowColors(True)
        self.table_articoli.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_articoli.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table_articoli.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.table_articoli.resizeColumnsToContents()
        self.table_articoli.resizeRowsToContents()

        self.table_articoli.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.v_layout.addWidget(self.table_articoli)

        self.setLayout(self.v_layout)
        self.resize(800, 350)
        self.setFixedSize(self.size())
        self.setWindowTitle("Fattura Numero {}".format(self.controller.get_assegnamento_numero_fattura()))

    def search_fornitore(self):
        self.controller_fornitore = ControlloreListaFornitori()
        self.lista_fornitori = self.controller_fornitore.get_lista_fornitori()

        for fornitore in self.lista_fornitori:
            if self.search_bar_fornitore.text().upper() in fornitore.ragione_sociale.upper() \
                    or fornitore.ragione_sociale.upper() in self.search_bar_fornitore.text().upper():
                self.mostra_fornitore_cercato(fornitore)

    def mostra_fornitore_cercato(self, fornitore):
        self.label_riga1_fornitore.setText("Codice ID: {} Ragione Sociale: {} Partita IVA: {}".format(fornitore.codice_id, fornitore.ragione_sociale, fornitore.partita_iva))
        self.label_riga2_fornitore.setText("Città: {} Indirizzo: {} Telefono: {} Email: {}".format(fornitore.citta, fornitore.indirizzo, fornitore.telefono, fornitore.email))

    def add_articolo_in_fattura(self):
        pass