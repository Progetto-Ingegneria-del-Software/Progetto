import json
import os
import pickle

from fattura.model.Fattura import Fattura   #Viene importata la classe di modellazione di una fattura


class ListaFatture():

    def __init__(self):
        super(ListaFatture, self).__init__()

        self.lista_fatture = []   #Lista delle fatture
        self.populate_lista_fatture()
        self.numero_fattura = self.assegna_numero_fattura()   #Assegnamento numero ad ogni fattura


    ######################################
    ###  FUNZIONE CHE ASSEGNA AD OGNI  ### 
    ###        FATTURA UN NUMERO       ###
    ######################################
    def assegna_numero_fattura(self):
        self.i = 0
        for fattura in self.lista_fatture:
            if fattura.num_fatt > 0:
                self.i = fattura.num_fatt
        return self.i


    ################################
    ###  FUNZIONE CHE POPOLA LA  ### 
    ###    LISTA DELLE FATTURE   ###
    ################################
    def populate_lista_fatture(self):
        #Controlla se il file esiste
        if os.path.isfile('listafatture/data/lista_fatture_salvata.pickle'):
            with open('listafatture/data/lista_fatture_salvata.pickle', 'rb') as f:
                self.lista_fatture = pickle.load(f)
        else:
            with open('listafatture/data/lista_fatture_iniziali.json') as f:
                lista_fatture_iniziali = json.load(f)
            for fattura_iniziale in lista_fatture_iniziali:
                self.aggiungi_fattura(Fattura(fattura_iniziale["num_fatt"], fattura_iniziale["tipo"], fattura_iniziale["data"],         ###### DA VEDERE #####
                                                fattura_iniziale["soggetto"], fattura_iniziale["lista_articoli"], fattura_iniziale["totale"]))


    def aggiungi_fattura(self, fattura):
        self.lista_fatture.append(fattura)


    def get_fattura_by_index(self, index):
        return self.lista_fatture[index]

  
    #################################################
    ###   FUNZIONE CHE SALVA I DATI ALL'INTERNO   ### 
    ###  DEL FILE "lista_fatture_salvata.pickle"  ###
    #################################################
    def save_data(self):
        with open('listafatture/data/lista_fatture_salvata.pickle', 'wb') as handle:
            pickle.dump(self.lista_fatture, handle, pickle.HIGHEST_PROTOCOL)