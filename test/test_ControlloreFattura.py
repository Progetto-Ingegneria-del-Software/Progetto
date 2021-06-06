import unittest
from fattura.model.Fattura import Fattura
from fattura.controller.ControlloreFattura import ControlloreFattura


class test_ControlloreFattura(unittest.TestCase):
    
    ###########################################################
    ##  FUNZIONE CHE INIZIALIZZA UN OGGETTO DI TIPO Fattura  ##
    ###########################################################
    def setUp(self):
        self.fattura = Fattura("3", "Carico", "21-06-2021", "Carta s.r.l.", "9005235068131, 4856235112831", 15)
        self.controller = ControlloreFattura(self.fattura)


    ####################################################################
    ##  TEST DELLA FUNZIONE PER LA GESTIONE DEL NUMERO DELLA FATTURA  ##
    ####################################################################
    def test_numero_fattura(self):
        self.assertEqual(self.controller.get_numero_fattura(), "3")  # TESTO IL CORRETTO FUNZIONAMENTO DELLA FUNZIONE get_numero_fattura()
        

    ###############################################################
    ##  TEST DELLA FUNZIONE PER LA GESTIONE DEL TIPO DI FATTURA  ##
    ###############################################################
    def test_tipo_fattura(self):
        self.assertEqual(self.controller.get_tipo_fattura(), 'Carico')  # TESTO IL CORRETTO FUNZIONAMENTO DELLA FUNZIONE get_tipo_fattura()


    ####################################################################
    ##  TEST DELLA FUNZIONE PER LA GESTIONE DELLA DATA DELLA FATTURA  ##
    ####################################################################
    def test_data(self):
        self.assertEqual(self.controller.get_data_fattura(), '21-06-2021')  # TESTO IL CORRETTO FUNZIONAMENTO DELLA FUNZIONE get_data_fattura()

    
    ##########################################################################################
    ##  TEST DELLA FUNZIONE PER LA GESTIONE DEL SOGGETTO AL QUALE È INDIRIZZATO LA FATTURA  ##
    ##########################################################################################
    def test_soggetto(self):
        self.assertEqual(self.controller.get_soggetto_fattura(), 'Carta s.r.l.')  # TESTO IL CORRETTO FUNZIONAMENTO DELLA FUNZIONE get_soggetto_fattura()


    ###################################################################
    ##  TEST DELLA FUNZIONE PER LA GESTIONE DEGLI ARTICOLI COMPRATI  ##
    ###################################################################
    def test_articoli_comprati(self):
        self.assertEqual(self.controller.get_articoli_fattura(), '9005235068131, 4856235112831')  # TESTO IL CORRETTO FUNZIONAMENTO DELLA FUNZIONE get_articoli_fattura()

    
    #############################################################################
    ##  TEST DELLA FUNZIONE PER LA GESTIONE DELL'IMPORTO TOTALE DELLA FATTURA  ##
    #############################################################################
    def test_importo_totale(self):
        self.assertEqual(self.controller.get_totale_fattura(), 15)  # TESTO IL CORRETTO FUNZIONAMENTO DELLA FUNZIONE get_totale_fattura()


    
if __name__ == '__main__':
    unittest.main()
