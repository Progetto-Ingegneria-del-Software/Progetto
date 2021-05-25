class ControlloreFattura:

    def __init__(self, fattura):
        super(ControlloreFattura, self).__init__()

        self.model = fattura

    ###################
    ###   GETTERS   ###
    ###################
    def get_numero_fattura(self):
        return self.model.num_fatt

    def get_tipo_fattura(self):
        return self.model.tipo_fatt

    def get_data_fattura(self):
        return self.model.data

    def get_soggetto_fattura(self):
        return self.model.soggetto

    def get_articoli_fattura(self):
        return self.model.articoli

    def get_totale_fattura(self):
        return self.model.totale


    ###################
    ###   SETTERS   ###
    ###################
    def set_tipo_fattura(self, tipo):
        self.model.tipo_fatt = tipo