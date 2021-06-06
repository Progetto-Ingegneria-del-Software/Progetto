#####################################################################
###  QUESTA CLASSE VIENE UTILIZZATA PER ELABORARE LE INTERAZIONI  ###
###        CHE L'UTENTE ATTUA CON LA VISTA DEL FORNITORE          ###
#####################################################################
class ControlloreFornitore():
    def __init__(self, fornitore):
        super(ControlloreFornitore, self).__init__()

        self.model = fornitore

    ###################
    ###   GETTERS   ###
    ###################

    def get_codice_id_fornitore(self):
        return self.model.codice_id

    def get_citta_fornitore(self):
        return self.model.citta

    def get_partita_iva_fornitore(self):
        return self.model.partita_iva

    def get_ragione_sociale_fornitore(self):
        return self.model.ragione_sociale

    def get_indirizzo_fornitore(self):
        return self.model.indirizzo

    def get_telefono_fornitore(self):
        return self.model.telefono

    def get_email_fornitore(self):
        return self.model.email

    ###################
    ###   SETTERS   ###
    ###################

    def set_partita_iva_fornitore(self, partita_iva):
        self.model.partita_iva = partita_iva

    def set_ragione_sociale_fornitore(self, ragione_sociale):
        self.model.ragione_sociale = ragione_sociale

    def set_indirizzo_fornitore(self, indirizzo):
        self.model.indirizzo = indirizzo

    def set_citta_fornitore(self, citta):
        self.model.citta = citta

    def set_telefono_fornitore(self, telefono):
        self.model.telefono = telefono

    def set_email_fornitore(self, email):
        self.model.email = email

