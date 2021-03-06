import json
import os
import pickle

from articolo.model.Articolo import Articolo

###########################################################################
###  QUESTA CLASSE MODELLA LA LISTA DEGLI ARTICOLI DELLA CARTOLIBRERIA  ###
###                  CON IL CORRISPONDENTW ATTRIBUTI                    ###
###########################################################################
class ListaArticoli():
    def __init__(self):
        super(ListaArticoli, self).__init__()

        self.lista_articoli = []
        self.populate_lista_articoli()

    ####################################################################
    ###   METODO CHE POPOLA LA LISTA DEGLI ARTICOLI CON LE ISTANZE   ###
    ###                   PRESENTI NEL FILE PICKLE                   ###
    ####################################################################
    def populate_lista_articoli(self):
        if os.path.isfile('listaarticoli/data/lista_articoli_salvata.pickle'):
            with open('listaarticoli/data/lista_articoli_salvata.pickle', 'rb') as f:
                self.lista_articoli = pickle.load(f)
        else:
            with open('listaarticoli/data/lista_articoli_iniziali.json') as f:
                lista_articoli_iniziali = json.load(f)
            for articolo_iniziale in lista_articoli_iniziali:
                self.aggiungi_articolo(Articolo(articolo_iniziale["codice"], articolo_iniziale["gruppo_merceologico"], articolo_iniziale["categoria"],
                                                articolo_iniziale["marca"], articolo_iniziale["prezzo_unitario"], articolo_iniziale["sconto_perc"],
                                                articolo_iniziale["descrizione"], articolo_iniziale["stock"]))

    def aggiungi_articolo(self, articolo):
        self.lista_articoli.append(articolo)

    def get_articolo_by_codice(self, codice):
        for articolo in self.lista_articoli:
            if codice == articolo.codice:
                return articolo

    def get_stock_by_codice(self, codice):
        for articolo in self.lista_articoli:
            if codice == articolo.codice:
                return articolo.stock

    def rimuovi_articolo_by_codice(self, codice):
        for articolo in self.lista_articoli:
            if codice == articolo.codice:
                self.lista_articoli.remove(articolo)

    def save_data(self):
        with open('listaarticoli/data/lista_articoli_salvata.pickle', 'wb') as handle:
            pickle.dump(self.lista_articoli, handle, pickle.HIGHEST_PROTOCOL)
