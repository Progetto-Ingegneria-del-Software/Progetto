from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QLabel, QHBoxLayout, QTableWidget, QAbstractItemView, \
    QHeaderView, QTableWidgetItem

from fattura.controller.ControlloreFattura import ControlloreFattura
from listaarticoli.controller.ControlloreListaArticoli import ControlloreListaArticoli
from listafornitori.control.ControlloreListaFornitori import ControlloreListaFornitori


class VistaFattura(QWidget):
    def __init__(self, fattura, callback):
        super(VistaFattura, self).__init__()

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

            self.h_layout2 = QHBoxLayout()

            self.label_riga1_fornitore = QLabel("Codice ID: {}, Ragione Sociale: {}, Partita IVA: {}".format(fattura.soggetto["codice_id"], fattura.soggetto["ragione_sociale"], fattura.soggetto["partita_iva"]))
            self.h_layout2.addWidget(self.label_riga1_fornitore)
            self.v_layout.addLayout(self.h_layout2)

            self.h_layout3 = QHBoxLayout()

            self.label_riga2_fornitore = QLabel("Città: {}, Indirizzo: {}, Telefono: {}, Email: {}".format(fattura.soggetto["citta"], fattura.soggetto["indirizzo"], fattura.soggetto["telefono"], fattura.soggetto["email"]))
            self.h_layout3.addWidget(self.label_riga2_fornitore)
            self.v_layout.addLayout(self.h_layout3)

        elif self.controller.get_tipo_fattura() == "Scarico":
            if "cf" in self.fattura.soggetto:
                self.label_cliente = QLabel("Dati Cliente:")
                self.label_cliente.setFont(bold_font)
                self.v_layout.addWidget(self.label_cliente)

                self.h_layout2 = QHBoxLayout()

                self.label_riga1_fornitore = QLabel(
                    "Codice ID: {}, Nome: {}, Cognome: {}, CF: {}".format(fattura.soggetto["codice_id"], fattura.soggetto["nome"], fattura.soggetto["cognome"], fattura.soggetto["cf"]))
                self.h_layout2.addWidget(self.label_riga1_fornitore)
                self.v_layout.addLayout(self.h_layout2)

                self.h_layout3 = QHBoxLayout()

                self.label_riga2_fornitore = QLabel(
                    "Email: {}, Telefono: {}, Città: {}, Indirizzo: {}".format(fattura.soggetto["email"], fattura.soggetto["telefono"], fattura.soggetto["citta"], fattura.soggetto["indirizzo"]))
                self.h_layout3.addWidget(self.label_riga2_fornitore)
                self.v_layout.addLayout(self.h_layout3)
            else:
                self.label_cliente = QLabel("Dati ClientePIVA:")
                self.label_cliente.setFont(bold_font)
                self.v_layout.addWidget(self.label_cliente)

                self.h_layout2 = QHBoxLayout()

                self.label_riga1_fornitore = QLabel(
                    "Codice ID: {}, Ragione Sociale: {}, Partita IVA: {}, Città: {}".format(fattura.soggetto["codice_id"],
                                                                          fattura.soggetto["ragione_sociale"],
                                                                          fattura.soggetto["partita_iva"],
                                                                          fattura.soggetto["citta"]))
                self.h_layout2.addWidget(self.label_riga1_fornitore)
                self.v_layout.addLayout(self.h_layout2)

                self.h_layout3 = QHBoxLayout()

                self.label_riga2_fornitore = QLabel(
                    "Indirizzo: {}, Telefono: {}, Email: {}".format(fattura.soggetto["indirizzo"],
                                                                               fattura.soggetto["telefono"],
                                                                               fattura.soggetto["email"]))
                self.h_layout3.addWidget(self.label_riga2_fornitore)
                self.v_layout.addLayout(self.h_layout3)

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
        self.table_articoli.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_articoli.setSelectionMode(QAbstractItemView.NoSelection)

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
        self.resize(900, 600)
        self.setFixedSize(self.size())
        self.setWindowTitle("Fattura Numero {}".format(self.controller.get_numero_fattura()))

    def show_articoli_in_table(self):
        self.table_articoli.setRowCount(len(self.controller.get_articoli_fattura()))

        i=0
        for articolo in self.fattura.articoli:
            item = QTableWidgetItem(str(articolo["codice"]))
            self.table_articoli.setItem(i, 0, item)
            item = QTableWidgetItem(str(articolo["descrizione"]))
            self.table_articoli.setItem(i, 1, item)
            item = QTableWidgetItem("€" + str(articolo["prezzo_unitario"]))
            self.table_articoli.setItem(i, 2, item)
            item = QTableWidgetItem(str(articolo["sconto_perc"]) + "%")
            self.table_articoli.setItem(i, 3, item)
            item = QTableWidgetItem(str(articolo["quantita"]))
            self.table_articoli.setItem(i, 4, item)
            item = QTableWidgetItem(str(articolo["totale_riga"]))
            self.table_articoli.setItem(i, 5, item)
            i = i+1
