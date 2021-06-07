from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QSpacerItem, QSizePolicy, QPushButton, QMessageBox, \
    QLabel, QLineEdit

from dipendente.model.Dipendente import Dipendente

#####################################################################
###   QUESTA CLASSE SERVE PER MOSTRARE ALL'UTENTE L'INTERFACCIA   ###
###       DI INSERIMENTO DI UN NUOVO DIPENDENTE NEL SISTEMA       ###
#####################################################################
class VistaInserisciDipendente(QWidget):
    def __init__(self, controller, callback):
        super(VistaInserisciDipendente, self).__init__()

        self.controller = controller
        self.callback = callback
        self.info = {}
        self.labels = ["Nome:", "Cognome:", "Codice Fiscale:", "Email:", "Telefono:", "Mansione:", "Stipendio Mensile:"]

        self.v_layout = QVBoxLayout()
        self.grid_layout = QGridLayout()

        self.add_item_view()

        self.v_layout.addLayout(self.grid_layout)

        self.v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_ok = QPushButton("Inserisci")
        btn_ok.clicked.connect(self.add_dipendente)

        self.v_layout.addWidget(btn_ok)

        self.setLayout(self.v_layout)
        self.resize(400, 300)
        self.setFixedSize(self.size())
        self.setWindowTitle("Inserisci Dipendente")

    ########################################################
    ###  METODO USATO PER MOSTRARE GLI ELEMENTI GRAFICI  ###
    ###    ALL'INTERNO DELL'INTERFACCIA DI INSERIMENTO   ###
    ########################################################
    def add_item_view(self):
        i=0
        for name in self.labels:
            self.grid_layout.addWidget(QLabel(name), i, 0)
            self.current_text_edit = QLineEdit(self)
            self.current_text_edit.returnPressed.connect(self.add_dipendente)
            self.grid_layout.addWidget(self.current_text_edit, i, 1)
            self.info[name] = self.current_text_edit
            i = i+1

    ##########################################################
    ###   METODO USATO PER AGGIUNGERE IL NUOVO DIPENDENTE  ###
    ###                      NEL SISTEMA                   ###
    ##########################################################
    def add_dipendente(self):
        nome = self.info["Nome:"].text()
        cognome = self.info["Cognome:"].text()
        cf = self.info["Codice Fiscale:"].text()
        email = self.info["Email:"].text()
        telefono = self.info["Telefono:"].text()
        mansione = self.info["Mansione:"].text()
        stipendio = self.info["Stipendio Mensile:"].text()

        if nome == "" or cognome == "" or cf == "" or stipendio == "":
            QMessageBox.critical(self, 'Errore di compilazione!', 'Per favore, riempi i seguenti campi: Nome, Cognome, Codice Fiscale e Stipendio.',
                                 QMessageBox.Ok, QMessageBox.Ok)
                            
        elif not self.is_float(stipendio) and not self.is_int(stipendio):
            QMessageBox.critical(self, 'Errore', 'Per favore, inserisci un valore numerico nel campo Stipendio.',
                                 QMessageBox.Ok, QMessageBox.Ok)

        else:
            self.controller.model.codice_id = self.controller.model.codice_id+1
            self.controller.aggiungi_dipendente(Dipendente(self.controller.model.codice_id, nome, cognome, cf, email, telefono, mansione, stipendio))
            self.callback()
            self.close()

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


