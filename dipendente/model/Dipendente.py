################################################################
###  QUESTA CLASSE MODELLA I DIPENDENTI DELLA CARTOLIBRERIA  ###
###             CON I CORRISPONDENTI ATTRIBUTI               ###
################################################################
class Dipendente():
    def __init__(self, codice_id, nome, cognome, cf, email, telefono, mansione, stipendio_mensile):
        super(Dipendente, self).__init__()

        self.codice_id = codice_id
        self.nome = nome
        self.cognome = cognome
        self.cf = cf
        self.email = email
        self.telefono = telefono
        self.mansione = mansione
        self.stipendio_mensile = stipendio_mensile
