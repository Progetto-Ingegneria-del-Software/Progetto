from listaarticolimagazzino.model.Lista_articoli_magazzino import Lista_articoli_magazzino


class ControlloreListaArticoli():
    def __init__(self):
        super(ControlloreListaArticoli, self).__init__()

        self.model = Lista_articoli_magazzino()

    def aggiungi_articolo(self, articolo):
        self.model.aggiungi_articolo(articolo)

    def get_lista_articoli(self):
        return self.model.lista_articoli_magazzino

    def get_articolo_by_id(self, id):
        return self.model.get_articolo_by_id(id)

    def elimina_articolo_by_id(self, id):
        self.model.rimuovi_articolo_by_id(id)

    def save_data(self):
        self.model.save_data()