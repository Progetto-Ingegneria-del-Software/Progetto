from listascontrini.model.ListaScontrini import ListaScontrini


class ControlloreListaScontrini():
    def __init__(self):
        super(ControlloreListaScontrini, self).__init__()

        self.model = ListaScontrini()

    def aggiungi_scontrino(self, scontrino):
        self.model.aggiungi_scontrino(scontrino)

    def get_assegnamento_numero_scontrino(self):
        return self.model.numero_scontrino

    def get_lista_scontrini(self):
        return self.model.lista_scontrini

    def get_scontrino_by_numero(self, numero):
        return self.model.get_scontrino_by_numero(numero)

    def elimina_scontrino_by_numero(self, numero):
        return self.model.elimina_scontrino_by_numero(numero)

    def save_data(self):
        self.model.save_data()