import json
import os
import pickle

from articolo.model.Articolo import Articolo


class ListaArticoli():
    def __init__(self):
        super(ListaArticoli, self).__init__()

        self.lista_articoli = []
        self.populate_lista_articoli()
        # self.codice_id = self.assegna_contatore_id

        '''
    def assegna_contatore_id(self):
        self.i = 0
        for articolo in self.lista_articoli:
            if articolo.codice_id > 0:
                self.i = articolo.codice_id
        return self.i
        '''

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

    def rimuovi_articolo_by_codice(self, codice):
        for articolo in self.lista_articoli:
            if codice == articolo.codice:
                self.lista_articoli.remove(articolo)

    def save_data(self):
        with open('listaarticoli/data/lista_articoli_salvata.pickle', 'wb') as handle:
            pickle.dump(self.lista_articoli, handle, pickle.HIGHEST_PROTOCOL)
