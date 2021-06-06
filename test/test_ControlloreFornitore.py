import unittest
from fornitore.model.Fornitore import Fornitore
from fornitore.control.ControlloreFornitore import ControlloreFornitore


class test_ControlloreFornitore(unittest.TestCase):
    
    #############################################################
    ##  FUNZIONE CHE INIZIALIZZA UN OGGETTO DI TIPO Fornitore  ##
    #############################################################
    def setUp(self):
        self.fornitore = Fornitore("6", "Apple s.p.a.", "082155846952", "Firenze", "Via Verdi, 16", "3391569874", "info@apple.it")
        self.controller = ControlloreFornitore(self.fornitore)


    #######################################################################
    ##  TEST DELLE FUNZIONI PER LA GESTIONE DEL CODICE ID DEL FORNITORE  ##
    #######################################################################
    def test_codice_id(self):
        self.assertEqual(self.controller.get_codice_id_fornitore(), "6")  # TESTO IL CORRETTO FUNZIONAMENTO DELLA FUNZIONE get_codice_id_fornitore()
        

    ###############################################################################
    ##  TEST DELLE FUNZIONI PER LA GESTIONE DELLA RAGIONE SOCIALE DEL FORNITORE  ##
    ###############################################################################
    def test_ragione_sociale(self):
        self.assertEqual(self.controller.get_ragione_sociale_fornitore(), 'Apple s.p.a.')  # TESTO IL CORRETTO FUNZIONAMENTO DELLA FUNZIONE get_ragione_sociale_fornitore()

        # ORA TESTO IL CORRETTO FUNZIONAMENTO DELLA FUNZIONE set_ragione_sociale_fornitore()
        self.controller.set_ragione_sociale_fornitore('Samsung s.p.a.')
        self.assertEqual(self.controller.get_ragione_sociale_fornitore(), 'Samsung s.p.a.')


    ###########################################################################
    ##  TEST DELLE FUNZIONI PER LA GESTIONE DELLA PARTITA IVA DEL FORNITORE  ##
    ###########################################################################
    def test_partita_iva(self):
        self.assertEqual(self.controller.get_partita_iva_fornitore(), '082155846952')  # TESTO IL CORRETTO FUNZIONAMENTO DELLA FUNZIONE get_partita_iva_fornitore()

        # ORA TESTO IL CORRETTO FUNZIONAMENTO DELLA FUNZIONE set_partita_iva_fornitore()
        self.controller.set_partita_iva_fornitore('085215649854')
        self.assertEqual(self.controller.get_partita_iva_fornitore(), '085215649854')

    
    #####################################################################
    ##  TEST DELLE FUNZIONI PER LA GESTIONE DELLA CITTÀ DEL FORNITORE  ##
    #####################################################################
    def test_citta(self):
        self.assertEqual(self.controller.get_citta_fornitore(), 'Firenze')  # TESTO IL CORRETTO FUNZIONAMENTO DELLA FUNZIONE get_citta_fornitore()

        # ORA TESTO IL CORRETTO FUNZIONAMENTO DELLA FUNZIONE set_citta_fornitore()
        self.controller.set_citta_fornitore('Palermo')
        self.assertEqual(self.controller.get_citta_fornitore(), 'Palermo')


    ########################################################################
    ##  TEST DELLE FUNZIONI PER LA GESTIONE DELL'INDIRIZZO DEL FORNITORE  ##
    ########################################################################
    def test_indirizzo(self):
        self.assertEqual(self.controller.get_indirizzo_fornitore(), 'Via Verdi, 16')  # TESTO IL CORRETTO FUNZIONAMENTO DELLA FUNZIONE get_indirizzo_fornitore()

        # ORA TESTO IL CORRETTO FUNZIONAMENTO DELLA FUNZIONE set_indirizzo_fornitore()
        self.controller.set_indirizzo_fornitore('Via Leopardi, 15')
        self.assertEqual(self.controller.get_indirizzo_fornitore(), 'Via Leopardi, 15')
        
    
    ##############################################################################
    ##  TEST DELLE FUNZIONI PER LA GESTIONE DELL'INDIRIZZO EMAIL DEL FORNITORE  ##
    ##############################################################################
    def test_email(self):
        self.assertEqual(self.controller.get_email_fornitore(), 'info@apple.it')  # TESTO IL CORRETTO FUNZIONAMENTO DELLA FUNZIONE get_email_fornitore()

        # ORA TESTO IL CORRETTO FUNZIONAMENTO DELLA FUNZIONE set_email_fornitore()
        self.controller.set_email_fornitore('commerciale@apple.com')
        self.assertEqual(self.controller.get_email_fornitore(), 'commerciale@apple.com')


    ################################################################################
    ##  TEST DELLE FUNZIONI PER LA GESTIONE DEL NUMERO DI TELEFONO DEL FORNITORE  ##
    ################################################################################
    def test_telefono(self):
        self.assertEqual(self.controller.get_telefono_fornitore(), '3391569874')  # TESTO IL CORRETTO FUNZIONAMENTO DELLA FUNZIONE get_telefono_fornitore()

        # ORA TESTO IL CORRETTO FUNZIONAMENTO DELLA FUNZIONE set_telefono_fornitore()
        self.controller.set_telefono_fornitore('3335684123')
        self.assertEqual(self.controller.get_telefono_fornitore(), '3335684123')


    
if __name__ == '__main__':
    unittest.main()
