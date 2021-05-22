
import os
import pickle


from clientePIva.model.Cliente_P_Iva import Cliente_P_Iva


class Lista_clientipiva():
    def __init__(self):
        super(Lista_clientipiva, self).__init__()

        self.lista_clientipiva = []
        self.populate_lista_clientipiva()
        self.codice_id = self.assegna_contatore_id()

    def assegna_contatore_id(self):
        self.i = 0
        for clientepiva in self.lista_clientipiva:
            if clientepiva.codice_id > 0:
                self.i = clientepiva.codice_id
        return self.i

    def populate_lista_clientipiva(self):
        if os.path.isfile('listaclientiPIva/data/lista_clientipiva_salvata.pickle'):
            with open('listaclientiPIva/data/lista_clientipiva_salvata.pickle', 'rb') as f:
                self.lista_clientipiva = pickle.load(f)


    def aggiungi_clientepiva(self, clientepiva):
        self.lista_clientipiva.append(clientepiva)

    def get_clientepiva_by_index(self, index):
        return self.lista_clientipiva[index]

    def rimuovi_clientepiva_by_id(self, id):
        for clientpiva in self.lista_clientipiva:
            if id == clientpiva.codice_id:
                self.lista_clientipiva.remove(clientpiva)

    def save_data(self):
        with open('listaclientiPIva/data/lista_clientipiva_salvata.pickle', 'wb') as handle:
            pickle.dump(self.lista_clientipiva, handle, pickle.HIGHEST_PROTOCOL)
