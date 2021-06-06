import unittest
from clientePIva.model.Cliente_P_Iva import Cliente_P_Iva
from clientePIva.control.Controllore_clientepiva import Controllore_clientepiva


class test_ControlloreClientePIva(unittest.TestCase):
    
    #################################################################
    ##  FUNZIONE CHE INIZIALIZZA UN OGGETTO DI TIPO Cliente_P_Iva  ##
    #################################################################
    def setUp(self):
        self.cliente = Cliente_P_Iva("5", "Rossi s.p.a.", "085215649854", "Ancona", "Corso Garibaldi, 45", "3394568412", "info@rossi.it")
        self.controller = Controllore_clientepiva(self.cliente)


    #####################################################################
    ##  TEST DELLE FUNZIONI PER LA GESTIONE DEL CODICE ID DEL CLIENTE  ##
    #####################################################################
    def test_codice_id(self):
        self.assertEqual(self.controller.get_codice_id_clientepiva(), "5")  # TESTO IL CORRETTO FUNZIONAMENTO DELLA FUNZIONE get_codice_id_clientepiva()
        

    #############################################################################
    ##  TEST DELLE FUNZIONI PER LA GESTIONE DELLA RAGIONE SOCIALE DEL CLIENTE  ##
    #############################################################################
    def test_ragione_sociale(self):
        self.assertEqual(self.controller.get_ragione_sociale_clientepiva(), 'Rossi s.p.a.')  # TESTO IL CORRETTO FUNZIONAMENTO DELLA FUNZIONE get_ragione_sociale_clientepiva()

        # ORA TESTO IL CORRETTO FUNZIONAMENTO DELLA FUNZIONE set_ragione_sociale_clientepiva()
        self.controller.set_ragione_sociale_clientepiva('Verdi s.p.a.')
        self.assertEqual(self.controller.get_ragione_sociale_clientepiva(), 'Verdi s.p.a.')


    #########################################################################
    ##  TEST DELLE FUNZIONI PER LA GESTIONE DELLA PARTITA IVA DEL CLIENTE  ##
    #########################################################################
    def test_partita_iva(self):
        self.assertEqual(self.controller.get_partita_iva_clientepiva(), '085215649854')  # TESTO IL CORRETTO FUNZIONAMENTO DELLA FUNZIONE get_partita_iva_clientepiva()

        # ORA TESTO IL CORRETTO FUNZIONAMENTO DELLA FUNZIONE set_partita_iva_clientepiva()
        self.controller.set_partita_iva_clientepiva('000451874652')
        self.assertEqual(self.controller.get_partita_iva_clientepiva(), '000451874652')

    
    ###################################################################
    ##  TEST DELLE FUNZIONI PER LA GESTIONE DELLA CITTÀ DEL CLIENTE  ##
    ###################################################################
    def test_citta(self):
        self.assertEqual(self.controller.get_citta_clientepiva(), 'Ancona')  # TESTO IL CORRETTO FUNZIONAMENTO DELLA FUNZIONE get_citta_clientepiva()

        # ORA TESTO IL CORRETTO FUNZIONAMENTO DELLA FUNZIONE set_citta_clientepiva()
        self.controller.set_citta_clientepiva('Torino')
        self.assertEqual(self.controller.get_citta_clientepiva(), 'Torino')


    ######################################################################
    ##  TEST DELLE FUNZIONI PER LA GESTIONE DELL'INDIRIZZO DEL CLIENTE  ##
    ######################################################################
    def test_indirizzo(self):
        self.assertEqual(self.controller.get_indirizzo_clientepiva(), 'Corso Garibaldi, 45')  # TESTO IL CORRETTO FUNZIONAMENTO DELLA FUNZIONE get_indirizzo_clientepiva()

        # ORA TESTO IL CORRETTO FUNZIONAMENTO DELLA FUNZIONE set_indirizzo_clientepiva()
        self.controller.set_indirizzo_clientepiva('Via Manzoni, 89')
        self.assertEqual(self.controller.get_indirizzo_clientepiva(), 'Via Manzoni, 89')
        
    
    ############################################################################
    ##  TEST DELLE FUNZIONI PER LA GESTIONE DELL'INDIRIZZO EMAIL DEL CLIENTE  ##
    ############################################################################
    def test_email(self):
        self.assertEqual(self.controller.get_email_clientepiva(), 'info@rossi.it')  # TESTO IL CORRETTO FUNZIONAMENTO DELLA FUNZIONE get_email_clientepiva()

        # ORA TESTO IL CORRETTO FUNZIONAMENTO DELLA FUNZIONE set_email_clientepiva()
        self.controller.set_email_clientepiva('commerciale@rossi.com')
        self.assertEqual(self.controller.get_email_clientepiva(), 'commerciale@rossi.com')


    ##############################################################################
    ##  TEST DELLE FUNZIONI PER LA GESTIONE DEL NUMERO DI TELEFONO DEL CLIENTE  ##
    ##############################################################################
    def test_telefono(self):
        self.assertEqual(self.controller.get_telefono_clientepiva(), '3394568412')  # TESTO IL CORRETTO FUNZIONAMENTO DELLA FUNZIONE get_telefono_clientepiva()

        # ORA TESTO IL CORRETTO FUNZIONAMENTO DELLA FUNZIONE set_telefono_clientepiva()
        self.controller.set_telefono_clientepiva('3335684123')
        self.assertEqual(self.controller.get_telefono_clientepiva(), '3335684123')


    
if __name__ == '__main__':
    unittest.main()
