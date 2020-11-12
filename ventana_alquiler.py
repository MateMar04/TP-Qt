from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import Slot

from Alquiladas_ui import Ui_MainWindow


class HireWindow(QMainWindow):
    def __init__(self):
        super(HireWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.alquiladas = []



    @Slot()
    def eliminar_propiedad_slot(self):
        pass

    @Slot()
    def terminar_contrato_slot(self):
        pass

    @Slot()
    def volver_slot(self):
        self.window().close()
