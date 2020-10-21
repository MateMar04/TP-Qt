import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import Slot

from Propiedades_ui import Ui_MainWindow
from ventana_lista import ListWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.list_window = ListWindow()
        self.all = [self.ui.le_direccion, self.ui.le_codigo_postal, self.ui.le_metros_cuadrados, self.ui.le_cant_pisos,
                    self.ui.le_nro_piso, self.ui.le_nro_departamento, self.ui.le_nro_ambientes,
                    self.ui.le_nro_dormitorios, self.ui.le_nro_banios, self.ui.cb_amueblado, self.ui.cb_habitado,
                    self.ui.le_precio_ars, self.ui.le_precio_uds, self.ui.le_imagenes]

        self.toggle_inputs(self.all, False)

    def toggle_inputs(self, input, state):
        for i in input:
            i.setEnabled(state)

    @Slot()
    def lista_slot(self):
        self.list_window.show()

    @Slot()
    def casa_slot(self):
        self.toggle_inputs(self.all, True)
        self.toggle_inputs([self.ui.le_nro_departamento, self.ui.le_nro_piso], False)

    @Slot()
    def departamento_slot(self):
        self.toggle_inputs(self.all, True)
        self.toggle_inputs([self.ui.le_codigo_postal, self.ui.le_precio_ars], False)

    @Slot()
    def borrar_todo_slot(self):
        self.ui.le_direccion.setText("")
        self.ui.le_codigo_postal.setText("")
        self.ui.le_metros_cuadrados.setText("")
        self.ui.le_cant_pisos.setText("")
        self.ui.le_nro_piso.setText("")
        self.ui.le_nro_departamento.setText("")
        self.ui.le_nro_ambientes.setText("")
        self.ui.le_nro_dormitorios.setText("")
        self.ui.le_nro_banios.setText("")
        self.ui.cb_amueblado.setCurrentIndex(0)
        self.ui.cb_habitado.setCurrentIndex(0)
        self.ui.le_precio_ars.setText("")
        self.ui.le_precio_uds.setText("")
        self.ui.le_imagenes.setText("")

    @Slot()
    def registrar_slot(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
