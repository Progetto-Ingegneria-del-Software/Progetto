from PyQt5 import QtGui
from PyQt5.QtWidgets import QAbstractItemView, QHBoxLayout, QHeaderView, QTableWidget, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

from scontrino.model.Scontrino import Scontrino
from scontrino.controller.ControlloreScontrino import ControlloreScontrino
from listascontrini.controller.ControlloreListaScontrini import ControlloreListaScontrini

class VistaCreaScontrino(QWidget):
    def __init__(self, numero_scontrino):
        super(VistaCreaScontrino, self).__init__()

        self.controller = ControlloreListaScontrini
        #self.callback = callback
        self.numero_scontrino = numero_scontrino
        self.info = {}

        # Impostazione del font da applicare ad alcune Label
        bold_font = QtGui.QFont()
        bold_font.setBold(True)
        bold_font.setPixelSize(12)

        #self.labels = ["Data:"]

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

        # Qui inizia la tabella degli articoli acquistati
        self.label_search_articolo = QLabel("Dati Articolo/i:")
        self.label_search_articolo.setFont(bold_font)
        self.h_layout2.addWidget(self.label_search_articolo)
        self.search_bar_articolo = QLineEdit("Inserisci il codice a barre dell'articolo")
        self.search_bar_articolo.setFixedWidth(300)
        self.h_layout2.addWidget(self.search_bar_articolo)
        self.search_bar_quantita = QLineEdit()
        self.search_bar_quantita.setFixedWidth(50)
        self.h_layout2.addWidget(self.search_bar_quantita)
        self.search_button = QPushButton("Aggiungi Articolo")
        self.h_layout2.addWidget(self.search_button)
        # self.search_button.pressed.connect(self.add_articolo_in_fattura)
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
        
        # Bottone che conferma la creazione dello scontrino
        btn_ok = QPushButton("Crea")
        btn_ok.clicked.connect(lambda: self.add_fattura())

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


    def filter(self, tipo_cliente):
        if tipo_cliente == 'Privato': #Caso in cui è stato impostato il Cliente Privato
            filter_list = []
            controllore = Controllore_Lista_clienti
            for cliente in controllore.get_lista_clienti():

                if (self.search_bar.text()).upper() in cliente.nome.upper() + " " + cliente.cognome.upper() or cliente.cognome.upper() + " " + cliente.nome.upper() in (self.search_bar.text()).upper():
                    filter_list.append(cliente)

        elif tipo_cliente == 'IVA': #Caso in cui è stato impostato il Cliente con Partita IVA
            filter_list = []
            controllore = Controllore_lista_clientipiva
            for cliente in controllore.get_lista_clientipiva():

                if (self.search_bar.text()).upper() in cliente.nome.upper() + " " + cliente.cognome.upper() or cliente.cognome.upper() + " " + cliente.nome.upper() in (self.search_bar.text()).upper():
                    filter_list.append(cliente)

        else: #Caso in cui è stato impostato il Fornitore
            filter_list = []
            controllore = ControlloreListaFornitori
            for cliente in controllore.get_lista_fornitori():

                if (self.search_bar.text()).upper() in cliente.nome.upper() + " " + cliente.cognome.upper() or cliente.cognome.upper() + " " + cliente.nome.upper() in (self.search_bar.text()).upper():
                    filter_list.append(cliente)