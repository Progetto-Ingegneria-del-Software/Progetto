################################################################
###   QUESTA CLASSE MODELLA I CLIENTI DELLA CARTOLIBRERIA    ###
###             CON I CORRISPONDENTI ATTRIBUTI               ###
################################################################
class Cliente():
    def __init__(self, codice_id, nome, cognome, cf, email, telefono, citta, indirizzo):
        super(Cliente, self).__init__()

        self.codice_id = codice_id
        self.nome = nome
        self.cognome = cognome
        self.cf = cf
        self.email = email
        self.telefono = telefono
        self.citta = citta
        self.indirizzo = indirizzo



