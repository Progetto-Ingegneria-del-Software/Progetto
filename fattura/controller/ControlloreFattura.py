class ControlloreFattura:

    def __init__(self, fattura):
        super(ControlloreFattura, self).__init__()

        self.model.Fattura = fattura

    ###################
    ###   GETTERS   ###
    ###################
    def get_numero_fattura(self):
        return self.model.num_fatt

    def get_tipo_fattura(self):
        return self.model.tipo

    def get_data(self):
        return self.model.data

    #def get_cliente(self):
    #    return self.model.Cliente

    #def get_fornitore(self):
    #    return self.model.Fornitore

    #def get_lista_articoli(self):
    #    return self.model.ListaArticoli

    def get_totale(self):
        return self.model.totale


    ###################
    ###   SETTERS   ###
    ###################
    def set_numero_fattura(self, num_fatt):
        self.model.num_fatt = num_fatt

    def set_tipo_fattura(self, tipo):
        self.model.tipo = tipo

    def set_data(self, data):
        self.model.data = data

    #def set_cliente(self, Cliente):
    #    self.model.Cliente = Cliente

    #def set_fornitore(self, Fornitore):
    #    self.model.Fornitore = Fornitore

    #def set_lista_articoli(self, ListaArticoli):
    #   self.model.ListaArticoli = ListaArticoli

    def set_totale(self, totale):
        self.model.totale = totale