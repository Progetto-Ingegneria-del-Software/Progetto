################################################################
###  QUESTA CLASSE MODELLA GLI ARTICOLI DELLA CARTOLIBRERIA  ###
###             CON I CORRISPONDENTI ATTRIBUTI               ###
################################################################
class Articolo():
    def __init__(self, codice, gruppo_merceologico, categoria, marca, prezzo_unitario, sconto_perc, descrizione, stock):
        super(Articolo, self).__init__()

        self.codice = codice
        self.gruppo_merceologico = gruppo_merceologico
        self.categoria = categoria
        self.marca = marca
        self.prezzo_unitario = prezzo_unitario
        self.sconto_perc = sconto_perc
        self.descrizione = descrizione
        self.stock = stock