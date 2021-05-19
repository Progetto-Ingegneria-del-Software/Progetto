from PyQt5.QtWidgets import QTextBrowser, QWidget, QVBoxLayout, QLabel, QPushButton, QGridLayout, \
    QMessageBox

from fattura.controller.ControlloreFattura import ControlloreFattura
from fornitore.control.ControlloreFornitore import ControlloreFornitore


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

            ## Ragione Sociale ##
            text_nome_fornitore = QTextBrowser(ControlloreFornitore.get_ragione_sociale_fornitore)
            text_nome_fornitore.isReadOnly(True)
            text_nome_fornitore.adjustSize


        label_prezzo_unitario = QLabel("Prezzo: €" + str(self.controller.get_prezzo_unitario_articolo()))
        grid_layout.addWidget(label_prezzo_unitario, 4, 0)

        button_prezzo_unitario = QPushButton("Modifica Prezzo Unitario")
        button_prezzo_unitario.clicked.connect(lambda: self.show_modifica_articolo("Modifica Prezzo Unitario"))
        grid_layout.addWidget(button_prezzo_unitario, 4, 1)

        label_sconto_perc = QLabel("Sconto: " + str(self.controller.get_sconto_perc_articolo()) + "%")
        grid_layout.addWidget(label_sconto_perc, 5, 0)

        button_sconto_perc = QPushButton("Modifica Sconto")
        button_sconto_perc.clicked.connect(lambda: self.show_modifica_articolo("Modifica Sconto"))
        grid_layout.addWidget(button_sconto_perc, 5, 1)

        label_quantita = QLabel("Quantità: " + str(self.controller.get_quantita_articolo()) + " pezzi")
        grid_layout.addWidget(label_quantita, 6, 0)

        v_layout.addLayout(grid_layout)
        button_elimina_articolo = QPushButton("Elimina Articolo " + str(self.controller.get_codice_id_articolo()))
        button_elimina_articolo.clicked.connect(self.delete_articolo)
        v_layout.addWidget(button_elimina_articolo)

        self.setLayout(v_layout)
        self.resize(500, 300)
        self.setFixedSize(self.size())
        self.setWindowTitle("Articolo " + str(self.controller.get_codice_id_articolo()))

    def delete_articolo(self):
        delete_view = QMessageBox.warning(self, 'Vuoi davvero eliminare l\'articolo ' + str(self.controller.get_codice_id_articolo()) + '?',
                                          'L\'articolo ' + str(self.controller.get_codice_id_articolo()) + ' sarà permanentemente eliminato dal sistema.\nVuoi continuare?',
                                          QMessageBox.Yes,
                                          QMessageBox.No)
        if delete_view == QMessageBox.Yes:
            self.elimina_articolo(self.controller.get_codice_id_articolo())
            self.callback()
            self.close()

    def show_modifica_articolo(self, elemento_modifica):
        self.vista_modifica_articolo = VistaModificaArticolo(elemento_modifica, self.controller, self.callback)
        self.vista_modifica_articolo.show()