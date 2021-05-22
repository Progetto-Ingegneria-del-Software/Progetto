from PyQt5.QtWidgets import QAbstractItemView, QTableWidget, QTableWidgetItem, QTextBrowser, QWidget, QVBoxLayout, QLabel, QPushButton, QGridLayout, \
    QMessageBox

from fattura.controller.ControlloreFattura import ControlloreFattura
from fornitore.control.ControlloreFornitore import ControlloreFornitore
from listaarticoli.controller.ControlloreListaArticoli import ControlloreListaArticoli


class VistaFattura(QWidget):
    def __init__(self, fattura, callback):
        super(VistaFattura, self).__init__()

        self.controller = ControlloreFattura(fattura)
        self.callback = callback

        v_layout = QVBoxLayout()

        grid_layout = QGridLayout()

        ## NUMERO FATTURA ##
        label_num_fatt = QLabel("Numero Fattura: " + str(self.controller.get_numero_fattura()))
        grid_layout.addWidget(label_num_fatt, 0, 0)

        ## TIPO FATTURA (CARICO O SCARICO) ##
        label_tipo_fattura = QLabel("Tipo: " + str(self.controller.get_tipo_fattura()))
        grid_layout.addWidget(label_tipo_fattura, 1, 0)

        ## DATA FATTURA ##
        label_data_fattura = QLabel("Data: " + str(self.controller.get_data()))
        grid_layout.addWidget(label_data_fattura, 2, 0)

        ## CONTROLLO SE LA FATTURA È DI CARICO ##
        ## IN QUESTO MODO STAMPO SOLO I DATI DEL FORNITORE E NON QUELLI DEL CLIENTE ##
        if self.controller.get_tipo_fattura() == 'Carico' :
            ## DATI FORNITORE ##
            label_dati_fornitore = QLabel("Dati Fornitore:")
            grid_layout.addWidget(label_dati_fornitore, 3, 0)

            ## Ragione Sociale Fornitore ##
            label_nome_fornitore = QLabel("Ragione sociale:")
            grid_layout.addWidget(label_nome_fornitore, 4, 0)
            text_nome_fornitore = QTextBrowser(ControlloreFornitore.get_ragione_sociale_fornitore())
            text_nome_fornitore.isReadOnly(True)
            text_nome_fornitore.adjustSize
            grid_layout.addWidget(text_nome_fornitore, 4, 1)

            ## Partita Iva Fornitore ##
            label_piva_fornitore = QLabel("Partita IVA:")
            grid_layout.addWidget(label_piva_fornitore, 4, 3)
            text_piva_fornitore = QTextBrowser(ControlloreFornitore.get_partita_iva_fornitore())
            text_piva_fornitore.isReadOnly(True)
            text_piva_fornitore.adjustSize
            grid_layout.addWidget(text_piva_fornitore, 4, 4)

            ## Indirizzo Fornitore ##
            label_indirizzo_fornitore = QLabel("Indirizzo:")
            grid_layout.addWidget(label_indirizzo_fornitore, 5, 0)
            text_indirizzo_fornitore = QTextBrowser(ControlloreFornitore.get_indirizzo_fornitore())
            text_indirizzo_fornitore.isReadOnly(True)
            text_indirizzo_fornitore.adjustSize
            grid_layout.addWidget(text_indirizzo_fornitore, 5, 1)

            ## Citta Fornitore ##
            label_citta_fornitore = QLabel("Città:")
            grid_layout.addWidget(label_citta_fornitore, 5, 3)
            text_citta_fornitore = QTextBrowser(ControlloreFornitore.get_citta_fornitore())
            text_citta_fornitore.isReadOnly(True)
            text_citta_fornitore.adjustSize
            grid_layout.addWidget(text_citta_fornitore, 5, 4)

            ## Telefono Fornitore ##
            label_telefono_fornitore = QLabel("Telefono:")
            grid_layout.addWidget(label_telefono_fornitore, 6, 0)
            text_telefono_fornitore = QTextBrowser(ControlloreFornitore.get_telefono_fornitore())
            text_telefono_fornitore.isReadOnly(True)
            text_telefono_fornitore.adjustSize
            grid_layout.addWidget(text_telefono_fornitore, 6, 1)

            ## Email Fornitore ##
            label_email_fornitore = QLabel("Email:")
            grid_layout.addWidget(label_email_fornitore, 6, 3)
            text_email_fornitore = QTextBrowser(ControlloreFornitore.get_email_fornitore())
            text_email_fornitore.isReadOnly(True)
            text_email_fornitore.adjustSize
            grid_layout.addWidget(text_email_fornitore, 6, 4)


        ## LISTA DEGLI ARTICOLI COMPRATI ##
        self.tableWidget = QTableWidget() 
        self.tableWidget.setColumnCount(7) #Numero prefissato di colonne
        self.name_colonne = ['Codice ID', 'Descrizione', 'Marca', 'Prezzo Unitario',
                             'Quantità', 'Totale']
        
        self.update_table_view()  #Viene mostrata la tabella degli articoli inclusi nella fattura

        self.table_view.setHorizontalHeaderLabels(self.name_colonne)
        self.table_view.verticalHeader().setVisible(False)
        self.table_view.setAlternatingRowColors(True)
        self.table_view.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_view.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table_view.setEditTriggers(QAbstractItemView.NoEditTriggers)
        

        self.setLayout(v_layout)
        self.resize(500, 300)
        self.setFixedSize(self.size())
        self.setWindowTitle("Fattura n: " + str(self.controller.get_numero_fattura))


    ##############################################
    ###     FUNZIONE CHE MOSTRA LA TABELLA     ###
    ##############################################
    def update_table_view(self):
        self.controller.save_data()
        self.tableWidget.setRowCount(len(self.controller.model.lista_articoli))   ## CONTROLLARE QUESTA PARTE
        self.show_table_items(self.controller.get_lista_articoli())


    ##############################################
    ###     FUNZIONE CHE MOSTRA LA TABELLA     ###
    ##############################################
    def show_table_items(self, item_list):
        i = 0
        for articolo in item_list:
            item = QTableWidgetItem(str(articolo.codice_id))
            self.table_view.setItem(i, 0, item)
            item = QTableWidgetItem(str(articolo.descrizione))
            self.table_view.setItem(i, 1, item)
            item = QTableWidgetItem(str(articolo.marca))
            self.table_view.setItem(i, 2, item)
            item = QTableWidgetItem("€" + str(articolo.prezzo_unitario))
            self.table_view.setItem(i, 3, item)
            item = QTableWidgetItem(str(articolo.quantita))
            self.table_view.setItem(i, 4, item)
            item = QTableWidgetItem(str(articolo.prezzo_unitario * articolo.quantita))
            self.table_view.setItem(i, 5, item)
            
            i = i + 1


    ##############################################
    ###   FUNZIONE PER ELIMINARE UNA FATTURA   ###
    ##############################################
    #def delete_fattura(self):
   #     delete_view = QMessageBox.warning(self, 'Vuoi davvero eliminare la fattura numero:' + str(self.controller.get_numero_fattura()) + '?',
   #                                       'La fattura numero: ' + str(self.controller.get_numero_fattura()) + ' sarà permanentemente eliminato dal sistema.\nVuoi continuare?',
   #                                       QMessageBox.Yes,
    #                                      QMessageBox.No)
        
    #    if delete_view == QMessageBox.Yes:
    #        self.elimina_fattura(self.controller.get_numero_fattura())
    #        self.callback()
     #       self.close()