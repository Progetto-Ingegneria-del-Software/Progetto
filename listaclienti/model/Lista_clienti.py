import json
import os
import pickle

from cliente.model.Cliente import Cliente

########################################################################
###  QUESTA CLASSE MODELLA LA LISTA DEI CLIENTI DELLA CARTOLIBRERIA  ###
###                 CON I CORRISPONDENTI ATTRIBUTI                   ###
########################################################################
class Lista_clienti():
    def __init__(self):
        super(Lista_clienti, self).__init__()

        self.lista_clienti = []
        self.populate_lista_clienti()
        self.codice_id = self.assegna_contatore_id()

    ############################################################
    ###   METODO CHE ASSEGNA UN CODICE ID AUTOINCREMENTANTE  ###
    ###               DIVERSO PER OGNI CLIENTE               ###
    ############################################################
    def assegna_contatore_id(self):
        self.i = 0
        for cliente in self.lista_clienti:
            if cliente.codice_id > 0:
                self.i = cliente.codice_id
        return self.i

    ####################################################################
    ###    METODO CHE POPOLA LA LISTA DEI CLIENTI CON LE ISTANZE    ###
    ###                   PRESENTI NEL FILE PICKLE                   ###
    ####################################################################
    def populate_lista_clienti(self):
        if os.path.isfile('listaclienti/data/lista_clienti_salvata.pickle'):
            with open('listaclienti/data/lista_clienti_salvata.pickle', 'rb') as f:
                self.lista_clienti = pickle.load(f)
        else:
            with open('listaclienti/data/lista_clienti_iniziali.json') as f:
                lista_cliente_iniziali = json.load(f)
            for cliente_iniziale in lista_cliente_iniziali:
                self.aggiungi_cliente(Cliente(cliente_iniziale["codice_id"], cliente_iniziale["nome"], cliente_iniziale["cognome"],
                                                cliente_iniziale["cf"], cliente_iniziale["email"], cliente_iniziale["telefono"],
                                                cliente_iniziale["citta"], cliente_iniziale["indirizzo"]))


    ##################################
    ###  FUNZIONE CHE AGGIUNGE UN  ###
    ###     CLIENTE ALLA LISTA     ###
    ##################################
    def aggiungi_cliente(self, cliente):
        self.lista_clienti.append(cliente)


    ####################################
    ###    FUNZIONE CHE PRENDE UN    ###
    ###   CLIENTE TRAMITE IL CODICE  ###
    ####################################
    def get_cliente_by_index(self, index):
        return self.lista_clienti[index]


    ####################################
    ###    FUNZIONE CHE RIMUOVE UN   ###
    ###   CLIENTE TRAMITE IL CODICE  ###
    ####################################
    def rimuovi_cliente_by_id(self, id):
        for cliente in self.lista_clienti:
            if id == cliente.codice_id:
                self.lista_clienti.remove(cliente)


    ###################################################
    ###    FUNZIONE CHE SALVA I DATI ALL'INTERNO    ### 
    ###   DEL FILE "lista_clienti_salvata.pickle"   ###
    ###################################################
    def save_data(self):
        with open('listaclienti/data/lista_clienti_salvata.pickle', 'wb') as handle:
            pickle.dump(self.lista_clienti, handle, pickle.HIGHEST_PROTOCOL)