class Articolo_magazzino():
    def __init__(self, codice_id, codice_barre, stock, descrizione):
        super(Articolo_magazzino, self).__init__()

        self.codice_id = codice_id
        self.codice_barre = codice_barre
        self.stock = stock

        self.descrizione = descrizione