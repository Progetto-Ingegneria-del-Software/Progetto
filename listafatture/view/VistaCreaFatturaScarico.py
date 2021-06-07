from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QComboBox, QPushButton, QTableWidget, \
    QAbstractItemView, QHeaderView, QTableWidgetItem, QMessageBox

from fattura.model.Fattura import Fattura
from listaarticoli.controller.ControlloreListaArticoli import ControlloreListaArticoli
from listaclienti.controller.Controllore_Lista_clienti import Controllore_Lista_clienti
from listaclientiPIva.control.Controllore_lista_clientipiva import Controllore_lista_clientipiva

#####################################################################
###   QUESTA CLASSE SERVE PER MOSTRARE ALL'UTENTE L'INTERFACCIA   ###
###            DI CREAZIONE DI UNA FATTURA DI SCARICO             ###
#####################################################################
class VistaCreaFatturaScarico(QWidget):
    def __init__(self, controller_articoli, controller_fattura, callback, callback_magazzino):
        super(VistaCreaFatturaScarico, self).__init__()

        self.callback = callback
        self.callback_magazzino = callback_magazzino
        self.tipo_fattura = "Scarico"
        self.controller_articoli = controller_articoli
        self.controller_fattura = controller_fattura
        self.numero_fattura = self.controller_fattura.get_assegnamento_numero_fattura() + 1
        self.data = None
        self.cliente = None
        self.carrello_acquisti = []
        self.totale = 0

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
        self.edit_giorno_fattura = QLineEdit("gg")
        self.edit_giorno_fattura.setFixedWidth(30)
        self.edit_mese_fattura = QLineEdit("mm")
        self.edit_mese_fattura.setFixedWidth(30)
        self.edit_anno_fattura = QLineEdit("aaaa")
        self.edit_anno_fattura.setFixedWidth(40)
        self.h_layout.addWidget(self.edit_giorno_fattura)
        self.h_layout.addWidget(self.edit_mese_fattura)
        self.h_layout.addWidget(self.edit_anno_fattura)

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
        self.table_articoli.setColumnCount(7)
        self.table_articoli.setRowCount(0)
        self.table_articoli.setHorizontalHeaderLabels(
            ["Codice", "Descrizione", "Prezzo Unitario", "Sconto", "Quantità", "Totale Riga", ""])
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

        self.label_totale = QLabel("Totale: €{}".format(self.totale))
        self.label_totale.setFont(self.bold_font)
        self.h_layout5.addWidget(self.label_totale)

        self.crea_fattura_button = QPushButton("Crea Fattura")
        self.crea_fattura_button.pressed.connect(self.crea_fattura)
        self.h_layout5.addWidget(self.crea_fattura_button)

        self.v_layout.addLayout(self.h_layout5)

        self.setLayout(self.v_layout)
        self.resize(950, 600)
        self.setFixedSize(self.size())
        self.setWindowTitle("Creazione Fattura Numero {}".format(self.numero_fattura))

    def combobox_change(self):
        self.cliente = None
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

    ##########################################################
    ###  METODO USATO PER CERCARE ALL'INTERNO DEL SISTEMA  ###
    ###               UN DETERMINATO CLIENTE               ###
    ##########################################################
    def search_cliente(self, tipologia_cliente):
        if tipologia_cliente == "Cliente":
            controller_cliente = Controllore_Lista_clienti()
            lista_clienti = controller_cliente.get_lista_clienti()

            for cliente in lista_clienti:
                if self.search_bar_cliente.text().upper() in cliente.cf.upper() \
                        or cliente.cf.upper() in self.search_bar_cliente.text().upper():
                    self.cliente = cliente
                    self.label_dati1_cliente.setText("Codice ID: {}, Nome: {}, Cognome: {}, CF: {},".format(cliente.codice_id, cliente.nome, cliente.cognome, cliente.cf))
                    self.label_dati2_cliente.setText("Email: {}, Telefono: {}, Città: {}, Indirizzo: {}.".format(cliente.email, cliente.telefono, cliente.citta, cliente.indirizzo))


        elif tipologia_cliente == "ClientePIVA":
            controller_cliente_piva = Controllore_lista_clientipiva()
            lista_clienti_piva = controller_cliente_piva.get_lista_clientipiva()

            for cliente in lista_clienti_piva:
                if self.search_bar_cliente.text().upper() in cliente.partita_iva.upper() \
                        or cliente.partita_iva.upper() in self.search_bar_cliente.text().upper():
                    self.cliente = cliente
                    self.label_dati1_cliente.setText("Codice ID: {}, Ragione Sociale: {}, Partita IVA: {}, Città: {},".format(cliente.codice_id, cliente.ragione_sociale, cliente.partita_iva, cliente.citta, cliente.indirizzo, cliente.telefono, cliente.email))
                    self.label_dati2_cliente.setText("Indirizzo: {}, Telefono: {}, Email: {}.".format(cliente.indirizzo, cliente.telefono, cliente.email))

    #################################################
    ###  METODO USATO PER INSERIRE NELLA FATTURA  ###
    ###                UN ARTICOLO                ###
    #################################################
    def add_articolo_in_fattura(self):
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

    ############################################
    ###  METODO USATO PER MOSTRARE LA LISTA  ###
    ###      DEGLI ARTICOLI ACQUISTATI       ###
    ############################################
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

    ################################################
    ###  METODO USATO PER RIMUOVERE UN ARTICOLO  ###
    ###    TRA QUELLI INSERITI NELLA FATTURA     ###
    ################################################
    @QtCore.pyqtSlot()
    def deleteClicked(self):
        button = self.sender()
        if button:
            row = self.table_articoli.indexAt(button.pos()).row()
            self.table_articoli.removeRow(row)
            self.carrello_acquisti.pop(row)
            self.show_table_items()

    ###########################################
    ###  METODO PER CONTROLLARE CHE I DATI  ###
    ###       INSERITI SONO CORRETTI        ###
    ###########################################
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
                    self.codici.append(articolo["codice"])
                if self.search_bar_articolo.text() in self.codici:
                    QMessageBox.critical(self, 'Errore',
                                         "L'articolo {} è già presente in lista!".format(self.search_bar_articolo.text()),
                                         QMessageBox.Ok, QMessageBox.Ok)
                else:
                    self.add_articolo_in_fattura()

    ############################################
    ###  METODO USATO PER INSERIRE LA NUOVA  ###
    ###         FATTURA NEL SISTEMA          ###
    ############################################
    def crea_fattura(self):
        if not self.is_int(self.edit_giorno_fattura.text()) or not self.is_int(self.edit_mese_fattura.text()) or not self.is_int(self.edit_anno_fattura.text()):
            QMessageBox.critical(self, 'Errore!', 'Per favore, inserisci una data valida.',
                                 QMessageBox.Ok, QMessageBox.Ok)
            return
        elif not int(self.edit_giorno_fattura.text()) > 0 or not int(self.edit_giorno_fattura.text()) < 32 \
                or not int(self.edit_mese_fattura.text()) > 0 or not int(self.edit_mese_fattura.text()) < 13 \
                or not int(self.edit_anno_fattura.text()) > 2020 or not int(self.edit_anno_fattura.text()):
            QMessageBox.critical(self, 'Errore!', 'Per favore, inserisci una data valida',
                                 QMessageBox.Ok, QMessageBox.Ok)
            return
        elif self.cliente == None:
            QMessageBox.critical(self, 'Errore!', 'Per favore, inserisci il cliente.',
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
                    QMessageBox.critical(self, 'Errore!', 'Non ci sono abbastanza scorte per l\'articolo {} nel magazzino!'.format(self.controller_articoli.get_articolo_by_codice(articolo["codice"]).codice),
                                         QMessageBox.Ok, QMessageBox.Ok)
                    return
        for articolo in self.carrello_acquisti:
            self.controller_articoli.scarico(articolo["codice"], articolo["quantita"])
        self.data = self.edit_giorno_fattura.text() + '-' + self.edit_mese_fattura.text() + '-' + self.edit_anno_fattura.text()
        self.controller_fattura.model.numero_fattura = self.controller_fattura.model.numero_fattura+1
        self.controller_fattura.aggiungi_fattura(Fattura(self.numero_fattura, self.tipo_fattura, self.data, self.cliente.__dict__,
                                                         self.carrello_acquisti, self.totale))
        self.callback_magazzino()
        self.callback()
        self.close()

    ##################################################
    ###       METODO USATO PER VERIFICARE SE       ###
    ###  UNA STRINGA PUÒ ESSERE CASTATA AD INTERO  ###
    ##################################################
    def is_int(self, val):
        try:
            num = int(val)
        except ValueError:
            return False
        return True

    ######################################
    ###  METODO USATO PER ARROTONDARE  ###
    ###   UNA VARIABILE DI TIPO FLOAT  ###
    ######################################
    def truncate(self, f, n):
        s = '{}'.format(f)
        if 'e' in s or 'E' in s:
            return '{0:.{1}f}'.format(f, n)
        i, p, d = s.partition('.')
        return '.'.join([i, (d + '0' * n)[:n]])





