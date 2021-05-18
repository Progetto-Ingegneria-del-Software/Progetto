from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QSpacerItem, QSizePolicy, QPushButton, QMessageBox, \
    QLabel, QLineEdit

from dipendente.model.Dipendente import Dipendente


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

    def add_item_view(self):
        i=0
        for name in self.labels:
            self.grid_layout.addWidget(QLabel(name), i, 0)
            self.current_text_edit = QLineEdit(self)
            self.current_text_edit.returnPressed.connect(self.add_dipendente)
            self.grid_layout.addWidget(self.current_text_edit, i, 1)
            self.info[name] = self.current_text_edit
            i = i+1

    def add_dipendente(self):
        nome = self.info["Nome:"].text()
        cognome = self.info["Cognome:"].text()
        cf = self.info["Codice Fiscale:"].text()
        email = self.info["Email:"].text()
        telefono = self.info["Telefono:"].text()
        mansione = self.info["Mansione:"].text()
        stipendio = self.info["Stipendio Mensile:"].text()

        '''
        if nome == "" or cognome == "" or cf == "" or email == "" or telefono == "" or mansione == "" or stipendio == "":
            QMessageBox.critical(self, 'Errore di compilazione!', 'Per favore, inserisci tutte le informazioni richieste.',
                                 QMessageBox.Ok, QMessageBox.Ok)
                            
        else:'''
        self.controller.model.codice_id = self.controller.model.codice_id+1
        self.controller.aggiungi_dipendente(Dipendente(self.controller.model.codice_id, nome, cognome, cf, email, telefono, mansione, stipendio))
        self.callback()
        self.close()


