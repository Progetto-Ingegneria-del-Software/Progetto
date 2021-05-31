from fattura.model.Fattura import Fattura
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, \
    QAbstractItemView, QHeaderView, QMessageBox, QLineEdit, QLabel

from fattura.view.VistaFatturaNuova import VistaFatturaNuova
from listafatture.controller.ControlloreListaFatture import ControlloreListaFatture
from fattura.controller.ControlloreFattura import ControlloreFattura
from listafatture.view.VistaScegliFattura import VistaScegliFattura


class VistaListaFatture(QWidget):
    def __init__(self, controller_articoli, callback_magazzino):
        super(VistaListaFatture, self).__init__()

        self.controller = ControlloreListaFatture()
        self.controller_articoli = controller_articoli
        self.callback_magazzino = callback_magazzino
        self.name_colonne = ['Numero Fattura', 'Tipo', 'Data', 'Cliente/Fornitore', 'Totale Prezzo']  # Nomi delle colonne della tabella delle fatture

        self.v_layout = QVBoxLayout()
        self.table_view = QTableWidget()
        self.navbar_layout = QHBoxLayout()

        ## PULSANTE CHE MOSTRA L'INTERA LISTA DI FATTURE
        self.show_all_button = QPushButton("Mostra tutto")
        self.show_all_button.clicked.connect(self.update_table_view)
        self.navbar_layout.addWidget(self.show_all_button)

        ## BARRA DI RICERCA PER RICERCARE UNA FATTURA SPECIFICA
        self.search_label = QLabel("Cerca tra le fatture:")
        self.navbar_layout.addWidget(self.search_label)
        self.search_bar = QLineEdit("Inserire il numero della fattura")
        self.navbar_layout.addWidget(self.search_bar)
        self.navbar_layout.addStretch()
        self.search_bar.returnPressed.connect(self.filter_fatture)  ## LA BARRA DI RICERCA RICHIAMA LA FUNZIONE filter_fatture
        self.v_layout.addLayout(self.navbar_layout)

        self.update_table_view()

        self.table_view.setHorizontalHeaderLabels(self.name_colonne)
        self.table_view.verticalHeader().setVisible(False)
        self.table_view.setAlternatingRowColors(True)
        self.table_view.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_view.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table_view.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.table_view.resizeColumnsToContents()
        self.table_view.resizeRowsToContents()

        self.table_view.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.table_view.doubleClicked.connect(self.show_selected_info)

        self.v_layout.addWidget(self.table_view)

        ## BOTTONE CHE RICHIAMA LA FUNZIONE show_selected_info PER LA VISUALIZZAZIONE DELLA FATTURA SELEZIONATA
        self.buttons_layout = QHBoxLayout()
        self.open_button = QPushButton("Visualizza Fattura")
        self.open_button.clicked.connect(self.show_selected_info)

        self.buttons_layout.addWidget(self.open_button)
        self.v_layout.addLayout(self.buttons_layout)

        ## BOTTONE CHE RICHIAMA LA FUNZIONE show_crea_fattura PER LA CREAZIONE DI UNA NUOVA FATTURA
        self.insert_button = QPushButton("Crea fattura")
        self.insert_button.clicked.connect(self.show_crea_fattura)
        self.buttons_layout.addWidget(self.insert_button)
        self.v_layout.addLayout(self.buttons_layout)

        self.setLayout(self.v_layout)
        self.resize(1500, 480)
        self.setWindowTitle("Fatture")


    #############################################
    ###  FUNZIONE CHE EFFETTUA IL FILTRAGGIO  ###
    ###    DELLE FATTURE IN BASE AL NUMERO    ###
    #############################################
    def filter_fatture(self):
        self.table_view.clearContents()
        self.table_view.model().removeRows(0, self.table_view.rowCount())

        filter_list = []
        ## In questo ciclo vengono iterate tutte le fatture in cerca di quella con il numero cercato ##
        for fattura in self.controller.get_lista_fatture():

            if self.search_bar.text() in  fattura.num_fatt  or fattura.num_fatt in self.search_bar.text():
                filter_list.append(fattura)  # Una volta trovata la fattura viene messa in append alla lista

        self.table_view.setRowCount(len(filter_list))
        self.table_view.setColumnCount(7)
        self.show_table_view_items(filter_list)


    ####################################################
    ###  FUNZIONE CHE MOSTRA LE INFORMAZIONI DI UNA  ###
    ###       FATTURA SELEZIONATA NELLA LISTA        ###
    ####################################################
    def show_selected_info(self):
        if self.table_view.selectedIndexes():
            self.vista_fattura = VistaFatturaNuova(self.controller.get_fattura_by_index(
                int(self.table_view.item(self.table_view.selectionModel().currentIndex().row(), 0).text())-1), self.update_table_view)
            self.vista_fattura.show()


    #####################################################
    ###  FUNZIONE CHE MOSTRA L'INTERFACCIA DI SCELTA  ###
    ###             DEL TIPO DI FATTURA               ###
    #####################################################
    def show_crea_fattura(self):
        self.vista_scegli_fattura = VistaScegliFattura(self.controller_articoli, self.controller, self.update_table_view, self.callback_magazzino)  ## CONTROLLARE GLI ARGOMENTI DA PASSARE A Vista_Scegli_Fattura
        self.vista_scegli_fattura.show()


    ##########################################
    ###  FUNZIONE CHE AGGIORNA LA TABELLA  ###
    ##########################################
    def update_table_view(self):
        self.controller.save_data()
        self.table_view.setRowCount(len(self.controller.model.lista_fatture))
        self.table_view.setColumnCount(5)
        self.show_table_view_items(self.controller.get_lista_fatture())


    ###########################################
    ###  FUNZIONE CHE STAMPA OGNI ELEMENTO  ###
    ###      DELLA LISTA DELLE FATTURE      ###
    ###########################################
    def show_table_view_items(self, item_list):
        i = 0
        for fattura in item_list:
            item = QTableWidgetItem(str(fattura.num_fatt))
            self.table_view.setItem(i, 0, item)
            item = QTableWidgetItem(str(fattura.tipo_fatt))
            self.table_view.setItem(i, 1, item)
            item = QTableWidgetItem(str(fattura.data))
            self.table_view.setItem(i, 2, item)
            if "ragione_sociale" in fattura.soggetto:
                item = QTableWidgetItem(str(fattura.soggetto["ragione_sociale"]))
            elif "cf" in fattura.soggetto:
                item = QTableWidgetItem(str(fattura.soggetto["cf"]))
            self.table_view.setItem(i, 3, item)
            item = QTableWidgetItem("€" + str(fattura.totale))
            self.table_view.setItem(i, 4, item)
            i = i + 1


    def closeEvent(self, event):
        self.controller.save_data()
        event.accept()
