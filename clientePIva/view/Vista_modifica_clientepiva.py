from PyQt5.QtWidgets import QWidget, QVBoxLayout, QFormLayout, QLineEdit, QHBoxLayout, QPushButton, QMessageBox

#####################################################################
###   QUESTA CLASSE SERVE PER MOSTRARE ALL'UTENTE L'INTERFACCIA   ###
###        DI MODIFICA DI UN CLIENTE PRESENTE NEL SISTEMA         ###
#####################################################################
class Vista_modifica_clientepiva(QWidget):
    def __init__(self, elemento_modifica, controller, controller_clientipiva, callback, callback_cliente):
        super(Vista_modifica_clientepiva, self).__init__()

        self.elemento_modifica = elemento_modifica
        self.controller = controller
        self.controller_clientipiva = controller_clientipiva
        self.callback = callback
        self.callback_cliente = callback_cliente

        self.v_layout = QVBoxLayout()
        self.layout = QFormLayout()
    
        
        
        if self.elemento_modifica == "Modifica Ragione Sociale":
            self.info = QLineEdit(self.controller.get_ragione_sociale_clientepiva())
        if self.elemento_modifica == "Modifica Partita IVA":
            self.info = QLineEdit(self.controller.get_partita_iva_clientepiva())
        if self.elemento_modifica == "Modifica Città":
            self.info = QLineEdit(self.controller.get_citta_clientepiva())
        if self.elemento_modifica == "Modifica Indirizzo":
            self.info = QLineEdit(self.controller.get_indirizzo_clientepiva())
        if self.elemento_modifica == "Modifica Telefono":
            self.info = QLineEdit(self.controller.get_telefono_clientepiva())
        if self.elemento_modifica == "Modifica Email":
            self.info = QLineEdit(self.controller.get_email_clientepiva())

        self.layout.addRow(self.elemento_modifica + ':', self.info)

        self.button_layout = QHBoxLayout()
        self.send_button = QPushButton("Ok")
        self.button_layout.addWidget(self.send_button)
        self.button_layout.addStretch()
        self.send_button.clicked.connect(self.completa_modifica)
        self.info.returnPressed.connect(self.completa_modifica)
        self.v_layout.addLayout(self.layout)
        self.v_layout.addLayout(self.button_layout)
        self.setLayout(self.v_layout)

        self.resize(500, 100)
        self.setFixedSize(self.size())
        self.setWindowTitle(self.elemento_modifica)

    ########################################################
    ###      METODO USATO PER APPLICARE UNA MODIFICA     ###
    ###   EFFETTUATA AD UN CLIENTE PRESENTE NEL SISTEMA  ###
    ########################################################
    def completa_modifica(self):
        if self.info.text() == "":
            QMessageBox.critical(self, 'Errore', 'Per favore, inserisci l\'informazione richiesta',
                                 QMessageBox.Ok, QMessageBox.Ok)
            return

        if self.elemento_modifica == "Modifica Ragione Sociale":
            self.controller.set_ragione_sociale_clientepiva(self.info.text())
        if self.elemento_modifica == "Modifica Partita IVA":
            for cliente in self.controller_clientipiva.get_lista_clientipiva():
                if cliente.partita_iva == self.info.text():
                    QMessageBox.critical(self, 'Errore di compilazione!',
                                         'La partita iva digitata è già presente nel sistema.',
                                         QMessageBox.Ok, QMessageBox.Ok)
                    return
            self.controller.set_partita_iva_clientepiva(self.info.text())
        if self.elemento_modifica == "Modifica Città":
            self.controller.set_citta_clientepiva(self.info.text())
        if self.elemento_modifica == "Modifica Indirizzo":
            self.controller.set_indirizzo_clientepiva(self.info.text())
        if self.elemento_modifica == "Modifica Telefono":
            self.controller.set_telefono_clientepiva(self.info.text())
        if self.elemento_modifica == "Modifica Email":
            self.controller.set_email_clientepiva(self.info.text())
        self.callback_cliente()
        self.callback()
        self.close()
