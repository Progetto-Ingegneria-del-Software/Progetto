from scontrino.model.Scontrino import Scontrino

class ControlloreScontrino:

    def __init__(self, fattura):
        super(ControlloreScontrino, self).__init__()

        self.model = fattura

    ###################
    ###   GETTERS   ###
    ###################
    def get_numero_scontrino(self):
        return self.model.num_scontrino

    def get_data_scontrino(self):
        return self.model.data

    def get_articoli_scontrino(self):
        return self.model.articoli

    def get_totale_scontrino(self):
        return self.model.totale
