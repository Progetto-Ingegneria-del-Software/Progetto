from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QGridLayout, \
    QMessageBox

from articolo.controller.ControlloreArticolo import ControlloreArticolo
from articolo.view.VistaDescrizioneArticolo import VistaDescrizioneArticolo
from articolo.view.VistaModificaArticolo import VistaModificaArticolo

#####################################################################
###   QUESTA CLASSE SERVE PER MOSTRARE ALL'UTENTE L'INTERFACCIA   ###
###   CON I DATI DI UN ARTICOLO PRESENTE IN ANAGRAFICA ARTICOLI   ###
#####################################################################
class VistaArticolo(QWidget):
    def __init__(self, articolo, controller_articoli, callback_articoli, callback_magazzino):
        super(VistaArticolo, self).__init__()

        self.controller = ControlloreArticolo(articolo)
        self.controller_articoli = controller_articoli
        self.callback_articoli = callback_articoli
        self.callback_magazzino = callback_magazzino

        v_layout = QVBoxLayout()

        grid_layout = QGridLayout()

        self.label_codice = QLabel("Codice: " + str(self.controller.get_codice_articolo()))
        grid_layout.addWidget(self.label_codice, 0, 0)

        button_gruppo_merceologico = QPushButton("Modifica Codice")
        button_gruppo_merceologico.clicked.connect(lambda: self.show_modifica_articolo("Modifica Codice"))
        grid_layout.addWidget(button_gruppo_merceologico, 0, 1)

        self.label_gruppo_merceologico = QLabel("Gruppo Merceologico: " + str(self.controller.get_gruppo_merceologico_articolo()))
        grid_layout.addWidget(self.label_gruppo_merceologico, 1, 0)

        button_gruppo_merceologico = QPushButton("Modifica Gruppo Merceologico")
        button_gruppo_merceologico.clicked.connect(lambda: self.show_modifica_articolo("Modifica Gruppo Merceologico"))
        grid_layout.addWidget(button_gruppo_merceologico, 1, 1)

        self.label_categoria = QLabel("Categoria: " + str(self.controller.get_categoria_articolo()))
        grid_layout.addWidget(self.label_categoria, 2, 0)

        button_categoria = QPushButton("Modifica Categoria")
        button_categoria.clicked.connect(lambda: self.show_modifica_articolo("Modifica Categoria"))
        grid_layout.addWidget(button_categoria, 2, 1)

        self.label_marca = QLabel("Marca: " + str(self.controller.get_marca_articolo()))
        grid_layout.addWidget(self.label_marca, 3, 0)

        button_marca = QPushButton("Modifica Marca")
        button_marca.clicked.connect(lambda: self.show_modifica_articolo("Modifica Marca"))
        grid_layout.addWidget(button_marca, 3, 1)

        self.label_prezzo_unitario = QLabel("Prezzo: ???" + str(self.controller.get_prezzo_unitario_articolo()))
        grid_layout.addWidget(self.label_prezzo_unitario, 4, 0)

        button_prezzo_unitario = QPushButton("Modifica Prezzo Unitario")
        button_prezzo_unitario.clicked.connect(lambda: self.show_modifica_articolo("Modifica Prezzo Unitario"))
        grid_layout.addWidget(button_prezzo_unitario, 4, 1)

        self.label_sconto_perc = QLabel("Sconto: " + str(self.controller.get_sconto_perc_articolo()) + "%")
        grid_layout.addWidget(self.label_sconto_perc, 5, 0)

        button_sconto_perc = QPushButton("Modifica Sconto")
        button_sconto_perc.clicked.connect(lambda: self.show_modifica_articolo("Modifica Sconto"))
        grid_layout.addWidget(button_sconto_perc, 5, 1)

        button_sconto_perc = QPushButton("Visualizza Descrizione")
        button_sconto_perc.clicked.connect(self.show_descrizione_articolo)
        grid_layout.addWidget(button_sconto_perc, 6, 0)

        button_sconto_perc = QPushButton("Modifica Descrizione")
        button_sconto_perc.clicked.connect(lambda: self.show_modifica_articolo("Modifica Descrizione"))
        grid_layout.addWidget(button_sconto_perc, 6, 1)

        v_layout.addLayout(grid_layout)
        button_elimina_articolo = QPushButton("Elimina Articolo " + str(self.controller.get_codice_articolo()))
        button_elimina_articolo.clicked.connect(self.delete_articolo)
        v_layout.addWidget(button_elimina_articolo)

        self.setLayout(v_layout)
        self.resize(600, 350)
        self.setFixedSize(self.size())
        self.setWindowTitle("Articolo " + str(self.controller.get_codice_articolo()))

    ########################################################
    ###    METODO USATO PER FAR CAMBIARE DINAMICAMENTE   ###
    ###   LA VISTA DI UN ARTICOLO, A MODIFICA AVVENUTA   ###
    ########################################################
    def update_info_view(self):
        self.label_codice.setText("Codice: " + str(self.controller.get_codice_articolo()))
        self.label_marca.setText("Marca: " + str(self.controller.get_marca_articolo()))
        self.label_gruppo_merceologico.setText("Gruppo Merceologico: " + str(self.controller.get_gruppo_merceologico_articolo()))
        self.label_categoria.setText("Categoria: " + str(self.controller.get_categoria_articolo()))
        self.label_prezzo_unitario.setText("Prezzo: ???" + str(self.controller.get_prezzo_unitario_articolo()))
        self.label_sconto_perc.setText("Sconto: " + str(self.controller.get_sconto_perc_articolo()) + "%")
        self.setWindowTitle("Articolo " + str(self.controller.get_codice_articolo()))

    ###################################################
    ###    METODO USATO PER ELIMINARE UN ARTICOLO   ###
    ###   PRESENTE NEL SISTEMA DOPO AVER CLICCATO   ###
    ###          SUL CORRISPONDENTE BOTTONE         ###
    ###################################################
    def delete_articolo(self):
        delete_view = QMessageBox.warning(self, 'Vuoi davvero eliminare l\'articolo ' + str(self.controller.get_codice_articolo()) + '?',
                                          'L\'articolo ' + str(self.controller.get_codice_articolo()) + ' sar?? permanentemente eliminato dal sistema.\nVuoi continuare?',
                                          QMessageBox.Yes,
                                          QMessageBox.No)
        if delete_view == QMessageBox.Yes:
            self.controller_articoli.elimina_articolo_by_codice(self.controller.get_codice_articolo())
            self.callback_articoli()
            self.callback_magazzino()
            self.close()

    #################################################
    ###    METODO USATO PER MOSTRARE ALL'UTENTE   ###
    ###  L'INTERFACCIA DI MODIFICA DELL'ARTICOLO  ###
    #################################################
    def show_modifica_articolo(self, elemento_modifica):
        self.vista_modifica_articolo = VistaModificaArticolo(elemento_modifica, self.controller, self.controller_articoli, self.callback_articoli, self.callback_magazzino, self.update_info_view)
        self.vista_modifica_articolo.show()

    #########################################################
    ###       METODO USATO PER MOSTRARE ALL'UTENTE        ###
    ###  L'INTERFACCIA CON LA DESCRIZIONE DELL' ARTICOLO  ###
    #########################################################
    def show_descrizione_articolo(self):
        self.vista_descrizione_articolo = VistaDescrizioneArticolo(self.controller)
        self.vista_descrizione_articolo.show()



