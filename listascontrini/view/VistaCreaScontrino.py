from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QAbstractItemView, QHBoxLayout, QHeaderView, QTableWidget, QTableWidgetItem, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

from scontrino.model.Scontrino import Scontrino
from scontrino.controller.ControlloreScontrino import ControlloreScontrino
from listascontrini.controller.ControlloreListaScontrini import ControlloreListaScontrini
from listaarticoli.controller.ControlloreListaArticoli import ControlloreListaArticoli

class VistaCreaScontrino(QWidget):
    def __init__(self, controller_scontrini, controller_articoli, callback_scontrini, callback_magazzino):
        super(VistaCreaScontrino, self).__init__()

        self.controller_scontrini = controller_scontrini
        self.controller_articoli = controller_articoli
        self.callback_scontrini = callback_scontrini
        self.callback_magazzino = callback_magazzino
        self.numero_scontrino = self.controller_scontrini.get_assegnamento_numero_scontrino() + 1
        self.data = None
        self.carrello_acquisti = []
        self.totale = 0

        # Impostazione del font da applicare ad alcune Label
        bold_font = QtGui.QFont()
        bold_font.setBold(True)

        # Impostazione del font corsivo da applicare alla scritta interna del QLineEdit
        italic_font = QtGui.QFont()
        italic_font.setItalic(True)

        self.v_layout = QVBoxLayout()
        self.h_layout = QHBoxLayout()

        self.label_data_scontrino = QLabel("Data: ")
        self.h_layout.addWidget(self.label_data_scontrino)
        self.edit_giorno_scontrino = QLineEdit("gg")
        self.edit_giorno_scontrino.setFixedWidth(30)
        self.edit_mese_scontrino = QLineEdit("mm")
        self.edit_mese_scontrino.setFixedWidth(30)
        self.edit_anno_scontrino = QLineEdit("aaaa")
        self.edit_anno_scontrino.setFixedWidth(40)
        self.h_layout.addWidget(self.edit_giorno_scontrino)
        self.h_layout.addWidget(self.edit_mese_scontrino)
        self.h_layout.addWidget(self.edit_anno_scontrino)

        self.h_layout.addStretch()

        self.v_layout.addLayout(self.h_layout)

        self.h_layout2 = QHBoxLayout()

        # INSERIMENTO DEGLI ARTICOLI
        self.label_search_articolo = QLabel("Dati Articolo/i:")
        self.label_search_articolo.setFont(bold_font)
        self.h_layout2.addWidget(self.label_search_articolo)
        self.search_bar_articolo = QLineEdit("Inserisci il codice a barre dell'articolo") # Viene preso in input il codice a barre dell'articolo da inserire nello scontrino
        self.search_bar_articolo.setFixedWidth(300)
        self.search_bar_articolo.setFont(italic_font)
        self.h_layout2.addWidget(self.search_bar_articolo)
        self.label_quantita = QLabel("Quantità:") # Viene preso in input la quantità di pezzi dell'articolo
        self.h_layout2.addWidget(self.label_quantita)
        self.search_bar_quantita = QLineEdit()
        self.search_bar_quantita.setFixedWidth(50)
        self.h_layout2.addWidget(self.search_bar_quantita)
        self.search_button = QPushButton("Aggiungi Articolo")  # Bottone che aggiunge l'articolo alla lista
        self.h_layout2.addWidget(self.search_button)
        self.search_button.pressed.connect(self.controllo_inserimento)
        self.h_layout2.addStretch()

        self.v_layout.addLayout(self.h_layout2)

        self.table_articoli = QTableWidget()
        self.table_articoli.setColumnCount(7)
        self.table_articoli.setRowCount(0)
        self.table_articoli.setHorizontalHeaderLabels(["Codice", "Descrizione", "Prezzo Unitario", "Sconto", "Quantità", "Totale Riga", ""]) # Nomi delle colonne della tabella
        self.table_articoli.verticalHeader().setVisible(False)
        self.table_articoli.setAlternatingRowColors(True)
        self.table_articoli.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_articoli.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table_articoli.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.table_articoli.resizeColumnsToContents()
        self.table_articoli.resizeRowsToContents()

        self.table_articoli.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.v_layout.addWidget(self.table_articoli)

        self.h_layout3 = QHBoxLayout()

        # Label dove verrà stampato il totale dell'importo dell'intero scontrino
        self.label_totale = QLabel("Totale: €{}".format(self.totale))
        self.label_totale.setFont(bold_font)
        self.h_layout3.addWidget(self.label_totale)
        
        # Bottone che conferma la creazione dello scontrino
        btn_crea = QPushButton("Crea Scontrino")
        btn_crea.clicked.connect(self.crea_scontrino)
        self.h_layout3.addWidget(btn_crea)
        self.h_layout3.addStretch()

        self.v_layout.addLayout(self.h_layout3)

        self.setLayout(self.v_layout)
        self.resize(800, 500)
        self.setFixedSize(self.size())
        self.setWindowTitle("Creazione Scontrino Numero {}".format(self.numero_scontrino))

    #######################################################
    ##  FUNZIONE CHE AGGIUNGE L'ARTICOLI PRESO IN INPUT  ##
    ##         DENTRO LA LISTA DELLO SCONTRINO           ##
    #######################################################
    def add_articolo_in_scontrino(self):
        controller_lista_articoli = ControlloreListaArticoli()
        lista_articoli = controller_lista_articoli.get_lista_articoli()

        for articolo in lista_articoli:
            if self.search_bar_articolo.text() == articolo.codice:
                articolo_dict = articolo.__dict__
                articolo_dict.pop("gruppo_merceologico", None)
                articolo_dict.pop("categoria", None)
                articolo_dict.pop("marca", None)
                articolo_dict["quantita"] = self.search_bar_quantita.text()
                articolo_dict["totale_riga"] = float(articolo.prezzo_unitario) * int(self.search_bar_quantita.text()) - (
                            float(articolo.prezzo_unitario) * float(articolo.sconto_perc) / 100) * int(
                    self.search_bar_quantita.text())
                self.carrello_acquisti.append(articolo_dict)
        self.show_table_items()

    def show_table_items(self):
        i = 0
        self.table_articoli.setRowCount(len(self.carrello_acquisti))
        for articolo in self.carrello_acquisti:
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
            item = QTableWidgetItem("€" + str(articolo["totale_riga"]))
            self.table_articoli.setItem(i, 5, item)
            remove_button = QPushButton("Rimuovi")
            remove_button = remove_button
            remove_button.clicked.connect(self.deleteClicked)
            self.table_articoli.setCellWidget(i, 6, remove_button)
            i = i + 1

        self.totale = 0

        for articolo in self.carrello_acquisti:
            self.totale += articolo["totale_riga"]
        self.label_totale.setText("Totale: €{}".format(self.truncate(self.totale, 2)))

    @QtCore.pyqtSlot()
    def deleteClicked(self):
        button = self.sender()
        if button:
            row = self.table_articoli.indexAt(button.pos()).row()
            self.table_articoli.removeRow(row)
            self.carrello_acquisti.pop(row)
            self.show_table_items()

    def controllo_inserimento(self):
        if self.search_bar_quantita.text() == "":
            QMessageBox.critical(self, 'Errore',
                                 "Il campo Quantità è vuoto!",
                                 QMessageBox.Ok, QMessageBox.Ok)
        elif not self.is_int(self.search_bar_quantita.text()):
            QMessageBox.critical(self, 'Errore',
                                 "Il campo Quantità deve contenere un numero intero!",
                                 QMessageBox.Ok, QMessageBox.Ok)
        else:
            if not self.carrello_acquisti:
                self.add_articolo_in_scontrino()
            else:
                self.codici = []
                for articolo in self.carrello_acquisti:
                    self.codici.append(articolo["codice"])
                if self.search_bar_articolo.text() in self.codici:
                    QMessageBox.critical(self, 'Errore',
                                         "L'articolo {} è già presente in lista!".format(self.search_bar_articolo.text()),
                                         QMessageBox.Ok, QMessageBox.Ok)
                else:
                    self.add_articolo_in_scontrino()

    def crea_scontrino(self):
        if not self.is_int(self.edit_giorno_scontrino.text()) or not self.is_int(self.edit_mese_scontrino.text()) or not self.is_int(self.edit_anno_scontrino.text()):
            QMessageBox.critical(self, 'Errore!', 'Per favore, inserisci una data valida.',
                                 QMessageBox.Ok, QMessageBox.Ok)
            return
        elif not int(self.edit_giorno_scontrino.text()) > 0 or not int(self.edit_giorno_scontrino.text()) < 32 \
                or not int(self.edit_mese_scontrino.text()) > 0 or not int(self.edit_mese_scontrino.text()) < 13 \
                or not int(self.edit_anno_scontrino.text()) > 2020 or not int(self.edit_anno_scontrino.text()):
            QMessageBox.critical(self, 'Errore!', 'Per favore, inserisci una data valida',
                                 QMessageBox.Ok, QMessageBox.Ok)
            return
        elif not self.carrello_acquisti:
            QMessageBox.critical(self, 'Errore!', 'Per favore, inserisci almeno un articolo.',
                                 QMessageBox.Ok, QMessageBox.Ok)
            return
        else:
            for articolo in self.carrello_acquisti:
                stock_massimo = self.controller_articoli.get_stock_by_codice(articolo["codice"])
                if int(articolo["quantita"]) > stock_massimo:
                    QMessageBox.critical(self, 'Errore!', 'Non ci sono abbastanza scorte nel magazzino!',
                                         QMessageBox.Ok, QMessageBox.Ok)
                    return
            for articolo in self.carrello_acquisti:
                self.controller_articoli.scarico(articolo["codice"], articolo["quantita"])

        self.data = self.edit_giorno_scontrino.text() + '-' + self.edit_mese_scontrino.text() + '-' + self.edit_anno_scontrino.text()
        self.controller_scontrini.model.numero_scontrino = self.controller_scontrini.model.numero_scontrino+1
        self.controller_scontrini.aggiungi_scontrino(Scontrino(self.numero_scontrino, self.data,
                                                                   self.carrello_acquisti, self.totale))
        self.callback_magazzino()
        self.callback_scontrini()
        self.close()

    def is_int(self, val):
        try:
            num = int(val)
        except ValueError:
            return False
        return True

    def truncate(self, f, n):
        s = '{}'.format(f)
        if 'e' in s or 'E' in s:
            return '{0:.{1}f}'.format(f, n)
        i, p, d = s.partition('.')
        return '.'.join([i, (d + '0' * n)[:n]])