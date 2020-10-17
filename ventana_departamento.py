from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import Slot

from Departamento_ui import Ui_Departamento


class FlatWindow(QMainWindow):
    def __init__(self):
        super(FlatWindow, self).__init__()
        self.ui = Ui_Departamento()
        self.ui.setupUi(self)

    @Slot()
    def volver_slot(self):
        self.window().close()




