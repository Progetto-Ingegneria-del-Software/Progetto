class ControlloreArticolo:
    def __init__(self, articolo):
        super(ControlloreArticolo, self).__init__()

        self.model = articolo

    def get_codice_articolo(self):
        return self.model.codice

    def get_gruppo_merceologico_articolo(self):
        return self.model.gruppo_merceologico

    def get_categoria_articolo(self):
        return self.model.categoria

    def get_marca_articolo(self):
        return self.model.marca

    def get_prezzo_unitario_articolo(self):
        return self.model.prezzo_unitario

    def get_sconto_perc_articolo(self):
        return self.model.sconto_perc

    def get_descrizione_articolo(self):
        return self.model.descrizione

    def set_codice_articolo(self, codice):
        self.model.codice = codice

    def set_gruppo_merceologico_articolo(self, gruppo_merceologico):
        self.model.gruppo_merceologico = gruppo_merceologico

    def set_categoria_articolo(self, categoria):
        self.model.categoria = categoria

    def set_marca_articolo(self, marca):
        self.model.marca = marca

    def set_prezzo_unitario_articolo(self, prezzo_unitario):
        self.model.prezzo_unitario = prezzo_unitario

    def set_sconto_perc_articolo(self, sconto_perc):
        self.model.sconto_perc = sconto_perc

    def set_descrizione_articolo(self, descrizione):
        self.model.descrizione = descrizione