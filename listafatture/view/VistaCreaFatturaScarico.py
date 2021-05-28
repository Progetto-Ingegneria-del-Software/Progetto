from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QComboBox, QPushButton, QTableWidget, \
    QAbstractItemView, QHeaderView, QTableWidgetItem, QMessageBox

from listaarticoli.controller.ControlloreListaArticoli import ControlloreListaArticoli
from listaclienti.controller.Controllore_Lista_clienti import Controllore_Lista_clienti
from listaclientiPIva.control.Controllore_lista_clientipiva import Controllore_lista_clientipiva
from listafatture.controller.ControlloreListaFatture import ControlloreListaFatture
from listafornitori.control.ControlloreListaFornitori import ControlloreListaFornitori


class VistaCreaFatturaScarico(QWidget):
    def __init__(self):
        super(VistaCreaFatturaScarico, self).__init__()

        self.tipo_fattura = "Scarico"
        self.controller = ControlloreListaFatture()
        self.carrello_acquisti = []
        self.lista_totali_riga = []

        self.bold_font = QtGui.QFont()
        self.bold_font.setBold(True)

        self.italic_font = QtGui.QFont()
        self.italic_font.setItalic(True)

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

        self.h_layout1 = QHBoxLayout()

        self.label_tipo_cliente = QLabel("Destinatario:")
        self.h_layout1.addWidget(self.label_tipo_cliente)
        self.tipo_cliente = QComboBox(self)
        self.tipo_cliente.addItems(["Cliente","ClientePIVA"])
        self.tipo_cliente.activated[str].connect(self.combobox_change)
        self.tipo_cliente.setFixedWidth(135)
        self.tipo_cliente.setFont(self.bold_font)
        self.h_layout1.addWidget(self.tipo_cliente)
        self.h_layout1.addStretch()
        self.v_layout.addLayout(self.h_layout1)

        self.label_search_cliente = QLabel("Dati Cliente:")
        self.label_search_cliente.setFont(self.bold_font)
        self.v_layout.addWidget(self.label_search_cliente)
        self.search_bar_cliente = QLineEdit("Inserisci il codice fiscale del cliente")
        self.search_bar_cliente.setFont(self.italic_font)
        self.search_bar_cliente.setFixedWidth(300)
        self.v_layout.addWidget(self.search_bar_cliente)
        self.search_bar_cliente.returnPressed.connect(lambda: self.search_cliente(self.tipo_cliente.currentText()))

        self.h_layout2 = QHBoxLayout()
        self.label_dati1_cliente = QLabel("Codice ID: Nome: Cognome: CF:")
        self.h_layout2.addWidget(self.label_dati1_cliente)
        self.v_layout.addLayout(self.h_layout2)
        self.h_layout3 = QHBoxLayout()
        self.label_dati2_cliente = QLabel("Email: Telefono: Indirizzo:")
        self.h_layout3.addWidget(self.label_dati2_cliente)
        self.v_layout.addLayout(self.h_layout3)

        self.h_layout4 = QHBoxLayout()

        self.label_search_articolo = QLabel("Dati Articolo/i:")
        self.label_search_articolo.setFont(self.bold_font)
        self.h_layout4.addWidget(self.label_search_articolo)
        self.search_bar_articolo = QLineEdit("Inserisci il codice a barre dell'articolo")
        self.search_bar_articolo.setFont(self.italic_font)
        self.search_bar_articolo.setFixedWidth(300)
        self.h_layout4.addWidget(self.search_bar_articolo)
        self.label_quantita = QLabel("Quantità:")
        self.h_layout4.addWidget(self.label_quantita)
        self.search_bar_quantita = QLineEdit()
        self.search_bar_quantita.setFixedWidth(50)
        self.h_layout4.addWidget(self.search_bar_quantita)
        self.search_button = QPushButton("Aggiungi Articolo")
        self.h_layout4.addWidget(self.search_button)
        self.search_button.pressed.connect(self.controllo_inserimento)
        self.h_layout4.addStretch()

        self.v_layout.addLayout(self.h_layout4)

        self.table_articoli = QTableWidget()
        self.table_articoli.setColumnCount(6)
        self.table_articoli.setRowCount(0)
        self.table_articoli.setHorizontalHeaderLabels(
            ["Codice", "Descrizione", "Prezzo Unitario", "Sconto", "Quantità", "Totale Riga"])
        self.table_articoli.verticalHeader().setVisible(False)
        self.table_articoli.setAlternatingRowColors(True)
        self.table_articoli.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_articoli.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table_articoli.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.table_articoli.resizeColumnsToContents()
        self.table_articoli.resizeRowsToContents()

        self.table_articoli.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.v_layout.addWidget(self.table_articoli)

        self.h_layout5 = QHBoxLayout()

        self.label_totale = QLabel("Totale: €0")
        self.label_totale.setFont(self.bold_font)
        self.h_layout5.addWidget(self.label_totale)

        self.crea_fattura_button = QPushButton("Crea Fattura")
        # self.crea_fattura_button.pressed.connect(self.crea_fattura)
        self.h_layout5.addWidget(self.crea_fattura_button)

        self.v_layout.addLayout(self.h_layout5)

        self.setLayout(self.v_layout)
        self.resize(800, 600)
        self.setFixedSize(self.size())
        self.setWindowTitle("Fattura Numero {}".format(self.controller.get_assegnamento_numero_fattura()))

    def combobox_change(self):
        if self.tipo_cliente.currentText() == "Cliente":
            self.label_search_cliente.setText("Dati Cliente:")
            self.search_bar_cliente.setText("Inserisci il codice fiscale del cliente")
            self.label_dati1_cliente.setText("Codice ID: Nome: Cognome: CF:")
            self.label_dati2_cliente.setText("Email: Telefono: Indirizzo:")
        elif self.tipo_cliente.currentText() == "ClientePIVA":
            self.label_search_cliente.setText("Dati ClientePIVA:")
            self.search_bar_cliente.setText("Inserisci la partita iva del cliente")
            self.label_dati1_cliente.setText("Codice ID: Ragione Sociale: Partita IVA: Città:")
            self.label_dati2_cliente.setText("Indirizzo: Telefono: Email:")

    def search_cliente(self, tipologia_cliente):
        if tipologia_cliente == "Cliente":
            self.controller_cliente = Controllore_Lista_clienti()
            self.lista_clienti = self.controller_cliente.get_lista_clienti()

            for cliente in self.lista_clienti:
                if self.search_bar_articolo.text().upper() in cliente.cf.upper() \
                        or cliente.cf.upper() in self.search_bar_articolo.text().upper():
                    self.label_dati1_cliente.setText("Codice ID: {} Nome: {} Cognome: {} CF: {}".format(cliente.codice_id, cliente.nome, cliente.cognome, cliente.cf))
                    self.label_dati2_cliente.setText("Email: {} Telefono: {} Indirizzo: {}".format(cliente.email, cliente.telefono, cliente.indirizzo))


        elif tipologia_cliente == "ClientePIVA":
            self.controller_cliente_piva = Controllore_lista_clientipiva()
            self.lista_clienti_piva = self.controller_cliente_piva.get_lista_clientipiva()

            for cliente in self.lista_clienti_piva:
                if self.search_bar_articolo.text().upper() in cliente.partita_iva \
                        or cliente.partita_iva in self.search_bar_articolo.text().upper():
                    self.label_dati1_cliente.setText("Codice ID: {}, Ragione Sociale: {}, Partita IVA: {}, Città: {}".format(cliente.codice_id, cliente.ragione_sociale, cliente.partita_iva, cliente.citta, cliente.indirizzo, cliente.telefono, cliente.email))
                    self.label_dati2_cliente.setText("Indirizzo: {}, Telefono: {}, Email: {}".format(cliente.indirizzo, cliente.telefono, cliente.email))

    def add_articolo_in_fattura(self):
        self.controllore_articoli = ControlloreListaArticoli()
        self.lista_articoli = self.controllore_articoli.get_lista_articoli()

        for articolo in self.lista_articoli:

            if self.search_bar_articolo.text() == articolo.codice:
                self.totale_riga = articolo.prezzo_unitario * int(self.search_bar_quantita.text()) - (
                            articolo.prezzo_unitario * articolo.sconto_perc / 100) * int(
                    self.search_bar_quantita.text())
                self.lista_totali_riga.append(articolo.prezzo_unitario * int(self.search_bar_quantita.text()) - (
                            articolo.prezzo_unitario * articolo.sconto_perc / 100) * int(
                    self.search_bar_quantita.text()))
                self.carrello_acquisti.append(articolo)

        self.table_articoli.setRowCount(len(self.carrello_acquisti))
        i = 0
        for articolo in self.carrello_acquisti:
            item = QTableWidgetItem(str(articolo.codice))
            self.table_articoli.setItem(i, 0, item)
            item = QTableWidgetItem(str(articolo.descrizione))
            self.table_articoli.setItem(i, 1, item)
            item = QTableWidgetItem("€" + str(articolo.prezzo_unitario))
            self.table_articoli.setItem(i, 2, item)
            item = QTableWidgetItem(str(articolo.sconto_perc) + "%")
            self.table_articoli.setItem(i, 3, item)
            item = QTableWidgetItem(self.search_bar_quantita.text())
            self.table_articoli.setItem(i, 4, item)
            item = QTableWidgetItem("€" + str(self.totale_riga))
            self.table_articoli.setItem(i, 5, item)
            i = i + 1

        self.totale = 0

        for totale_riga in self.lista_totali_riga:
            self.totale += totale_riga
        self.label_totale.setText("Totale: {}".format(self.totale))

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
                self.add_articolo_in_fattura()
            else:
                self.codici = []
                for articolo in self.carrello_acquisti:
                    self.codici.append(articolo.codice)
                if self.search_bar_articolo.text() in self.codici:
                    QMessageBox.critical(self, 'Errore',
                                         "L'articolo {} è già presente in lista!".format(articolo.codice),
                                         QMessageBox.Ok, QMessageBox.Ok)
                else:
                    self.add_articolo_in_fattura()

    def is_int(self, val):
        try:
            num = int(val)
        except ValueError:
            return False
        return True
