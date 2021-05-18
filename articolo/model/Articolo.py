class Articolo():
    def __init__(self, codice_id, gruppo_merceologico, categoria, marca, prezzo_unitario, sconto_perc, quantita):
        super(Articolo, self).__init__()

        self.codice_id = codice_id
        self.gruppo_merceologico = gruppo_merceologico
        self.categoria = categoria
        self.marca = marca
        self.prezzo_unitario = prezzo_unitario
        self.sconto_perc = sconto_perc
        self.quantita = quantita

    def scorte_terminate(self):
        return self.quantita == 0
