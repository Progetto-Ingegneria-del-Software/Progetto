from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QAbstractItemView, QHeaderView, QHBoxLayout, \
    QPushButton, QTableWidgetItem, QMessageBox, QLabel, QLineEdit



from clientePIva.view.Vista_clientepiva import Vista_clientepiva

from listaclientiPIva.control.Controllore_lista_clientipiva import Controllore_lista_clientipiva

from listaclientiPIva.view.Vista_inserisci_clientepiva import Vista_inserisci_clientepiva


class Vista_lista_clientipiva(QWidget):
    def __init__(self):
        super(Vista_lista_clientipiva, self).__init__()

        self.controller = Controllore_lista_clientipiva()
        self.name_colonne = ['Codice ID', 'Ragione Sociale', 'Partita IVA', 'Città', 'Indirizzo', 'Telefono', 'Email']

        self.v_layout = QVBoxLayout()
        self.table_view = QTableWidget()
        self.navbar_layout = QHBoxLayout()

        self.show_all_button = QPushButton("Mostra tutto")
        self.show_all_button.clicked.connect(self.update_ui)
        self.navbar_layout.addWidget(self.show_all_button)



        self.search_label = QLabel("Cerca tra i clienti PIva:")
        self.navbar_layout.addWidget(self.search_label)
        self.search_bar = QLineEdit("Ragione Sociale")
        self.navbar_layout.addWidget(self.search_bar)

        self.navbar_layout.addStretch()
        self.search_bar.returnPressed.connect(self.filter_clientipiva)
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
        self.open_button = QPushButton("Visualizza Cliente PIva")

        self.open_button.clicked.connect(self.show_selected_info)

        self.buttons_layout.addWidget(self.open_button)
        self.v_layout.addLayout(self.buttons_layout)

        self.insert_button = QPushButton("Inserisci Cliente PIva")
        self.insert_button.clicked.connect(self.show_insert_clientepiva)
        self.buttons_layout.addWidget(self.insert_button)
        self.v_layout.addLayout(self.buttons_layout)

        self.delete_button = QPushButton("Elimina Cliente PIva")
        self.delete_button.clicked.connect(self.delete_clientepiva)
        self.buttons_layout.addWidget(self.delete_button)
        self.v_layout.addLayout(self.buttons_layout)

        self.setLayout(self.v_layout)
        self.resize(1500, 480)
        self.setWindowTitle("Clienti PIva")

#bisogna cercare con lo spazio
    def filter_clientipiva(self):
        self.table_view.clearContents()
        self.table_view.model().removeRows(0, self.table_view.rowCount())

        filter_list = []
        for clientepiva in self.controller.get_lista_clientipiva():

            if (self.search_bar.text()).upper() in clientepiva.ragione_sociale.upper():
                filter_list.append(clientepiva)

        self.table_view.setRowCount(len(filter_list))
        self.table_view.setColumnCount(7)
        self.show_table_view_items(filter_list)


    def show_selected_info(self):
        if self.table_view.selectedIndexes():
            self.vista_clientepiva = Vista_clientepiva(self.controller.get_clientepiva_by_index(
                self.table_view.selectedIndexes()[0].row()), self.controller, self.update_ui)
            self.vista_clientepiva.show()

    def show_insert_clientepiva(self):
        self.Vista_inserisci_clientepiva = Vista_inserisci_clientepiva(self.controller, self.update_ui)
        self.Vista_inserisci_clientepiva.show()

    def delete_clientepiva(self):
        if self.table_view.selectedIndexes():
            clientepiva_selezionato = self.controller.get_clientepiva_by_index(
                self.table_view.selectedIndexes()[0].row())
            delete_view = QMessageBox.warning(self, 'Vuoi davvero eliminare il cliente PIva ' + str(
                 clientepiva_selezionato.codice_id) + '?',
                                              'Il cliente ' + str(
                                                  clientepiva_selezionato.codice_id) + ' con P.ta IVA sarà permanentemente eliminato dal sistema.\nVuoi continuare?',
                                              QMessageBox.Yes,
                                              QMessageBox.No)
            if delete_view == QMessageBox.Yes:
                self.controller.elimina_clientepiva_by_id(clientepiva_selezionato.codice_id)
                self.update_ui()

    def update_ui(self):
        self.controller.save_data()
        self.table_view.setRowCount(len(self.controller.model.lista_clientipiva))
        self.table_view.setColumnCount(7)
        self.show_table_view_items(self.controller.get_lista_clientipiva())

    def show_table_view_items(self, item_list):
        i = 0
        for clientepiva in item_list:
            item = QTableWidgetItem(str(clientepiva.codice_id))
            self.table_view.setItem(i, 0, item)
            item = QTableWidgetItem(str(clientepiva.ragione_sociale))
            self.table_view.setItem(i, 1, item)
            item = QTableWidgetItem(str(clientepiva.partita_iva))
            self.table_view.setItem(i, 2, item)
            item = QTableWidgetItem(str(clientepiva.citta))
            self.table_view.setItem(i, 3, item)
            item = QTableWidgetItem(str(clientepiva.indirizzo))
            self.table_view.setItem(i, 4, item)
            item = QTableWidgetItem(str(clientepiva.telefono))
            self.table_view.setItem(i, 5, item)
            item = QTableWidgetItem(str(clientepiva.email))
            self.table_view.setItem(i, 6, item)
            i = i + 1

    def closeEvent(self, event):
        self.controller.save_data()
        event.accept()