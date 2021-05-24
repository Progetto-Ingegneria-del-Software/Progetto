from fornitore.model.Fornitore import Fornitore
from listaarticoli.model.ListaArticoli import ListaArticoli

class Fattura():
    def __init__(self, num_fatt, tipo_fatt, data, tipo_cliente, totale):
        super(Fattura, self).__init__()

        self.num_fatt = num_fatt
        self.tipo_fatt = tipo_fatt  #Fattura di carico o scarico
        self.data = data
        self.tipo_cliente = tipo_cliente
        #self.Fornitore = Fornitore
        #self.ListaArticoli = ListaArticoli
        self.totale = totale

