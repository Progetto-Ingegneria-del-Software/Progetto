from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QSpacerItem, QSizePolicy, QPushButton, \
    QMessageBox, QGridLayout

#####################################################################
###   QUESTA CLASSE SERVE PER MOSTRARE ALL'UTENTE L'INTERFACCIA   ###
###            DI SCARICO DI UN ARTICOLO DEL MAGAZZINO            ###
#####################################################################
class Vista_scarico_articolo(QWidget):
    def __init__(self, controller, callback):
        super(Vista_scarico_articolo, self).__init__()

        self.controller = controller
        self.callback = callback
        self.info = {}
        self.labels = ["Codice a barre:", "Quantità da decrementare:"]

        self.v_layout = QVBoxLayout()
        self.grid_layout = QGridLayout()

        self.unload_item_view()

        self.v_layout.addLayout(self.grid_layout)

        self.v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_ok = QPushButton("Scarica articolo")
        btn_ok.clicked.connect(self.unload_articolo)

        self.v_layout.addWidget(btn_ok)

        self.setLayout(self.v_layout)
        self.resize(400, 150)
        self.setFixedSize(self.size())
        self.setWindowTitle("Scarico articolo")

    ########################################################
    ###  METODO USATO PER MOSTRARE GLI ELEMENTI GRAFICI  ###
    ###      ALL'INTERNO DELL'INTERFACCIA DI SCARICO     ###
    ########################################################
    def unload_item_view(self):
        i=0
        for name in self.labels:
            self.grid_layout.addWidget(QLabel(name), i, 0)
            self.current_text_edit = QLineEdit(self)
            self.current_text_edit.returnPressed.connect(self.unload_articolo)
            self.grid_layout.addWidget(self.current_text_edit, i, 1)
            self.info[name] = self.current_text_edit
            i = i+1

    ################################################
    ###  METODO USATO PER AGGIUNGERE LO SCARICO  ###
    ###        DELL' ARTICOLO NEL SISTEMA        ###
    ################################################
    def unload_articolo(self):
        codice_immesso = self.info["Codice a barre:"].text()
        stock = self.info["Quantità da decrementare:"].text()

        if codice_immesso == "" or stock == "":
            QMessageBox.critical(self, 'Errore di compilazione!', 'Per favore, inserisci tutte le informazioni richieste.',
                                 QMessageBox.Ok, QMessageBox.Ok)
            return
        elif self.is_int(stock) and int(stock)>0:
            articolo_trovato = self.controller.scarico(codice_immesso, stock)
            if articolo_trovato == True:
                self.callback()
                self.close()
            else:
                QMessageBox.critical(self, 'Errore',
                                     'I dati inseriti sono errati!  \n Articolo non presente in anagrafica articolo oppure \n quantità richiesta non disponibile in magazzino.',
                                     QMessageBox.Ok, QMessageBox.Ok)
                return

        else:
            QMessageBox.critical(self, 'Errore',
                                 'Per favore, inserisci un valore numerico, intero e positivo per decrementare la quantità.',
                                 QMessageBox.Ok, QMessageBox.Ok)
            return

    ##########################################################
    ###           METODO USATO PER VERIFICARE SE           ###
    ###  UNA STRINGA PUÒ ESSERE CASTATA A VARIABILE FLOAT  ###
    ##########################################################
    def is_float(self, val):

        try:
            num = float(val)
        except ValueError:
            return False
        return True

    ##################################################
    ###       METODO USATO PER VERIFICARE SE       ###
    ###  UNA STRINGA PUÒ ESSERE CASTATA AD INTERO  ###
    ##################################################
    def is_int(self, val):
        try:
            num = int(val)
        except ValueError:
            return False
        return True