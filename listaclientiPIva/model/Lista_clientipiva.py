import json
import os
import pickle

from clientePIva.model.Cliente_P_Iva import Cliente_P_Iva

########################################################################
###  QUESTA CLASSE MODELLA LA LISTA DEI CLIENTI DELLA CARTOLIBRERIA  ###
###       DOTATI DI PARTITA IVA CON I CORRISPONDENTI ATTRIBUTI       ###
########################################################################
class Lista_clientipiva():
    def __init__(self):
        super(Lista_clientipiva, self).__init__()

        self.lista_clientipiva = []
        self.populate_lista_clientipiva()
        self.codice_id = self.assegna_contatore_id()

    ############################################################
    ###   METODO CHE ASSEGNA UN CODICE ID AUTOINCREMENTANTE  ###
    ###               DIVERSO PER OGNI CLIENTE               ###
    ############################################################
    def assegna_contatore_id(self):
        self.i = 0
        for clientepiva in self.lista_clientipiva:
            if clientepiva.codice_id > 0:
                self.i = clientepiva.codice_id
        return self.i

    ####################################################################
    ###    METODO CHE POPOLA LA LISTA DEI CLIENTI CON LE ISTANZE    ###
    ###                   PRESENTI NEL FILE PICKLE                   ###
    ####################################################################
    def populate_lista_clientipiva(self):
        if os.path.isfile('listaclientiPIva/data/lista_clientipiva_salvata.pickle'):
            with open('listaclientiPIva/data/lista_clientipiva_salvata.pickle', 'rb') as f:
                self.lista_clientipiva = pickle.load(f)
        else:
            with open('listaclientiPIva/data/lista_clientipiva_iniziali.json') as f:
                lista_clientipiva_iniziali = json.load(f)
            for clientepiva_iniziale in lista_clientipiva_iniziali:
                self.aggiungi_clientepiva(Cliente_P_Iva(clientepiva_iniziale["codice_id"], clientepiva_iniziale["ragione_sociale"], clientepiva_iniziale["partita_iva"],
                                                clientepiva_iniziale["citta"], clientepiva_iniziale["indirizzo"], clientepiva_iniziale["telefono"],
                                                clientepiva_iniziale["email"]))


    ##########################################
    ###  FUNZIONE CHE AGGIUNGE UN CLIENTE  ###
    ###     CON PARTITA IVA ALLA LISTA     ###
    ##########################################
    def aggiungi_clientepiva(self, clientepiva):
        self.lista_clientipiva.append(clientepiva)


    ###########################################
    ###   FUNZIONE CHE PRENDE UN CLIENTE    ###
    ###  CON PARTITA IVA TRAMITE IL CODICE  ###
    ###########################################
    def get_clientepiva_by_index(self, index):
        return self.lista_clientipiva[index]


    ###########################################
    ###   FUNZIONE CHE ELIMINA UN CLIENTE   ###
    ###  CON PARTITA IVA TRAMITE IL CODICE  ###
    ###########################################
    def rimuovi_clientepiva_by_id(self, id):
        for clientpiva in self.lista_clientipiva:
            if id == clientpiva.codice_id:
                self.lista_clientipiva.remove(clientpiva)


    #####################################################
    ###     FUNZIONE CHE SALVA I DATI ALL'INTERNO     ### 
    ###  DEL FILE "lista_clientipiva_salvata.pickle"  ###
    #####################################################
    def save_data(self):
        with open('listaclientiPIva/data/lista_clientipiva_salvata.pickle', 'wb') as handle:
            pickle.dump(self.lista_clientipiva, handle, pickle.HIGHEST_PROTOCOL)
