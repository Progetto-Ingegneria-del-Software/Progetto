from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QAbstractItemView, QHeaderView, QHBoxLayout, \
    QPushButton, QTableWidgetItem, QMessageBox, QLabel, QLineEdit

from cliente.view.Vista_cliente import Vista_cliente
from listaclienti.controller.Controllore_Lista_clienti import Controllore_Lista_clienti
from listaclienti.view.Vista_Inserisci_cliente import Vista_Inserisci_cliente


class Vista_Lista_clienti(QWidget):
    def __init__(self):
        super(Vista_Lista_clienti, self).__init__()

        self.controller = Controllore_Lista_clienti()
        self.name_colonne = ['Codice ID', 'Nome', 'Cognome', 'Codice Fiscale', 'Email', 'Telefono' ,'Indirizzo']

        self.v_layout = QVBoxLayout()
        self.table_view = QTableWidget()
        self.navbar_layout = QHBoxLayout()

        self.show_all_button = QPushButton("Mostra tutto")
        self.show_all_button.clicked.connect(self.update_ui)
        self.navbar_layout.addWidget(self.show_all_button)

        self.search_label = QLabel("Cerca tra i clienti:")
        self.navbar_layout.addWidget(self.search_label)
        self.search_bar = QLineEdit("Nome Cognome")
        self.navbar_layout.addWidget(self.search_bar)

        self.navbar_layout.addStretch()
        self.search_bar.returnPressed.connect(self.filter_clienti)
        self.v_layout.addLayout(self.navbar_layout)

        self.update_ui()

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
        self.open_button = QPushButton("Apri cliente")


        self.open_button.clicked.connect(self.show_selected_info)



        self.buttons_layout.addWidget(self.open_button)
        self.v_layout.addLayout(self.buttons_layout)

        self.insert_button = QPushButton("Inserisci cliente")
        self.insert_button.clicked.connect(self.show_insert_cliente)
        self.buttons_layout.addWidget(self.insert_button)
        self.v_layout.addLayout(self.buttons_layout)

        self.delete_button = QPushButton("Elimina cliente")
        self.delete_button.clicked.connect(self.delete_cliente)
        self.buttons_layout.addWidget(self.delete_button)
        self.v_layout.addLayout(self.buttons_layout)

        self.setLayout(self.v_layout)
        self.resize(1500, 480)
        self.setWindowTitle("Clienti")

    def filter_clienti(self):
        self.table_view.clearContents()
        self.table_view.model().removeRows(0, self.table_view.rowCount())

        filter_list = []
        for cliente in self.controller.get_lista_clienti():

            if (self.search_bar.text()).upper() in cliente.nome.upper() + " " + cliente.cognome.upper() \
                    or cliente.cognome.upper() + " " + cliente.nome.upper() in (self.search_bar.text()).upper():


                filter_list.append(cliente)

        self.table_view.setRowCount(len(filter_list))
        self.table_view.setColumnCount(7)
        self.show_table_view_items(filter_list)

    def show_selected_info(self):
        if self.table_view.selectedIndexes():
            self.vista_cliente = Vista_cliente(self.controller.get_cliente_by_index(
                self.table_view.selectedIndexes()[0].row()), self.controller.elimina_cliente_by_id, self.update_ui)
            self.vista_cliente.show()

    def show_insert_cliente(self):
        self.vista_inserisci_cliente = Vista_Inserisci_cliente(self.controller, self.update_ui)
        self.vista_inserisci_cliente.show()

    def delete_cliente(self):
        if self.table_view.selectedIndexes():
            cliente_selezionato = self.controller.get_cliente_by_index(
                self.table_view.selectedIndexes()[0].row())
            delete_view = QMessageBox.warning(self, 'Vuoi davvero eliminare il fornitore ' + str(
                 cliente_selezionato.codice_id) + '?',
                                              'Il f'
                                              'ornitore ' + str(
                                                  cliente_selezionato.codice_id) + ' sarà permanentemente eliminato dal sistema.\nVuoi continuare?',
                                              QMessageBox.Yes,
                                              QMessageBox.No)
            if delete_view == QMessageBox.Yes:
                self.controller.elimina_cliente_by_id(cliente_selezionato.codice_id)
                self.update_ui()

    def update_ui(self):
        self.controller.save_data()
        self.table_view.setRowCount(len(self.controller.model.lista_clienti))
        self.table_view.setColumnCount(7)
        self.show_table_view_items(self.controller.get_lista_clienti())
       # self.controller.save_data()
        #self.table_view.setRowCount(len(self.controller.model.lista_clienti))
        #self.table_view.setColumnCount(7)

    def show_table_view_items(self, item_list):
        i = 0
        for cliente in item_list:
            item = QTableWidgetItem(str(cliente.codice_id))
            self.table_view.setItem(i, 0, item)
            item = QTableWidgetItem(str(cliente.nome))
            self.table_view.setItem(i, 1, item)
            item = QTableWidgetItem(str(cliente.cognome))
            self.table_view.setItem(i, 2, item)
            item = QTableWidgetItem(str(cliente.cf))
            self.table_view.setItem(i, 3, item)
            item = QTableWidgetItem(str(cliente.email))
            self.table_view.setItem(i, 4, item)
            item = QTableWidgetItem(str(cliente.telefono))
            self.table_view.setItem(i, 5, item)
            item = QTableWidgetItem(str(cliente.indirizzo))
            self.table_view.setItem(i, 6, item)
            i = i + 1


    def closeEvent(self, event):
        self.controller.save_data()
        event.accept()
