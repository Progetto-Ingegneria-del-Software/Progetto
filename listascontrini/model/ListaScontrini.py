import json
import os
import pickle

from scontrino.model.Scontrino import Scontrino

############################################################################
###  QUESTA CLASSE MODELLA LA LISTA DEGLI SCONTRINI DELLA CARTOLIBRERIA  ###
###                   CON I CORRISPONDENTI ATTRIBUTI                     ###
############################################################################
class ListaScontrini():

    def __init__(self):
        super(ListaScontrini, self).__init__()

        self.lista_scontrini = []   #Lista degli scontrini
        self.populate_lista_scontrini()
        self.numero_scontrino = self.assegna_numero_scontrino()   #Assegnamento numero ad ogni scontrino


    ######################################
    ###  FUNZIONE CHE ASSEGNA AD OGNI  ### 
    ###      SCONTRINO UN NUMERO       ###
    ######################################
    def assegna_numero_scontrino(self):
        self.i = 0
        for scontrino in self.lista_scontrini:
            if scontrino.num_scontrino > 0:
                self.i = scontrino.num_scontrino
        return self.i


    ################################
    ###  FUNZIONE CHE POPOLA LA  ### 
    ###  LISTA DEGLI SCONTRINI   ###
    ################################
    def populate_lista_scontrini(self):
        #Controlla se il file esiste
        if os.path.isfile('listascontrini/data/lista_scontrini_salvata.pickle'):
            with open('listascontrini/data/lista_scontrini_salvata.pickle', 'rb') as f:
                self.lista_scontrini = pickle.load(f)
        else:
            with open('listascontrini/data/lista_scontrini_iniziali.json') as f:
                lista_scontrini_iniziali = json.load(f)
            for scontrino_iniziale in lista_scontrini_iniziali:
                self.aggiungi_scontrino(Scontrino(scontrino_iniziale["num_scontrino"], scontrino_iniziale["data"], scontrino_iniziale["lista_articoli"], scontrino_iniziale["totale"]))


    ###################################
    ###  FUNZIONE CHE AGGIUNGE UNO  ###
    ###     SCONTRINO ALLA LISTA    ###
    ###################################
    def aggiungi_scontrino(self, scontrino):
        self.lista_scontrini.append(scontrino)


    #####################################
    ###    FUNZIONE CHE PRENDE UNO    ###
    ###  SCONTRINO TRAMITE IL NUMERO  ###
    #####################################
    def get_scontrino_by_numero(self, numero):
        for scontrino in self.lista_scontrini:
            if scontrino.num_scontrino == numero:
                return scontrino


    #####################################
    ###   FUNZIONE CHE ELIMINA UNO    ###
    ###  SCONTRINO TRAMITE IL NUMERO  ###
    #####################################
    def elimina_scontrino_by_numero(self, numero):
        for scontrino in self.lista_scontrini:
            if scontrino.num_scontrino == numero:
                self.lista_scontrini.remove(scontrino)
  

    ####################################################
    ###    FUNZIONE CHE SALVA I DATI ALL'INTERNO     ### 
    ###   DEL FILE "lista_scontrini_salvata.pickle"  ###
    ####################################################
    def save_data(self):
        with open('listascontrini/data/lista_scontrini_salvata.pickle', 'wb') as handle:
            pickle.dump(self.lista_scontrini, handle, pickle.HIGHEST_PROTOCOL)