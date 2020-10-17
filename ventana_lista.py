from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import Slot

from Lista_ui import Ui_Lista


class ListWindow(QMainWindow):
    def __init__(self):
        super(ListWindow, self).__init__()
        self.ui = Ui_Lista()
        self.ui.setupUi(self)

    @Slot()
    def volver_slot(self):
        self.window().close()


