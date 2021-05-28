from listascontrini.model.ListaScontrini import ListaScontrini


class ControlloreListaScontrini():
    def __init__(self):
        super(ControlloreListaScontrini, self).__init__()

        self.model = ListaScontrini()

    def aggiungi_scontrino(self, scontrino):
        self.model.aggiungi_fattura(scontrino)

    def get_lista_scontrini(self):
        return self.model.lista_scontrini

    def get_scontrino_by_index(self, id):
        return self.model.get_scontrino_by_index(id)

    def save_data(self):
        self.model.save_data()