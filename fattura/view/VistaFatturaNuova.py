from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QLabel, QHBoxLayout, QTableWidget, QAbstractItemView, \
    QHeaderView, QTableWidgetItem

from fattura.controller.ControlloreFattura import ControlloreFattura
from listaarticoli.controller.ControlloreListaArticoli import ControlloreListaArticoli
from listafornitori.control.ControlloreListaFornitori import ControlloreListaFornitori


class VistaFatturaNuova(QWidget):
    def __init__(self, fattura, callback):
        super(VistaFatturaNuova, self).__init__()

'''
        self.fattura = fattura
        self.controller = ControlloreFattura(self.fattura)
        self.callback = callback

        bold_font = QtGui.QFont()
        bold_font.setBold(True)

        italic_font = QtGui.QFont()
        italic_font.setItalic(True)

        self.v_layout = QVBoxLayout()
        self.h_layout = QHBoxLayout()

        self.label_tipo_fattura = QLabel("Tipo: {}".format(self.controller.get_tipo_fattura()))
        self.h_layout.addWidget(self.label_tipo_fattura)

        self.label_data_fattura = QLabel("Data: {}".format(self.controller.get_data_fattura()))
        self.h_layout.addWidget(self.label_data_fattura)

        self.h_layout.addStretch()

        self.v_layout.addLayout(self.h_layout)

        if self.controller.get_tipo_fattura() == "Carico":
            self.label_fornitore = QLabel("Dati Fornitore:")
            self.label_fornitore.setFont(bold_font)
            self.v_layout.addWidget(self.label_fornitore)
            fornitore = self.cerca_fornitore(self.controller.get_soggetto_fattura())

            self.h_layout2 = QHBoxLayout()

            self.label_riga1_fornitore = QLabel("Codice ID: {}, Ragione Sociale: {}, Partita IVA: {}".format(fornitore.codice_id, fornitore.ragione_sociale, fornitore.partita_iva))
            self.h_layout2.addWidget(self.label_riga1_fornitore)
            self.v_layout.addLayout(self.h_layout2)

            self.h_layout3 = QHBoxLayout()

            self.label_riga2_fornitore = QLabel("Città: {}, Indirizzo: {}, Telefono: {}, Email: {}".format(fornitore.citta, fornitore.indirizzo, fornitore.telefono, fornitore.email))
            self.h_layout3.addWidget(self.label_riga2_fornitore)
            self.v_layout.addLayout(self.h_layout3)

        elif self.controller.get_tipo_fattura() == "Scarico":
            self.h_layout_3 = QHBoxLayout()

            self.label_cliente = QLabel("Cliente: {}".format(self.fattura.soggetto))
            self.h_layout_3.addWidget(self.label_cliente)
            self.v_layout.addLayout(self.h_layout_3)

        self.h_layout4 = QHBoxLayout()

        self.label_articolo = QLabel("Dati Articolo/i:")
        self.label_articolo.setFont(bold_font)
        self.h_layout4.addWidget(self.label_articolo)
        self.h_layout4.addStretch()

        self.v_layout.addLayout(self.h_layout4)

        self.table_articoli = QTableWidget()
        self.table_articoli.setColumnCount(6)
        self.table_articoli.setRowCount(0)
        self.table_articoli.setHorizontalHeaderLabels(["Codice", "Descrizione", "Prezzo Unitario", "Sconto", "Quantità", "Totale Riga"])
        self.table_articoli.verticalHeader().setVisible(False)
        self.table_articoli.setAlternatingRowColors(True)
        self.table_articoli.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_articoli.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table_articoli.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.table_articoli.resizeColumnsToContents()
        self.table_articoli.resizeRowsToContents()

        self.table_articoli.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.show_articoli_in_table()

        self.v_layout.addWidget(self.table_articoli)

        self.h_layout5 = QHBoxLayout()

        self.label_totale = QLabel("Totale: {}".format(self.controller.get_totale_fattura()))
        self.label_totale.setFont(bold_font)
        self.h_layout5.addWidget(self.label_totale)

        self.v_layout.addLayout(self.h_layout5)

        self.setLayout(self.v_layout)
        self.resize(800, 600)
        self.setFixedSize(self.size())
        self.setWindowTitle("Fattura Numero {}".format(self.controller.get_numero_fattura()))

    def cerca_fornitore(self, ragione_sociale):
        controller_fornitore = ControlloreListaFornitori()
        lista_fornitori = controller_fornitore.get_lista_fornitori()
        for fornitore in lista_fornitori:
            if fornitore.ragione_sociale == ragione_sociale:
                return fornitore

    def show_articoli_in_table(self):
        self.table_articoli.setRowCount(len(self.controller.get_articoli_fattura()))
        controller_articoli = ControlloreListaArticoli()
        lista_articoli = self.fattura.articoli

        i=0
        for articolo in controller_articoli.get_lista_articoli():
            if int(articolo.codice) in lista_articoli:
                item = QTableWidgetItem(str(articolo.codice))
                self.table_articoli.setItem(i, 0, item)
                item = QTableWidgetItem(str(articolo.descrizione))
                self.table_articoli.setItem(i, 1, item)
                item = QTableWidgetItem("€" + str(articolo.prezzo_unitario))
                self.table_articoli.setItem(i, 2, item)
                item = QTableWidgetItem(str(articolo.sconto_perc) + "%")
                i = i+1
                '''
