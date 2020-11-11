import sys
import requests
import pickle

from PySide2.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide2.QtCore import Slot

from Propiedades_ui import Ui_MainWindow
from ventana_lista import ListWindow

from Departamento import Departamento
from Casa import Casa


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.list_window = ListWindow()

        self.all = [self.ui.le_direccion, self.ui.le_codigo_postal, self.ui.le_metros_cuadrados, self.ui.le_cant_pisos,
                    self.ui.le_nro_piso, self.ui.le_nro_departamento, self.ui.le_nro_ambientes,
                    self.ui.le_nro_dormitorios, self.ui.le_nro_banios, self.ui.cb_amueblado, self.ui.cb_habitado,
                    self.ui.le_precio_ars, self.ui.le_precio_uds, self.ui.le_imagenes, self.ui.pb_registrar]

        self.propiedades = []

        self.toggle_inputs(self.all, False)

        self.dolar = self.init_dolar()
        self.ui.le_precio_uds.setReadOnly(True)

    def init_dolar(self):
        self.url = "https://www.dolarsi.com/api/api.php?type=valoresprincipales"
        self.payload = {}
        self.headers = {}
        self.response = requests.get(self.url, headers=self.headers, data=self.payload).json()

        for i, item in enumerate(self.response):
            self.casa = item["casa"]
            self.nombre = self.casa["nombre"]
            if self.nombre == "Dolar Oficial":
                self.dolar_oficial = self.casa["venta"]
                return float(self.dolar_oficial.replace(",", "."))
        return 0

    def toggle_inputs(self, input, state):
        for i in input:
            i.setEnabled(state)

    @Slot()
    def peso_change_slot(self):
        if len(self.ui.le_precio_ars.text()) > 0:
            self.ui.le_precio_uds.setText(str(round((int(self.ui.le_precio_ars.text()) / self.dolar), 2)))
        else:
            self.ui.le_precio_uds.setText("0")

    @Slot()
    def casa_slot(self):
        self.toggle_inputs(self.all, True)
        self.toggle_inputs([self.ui.le_nro_departamento, self.ui.le_nro_piso], False)

    @Slot()
    def departamento_slot(self):
        self.toggle_inputs(self.all, True)
        self.toggle_inputs([self.ui.le_cant_pisos], False)

    @Slot()
    def lista_slot(self):
        self.list_window.show()

    @Slot()
    def registrar_slot(self):
        departamento = Departamento(
            self.ui.le_direccion.text(),
            self.ui.le_codigo_postal.text(),
            self.ui.le_metros_cuadrados.text(),
            self.ui.le_nro_piso.text(),
            self.ui.le_nro_departamento.text(),
            self.ui.le_nro_ambientes.text(),
            self.ui.le_nro_dormitorios.text(),
            self.ui.le_nro_banios.text(),
            self.ui.cb_amueblado.currentText(),
            self.ui.cb_habitado.currentText(),
            self.ui.le_precio_ars.text(),
            self.ui.le_precio_uds.text()
        )

        casa = Casa(
            self.ui.le_direccion.text(),
            self.ui.le_codigo_postal.text(),
            self.ui.le_metros_cuadrados.text(),
            self.ui.le_cant_pisos.text(),
            self.ui.le_nro_ambientes.text(),
            self.ui.le_nro_dormitorios.text(),
            self.ui.le_nro_banios.text(),
            self.ui.cb_amueblado.currentText(),
            self.ui.cb_habitado.currentText(),
            self.ui.le_precio_ars.text(),
            self.ui.le_precio_uds.text()
        )

        if not departamento.is_empty_f():
            self.propiedades.append(departamento)
            self.save_file()
            self.borrar_todo_slot()
            self.list_window.agregar_row_departamento(departamento)

            if self.list_window.isHidden():
                self.list_window.show()

        elif not casa.is_empty_h():
            self.propiedades.append(casa)
            self.save_file()
            self.borrar_todo_slot()
            self.list_window.agregar_row_casa(casa)

            if self.list_window.isHidden():
                self.list_window.show()


        else:
            warn = QMessageBox().critical(self, "Datos faltantes", "Ingrese los datos necesarios")

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

    def save_file(self):
        with open("propiedades.v", "wb") as file:
            pickle.dump(self.propiedades, file)

    def read_file(self):
        try:
            with open("propiedades.v", "rb") as file:
                propiedades = pickle.load(file)
        except FileNotFoundError:
            propiedades = []
        return propiedades


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
