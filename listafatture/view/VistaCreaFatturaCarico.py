from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit

from listafatture.controller.ControlloreListaFatture import ControlloreListaFatture
from listafornitori.control.ControlloreListaFornitori import ControlloreListaFornitori


class VistaCreaFatturaCarico(QWidget):
    def __init__(self, tipo_fattura):
        super(VistaCreaFatturaCarico, self).__init__()

        self.tipo_fattura = tipo_fattura
        self.data_fattura = ''

        self.controller = ControlloreListaFatture()

        self.v_layout = QVBoxLayout()
        self.h_layout = QHBoxLayout()

        self.label_h_layout = QLabel("Numero: {} Tipo: {} Data: {}".format(self.controller.get_assegnamento_numero_fattura(), self.tipo_fattura, self.data_fattura))
        self.h_layout.addWidget(self.label_h_layout)

        self.v_layout.addLayout(self.h_layout)

        self.label_search_fornitore = QLabel("Fornitore: ")
        self.v_layout.addWidget(self.label_search_fornitore)
        self.search_bar_fornitore = QLineEdit("Inserisci qui la ragione sociale del fornitore")
        self.v_layout.addWidget(self.search_bar_fornitore)
        self.search_bar_fornitore.returnPressed.connect(self.search_fornitore)

        self.h_layout2 = QHBoxLayout()

        self.label_riga1_fornitore = QLabel("Codice ID:   Ragione Sociale:   Partita IVA:")
        self.h_layout2.addWidget(self.label_riga1_fornitore)

        self.v_layout.addLayout(self.h_layout2)

        self.h_layout3 = QHBoxLayout()

        self.label_riga2_fornitore = QLabel("Città:   Indirizzo:   Telefono:   Email:")
        self.h_layout3.addWidget(self.label_riga2_fornitore)

        self.v_layout.addLayout(self.h_layout3)

        self.setLayout(self.v_layout)
        self.resize(800, 350)
        self.setFixedSize(self.size())
        self.setWindowTitle("Vista Crea Fattura")

    def search_fornitore(self):
        self.controller_fornitore = ControlloreListaFornitori()
        self.lista_fornitori = self.controller_fornitore.get_lista_fornitori()

        for fornitore in self.lista_fornitori:
            if self.search_bar_fornitore.text().upper() in fornitore.ragione_sociale.upper() \
                    or fornitore.ragione_sociale.upper() in self.search_bar_fornitore.text().upper():
                self.mostra_fornitore_cercato(fornitore)

    def mostra_fornitore_cercato(self, fornitore):
        self.label_riga1_fornitore.setText("Codice ID: {} Ragione Sociale: {} Partita IVA: {}".format(fornitore.codice_id, fornitore.ragione_sociale, fornitore.partita_iva))
        self.label_riga2_fornitore.setText("Città: {} Indirizzo: {} Telefono: {} Email: {}".format(fornitore.citta, fornitore.indirizzo, fornitore.telefono, fornitore.email))
