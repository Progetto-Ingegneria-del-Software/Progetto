import json
import os
import pickle

from dipendente.model.Dipendente import Dipendente

###########################################################################
###  QUESTA CLASSE MODELLA LA LISTA DEI DIPENDENTI DELLA CARTOLIBRERIA  ###
###                  CON I CORRISPONDENTI ATTRIBUTI                     ###
###########################################################################
class ListaDipendenti():
    def __init__(self):
        super(ListaDipendenti, self).__init__()

        self.lista_dipendenti = []
        self.populate_lista_dipendenti()
        self.codice_id = self.assegna_contatore_id()

    ############################################################
    ###   METODO CHE ASSEGNA UN CODICE ID AUTOINCREMENTANTE  ###
    ###             DIVERSO PER OGNI DIPENDENTE              ###
    ############################################################
    def assegna_contatore_id(self):
        self.i = 0
        for dipendente in self.lista_dipendenti:
            if dipendente.codice_id > 0:
                self.i = dipendente.codice_id
        return self.i

    ####################################################################
    ###   METODO CHE POPOLA LA LISTA DEI DIPENDENTI CON LE ISTANZE   ###
    ###                   PRESENTI NEL FILE PICKLE                   ###
    ####################################################################
    def populate_lista_dipendenti(self):
        if os.path.isfile('listadipendenti/data/lista_dipendenti_salvata.pickle'):
            with open('listadipendenti/data/lista_dipendenti_salvata.pickle', 'rb') as f:
                self.lista_dipendenti = pickle.load(f)
        else:
            with open('listadipendenti/data/lista_dipendenti_iniziali.json') as f:
                lista_dipendenti_iniziali = json.load(f)
            for dipendente_iniziale in lista_dipendenti_iniziali:
                self.aggiungi_dipendente(Dipendente(dipendente_iniziale["codice_id"], dipendente_iniziale["nome"], dipendente_iniziale["cognome"],
                                                dipendente_iniziale["cf"], dipendente_iniziale["email"], dipendente_iniziale["telefono"],
                                                dipendente_iniziale["mansione"], dipendente_iniziale["stipendio"]))

    def aggiungi_dipendente(self, dipendente):
        self.lista_dipendenti.append(dipendente)

    def get_dipendente_by_id(self, id):
        for dipendente in self.lista_dipendenti:
            if id == dipendente.codice_id:
                return dipendente

    def rimuovi_dipendente_by_id(self, id):
        for dipendente in self.lista_dipendenti:
            if id == dipendente.codice_id:
                self.lista_dipendenti.remove(dipendente)

    def save_data(self):
        with open('listadipendenti/data/lista_dipendenti_salvata.pickle', 'wb') as handle:
            pickle.dump(self.lista_dipendenti, handle, pickle.HIGHEST_PROTOCOL)