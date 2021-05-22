import json
import os
import pickle

from cliente.model.Cliente import Cliente


class Lista_clienti():
    def __init__(self):
        super(Lista_clienti, self).__init__()

        self.lista_clienti = []
        self.populate_lista_clienti()
        self.codice_id = self.assegna_contatore_id()

    def assegna_contatore_id(self):
        self.i = 0
        for cliente in self.lista_clienti:
            if cliente.codice_id > 0:
                self.i = cliente.codice_id
        return self.i

    def populate_lista_clienti(self):
        if os.path.isfile('listaclienti/data/lista_clienti_salvata.pickle'):
            with open('listaclienti/data/lista_clienti_salvata.pickle', 'rb') as f:
                self.lista_clienti = pickle.load(f)

    def aggiungi_cliente(self, cliente):
        self.lista_clienti.append(cliente)

    def get_cliente_by_index(self, index):
        return self.lista_clienti[index]

    #def get_cliente_by_id(self, id):
       # for cliente in self.lista_clienti:
        #    if id == cliente.codice_id:
          #      return cliente

    def rimuovi_cliente_by_id(self, id):
        for cliente in self.lista_clienti:
            if id == cliente.codice_id:
                self.lista_clienti.remove(cliente)

    def save_data(self):
        with open('listaclienti/data/lista_clienti_salvata.pickle', 'wb') as handle:
            pickle.dump(self.lista_clienti, handle, pickle.HIGHEST_PROTOCOL)