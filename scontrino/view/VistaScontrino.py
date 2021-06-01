from PyQt5 import QtGui
from PyQt5.QtWidgets import QAbstractItemView, QTableWidget, QTableWidgetItem, QTextBrowser, QWidget, QVBoxLayout, \
    QLabel, QPushButton, QGridLayout, \
    QMessageBox, QHBoxLayout, QHeaderView

from scontrino.controller.ControlloreScontrino import ControlloreScontrino
from listaarticoli.controller.ControlloreListaArticoli import ControlloreListaArticoli


class VistaScontrino(QWidget):
    def __init__(self, scontrino, callback):
        super(VistaScontrino, self).__init__()


        self.scontrino = scontrino
        self.controller = ControlloreScontrino(self.scontrino)
        self.callback = callback

        bold_font = QtGui.QFont()
        bold_font.setBold(True)

        italic_font = QtGui.QFont()
        italic_font.setItalic(True)

        self.v_layout = QVBoxLayout()
        self.h_layout = QHBoxLayout()

        self.label_data_scontrino = QLabel("Data: {}".format(self.controller.get_data_scontrino()))
        self.h_layout.addWidget(self.label_data_scontrino)

        self.h_layout.addStretch()

        self.v_layout.addLayout(self.h_layout)

        self.h_layout2 = QHBoxLayout()

        self.label_articolo = QLabel("Dati Articolo/i:")
        self.label_articolo.setFont(bold_font)
        self.h_layout2.addWidget(self.label_articolo)
        self.h_layout2.addStretch()

        self.v_layout.addLayout(self.h_layout2)

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

        self.h_layout3 = QHBoxLayout()

        self.label_totale = QLabel("Totale: {}".format(self.controller.get_totale_scontrino()))
        self.label_totale.setFont(bold_font)
        self.h_layout3.addWidget(self.label_totale)

        self.v_layout.addLayout(self.h_layout3)

        self.setLayout(self.v_layout)
        self.resize(800, 500)
        self.setFixedSize(self.size())
        self.setWindowTitle("Scontrino Numero {}".format(self.controller.get_numero_scontrino()))


    ##############################################
    ###     FUNZIONE CHE MOSTRA LA TABELLA     ###
    ##############################################
    def show_articoli_in_table(self):
        self.table_articoli.setRowCount(len(self.controller.get_articoli_scontrino()))

        i=0
        for articolo in self.scontrino.articoli:
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
