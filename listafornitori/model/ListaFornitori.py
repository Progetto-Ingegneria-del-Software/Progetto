import json
import os
import pickle

from fornitore.model.Fornitore import Fornitore

##########################################################################
###  QUESTA CLASSE MODELLA LA LISTA DEI FORNITORI DELLA CARTOLIBRERIA  ###
###                  CON I CORRISPONDENTI ATTRIBUTI                    ###
##########################################################################
class ListaFornitori():
    def __init__(self):
        super(ListaFornitori, self).__init__()

        self.lista_fornitori = []
        self.populate_lista_fornitori()
        self.codice_id = self.assegna_contatore_id()

    ############################################################
    ###   METODO CHE ASSEGNA UN CODICE ID AUTOINCREMENTANTE  ###
    ###              DIVERSO PER OGNI FORNITORE              ###
    ############################################################
    def assegna_contatore_id(self):
        self.i = 0
        for fornitore in self.lista_fornitori:
            if fornitore.codice_id > 0:
                self.i = fornitore.codice_id
        return self.i

    ####################################################################
    ###    METODO CHE POPOLA LA LISTA DEI CLIENTI CON LE ISTANZE    ###
    ###                   PRESENTI NEL FILE PICKLE                   ###
    ####################################################################
    def populate_lista_fornitori(self):
        if os.path.isfile('listafornitori/data/lista_fornitori_salvata.pickle'):
            with open('listafornitori/data/lista_fornitori_salvata.pickle', 'rb') as f:
                self.lista_fornitori = pickle.load(f)
        else:
            with open('listafornitori/data/lista_fornitori_iniziali.json') as f:
                lista_fornitori_iniziali = json.load(f)
            for fornitore_iniziale in lista_fornitori_iniziali:
                self.aggiungi_fornitore(Fornitore(fornitore_iniziale["codice_id"], fornitore_iniziale["ragione_sociale"], fornitore_iniziale["partita_iva"],
                                                fornitore_iniziale["citta"], fornitore_iniziale["indirizzo"], fornitore_iniziale["telefono"],
                                                fornitore_iniziale["email"]))

    def aggiungi_fornitore(self, fornitore):
        self.lista_fornitori.append(fornitore)

    def get_fornitore_by_index(self, index):
        return self.lista_fornitori[index]

    def rimuovi_fornitore_by_id(self, id):
        for fornitore in self.lista_fornitori:
            if id == fornitore.codice_id:
                self.lista_fornitori.remove(fornitore)

    def save_data(self):
        with open('listafornitori/data/lista_fornitori_salvata.pickle', 'wb') as handle:
            pickle.dump(self.lista_fornitori, handle, pickle.HIGHEST_PROTOCOL)