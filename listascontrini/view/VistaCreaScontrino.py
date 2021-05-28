from PyQt5 import QtGui
from PyQt5.QtWidgets import QAbstractItemView, QHBoxLayout, QHeaderView, QTableWidget, QTableWidgetItem, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

from scontrino.model.Scontrino import Scontrino
from scontrino.controller.ControlloreScontrino import ControlloreScontrino
from listascontrini.controller.ControlloreListaScontrini import ControlloreListaScontrini
from listaarticoli.controller.ControlloreListaArticoli import ControlloreListaArticoli

class VistaCreaScontrino(QWidget):
    def __init__(self, numero_scontrino):
        super(VistaCreaScontrino, self).__init__()

        self.controller = ControlloreListaScontrini
        #self.callback = callback
        self.numero_scontrino = numero_scontrino
        self.carrello_acquisti = []
        self.lista_totali_riga = []

        # Impostazione del font da applicare ad alcune Label
        bold_font = QtGui.QFont()
        bold_font.setBold(True)
        bold_font.setPixelSize(12)

        # Impostazione del font corsivo da applicare alla scritta interna del QLineEdit
        italic_font = QtGui.QFont()
        italic_font.setItalic(True)

        self.v_layout = QVBoxLayout()
        self.h_layout = QHBoxLayout()

        # Viene stampato il numero dello scontrino
        self.label_num_scontrino = QLabel("Scontrino numero: ")
        self.label_num_scontrino.setFont(bold_font)
        self.label_numero = QLabel("{}        ".format(self.numero_scontrino))
        self.h_layout.addWidget(self.label_num_scontrino)
        self.h_layout.addWidget(self.label_numero)

        # Viene permesso l'inserimento della Data
        self.label_data_scontrino = QLabel("Data: ")
        self.label_data_scontrino.setFont(bold_font)
        self.h_layout.addWidget(self.label_data_scontrino)
        self.edit_data_scontrino = QLineEdit("gg/mm/aaaa")
        self.edit_data_scontrino.setFixedWidth(100)
        self.h_layout.addWidget(self.edit_data_scontrino)

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
        self.label_quantita.setFont(bold_font)
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
        self.table_articoli.setColumnCount(5)
        self.table_articoli.setRowCount(0)
        self.table_articoli.setHorizontalHeaderLabels(["Codice", "Descrizione", "Prezzo Unitario", "Sconto", "Totale Riga"]) # Nomi delle colonne della tabella 
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
        self.label_totale = QLabel("Totale: €0")
        self.label_totale.setFont(bold_font)
        self.h_layout3.addWidget(self.label_totale)

        self.v_layout.addLayout(self.h_layout3)
        
        # Bottone che conferma la creazione dello scontrino
        btn_crea = QPushButton("Crea")
        #btn_crea.clicked.connect(lambda: self.add_fattura())

        self.setLayout(self.v_layout)
        self.resize(800, 350)
        self.setFixedSize(self.size())
        self.setWindowTitle("Creazione Scontrino Numero {}".format(self.numero_scontrino))

        #self.add_item_view()

        #self.v_layout.addLayout(self.grid_layout)

        #self.v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        

        #self.v_layout.addWidget(btn_ok)

        #self.setLayout(self.v_layout)
        #self.resize(400, 300)
        #self.setFixedSize(self.size())
        #self.setWindowTitle("Crea Scontrino")


    ###########################################
    ##  INTERFACCIA DI INSERIMENTO DEI DATI  ##
    ###########################################
    def add_item_view(self):
        ## PRIMA LABEL "DATA"
        self.grid_layout.addWidget(QLabel(self.labels[0]), 1, 0)
        self.current_text_edit = QLineEdit(self)
        self.current_text_edit.returnPressed.connect(lambda: self.add_scontrino())
        self.grid_layout.addWidget(self.current_text_edit, 1, 1)
        self.info["Data:"] = self.current_text_edit

        ## SECONDA LABEL
        self.grid_layout.addWidget(QLabel(self.labels[1]), 2, 0)
        self.search_bar = QLineEdit(self)
        self.search_bar.returnPressed.connect(lambda: self.filter())
        self.grid_layout.addWidget(self.search_bar, 1, 1)
        self.table_view = QTableWidget()
        
        
        self.table_view.setHorizontalHeaderLabels(self.name_colonne)
        self.table_view.verticalHeader().setVisible(False)
        self.table_view.setAlternatingRowColors(True)
        self.table_view.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_view.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table_view.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.table_view.resizeColumnsToContents()
        self.table_view.resizeRowsToContents()

        self.table_view.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.current_text_edit = QLineEdit(self)
        self.current_text_edit.returnPressed.connect(lambda: self.add_scontrino())
        self.grid_layout.addWidget(self.current_text_edit, 1, 1)


        
        i=0
        for name in self.labels:
            self.grid_layout.addWidget(QLabel(name), i, 0)
            self.current_text_edit = QLineEdit(self)
            self.current_text_edit.returnPressed.connect(lambda: self.add_scontrino())
            self.grid_layout.addWidget(self.current_text_edit, i, 1)
            self.info[name] = self.current_text_edit
            i = i+1



    #######################################################
    ##  FUNZIONE CHE AGGIUNGE L'ARTICOLI PRESO IN INPUT  ##
    ##         DENTRO LA LISTA DELLO SCONTRINO           ##
    #######################################################
    def add_articolo_in_scontrino(self):
        self.controllore_articoli = ControlloreListaArticoli()
        self.lista_articoli = self.controllore_articoli.get_lista_articoli()

        # Viene cercato l'articolo preso in input dentro la lista degli articoli dell'anagrafica articolo
        for articolo in self.lista_articoli:

            # Se c'è corrispondenza di codice a barre allora vengono inizializzate le variabili
            if self.search_bar_articolo.text() == articolo.codice:
                self.totale_riga = articolo.prezzo_unitario*int(self.search_bar_quantita.text())-(articolo.prezzo_unitario*articolo.sconto_perc/100)*int(self.search_bar_quantita.text())
                self.lista_totali_riga.append(articolo.prezzo_unitario*int(self.search_bar_quantita.text())-(articolo.prezzo_unitario*articolo.sconto_perc/100)*int(self.search_bar_quantita.text()))
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

        # Viene calcolato il totale dell'intero scontrino
        for totale_riga in self.lista_totali_riga:
            self.totale += totale_riga
        self.label_totale.setText("Totale: {}".format(self.totale))



    ###########################################
    ##  FUNZIONE CHE PERMETTE LA CREAZIONE   ## 
    ##            DELLO SCONTRINO            ##
    ###########################################
    def add_scontrino(self):
        numero_scontrino = self.info["Numero:"].text()
        data = self.info["Data:"].text()

        if numero_scontrino == "" or data == "":
            QMessageBox.critical(self, 'Errore di compilazione!', 'Per favore, inserisci tutte le informazioni richieste.', QMessageBox.Ok, QMessageBox.Ok)
        else:
            self.controller.model.numero_scontrino = self.controller.model.numero_scontrino + 1
            #self.controller.aggiungi_fattura(Fattura(self.controller.model.numero_fattura, gruppo_merciologico, categoria, marca, prezzo_unitario, None, None))   #CONTROLLARE QUESTA FUNZIONE
            self.callback()
            self.close()


    ###########################################
    ##  FUNZIONE CHE CONTROLLA IL CORRETTO   ## 
    ##  INSERIMENTO DEI DATI DELL'ARTICOLO   ##
    ###########################################
    def controllo_inserimento(self):
        if self.search_bar_quantita.text() == "":  # CASO IN CUI NON SIA STATA INSERITA NESSUNA QUANTITÀ
            QMessageBox.critical(self, 'Errore',
                                 "Il campo Quantità è vuoto!",
                                 QMessageBox.Ok, QMessageBox.Ok)
        elif not self.is_int(self.search_bar_quantita.text()):  # CASO IN CUI LA QUANTITÀ INSERITA NON SIA UN NUMERO INTERO
            QMessageBox.critical(self, 'Errore',
                                 "Il campo Quantità deve contenere un numero intero!",
                                 QMessageBox.Ok, QMessageBox.Ok)
        else:
            if not self.carrello_acquisti:
                self.add_articolo_in_scontrino()
            else:
                self.codici = []
                for articolo in self.carrello_acquisti:
                    self.codici.append(articolo.codice)
                if self.search_bar_articolo.text() in self.codici:
                    QMessageBox.critical(self, 'Errore',
                                         "L'articolo {} è già presente in lista!".format(articolo.codice),
                                         QMessageBox.Ok, QMessageBox.Ok)
                else:
                    self.add_articolo_in_scontrino()
    

    ###################################################
    ##  FUNZIONE CHE CONTROLLA CHE IL DATO IN ESAME  ## 
    ##              SIA DI TIPO INTERO               ##
    ###################################################
    def is_int(self, val):
        try:
            num = int(val)
        except ValueError:
            return False
        return True