#################################################################
###  QUESTA CLASSE MODELLA GLI SCONTRINI DELLA CARTOLIBRERIA  ###
###              CON I CORRISPONDENTI ATTRIBUTI               ###
#################################################################
class Scontrino():
    def __init__(self, num_scontrino, data, articoli, totale):
        super(Scontrino, self).__init__()

        self.num_scontrino = num_scontrino
        self.data = data
        self.articoli = articoli
        self.totale = totale

