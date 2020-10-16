import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import Slot

from Propiedad_ui import Ui_Propiedad


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Propiedad()
        self.ui.setupUi(self)

    @Slot()
    def casa_slot(self):
        print("hola")

    @Slot()
    def departamento_slot(self):
        pass

    @Slot()
    def lista_slot(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
