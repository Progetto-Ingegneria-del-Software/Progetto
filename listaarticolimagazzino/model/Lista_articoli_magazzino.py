#import json
import os
import pickle

from articolomagazzino.model.Articolo_magazzino import Articolo_magazzino


class Lista_articoli_magazzino():
    def __init__(self):
        super(Lista_articoli_magazzino, self).__init__()

        self.lista_articoli_magazzino = []
        self.populate_lista_articoli_magazzino()
        self.codice_id = self.assegna_contatore_id()

    def assegna_contatore_id(self):
        self.i = 0
        for articolo_magazzino in self.lista_articoli_magazzino:
            if articolo_magazzino.codice_id > 0:
                self.i = articolo_magazzino.codice_id
        return self.i

    def populate_lista_articoli_magazzino(self):
        if os.path.isfile('listaarticolimagazzino/data/lista_articoli_magazzino_salvata.pickle'):
            with open('listaarticolimagazzino/data/lista_articoli_magazzino_salvata.pickle', 'rb') as f:
                self.lista_articoli_magazzino = pickle.load(f)
      #  else:
       #     with open('listaarticolimagazzino/data/lista_articoli_iniziali.json') as f:
        #        lista_articoli_iniziali = json.load(f)
         #   for articolo_iniziale in lista_articoli_iniziali:
          #      self.aggiungi_articolo(Articolo_magazzino(articolo_iniziale["codice_id"], articolo_iniziale["gruppo_merceologico"], articolo_iniziale["categoria"],
           #                                               articolo_iniziale["marca"], articolo_iniziale["prezzo_unitario"], articolo_iniziale["sconto_perc"],
            #                                              articolo_iniziale["descrizione"]))

    def aggiungi_articolo(self, articolo_magazzino):
        self.lista_articoli_magazzino.append(articolo_magazzino)

    def get_articolo_by_id(self, id):
        for articolo_magazzino in self.lista_articoli_magazzino:
            if id == articolo_magazzino.codice_id:
                return articolo_magazzino

    def rimuovi_articolo_by_id(self, id):
        for articolo_magazzino in self.lista_articoli_magazzino:
            if id == articolo_magazzino.codice_id:
                self.lista_articoli_magazzino.remove(articolo_magazzino)

    def save_data(self):
        with open('listaarticolimagazzino/data/lista_articoli_magazzino_salvata.pickle', 'wb') as handle:
            pickle.dump(self.lista_articoli_magazzino, handle, pickle.HIGHEST_PROTOCOL)
