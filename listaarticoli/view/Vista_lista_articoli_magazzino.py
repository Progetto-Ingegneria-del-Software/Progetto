from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, \
    QAbstractItemView, QHeaderView, QMessageBox, QLineEdit, QLabel

from articolo.view.VistaArticolo import VistaArticolo
from articolo.view.Vista_articolo_magazzino import Vista_articolo_magazzino

from listaarticoli.controller.ControlloreListaArticoli import ControlloreListaArticoli
from listaarticoli.view.Vista_carico_articolo import Vista_carico_articolo
from listaarticoli.view.Vista_scarico_articolo import Vista_scarico_articolo




class Vista_lista_articoli_magazzino(QWidget):


    def __init__(self, controller):
        super(Vista_lista_articoli_magazzino, self).__init__()


        self.controller = controller
        self.name_colonne = ['Codice a barre', 'Quantità', 'Descrizione']

        self.v_layout = QVBoxLayout()
        self.table_view = QTableWidget()
        self.navbar_layout = QHBoxLayout()

        self.show_all_button = QPushButton("Mostra tutto")
        self.show_all_button.clicked.connect(self.update_table_view)
        self.navbar_layout.addWidget(self.show_all_button)

        self.search_label = QLabel("Cerca tra gli articoli nel magazzino:")
        self.navbar_layout.addWidget(self.search_label)
        self.search_bar = QLineEdit("Codice a barre")
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

        self.increment_button = QPushButton("Carica articolo")
        self.increment_button.clicked.connect(self.show_increment_articolo)
        self.buttons_layout.addWidget(self.increment_button)
        self.v_layout.addLayout(self.buttons_layout)

        self.decrement_button = QPushButton("Scarica articolo")
        self.decrement_button.clicked.connect(self.show_decrement_articolo)
        self.buttons_layout.addWidget(self.decrement_button)
        self.v_layout.addLayout(self.buttons_layout)

        self.setLayout(self.v_layout)
        self.resize(1500, 480)
        self.setWindowTitle("Magazzino")

    def filter_articoli(self):
        self.table_view.clearContents()
        self.table_view.model().removeRows(0, self.table_view.rowCount())

        filter_list = []
        for articolo in self.controller.get_lista_articoli():

            if self.search_bar.text() == articolo.codice:
                filter_list.append(articolo)

        self.table_view.setRowCount(len(filter_list))
        self.table_view.setColumnCount(3)
        self.show_table_view_items(filter_list)



    def show_selected_info(self):
        if self.table_view.selectedIndexes():
            self.vista_articolo = Vista_articolo_magazzino(self.controller.get_articolo_by_codice(
            self.table_view.item(self.table_view.selectionModel().currentIndex().row(), 0).text()), self.update_table_view)
            self.vista_articolo.show()


    def show_increment_articolo(self):
        self.vista_carico_articolo = Vista_carico_articolo(self.controller, self.update_table_view)
        self.vista_carico_articolo.show()

    def show_decrement_articolo(self):
        self.vista_scarico_articolo = Vista_scarico_articolo(self.controller, self.update_table_view)
        self.vista_scarico_articolo.show()



    def update_table_view(self):
        self.controller.save_data()
        self.table_view.setRowCount(len(self.controller.model.lista_articoli))
        self.table_view.setColumnCount(3)
        self.show_table_view_items(self.controller.get_lista_articoli())

#mostra gli articoli in ordine crescente secondo l'attributo stock (quantità),
# in modo da avere a colpo d'occhio gli articoli esauriti o non riforniti e i meno riforniti
    def show_table_view_items(self, item_list):
        i = 0

        for articolo in  sorted(item_list, key=lambda x: x.stock):
            item = QTableWidgetItem(str(articolo.codice))
            self.table_view.setItem(i, 0, item)
            item = QTableWidgetItem(str(articolo.stock))
            self.table_view.setItem(i, 1, item)
            item = QTableWidgetItem(str(articolo.descrizione))
            self.table_view.setItem(i, 2, item)
            i = i + 1

    def closeEvent(self, event):
        self.controller.save_data()
        event.accept()
