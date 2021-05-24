from fornitore.model.Fornitore import Fornitore
from listaarticoli.model.ListaArticoli import ListaArticoli

class Fattura():
    def __init__(self, num_fatt, tipo_fatt, data, soggetto, articoli, totale):
        super(Fattura, self).__init__()

        self.num_fatt = num_fatt
        self.tipo_fatt = tipo_fatt  #Fattura di carico o scarico
        self.data = data
        self.soggetto = soggetto
        self.articoli = articoli
        self.totale = totale

