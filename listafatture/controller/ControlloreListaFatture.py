from listafatture.model.ListaFatture import ListaFatture


class ControlloreListaFatture():
    def __init__(self):
        super(ControlloreListaFatture, self).__init__()

        self.model = ListaFatture()

    def aggiungi_fattura(self, fattura):
        self.model.aggiungi_fattura(fattura)

    def get_lista_fatture(self):
        return self.model.lista_fatture

    def get_fattura_by_index(self, id):
        return self.model.get_fattura_by_index(id)

    def save_data(self):
        self.model.save_data()