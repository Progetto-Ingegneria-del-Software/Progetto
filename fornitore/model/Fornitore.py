###############################################################
###  QUESTA CLASSE MODELLA I FORNITORI DELLA CARTOLIBRERIA  ###
###            CON I CORRISPONDENTI ATTRIBUTI               ###
###############################################################
class Fornitore():
    def __init__(self, codice_id, ragione_sociale, partita_iva, citta, indirizzo, telefono, email):
        super(Fornitore, self).__init__()

        self.codice_id = codice_id
        self.ragione_sociale = ragione_sociale
        self.partita_iva = partita_iva
        self.citta = citta
        self.indirizzo = indirizzo
        self.telefono = telefono
        self.email = email
