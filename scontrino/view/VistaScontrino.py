from PyQt5.QtWidgets import QAbstractItemView, QTableWidget, QTableWidgetItem, QTextBrowser, QWidget, QVBoxLayout, QLabel, QPushButton, QGridLayout, \
    QMessageBox

from scontrino.controller.ControlloreScontrino import ControlloreScontrino
from listaarticoli.controller.ControlloreListaArticoli import ControlloreListaArticoli


class VistaScontrino(QWidget):
    def __init__(self, scontrino, callback):
        super(VistaScontrino, self).__init__()

        self.controller = ControlloreScontrino(scontrino)
        self.callback = callback

        v_layout = QVBoxLayout()

        grid_layout = QGridLayout()

        ## NUMERO SCONTRINO ##
        label_num_scontrino = QLabel("Numero Fattura: " + str(self.controller.get_numero_scontrino()))
        grid_layout.addWidget(label_num_scontrino, 0, 0)

        ## DATA SCONTRINO ##
        label_data_scontrino = QLabel("Data: " + str(self.controller.get_data_scontrino()))
        grid_layout.addWidget(label_data_scontrino, 2, 0)

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
        self.setWindowTitle("Scontrino n: " + str(self.controller.get_numero_scontrino))


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