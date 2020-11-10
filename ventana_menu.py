import sys

from PySide2.QtWidgets import QMainWindow, QApplication
from PySide2.QtCore import Slot

from Menu_ui import Ui_Menu


class MenuWindow(QMainWindow):
    def __init__(self):
        super(MenuWindow, self).__init__()
        self.ui = Ui_Menu()
        self.ui.setupUi(self)


    @Slot()
    def agregar_propiedades_slot(self):
        pass

    @Slot()
    def ver_propiedades_slot(self):
        pass

    @Slot()
    def ver_lista_slot(self):
        pass



if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MenuWindow()
    window.show()

    sys.exit(app.exec_())
