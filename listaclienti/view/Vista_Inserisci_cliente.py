from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QSpacerItem, QSizePolicy, QPushButton, QMessageBox, \
    QLabel, QLineEdit

from cliente.model.Cliente import Cliente

#####################################################################
###   QUESTA CLASSE SERVE PER MOSTRARE ALL'UTENTE L'INTERFACCIA   ###
###        DI INSERIMENTO DI UN NUOVO CLIENTE NEL SISTEMA         ###
#####################################################################
class Vista_Inserisci_cliente(QWidget):
    def __init__(self, controller, callback):
        super(Vista_Inserisci_cliente, self).__init__()

        self.controller = controller
        self.callback = callback
        self.info = {}
        self.labels = ["Nome:", "Cognome:", "Codice Fiscale:", "Email:", "Telefono:", "Città:", "Indirizzo:"]

        self.v_layout = QVBoxLayout()
        self.grid_layout = QGridLayout()

        self.add_item_view()

        self.v_layout.addLayout(self.grid_layout)

        self.v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_ok = QPushButton("Inserisci")
        btn_ok.clicked.connect(self.add_cliente)

        self.v_layout.addWidget(btn_ok)

        self.setLayout(self.v_layout)
        self.resize(400, 300)
        self.setFixedSize(self.size())
        self.setWindowTitle("Inserisci cliente")

    ########################################################
    ###  METODO USATO PER MOSTRARE GLI ELEMENTI GRAFICI  ###
    ###    ALL'INTERNO DELL'INTERFACCIA DI INSERIMENTO   ###
    ########################################################
    def add_item_view(self):
        i = 0
        for name in self.labels:
            self.grid_layout.addWidget(QLabel(name), i, 0)
            self.current_text_edit = QLineEdit(self)
            self.current_text_edit.returnPressed.connect(self.add_cliente)
            self.grid_layout.addWidget(self.current_text_edit, i, 1)
            self.info[name] = self.current_text_edit
            i = i + 1

    #######################################################
    ###   METODO USATO PER AGGIUNGERE IL NUOVO CLIENTE  ###
    ###                   NEL SISTEMA                   ###
    #######################################################
    def add_cliente(self):

        nome = self.info["Nome:"].text()
        cognome = self.info["Cognome:"].text()
        cf = self.info["Codice Fiscale:"].text()
        email = self.info["Email:"].text()
        telefono = self.info["Telefono:"].text()
        citta = self.info["Città:"].text()
        indirizzo = self.info["Indirizzo:"].text()

        if nome == "" or cognome == "" or cf == "" or email == "" or telefono == "":  #or #indirizzo == "":
            QMessageBox.critical(self, 'Errore di compilazione!',
                                 'Per favore, inserisci tutte le informazioni richieste.',
                                 QMessageBox.Ok, QMessageBox.Ok)
            return
        for cliente in self.controller.get_lista_clienti():
            if cliente.cf.upper() == cf.upper():
                QMessageBox.critical(self, 'Errore di compilazione!',
                                     'Il codice fiscale inserito è già presente nel sistema.',
                                     QMessageBox.Ok, QMessageBox.Ok)
                return
        self.controller.model.codice_id = self.controller.model.codice_id + 1
        self.controller.aggiungi_cliente(Cliente(self.controller.model.codice_id, nome, cognome, cf, email, telefono, citta,indirizzo))
        self.callback()
        self.close()