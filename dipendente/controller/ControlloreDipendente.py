class ControlloreDipendente():
    def __init__(self, dipendente):
        super(ControlloreDipendente, self).__init__()

        self.model = dipendente

    def get_codice_id_dipendente(self):
        return self.model.codice_id

    def get_nome_dipendente(self):
        return self.model.nome

    def get_cognome_dipendente(self):
        return self.model.cognome

    def get_cf_dipendente(self):
        return self.model.cf

    def get_email_dipendente(self):
        return self.model.email

    def get_telefono_dipendente(self):
        return self.model.telefono

    def get_mansione_dipendente(self):
        return self.model.mansione

    def get_stipendio_dipendente(self):
        return self.model.stipendio_mensile

    def set_nome_dipendente(self, nome):
        self.model.nome = nome

    def set_cognome_dipendente(self, cognome):
        self.model.cognome = cognome

    def set_cf_dipendente(self, cf):
        self.model.cf = cf

    def set_email_dipendente(self, email):
        self.model.email = email

    def set_telefono_dipendente(self, telefono):
        self.model.telefono = telefono

    def set_mansione_dipendente(self, mansione):
        self.model.mansione = mansione

    def set_stipendio_dipendente(self, stipendio):
        self.model.stipendio_mensile = stipendio
