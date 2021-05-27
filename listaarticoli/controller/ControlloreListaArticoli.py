from listaarticoli.model.ListaArticoli import ListaArticoli


class ControlloreListaArticoli():
    def __init__(self):
        super(ControlloreListaArticoli, self).__init__()

        self.model = ListaArticoli()

    def aggiungi_articolo(self, articolo):
        self.model.aggiungi_articolo(articolo)

    def get_lista_articoli(self):
        return self.model.lista_articoli

    def get_articolo_by_codice(self, codice):
        return self.model.get_articolo_by_codice(codice)

    def elimina_articolo_by_codice(self, codice):
        self.model.rimuovi_articolo_by_codice(codice)

    def save_data(self):
        self.model.save_data()