#####################################################################
###  QUESTA CLASSE VIENE UTILIZZATA PER ELABORARE LE INTERAZIONI  ###
###          CHE L'UTENTE ATTUA CON LA VISTA DEL CLIENTE          ###
#####################################################################
class Controllore_cliente():
    def __init__(self, cliente):
        super(Controllore_cliente, self).__init__()

        self.model = cliente

    ###################
    ###   GETTERS   ###
    ###################

    def get_codice_id_cliente(self):
        return self.model.codice_id

    def get_nome_cliente(self):
        return self.model.nome

    def get_cognome_cliente(self):
        return self.model.cognome

    def get_cf_cliente(self):
        return self.model.cf

    def get_email_cliente(self):
        return self.model.email

    def get_telefono_cliente(self):
        return self.model.telefono

    def get_citta_cliente(self):
        return self.model.citta

    def get_indirizzo_cliente(self):
        return self.model.indirizzo

    ###################
    ###   SETTERS   ###
    ###################

    def set_nome_cliente(self, nome):
        self.model.nome = nome

    def set_cognome_cliente(self, cognome):
        self.model.cognome = cognome

    def set_cf_cliente(self, cf):
        self.model.cf = cf

    def set_email_cliente(self, email):
        self.model.email = email

    def set_telefono_cliente(self, telefono):
        self.model.telefono = telefono

    def set_citta_cliente(self, citta):
        self.model.citta = citta

    def set_indirizzo_cliente(self, indirizzo):
        self.model.indirizzo = indirizzo


