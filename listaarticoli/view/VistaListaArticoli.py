from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, \
    QAbstractItemView, QHeaderView, QMessageBox, QLineEdit, QLabel

from articolo.view.VistaArticolo import VistaArticolo
from listaarticoli.controller.ControlloreListaArticoli import ControlloreListaArticoli
from listaarticoli.view.VistaInserisciArticolo import VistaInserisciArticolo
from listaarticoli.view.Vista_lista_articoli_magazzino import Vista_lista_articoli_magazzino


class VistaListaArticoli(QWidget):
    def __init__(self, controller, magazzino_update_table):
        super(VistaListaArticoli, self).__init__()

        self.magazzino_update_table = magazzino_update_table
        self.controller = controller
        self.name_colonne = ['Codice a Barre', 'Gruppo Merceologico', 'Categoria', 'Marca', 'Prezzo Unitario',
                   'Sconto', 'Descrizione']

        self.v_layout = QVBoxLayout()
        self.table_view = QTableWidget()
        self.navbar_layout = QHBoxLayout()

        self.show_all_button = QPushButton("Mostra tutto")
        self.show_all_button.clicked.connect(self.update_table_view)
        self.navbar_layout.addWidget(self.show_all_button)

        self.search_label = QLabel("Cerca tra gli articoli:")
        self.navbar_layout.addWidget(self.search_label)
        self.search_bar = QLineEdit("Categoria Marca")
        self.navbar_layout.addWidget(self.search_bar)

        self.navbar_layout.addStretch()
        self.search_bar.returnPressed.connect(self.filter_articoli)
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

        self.buttons_layout = QHBoxLayout()
        self.open_button = QPushButton("Visualizza Articolo")

        self.open_button.clicked.connect(self.show_selected_info)

        self.buttons_layout.addWidget(self.open_button)
        self.v_layout.addLayout(self.buttons_layout)

        self.insert_button = QPushButton("Inserisci Articolo")
        self.insert_button.clicked.connect(self.show_insert_articolo)
        self.buttons_layout.addWidget(self.insert_button)
        self.v_layout.addLayout(self.buttons_layout)

        self.delete_button = QPushButton("Elimina Articolo")
        self.delete_button.clicked.connect(self.delete_articolo)
        self.buttons_layout.addWidget(self.delete_button)
        self.v_layout.addLayout(self.buttons_layout)

        self.setLayout(self.v_layout)
        self.resize(1500, 480)
        self.setWindowTitle("Articoli")

    def filter_articoli(self):
        self.table_view.clearContents()
        self.table_view.model().removeRows(0, self.table_view.rowCount())

        filter_list = []
        for articolo in self.controller.get_lista_articoli():

            if self.search_bar.text().upper() in articolo.categoria.upper() + " " + articolo.marca.upper() \
                    or articolo.categoria.upper() + " " + articolo.marca.upper() in self.search_bar.text().upper():
                filter_list.append(articolo)

        self.table_view.setRowCount(len(filter_list))
        self.table_view.setColumnCount(7)
        self.show_table_view_items(filter_list)

    def show_selected_info(self):
        if self.table_view.selectedIndexes():
            self.vista_articolo = VistaArticolo(self.controller.get_articolo_by_codice(
            self.table_view.item(self.table_view.selectionModel().currentIndex().row(), 0).text()), self.controller, self.update_table_view, self.magazzino_update_table)
            self.vista_articolo.show()


    def show_insert_articolo(self):
        self.vista_inserisci_articolo = VistaInserisciArticolo(self.controller, self.update_table_view, self.magazzino_update_table)
        self.vista_inserisci_articolo.show()

    def delete_articolo(self):
        if self.table_view.selectedIndexes():
            articolo_selezionato = self.controller.get_articolo_by_codice(
                self.table_view.item(self.table_view.selectionModel().currentIndex().row(), 0).text())
            delete_view = QMessageBox.warning(self, 'Vuoi davvero eliminare l\'articolo '  + str(articolo_selezionato.codice) + '?',
                                          'L\'articolo ' + str(articolo_selezionato.codice) +' sarà permanentemente eliminato dal sistema.\nVuoi continuare?',
                                          QMessageBox.Yes,
                             QMessageBox.No)
            if delete_view == QMessageBox.Yes:
                self.controller.elimina_articolo_by_codice(articolo_selezionato.codice)
                self.magazzino_update_table()
                self.update_table_view()

    def update_table_view(self):
        self.controller.save_data()

        self.table_view.setRowCount(len(self.controller.model.lista_articoli))
        self.table_view.setColumnCount(7)
        self.show_table_view_items(self.controller.get_lista_articoli())

    def show_table_view_items(self, item_list):
        i = 0
        for articolo in item_list:
            item = QTableWidgetItem(str(articolo.codice))
            self.table_view.setItem(i, 0, item)
            item = QTableWidgetItem(str(articolo.gruppo_merceologico))
            self.table_view.setItem(i, 1, item)
            item = QTableWidgetItem(str(articolo.categoria))
            self.table_view.setItem(i, 2, item)
            item = QTableWidgetItem(str(articolo.marca))
            self.table_view.setItem(i, 3, item)
            item = QTableWidgetItem("€" + str(articolo.prezzo_unitario))
            self.table_view.setItem(i, 4, item)
            item = QTableWidgetItem(str(articolo.sconto_perc) + "%")
            self.table_view.setItem(i, 5, item)
            item = QTableWidgetItem(str(articolo.descrizione))
            self.table_view.setItem(i, 6, item)
            i = i + 1

    def closeEvent(self, event):
        self.controller.save_data()
        event.accept()
