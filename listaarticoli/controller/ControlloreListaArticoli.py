from articolo.controller.ControlloreArticolo import ControlloreArticolo
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

    def inserimento_carico (self, codice_barre, stock):
        for articolo in self.get_lista_articoli():
            if codice_barre == articolo.codice:
                controller_articolo = ControlloreArticolo(articolo)
                getstock=controller_articolo.get_stock_articolo()
                totstock= getstock + int(stock)
                controller_articolo.set_stock_articolo(totstock)
                return True
        return False

    def scarico (self, codice_barre, stock):
        for articolo in self.get_lista_articoli():
            if codice_barre == articolo.codice:
                controller_articolo = ControlloreArticolo(articolo)
                getstock = controller_articolo.get_stock_articolo()
                totstock = getstock - int(stock)
                if totstock < 0:
                    return False
                controller_articolo.set_stock_articolo(totstock)
                return True
        return False

    def save_data(self):
        self.model.save_data()