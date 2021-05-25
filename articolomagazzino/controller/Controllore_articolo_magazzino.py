class Controllore_articolo_magazzino:
    def __init__(self, articolo_magazzino):
        super(Controllore_articolo_magazzino, self).__init__()

        self.model = articolo_magazzino

    def get_codice_id_articolo(self):
        return self.model.codice_id

    def get_codice_barre(self):
        return self.model.get_codice_barre


    def get_stock(self):
        return self.model.get_stock




    def get_descrizione_articolo(self):
        return self.model.descrizione

    def set_codice_barre(self, codice_barre):
        self.model.get_codice_barre = codice_barre


    def set_stock(self):
        return self.model.get_stock

    def set_descrizione_articolo(self, descrizione):
        self.model.descrizione = descrizione