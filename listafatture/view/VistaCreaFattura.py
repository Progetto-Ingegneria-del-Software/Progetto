from PyQt5.QtWidgets import QAbstractItemView, QHeaderView, QTableWidget, QWidget, QVBoxLayout, QLabel, QLineEdit, QSpacerItem, QSizePolicy, QPushButton, \
    QMessageBox, QGridLayout

from fattura.model.Fattura import Fattura
from cliente.model.Cliente import Cliente
from listaclienti.controller.Controllore_Lista_clienti import Controllore_Lista_clienti
from listaclientiPIva.control.Controllore_lista_clientipiva import Controllore_lista_clientipiva
from listafornitori.control.ControlloreListaFornitori import ControlloreListaFornitori
from fattura.controller.ControlloreFattura import ControlloreFattura

class VistaCreaFattura(QWidget):
    def __init__(self, controller, callback):
        super(VistaCreaFattura, self).__init__()

        tipo_fatt = self.messaggio_tipo_fattura(ControlloreFattura.get_tipo_fattura())  # Viene stabilito il tipo di fattura Carico/Scarico
        
        #Se la fattura è di scarico allora viene lanciato il popup per la scelta del tipo di cliente
        if tipo_fatt == 'Scarico':
            tipo_cliente = self.messaggio_tipo_cliente(ControlloreFattura.get_tipo_cliente())
            if tipo_cliente == 'Privato':
                self.labels = ["Data:", "Cliente"]  # Nomi delle labels dei dati da prendere in input
            else:
                self.labels = ["Data:", "Cliente Partita IVA"]  # Nomi delle labels dei dati da prendere in input  
        else: #Altrimenti il tipo di cliente viene impostato come Fornitore
            tipo_cliente = 'Fornitore'
            self.labels = ["Data:", "Fornitore:"]  # Nomi delle labels dei dati da prendere in input 

        self.controller = controller
        self.callback = callback
        self.info = {}

        self.v_layout = QVBoxLayout()
        self.grid_layout = QGridLayout()

        self.add_item_view(tipo_cliente)

        self.v_layout.addLayout(self.grid_layout)

        self.v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        

        btn_ok = QPushButton("Crea")
        btn_ok.clicked.connect(lambda: self.add_fattura(tipo_cliente))

        self.v_layout.addWidget(btn_ok)

        self.setLayout(self.v_layout)
        self.resize(400, 300)
        self.setFixedSize(self.size())
        self.setWindowTitle("Crea Fattura")


    ###########################################
    ##  INTERFACCIA DI INSERIMENTO DEI DATI  ##
    ###########################################
    def add_item_view(self, tipo_cliente):
        ## PRIMA LABEL "DATA"
        self.grid_layout.addWidget(QLabel(self.labels[0]), 1, 0)
        self.current_text_edit = QLineEdit(self)
        self.current_text_edit.returnPressed.connect(lambda: self.add_fattura(tipo_cliente))
        self.grid_layout.addWidget(self.current_text_edit, 1, 1)
        self.info["Data:"] = self.current_text_edit

        ## SECONDA LABEL
        self.grid_layout.addWidget(QLabel(self.labels[1]), 2, 0)
        self.search_bar = QLineEdit(self)
        self.search_bar.returnPressed.connect(lambda: self.filter(tipo_cliente))
        self.grid_layout.addWidget(self.search_bar, 1, 1)
        self.table_view = QTableWidget()
        
        if tipo_cliente == 'Privato': #Caso in cui è stato impostato il Cliente Privato
            controller = Controllore_Lista_clienti
            self.table_view.setRowCount(len(self.controller.model.lista_clienti))
            self.table_view.setColumnCount(7)
            self.show_table_view_items(self.controller.get_lista_clienti())
        elif tipo_cliente == 'IVA': #Caso in cui è stato impostato il Cliente con Partita IVA
            

        self.table_view.setHorizontalHeaderLabels(self.name_colonne)
        self.table_view.verticalHeader().setVisible(False)
        self.table_view.setAlternatingRowColors(True)
        self.table_view.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_view.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table_view.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.table_view.resizeColumnsToContents()
        self.table_view.resizeRowsToContents()

        self.table_view.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        #if tipo_cliente == 'Privato': #Caso in cui è stato impostato il Cliente Privato
            
        #elif tipo_cliente == 'IVA': #Caso in cui è stato impostato il Cliente con Partita IVA
            
        #else: #Caso in cui è stato impostato il Fornitore
            

        self.current_text_edit = QLineEdit(self)
        self.current_text_edit.returnPressed.connect(self.add_fattura(tipo_cliente))
        self.grid_layout.addWidget(self.current_text_edit, 1, 1)


        
        i=0
        for name in self.labels:
            self.grid_layout.addWidget(QLabel(name), i, 0)
            self.current_text_edit = QLineEdit(self)
            self.current_text_edit.returnPressed.connect(self.add_fattura(tipo_cliente))
            self.grid_layout.addWidget(self.current_text_edit, i, 1)
            self.info[name] = self.current_text_edit
            i = i+1


    ###########################################
    ##  FUNZIONE CHE PERMETTE LA CREAZIONE   ## 
    ##             DELLA FATTURA             ##
    ###########################################
    def add_fattura(self, tipo_cliente):
        numero_fattura = self.info["Numero:"].text()
        data = self.info["Data:"].text()

        if tipo_cliente == 'Privato': #Caso in cui è stato impostato il Cliente Privato
            cliente = self.info["Cliente:"].text()
            if numero_fattura == "" or data == "" or cliente == "":
                QMessageBox.critical(self, 'Errore di compilazione!', 'Per favore, inserisci tutte le informazioni richieste.', QMessageBox.Ok, QMessageBox.Ok)
            else:
                self.controller.model.numero_fattura = self.controller.model.numero_fattura+1
                #self.controller.aggiungi_fattura(Fattura(self.controller.model.numero_fattura, gruppo_merciologico, categoria, marca, prezzo_unitario, None, None))   #CONTROLLARE QUESTA FUNZIONE
                self.callback()
                self.close()

        elif tipo_cliente == 'IVA': #Caso in cui è stato impostato il Cliente con Partita IVA
            cliente = self.info["Cliente Partita IVA:"].text()
            if numero_fattura == "" or data == "" or cliente == "":
                QMessageBox.critical(self, 'Errore di compilazione!', 'Per favore, inserisci tutte le informazioni richieste.', QMessageBox.Ok, QMessageBox.Ok)
            else:
                self.controller.model.numero_fattura = self.controller.model.numero_fattura+1
                #self.controller.aggiungi_fattura(Fattura(self.controller.model.numero_fattura, gruppo_merciologico, categoria, marca, prezzo_unitario, None, None))   #CONTROLLARE QUESTA FUNZIONE
                self.callback()
                self.close()
        
        else:  #Caso in cui è stato impostato il Fornitore
            fornitore = self.info["Fornitore:"].text()
            if numero_fattura == "" or data == "" or fornitore == "":
                QMessageBox.critical(self, 'Errore di compilazione!', 'Per favore, inserisci tutte le informazioni richieste.', QMessageBox.Ok, QMessageBox.Ok)
            else:
                self.controller.model.numero_fattura = self.controller.model.numero_fattura+1
                #self.controller.aggiungi_fattura(Fattura(self.controller.model.numero_fattura, gruppo_merciologico, categoria, marca, prezzo_unitario, None, None))   #CONTROLLARE QUESTA FUNZIONE
                self.callback()
                self.close()

        
    ###########################################
    ##  FUNZIONE CHE MOSTRA UN POPUP PER LA  ## 
    ##      SCELTA DEL TIPO DI FATTURA       ##
    ###########################################
    def messaggio_tipo_fattura(self, tipo_fatt):
        message_tipo = QMessageBox.question(self, 'Che tipo di fattura vuoi creare?', 'Carico o Scarico?', QMessageBox.Carico, QMessageBox.Scarico)
        if message_tipo == QMessageBox.Carico:
            tipo_fatt = 'Carico'
        else:
            tipo_fatt = 'Scarico'


    ###########################################
    ##  FUNZIONE CHE MOSTRA UN POPUP PER LA  ## 
    ##      SCELTA DEL TIPO DI CLIENTE       ##
    ##                                       ##
    ##    PRE-CONDIZIONE: La fattura deve    ##
    ##        essere di tipo "SCARICO"       ##
    ###########################################
    def messaggio_tipo_cliente(self, tipo_cliente):
        message_tipo = QMessageBox.question(self, 'Che tipo di cliente richiede la fattura?', 'Cliente Privato o possessore di Partita IVA?', QMessageBox.Privato, QMessageBox.Partita_IVA)
        if message_tipo == QMessageBox.Privato:
            tipo_cliente = 'Privato'
        else:
            tipo_cliente = 'IVA'

    
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