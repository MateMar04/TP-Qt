from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import Slot

from Casa_ui import Ui_Casa


class HouseWindow(QMainWindow):
    def __init__(self):
        super(HouseWindow, self).__init__()
        self.ui = Ui_Casa()
        self.ui.setupUi(self)

    @Slot()
    def volver_slot(self):
        self.window().close()