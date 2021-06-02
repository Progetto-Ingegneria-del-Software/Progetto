from listaclienti.model.Lista_clienti import Lista_clienti


class Controllore_Lista_clienti():
    def __init__(self):
        super(Controllore_Lista_clienti, self).__init__()

        self.model = Lista_clienti()

    def aggiungi_cliente(self, cliente):
        self.model.aggiungi_cliente(cliente)

    def get_lista_clienti(self):
        return self.model.lista_clienti

    def get_cliente_by_index(self, index):
        return self.model.get_cliente_by_index(index)

    def elimina_cliente_by_id(self, id):
        self.model.rimuovi_cliente_by_id(id)

    def save_data(self):
        self.model.save_data()