from listafornitori.model.ListaFornitori import ListaFornitori


class ControlloreListaFornitori():
    def __init__(self):
        super(ControlloreListaFornitori, self).__init__()

        self.model = ListaFornitori()

    def aggiungi_fornitore(self, fornitore):
        self.model.aggiungi_fornitore(fornitore)

    def get_lista_fornitori(self):
        return self.model.lista_fornitori

    def get_fornitore_by_index(self, index):
        return self.model.get_fornitore_by_index(index)

    def elimina_fornitore_by_id(self, id):
        self.model.rimuovi_fornitore_by_id(id)

    def save_data(self):
        self.model.save_data()