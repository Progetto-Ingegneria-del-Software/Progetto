from fornitore.model.Fornitore import Fornitore
from listaarticoli.model.ListaArticoli import ListaArticoli

class Fattura():
    def __init__(self, num_fatt, tipo, data, Cliente, Fornitore, ListaArticoli, totale):
        super(Fattura, self).__init__()

        self.num_fatt = num_fatt
        self.tipo = tipo  #Fattura di carico o scarico
        self.data = data
        #self.Cliente = Cliente
        self.Fornitore = Fornitore
        self.ListaArticoli = ListaArticoli
        self.totale = totale

