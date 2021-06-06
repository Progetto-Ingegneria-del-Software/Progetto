import unittest
from cliente.model.Cliente import Cliente
from cliente.controller.Controllore_cliente import Controllore_cliente


class test_ControlloreCliente(unittest.TestCase):
    
    ###########################################################
    ##  FUNZIONE CHE INIZIALIZZA UN OGGETTO DI TIPO Cliente  ##
    ###########################################################
    def setUp(self):
        self.cliente = Cliente("1", "Salvo", "Savadori", "SLVSVD78D12E456D", "salvosava@yahoo.it", "3895568741", "Roma", "Via Pascoli, 9")
        self.controller = Controllore_cliente(self.cliente)


    #############################################################################
    ##  TEST DELLE FUNZIONI PER LA GESTIONE DEL CODICE ID DEL CLIENTE PRIVATO  ##
    #############################################################################
    def test_codice_id(self):
        self.assertEqual(self.controller.get_codice_id_cliente(), "1")  # TESTO IL CORRETTO FUNZIONAMENTO DELLA FUNZIONE get_codice_id_cliente()
        

    ########################################################################
    ##  TEST DELLE FUNZIONI PER LA GESTIONE DEL NOME DEL CLIENTE PRIVATO  ##
    ########################################################################
    def test_nome(self):
        self.assertEqual(self.controller.get_nome_cliente(), 'Salvo')  # TESTO IL CORRETTO FUNZIONAMENTO DELLA FUNZIONE get_nome_cliente()

        # ORA TESTO IL CORRETTO FUNZIONAMENTO DELLA FUNZIONE set_nome_cliente()
        self.controller.set_nome_cliente('Andrea')
        self.assertEqual(self.controller.get_nome_cliente(), 'Andrea')


    ###########################################################################
    ##  TEST DELLE FUNZIONI PER LA GESTIONE DEL COGNOME DEL CLIENTE PRIVATO  ##
    ###########################################################################
    def test_cognome(self):
        self.assertEqual(self.controller.get_cognome_cliente(), 'Savadori')  # TESTO IL CORRETTO FUNZIONAMENTO DELLA FUNZIONE get_cognome_cliente()

        # ORA TESTO IL CORRETTO FUNZIONAMENTO DELLA FUNZIONE set_gruppo_merceologico_articolo()
        self.controller.set_cognome_cliente('Camilleri')
        self.assertEqual(self.controller.get_cognome_cliente(), 'Camilleri')

    
    ##################################################################################
    ##  TEST DELLE FUNZIONI PER LA GESTIONE DEL CODICE FISCALE DEL CLIENTE PRIVATO  ##
    ##################################################################################
    def test_codice_fiscale(self):
        self.assertEqual(self.controller.get_cf_cliente(), 'SLVSVD78D12E456D')  # TESTO IL CORRETTO FUNZIONAMENTO DELLA FUNZIONE get_cf_cliente()

        # ORA TESTO IL CORRETTO FUNZIONAMENTO DELLA FUNZIONE set_cf_cliente()
        self.controller.set_cf_cliente('VVVDDDE345SYYYY')
        self.assertEqual(self.controller.get_cf_cliente(), 'VVVDDDE345SYYYY')


    ####################################################################################
    ##  TEST DELLE FUNZIONI PER LA GESTIONE DELL'INDIRIZZO EMAIL DEL CLIENTE PRIVATO  ##
    ####################################################################################
    def test_email(self):
        self.assertEqual(self.controller.get_email_cliente(), 'salvosava@yahoo.it')  # TESTO IL CORRETTO FUNZIONAMENTO DELLA FUNZIONE get_email_cliente()

        # ORA TESTO IL CORRETTO FUNZIONAMENTO DELLA FUNZIONE set_email_cliente()
        self.controller.set_email_cliente('salvosavadori@gmail.it')
        self.assertEqual(self.controller.get_email_cliente(), 'salvosavadori@gmail.it')


    ######################################################################################
    ##  TEST DELLE FUNZIONI PER LA GESTIONE DEL NUMERO DI TELEFONO DEL CLIENTE PRIVATO  ##
    ######################################################################################
    def test_telefono(self):
        self.assertEqual(self.controller.get_telefono_cliente(), '3895568741')  # TESTO IL CORRETTO FUNZIONAMENTO DELLA FUNZIONE get_telefono_cliente()

        # ORA TESTO IL CORRETTO FUNZIONAMENTO DELLA FUNZIONE set_telefono_cliente()
        self.controller.set_telefono_cliente('3335684123')
        self.assertEqual(self.controller.get_telefono_cliente(), '3335684123')


    ###########################################################################
    ##  TEST DELLE FUNZIONI PER LA GESTIONE DELLA CITTÀ DEL CLIENTE PRIVATO  ##
    ###########################################################################
    def test_citta(self):
        self.assertEqual(self.controller.get_citta_cliente(), 'Roma')  # TESTO IL CORRETTO FUNZIONAMENTO DELLA FUNZIONE get_citta_cliente()

        # ORA TESTO IL CORRETTO FUNZIONAMENTO DELLA FUNZIONE set_citta_cliente()
        self.controller.set_citta_cliente('Torino')
        self.assertEqual(self.controller.get_citta_cliente(), 'Torino')


    ##############################################################################
    ##  TEST DELLE FUNZIONI PER LA GESTIONE DELL'INDIRIZZO DEL CLIENTE PRIVATO  ##
    ##############################################################################
    def test_indirizzo(self):
        self.assertEqual(self.controller.get_indirizzo_cliente(), 'Via Pascoli, 9')  # TESTO IL CORRETTO FUNZIONAMENTO DELLA FUNZIONE get_indirizzo_cliente()

        # ORA TESTO IL CORRETTO FUNZIONAMENTO DELLA FUNZIONE set_indirizzo_cliente()
        self.controller.set_indirizzo_cliente('Via Cavour, 22')
        self.assertEqual(self.controller.get_indirizzo_cliente(), 'Via Cavour, 22')

    
if __name__ == '__main__':
    unittest.main()
