from PySide2 import QtWidgets
from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import Slot

from Lista_ui import Ui_Lista
from ventana_alquiler import HireWindow


class ListWindow(QMainWindow):
    def __init__(self):
        super(ListWindow, self).__init__()
        self.ui = Ui_Lista()
        self.ui.setupUi(self)
        self.hire_window = HireWindow()

    @Slot()
    def volver_slot(self):
        self.window().close()

    @Slot()
    def alquilar_propiedad_slot(self):
        self.hire_window.show()

    @Slot()
    def eliminar_propiedad_slot(self):
        pass

    def agregar_row_casa(self, casa):
        row_position = self.ui.tb_casas.rowCount()
        self.ui.tb_casas.insertRow(row_position)
        self.ui.tb_casas.setItem(row_position, 0, QtWidgets.QTableWidgetItem(casa.direccion))
        self.ui.tb_casas.setItem(row_position, 1, QtWidgets.QTableWidgetItem(casa.cant_pisos))
        self.ui.tb_casas.setItem(row_position, 2, QtWidgets.QTableWidgetItem(casa.codigo_postal))
        self.ui.tb_casas.setItem(row_position, 3, QtWidgets.QTableWidgetItem(casa.m2))
        self.ui.tb_casas.setItem(row_position, 4, QtWidgets.QTableWidgetItem(casa.nro_dormitorios))
        self.ui.tb_casas.setItem(row_position, 5, QtWidgets.QTableWidgetItem(casa.nro_banios))
        self.ui.tb_casas.setItem(row_position, 6, QtWidgets.QTableWidgetItem(casa.amueblado))
        self.ui.tb_casas.setItem(row_position, 7, QtWidgets.QTableWidgetItem(casa.habitado))
        self.ui.tb_casas.setItem(row_position, 8, QtWidgets.QTableWidgetItem(casa.precio_ars))
        self.ui.tb_casas.setItem(row_position, 9, QtWidgets.QTableWidgetItem(casa.precio_uds))

    def agregar_row_departamento(self, departamento):
        row_position = self.ui.tb_departamentos.rowCount()
        self.ui.tb_departamentos.insertRow(row_position)
        self.ui.tb_departamentos.setItem(row_position, 0, QtWidgets.QTableWidgetItem(departamento.direccion))
        self.ui.tb_departamentos.setItem(row_position, 1, QtWidgets.QTableWidgetItem(departamento.nro_piso))
        self.ui.tb_departamentos.setItem(row_position, 2, QtWidgets.QTableWidgetItem(departamento.nro_depto))
        self.ui.tb_departamentos.setItem(row_position, 3, QtWidgets.QTableWidgetItem(departamento.codigo_postal))
        self.ui.tb_departamentos.setItem(row_position, 4, QtWidgets.QTableWidgetItem(departamento.m2))
        self.ui.tb_departamentos.setItem(row_position, 5, QtWidgets.QTableWidgetItem(departamento.nro_ambientes))
        self.ui.tb_departamentos.setItem(row_position, 6, QtWidgets.QTableWidgetItem(departamento.nro_dormitorios))
        self.ui.tb_departamentos.setItem(row_position, 7, QtWidgets.QTableWidgetItem(departamento.amueblado))
        self.ui.tb_departamentos.setItem(row_position, 8, QtWidgets.QTableWidgetItem(departamento.habitado))
        self.ui.tb_departamentos.setItem(row_position, 9, QtWidgets.QTableWidgetItem(departamento.precio_ars))
        self.ui.tb_departamentos.setItem(row_position, 10, QtWidgets.QTableWidgetItem(departamento.precio_uds))
