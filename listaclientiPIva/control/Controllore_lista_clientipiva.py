
from listaclientiPIva.model.Lista_clientipiva import Lista_clientipiva


class Controllore_lista_clientipiva():
    def __init__(self):
        super(Controllore_lista_clientipiva, self).__init__()

        self.model = Lista_clientipiva()

    def aggiungi_clientepiva(self, clientepiva):
        self.model.aggiungi_clientepiva(clientepiva)

    def get_lista_clientipiva(self):
        return self.model.lista_clientipiva

    def get_clientepiva_by_index(self, index):
        return self.model.get_clientepiva_by_index(index)

    def elimina_clientepiva_by_id(self, id):
        self.model.rimuovi_clientepiva_by_id(id)

    def save_data(self):
        self.model.save_data()