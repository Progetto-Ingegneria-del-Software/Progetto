#############################################################
###  QUESTA CLASSE MODELLA I CLIENTI DELLA CARTOLIBRERIA  ###
###             POSSESSORI DI PARTITA IVA                 ###
###           CON I CORRISPONDENTI ATTRIBUTI              ###
#############################################################
class Cliente_P_Iva():
    def __init__(self, codice_id, ragione_sociale, partita_iva, citta, indirizzo, telefono, email):
        super(Cliente_P_Iva, self).__init__()

        self.codice_id = codice_id
        self.ragione_sociale = ragione_sociale
        self.partita_iva = partita_iva
        self.citta = citta
        self.indirizzo = indirizzo
        self.telefono = telefono
        self.email = email
