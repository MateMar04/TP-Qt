import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import Slot

from Propiedad_ui import Ui_Propiedad

from ventana_lista import ListWindow
from ventana_casa import HouseWindow
from ventana_departamento import FlatWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Propiedad()
        self.ui.setupUi(self)
        self.list_window = ListWindow()
        self.house_window = HouseWindow()
        self.flat_window = FlatWindow()

    @Slot()
    def casa_slot(self):
        self.house_window.show()

    @Slot()
    def departamento_slot(self):
        self.flat_window.show()

    @Slot()
    def lista_slot(self):
        self.list_window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
