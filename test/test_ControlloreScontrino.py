import unittest
from scontrino.model.Scontrino import Scontrino
from scontrino.controller.ControlloreScontrino import ControlloreScontrino

class test_ControlloreScontrino(unittest.TestCase):
    
    #############################################################
    ##  FUNZIONE CHE INIZIALIZZA UN OGGETTO DI TIPO Scontrino  ##
    #############################################################
    def setUp(self):
        self.scontrino = Scontrino("4", "21-06-2021", "4856235112831, 9005235068131", 35)
        self.controller = ControlloreScontrino(self.scontrino)


    ######################################################################
    ##  TEST DELLA FUNZIONE PER LA GESTIONE DEL NUMERO DELLO SCONTRINO  ##
    ######################################################################
    def test_numero_scontrino(self):
        self.assertEqual(self.controller.get_numero_scontrino(), "4")  # TESTO IL CORRETTO FUNZIONAMENTO DELLA FUNZIONE get_numero_scontrino()
        

    ######################################################################
    ##  TEST DELLA FUNZIONE PER LA GESTIONE DELLA DATA DELLO SCONTRINO  ##
    ######################################################################
    def test_data(self):
        self.assertEqual(self.controller.get_data_scontrino(), '21-06-2021')  # TESTO IL CORRETTO FUNZIONAMENTO DELLA FUNZIONE get_data_scontrino()

    
    ###################################################################
    ##  TEST DELLA FUNZIONE PER LA GESTIONE DEGLI ARTICOLI COMPRATI  ##
    ###################################################################
    def test_articoli_comprati(self):
        self.assertEqual(self.controller.get_articoli_scontrino(), '4856235112831, 9005235068131')  # TESTO IL CORRETTO FUNZIONAMENTO DELLA FUNZIONE get_articoli_scontrino()

    
    ###############################################################################
    ##  TEST DELLA FUNZIONE PER LA GESTIONE DELL'IMPORTO TOTALE DELLO SCONTRINO  ##
    ###############################################################################
    def test_importo_totale(self):
        self.assertEqual(self.controller.get_totale_scontrino(), 35)  # TESTO IL CORRETTO FUNZIONAMENTO DELLA FUNZIONE get_totale_scontrino()


    
if __name__ == '__main__':
    unittest.main()
