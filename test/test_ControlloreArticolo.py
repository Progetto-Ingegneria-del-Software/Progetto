import unittest
from articolo.model.Articolo import Articolo
from articolo.controller.ControlloreArticolo import ControlloreArticolo


class test_ControlloreArticolo(unittest.TestCase):
    
    ############################################################
    ##  FUNZIONE CHE INIZIALIZZA UN OGGETTO DI TIPO Articolo  ##
    ############################################################
    def setUp(self):
        self.articolo = Articolo(codice="1", gruppo_merceologico="cartoleria", categoria="penne", marca="Bic", prezzo_unitario="0.69", sconto_perc="0", descrizione="penna normale", stock=45)
        self.controller = ControlloreArticolo(self.articolo)


    #######################################################
    ##  TEST DELLE FUNZIONI PER LA GESTIONE DELLO STOCK  ##
    #######################################################
    def test_stock(self):
        self.assertEqual(self.controller.get_stock_articolo(), 45)  # TESTO IL CORRETTO FUNZIONAMENTO DELLA FUNZIONE get_stock_articolo()

        # ORA TESTO IL CORRETTO FUNZIONAMENTO DELLA FUNZIONE set_stock_articolo()
        self.controller.set_stock_articolo(150)
        self.assertEqual(self.controller.get_stock_articolo(), 150)
        

    ##############################################################
    ##  TEST DELLE FUNZIONI PER LA GESTIONE DEL CODICE A BARRE  ##
    ##############################################################
    def test_codicearticolo(self):
        self.assertEqual(self.controller.get_codice_articolo(), '1')  # TESTO IL CORRETTO FUNZIONAMENTO DELLA FUNZIONE get_codice_articolo()

        # ORA TESTO IL CORRETTO FUNZIONAMENTO DELLA FUNZIONE set_codice_articolo()
        self.controller.set_codice_articolo('905847222')
        self.assertEqual(self.controller.get_codice_articolo(), '905847222')


    ###################################################################
    ##  TEST DELLE FUNZIONI PER LA GESTIONE DEL GRUPPO MERCEOLOGICO  ##
    ###################################################################
    def test_gruppomerceologico(self):
        self.assertEqual(self.controller.get_gruppo_merceologico_articolo(), 'cartoleria')  # TESTO IL CORRETTO FUNZIONAMENTO DELLA FUNZIONE get_gruppo_merceologico_articolo()

        # ORA TESTO IL CORRETTO FUNZIONAMENTO DELLA FUNZIONE set_gruppo_merceologico_articolo()
        self.controller.set_gruppo_merceologico_articolo('Modulistica Fiscale')
        self.assertEqual(self.controller.get_gruppo_merceologico_articolo(), 'Modulistica Fiscale')

    
    ###########################################################
    ##  TEST DELLE FUNZIONI PER LA GESTIONE DELLA CATEGORIA  ##
    ###########################################################
    def test_categoria(self):
        self.assertEqual(self.controller.get_categoria_articolo(), 'penne')  # TESTO IL CORRETTO FUNZIONAMENTO DELLA FUNZIONE get_categoria_articolo()

        # ORA TESTO IL CORRETTO FUNZIONAMENTO DELLA FUNZIONE set_categoria_articolo()
        self.controller.set_categoria_articolo('matite')
        self.assertEqual(self.controller.get_categoria_articolo(), 'matite')


    #######################################################
    ##  TEST DELLE FUNZIONI PER LA GESTIONE DELLA MARCA  ##
    #######################################################
    def test_marca(self):
        self.assertEqual(self.controller.get_marca_articolo(), 'Bic')  # TESTO IL CORRETTO FUNZIONAMENTO DELLA FUNZIONE get_marca_articolo()

        # ORA TESTO IL CORRETTO FUNZIONAMENTO DELLA FUNZIONE set_marca_articolo()
        self.controller.set_marca_articolo('Steadler')
        self.assertEqual(self.controller.get_marca_articolo(), 'Steadler')


    ###############################################################
    ##  TEST DELLE FUNZIONI PER LA GESTIONE DEL PREZZO UNITARIO  ##
    ###############################################################
    def test_prezzounitario(self):
        self.assertEqual(self.controller.get_prezzo_unitario_articolo(), '0.69')  # TESTO IL CORRETTO FUNZIONAMENTO DELLA FUNZIONE get_prezzo_unitario_articolo()

        # ORA TESTO IL CORRETTO FUNZIONAMENTO DELLA FUNZIONE set_prezzo_unitario_articolo()
        self.controller.set_prezzo_unitario_articolo('1.56')
        self.assertEqual(self.controller.get_prezzo_unitario_articolo(), '1.56')


    ########################################################
    ##  TEST DELLE FUNZIONI PER LA GESTIONE DELLO SCONTO  ##
    ########################################################
    def test_sconto(self):
        self.assertEqual(self.controller.get_sconto_perc_articolo(), '0')  # TESTO IL CORRETTO FUNZIONAMENTO DELLA FUNZIONE get_sconto_perc_articolo()

        # ORA TESTO IL CORRETTO FUNZIONAMENTO DELLA FUNZIONE set_sconto_perc_articolo()
        self.controller.set_sconto_perc_articolo('10')
        self.assertEqual(self.controller.get_sconto_perc_articolo(), '10')


    #############################################################
    ##  TEST DELLE FUNZIONI PER LA GESTIONE DELLA DESCRIZIONE  ##
    #############################################################
    def test_descrizione(self):
        self.assertEqual(self.controller.get_descrizione_articolo(), 'penna normale')  # TESTO IL CORRETTO FUNZIONAMENTO DELLA FUNZIONE get_descrizione_articolo()

        # ORA TESTO IL CORRETTO FUNZIONAMENTO DELLA FUNZIONE set_descrizione_articolo()
        self.controller.set_descrizione_articolo('Penna nera, grandezza S')
        self.assertEqual(self.controller.get_descrizione_articolo(), 'Penna nera, grandezza S')

    
if __name__ == '__main__':
    unittest.main()
