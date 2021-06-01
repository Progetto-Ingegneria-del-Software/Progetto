from os import times
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, \
    QAbstractItemView, QHeaderView, QMessageBox, QLineEdit, QLabel

from scontrino.view.VistaScontrino import VistaScontrino
from listascontrini.controller.ControlloreListaScontrini import ControlloreListaScontrini
from listascontrini.view.VistaCreaScontrino import VistaCreaScontrino

class VistaListaScontrini(QWidget):
    def __init__(self, controller_articoli, callback_magazzino):
        super(VistaListaScontrini, self).__init__()

        self.controller = ControlloreListaScontrini()
        self.controller_articoli = controller_articoli
        self.callback_magazzino = callback_magazzino
        self.name_colonne = ['Numero Scontrino', 'Data', 'Totale Prezzo']  # Nomi delle colonne della tabella degli scontrini

        self.v_layout = QVBoxLayout()
        self.table_view = QTableWidget()
        self.navbar_layout = QHBoxLayout()

        ## PULSANTE CHE MOSTRA L'INTERA LISTA DI SCONTRINI
        self.show_all_button = QPushButton("Mostra tutto")
        self.show_all_button.clicked.connect(self.update_table_view)
        self.navbar_layout.addWidget(self.show_all_button)

        ## BARRA DI RICERCA PER RICERCARE UNO SCONTRINI SPECIFICO
        self.search_label = QLabel("Cerca tra gli scontrini:")
        self.navbar_layout.addWidget(self.search_label)
        self.search_bar = QLineEdit("Inserire il numero dello scontrino")
        self.navbar_layout.addWidget(self.search_bar)
        self.navbar_layout.addStretch()
        self.search_bar.returnPressed.connect(self.filter_scontrini)  ## LA BARRA DI RICERCA RICHIAMA LA FUNZIONE filter_scontrini
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

        ## BOTTONE CHE RICHIAMA LA FUNZIONE show_selected_info PER LA VISUALIZZAZIONE DELLO SCONTRINO SELEZIONATO
        self.buttons_layout = QHBoxLayout()
        self.open_button = QPushButton("Visualizza Scontrino")
        self.open_button.clicked.connect(self.show_selected_info)

        self.buttons_layout.addWidget(self.open_button)
        self.v_layout.addLayout(self.buttons_layout)

        ## BOTTONE CHE RICHIAMA LA FUNZIONE delete_scontrino PER LA ELIMINAZIONE DI UNO SCONTRINO
        self.delete_button = QPushButton("Elimina scotrino")
        self.delete_button.clicked.connect(self.delete_scontrino)
        self.buttons_layout.addWidget(self.delete_button)
        self.v_layout.addLayout(self.buttons_layout)

        ## BOTTONE CHE RICHIAMA LA FUNZIONE show_crea_scontrino PER LA CREAZIONE DI UNO NUOVO SCONTRINO
        self.insert_button = QPushButton("Crea scotrino")
        self.insert_button.clicked.connect(self.show_crea_scontrino)
        self.buttons_layout.addWidget(self.insert_button)
        self.v_layout.addLayout(self.buttons_layout)

        self.setLayout(self.v_layout)
        self.resize(1500, 480)
        self.setWindowTitle("Scontrini")


    #############################################
    ###  FUNZIONE CHE EFFETTUA IL FILTRAGGIO  ###
    ###   DEGLI SCONTRINI IN BASE AL NUMERO   ###
    #############################################
    def filter_scontrini(self):
        self.table_view.clearContents()
        self.table_view.model().removeRows(0, self.table_view.rowCount())

        filter_list = []
        ## In questo ciclo vengono iterati tutti gli scontrini in cerca di quello con il numero cercato ##
        for scontrino in self.controller.get_lista_scontrini():

            if self.search_bar.text() in  scontrino.num_scontrino  or scontrino.num_scontrino in self.search_bar.text():
                filter_list.append(scontrino)  # Una volta trovata la fattura viene messa in append alla lista

        self.table_view.setRowCount(len(filter_list))
        self.table_view.setColumnCount(7)
        self.show_table_view_items(filter_list)


    ####################################################
    ###  FUNZIONE CHE MOSTRA LE INFORMAZIONI DI UNO  ###
    ###      SCONTRINO SELEZIONATO NELLA LISTA       ###
    ####################################################
    def show_selected_info(self):
        if self.table_view.selectedIndexes():
            self.vista_fattura = VistaScontrino(self.controller.get_scontrino_by_numero(
                int(self.table_view.item(self.table_view.selectionModel().currentIndex().row(), 0).text())), self.update_table_view, self.callback_magazzino, self.controller, self.controller_articoli)
            self.vista_fattura.show()


    #####################################################
    ###  FUNZIONE CHE MOSTRA L'INTERFACCIA DI SCELTA  ###
    ###             DEL TIPO DI FATTURA               ###
    #####################################################
    def show_crea_scontrino(self):
        self.registratore_cassa = QMessageBox.information(self, "Collegamento...", 
                                    "Collegamento al registratore di cassa in corso..." + '\n \n' + "Cliccare su OK per avanzare alla creazione dello scontrino!") # Avviso di collegamento al registratore di cassa.
                                                                                                                                                                   # Non avviene nessun collegamento reale, questo è un esempio.
                                                                                                                                                                   # Visionare il Diagramma dei sistemi
        self.vista_crea_scontrino = VistaCreaScontrino(self.controller, self.controller_articoli, self.update_table_view, self.callback_magazzino) # Viene aperta l'interfaccia di creazione dello scontrino
        self.vista_crea_scontrino.show()

    def delete_scontrino(self):
        if self.table_view.selectedIndexes():
            scontrino_selezionato = self.controller.get_scontrino_by_numero(
                int(self.table_view.item(self.table_view.selectionModel().currentIndex().row(), 0).text()))
            delete_view = QMessageBox.warning(self, 'Vuoi davvero eliminare lo scontrino '  + str(scontrino_selezionato.num_scontrino) + '?',
                                          'Lo scontrino numero ' + str(scontrino_selezionato.num_scontrino) +' sarà permanentemente eliminato dal sistema.\nVuoi continuare?',
                                          QMessageBox.Yes,
                             QMessageBox.No)
            if delete_view == QMessageBox.Yes:
                self.riassegna_articoli_in_magazzino(scontrino_selezionato)
                self.callback_magazzino()
                self.controller.elimina_scontrino_by_numero(scontrino_selezionato.num_scontrino)
                self.update_table_view()

    def riassegna_articoli_in_magazzino(self, scontrino):
        for articolo_da_riassegnare in scontrino.articoli:
            for articolo in self.controller_articoli.get_lista_articoli():
                if articolo.codice == articolo_da_riassegnare["codice"]:
                    self.controller_articoli.inserimento_carico(articolo.codice, articolo_da_riassegnare["quantita"])


    ##########################################
    ###  FUNZIONE CHE AGGIORNA LA TABELLA  ###
    ##########################################
    def update_table_view(self):
        self.controller.save_data()
        self.table_view.setRowCount(len(self.controller.model.lista_scontrini))
        self.table_view.setColumnCount(3)
        self.show_table_view_items(self.controller.get_lista_scontrini())


    ###########################################
    ###  FUNZIONE CHE STAMPA OGNI ELEMENTO  ###
    ###     DELLA LISTA DEGLI SCONTRINI     ###
    ###########################################
    def show_table_view_items(self, item_list):
        i = 0
        for scontrino in item_list:
            item = QTableWidgetItem(str(scontrino.num_scontrino))
            self.table_view.setItem(i, 0, item)
            item = QTableWidgetItem(str(scontrino.data))
            self.table_view.setItem(i, 1, item)
            item = QTableWidgetItem("€" + str(scontrino.totale))
            self.table_view.setItem(i, 2, item)
            i = i + 1


    def closeEvent(self, event):
        self.controller.save_data()
        event.accept()
