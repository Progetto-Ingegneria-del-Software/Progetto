from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QAbstractItemView, QHeaderView, QHBoxLayout, \
    QPushButton, QTableWidgetItem, QMessageBox, QLabel, QLineEdit

from dipendente.view.VistaDipendente import VistaDipendente
from listadipendenti.controller.ControlloreListaDipendenti import ControlloreListaDipendenti
from listadipendenti.view.VistaInserisciDipendente import VistaInserisciDipendente


class VistaListaDipendenti(QWidget):
    def __init__(self):
        super(VistaListaDipendenti, self).__init__()

        self.controller = ControlloreListaDipendenti()
        self.name_colonne = ['Codice ID', 'Nome', 'Cognome', 'Codice Fiscale', 'Email',
                   'Telefono', 'Mansione', 'Stipendio Mensile']

        self.v_layout = QVBoxLayout()
        self.table_view = QTableWidget()
        self.navbar_layout = QHBoxLayout()

        self.show_all_button = QPushButton("Mostra tutto")
        self.show_all_button.clicked.connect(self.update_table_view)
        self.navbar_layout.addWidget(self.show_all_button)

        self.search_label = QLabel("Cerca tra i dipendenti:")
        self.navbar_layout.addWidget(self.search_label)
        self.search_bar = QLineEdit("Nome Cognome")
        self.navbar_layout.addWidget(self.search_bar)

        self.navbar_layout.addStretch()
        self.search_bar.returnPressed.connect(self.filter_dipendenti)
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
        self.open_button = QPushButton("Apri Dipendente")

        self.open_button.clicked.connect(self.show_selected_info)

        self.buttons_layout.addWidget(self.open_button)
        self.v_layout.addLayout(self.buttons_layout)

        self.insert_button = QPushButton("Inserisci Dipendente")
        self.insert_button.clicked.connect(self.show_insert_dipendente)
        self.buttons_layout.addWidget(self.insert_button)
        self.v_layout.addLayout(self.buttons_layout)

        self.delete_button = QPushButton("Elimina Dipendente")
        self.delete_button.clicked.connect(self.delete_dipendente)
        self.buttons_layout.addWidget(self.delete_button)
        self.v_layout.addLayout(self.buttons_layout)

        self.setLayout(self.v_layout)
        self.resize(1500, 480)
        self.setWindowTitle("Dipendenti")

    def filter_dipendenti(self):
        self.table_view.clearContents()
        self.table_view.model().removeRows(0, self.table_view.rowCount())

        filter_list = []
        for dipendente in self.controller.get_lista_dipendenti():

            if self.search_bar.text().upper() in dipendente.nome.upper() + " " + dipendente.cognome.upper() \
                    or dipendente.nome.upper() + " " + dipendente.cognome.upper() in self.search_bar.text().upper():
                filter_list.append(dipendente)

        self.table_view.setRowCount(len(filter_list))
        self.table_view.setColumnCount(8)
        self.show_table_view_items(filter_list)

    def show_selected_info(self):
        if self.table_view.selectedIndexes():
            self.vista_dipendente = VistaDipendente(self.controller.get_dipendente_by_id(
            int(self.table_view.item(self.table_view.selectionModel().currentIndex().row(), 0).text())), self.controller.elimina_dipendente_by_id, self.update_table_view)
            self.vista_dipendente.show()

    def show_insert_dipendente(self):
        self.vista_inserisci_dipendente = VistaInserisciDipendente(self.controller, self.update_table_view)
        self.vista_inserisci_dipendente.show()

    def delete_dipendente(self):
        if self.table_view.selectedIndexes():
            dipendente_selezionato = self.controller.get_dipendente_by_id(
                int(self.table_view.item(self.table_view.selectionModel().currentIndex().row(), 0).text()))
            delete_view = QMessageBox.warning(self, 'Vuoi davvero eliminare il dipendente '  + str(dipendente_selezionato.codice_id) + '?',
                                          'Il dipendente ' + str(dipendente_selezionato.codice_id) +' sarà permanentemente eliminato dal sistema.\nVuoi continuare?',
                                          QMessageBox.Yes,
                             QMessageBox.No)
            if delete_view == QMessageBox.Yes:
                self.controller.elimina_dipendente_by_id(dipendente_selezionato.codice_id)
                self.update_table_view()

    def update_table_view(self):
        self.controller.save_data()
        self.table_view.setRowCount(len(self.controller.model.lista_dipendenti))
        self.table_view.setColumnCount(8)
        self.show_table_view_items(self.controller.get_lista_dipendenti())

    def show_table_view_items(self, item_list):
        i = 0
        for dipendente in item_list:
            item = QTableWidgetItem(str(dipendente.codice_id))
            self.table_view.setItem(i, 0, item)
            item = QTableWidgetItem(str(dipendente.nome))
            self.table_view.setItem(i, 1, item)
            item = QTableWidgetItem(str(dipendente.cognome))
            self.table_view.setItem(i, 2, item)
            item = QTableWidgetItem(str(dipendente.cf))
            self.table_view.setItem(i, 3, item)
            item = QTableWidgetItem(str(dipendente.email))
            self.table_view.setItem(i, 4, item)
            item = QTableWidgetItem(str(dipendente.telefono))
            self.table_view.setItem(i, 5, item)
            item = QTableWidgetItem(str(dipendente.mansione))
            self.table_view.setItem(i, 6, item)
            item = QTableWidgetItem("€"+str(dipendente.stipendio_mensile))
            self.table_view.setItem(i, 7, item)
            i = i + 1

    def closeEvent(self, event):
        self.controller.save_data()
        event.accept()
