from clientePIva.model.Cliente_P_Iva import Cliente_P_Iva


class Controllore_clientepiva():
    def __init__(self, clientepiva):
        super(Controllore_clientepiva, self).__init__()

        self.model = clientepiva

    def get_codice_id_clientepiva(self):
        return self.model.codice_id

    def get_citta_clientepiva(self):
        return self.model.citta

    def get_partita_iva_clientepiva(self):
        return self.model.partita_iva

    def get_ragione_sociale_clientepiva(self):
        return self.model.ragione_sociale

    def get_indirizzo_clientepiva(self):
        return self.model.indirizzo

    def get_telefono_clientepiva(self):
        return self.model.telefono

    def get_email_clientepiva(self):
        return self.model.email

    def set_partita_iva_clientepiva(self, partita_iva):
        self.model.partita_iva = partita_iva

    def set_ragione_sociale_clientepiva(self, ragione_sociale):
        self.model.ragione_sociale = ragione_sociale

    def set_indirizzo_clientepiva(self, indirizzo):
        self.model.indirizzo = indirizzo

    def set_citta_clientepiva(self, citta):
        self.model.citta = citta

    def set_telefono_clientepiva(self, telefono):
        self.model.telefono = telefono

    def set_email_clientepiva(self, email):
        self.model.email = email

