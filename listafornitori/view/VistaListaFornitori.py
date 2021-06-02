from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QAbstractItemView, QHeaderView, QHBoxLayout, \
    QPushButton, QTableWidgetItem, QMessageBox, QLabel, QLineEdit

from fornitore.view.VistaFornitore import VistaFornitore
from listafornitori.control.ControlloreListaFornitori import ControlloreListaFornitori
from listafornitori.view.VistaInserisciFornitore import VistaInserisciFornitore


class VistaListaFornitori(QWidget):
    def __init__(self):
        super(VistaListaFornitori, self).__init__()

        self.controller = ControlloreListaFornitori()
        self.name_colonne = ['Codice ID', 'Ragione Sociale', 'Partita IVA', 'Città', 'Indirizzo', 'Telefono', 'Email']

        self.v_layout = QVBoxLayout()
        self.table_view = QTableWidget()
        self.navbar_layout= QHBoxLayout()

        self.show_all_button = QPushButton("Mostra tutto")
        self.show_all_button.clicked.connect(self.update_table_view)
        self.navbar_layout.addWidget(self.show_all_button)

        self.search_label = QLabel("Cerca tra i fornitori:")
        self.navbar_layout.addWidget(self.search_label)
        self.search_bar = QLineEdit("Ragione Sociale")
        self.navbar_layout.addWidget(self.search_bar)

        self.navbar_layout.addStretch()
        self.search_bar.returnPressed.connect(self.filter_fornitori)
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
        self.open_button = QPushButton("Visualizza Fornitore")

        self.open_button.clicked.connect(self.show_selected_info)

        self.buttons_layout.addWidget(self.open_button)
        self.v_layout.addLayout(self.buttons_layout)

        self.insert_button = QPushButton("Inserisci Fornitore")
        self.insert_button.clicked.connect(self.show_insert_fornitore)
        self.buttons_layout.addWidget(self.insert_button)
        self.v_layout.addLayout(self.buttons_layout)

        self.delete_button = QPushButton("Elimina Fornitore")
        self.delete_button.clicked.connect(self.delete_fornitore)
        self.buttons_layout.addWidget(self.delete_button)
        self.v_layout.addLayout(self.buttons_layout)

        self.setLayout(self.v_layout)
        self.resize(1500, 480)
        self.setWindowTitle("Fornitori")

    def filter_fornitori(self):
        self.table_view.clearContents()
        self.table_view.model().removeRows(0, self.table_view.rowCount())

        filter_list = []
        for fornitore in self.controller.get_lista_fornitori():

            if self.search_bar.text().upper() in fornitore.ragione_sociale.upper() \
                    or fornitore.ragione_sociale.upper() in self.search_bar.text().upper():
                filter_list.append(fornitore)

        self.table_view.setRowCount(len(filter_list))
        self.table_view.setColumnCount(7)
        self.show_table_view_items(filter_list)

    def show_selected_info(self):
        if self.table_view.selectedIndexes():
            self.vista_fornitore = VistaFornitore(self.controller.get_fornitore_by_index(
            self.table_view.selectedIndexes()[0].row()), self.controller, self.update_table_view)
            self.vista_fornitore.show()

    def show_insert_fornitore(self):
        self.vista_inserisci_fornitore = VistaInserisciFornitore(self.controller, self.update_table_view)
        self.vista_inserisci_fornitore.show()

    def delete_fornitore(self):
        if self.table_view.selectedIndexes():
            fornitore_selezionato = self.controller.get_fornitore_by_index(
                self.table_view.selectedIndexes()[0].row())
            delete_view = QMessageBox.warning(self, 'Vuoi davvero eliminare il fornitore '  + str(fornitore_selezionato.codice_id) + '?',
                                          'Il fornitore ' + str(fornitore_selezionato.codice_id) +' sarà permanentemente eliminato dal sistema.\nVuoi continuare?',
                                          QMessageBox.Yes,
                             QMessageBox.No)
            if delete_view == QMessageBox.Yes:
                self.controller.elimina_fornitore_by_id(fornitore_selezionato.codice_id)
                self.update_table_view()

    def update_table_view(self):
        self.controller.save_data()
        self.table_view.setRowCount(len(self.controller.model.lista_fornitori))
        self.table_view.setColumnCount(7)
        self.show_table_view_items(self.controller.get_lista_fornitori())

    def show_table_view_items(self, item_list):
        i = 0
        for fornitore in item_list:
            item = QTableWidgetItem(str(fornitore.codice_id))
            self.table_view.setItem(i, 0, item)
            item = QTableWidgetItem(str(fornitore.ragione_sociale))
            self.table_view.setItem(i, 1, item)
            item = QTableWidgetItem(str(fornitore.partita_iva))
            self.table_view.setItem(i, 2, item)
            item = QTableWidgetItem(str(fornitore.citta))
            self.table_view.setItem(i, 3, item)
            item = QTableWidgetItem(str(fornitore.indirizzo))
            self.table_view.setItem(i, 4, item)
            item = QTableWidgetItem(str(fornitore.telefono))
            self.table_view.setItem(i, 5, item)
            item = QTableWidgetItem(str(fornitore.email))
            self.table_view.setItem(i, 6, item)
            i = i + 1

    def closeEvent(self, event):
        self.controller.save_data()
        event.accept()