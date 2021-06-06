import sys
from PyQt5.QtWidgets import QApplication

from home.Home.Home import Home

if __name__ == '__main__':
    app = QApplication(sys.argv)
    vista_home = Home()
    vista_home.show()
    sys.exit(app.exec_())