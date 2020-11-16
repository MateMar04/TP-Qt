
from PySide2 import QtWidgets
from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import Slot

from Alquiladas_ui import Ui_MainWindow
from Casa import Casa


class HireWindow(QMainWindow):
    def __init__(self, base_de_datos):
        super(HireWindow, self).__init__()
        self.base_de_datos = base_de_datos
        self.base_de_datos.add_listener(self.refresh)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.alquiladas = []

    @Slot()
    def eliminar_propiedad_slot(self):
        selected_house = self.ui.tb_casas.selectedItems()
        selected_flat = self.ui.tb_departamentos.selectedItems()
        ids = []

        for i in range(len(selected_house)):
            house_row = selected_house[i].row()
            ids.append(self.ui.tb_casas.item(house_row, 0).text())

        for i in range(len(selected_flat)):
            flat_row = selected_flat[i].row()
            ids.append(self.ui.tb_departamentos.item(flat_row, 0).text())

        self.base_de_datos.delete(ids)


    @Slot()
    def terminar_contrato_slot(self):
        selected_house = self.ui.tb_casas.selectedItems()
        selected_flat = self.ui.tb_departamentos.selectedItems()
        ids = []

        for i in range(len(selected_house)):
            house_row = selected_house[i].row()
            ids.append(self.ui.tb_casas.item(house_row, 0).text())

        for i in range(len(selected_flat)):
            flat_row = selected_flat[i].row()
            ids.append(self.ui.tb_departamentos.item(flat_row, 0).text())

        self.base_de_datos.terminar_contrato(ids)

    @Slot()
    def volver_slot(self):
        self.window().close()

    def agregar_casa_a_lista(self, casa):
        row_position = self.ui.tb_casas.rowCount()
        self.ui.tb_casas.insertRow(row_position)
        self.ui.tb_casas.setItem(row_position, 0, QtWidgets.QTableWidgetItem(casa.id))
        self.ui.tb_casas.setItem(row_position, 1, QtWidgets.QTableWidgetItem(casa.direccion))
        self.ui.tb_casas.setItem(row_position, 2, QtWidgets.QTableWidgetItem(casa.cant_pisos))
        self.ui.tb_casas.setItem(row_position, 3, QtWidgets.QTableWidgetItem(casa.codigo_postal))
        self.ui.tb_casas.setItem(row_position, 4, QtWidgets.QTableWidgetItem(casa.m2))
        self.ui.tb_casas.setItem(row_position, 5, QtWidgets.QTableWidgetItem(casa.nro_dormitorios))
        self.ui.tb_casas.setItem(row_position, 6, QtWidgets.QTableWidgetItem(casa.nro_banios))
        self.ui.tb_casas.setItem(row_position, 7, QtWidgets.QTableWidgetItem(casa.amueblado))
        self.ui.tb_casas.setItem(row_position, 8, QtWidgets.QTableWidgetItem(casa.habitado))
        self.ui.tb_casas.setItem(row_position, 9, QtWidgets.QTableWidgetItem(casa.precio_ars))
        self.ui.tb_casas.setItem(row_position, 10, QtWidgets.QTableWidgetItem(casa.precio_uds))

    def agregar_departamento_a_lista(self, departamento):
        row_position = self.ui.tb_departamentos.rowCount()
        self.ui.tb_departamentos.insertRow(row_position)
        self.ui.tb_departamentos.setItem(row_position, 0, QtWidgets.QTableWidgetItem(departamento.id))
        self.ui.tb_departamentos.setItem(row_position, 1, QtWidgets.QTableWidgetItem(departamento.direccion))
        self.ui.tb_departamentos.setItem(row_position, 2, QtWidgets.QTableWidgetItem(departamento.nro_piso))
        self.ui.tb_departamentos.setItem(row_position, 3, QtWidgets.QTableWidgetItem(departamento.nro_depto))
        self.ui.tb_departamentos.setItem(row_position, 4, QtWidgets.QTableWidgetItem(departamento.codigo_postal))
        self.ui.tb_departamentos.setItem(row_position, 5, QtWidgets.QTableWidgetItem(departamento.m2))
        self.ui.tb_departamentos.setItem(row_position, 6, QtWidgets.QTableWidgetItem(departamento.nro_ambientes))
        self.ui.tb_departamentos.setItem(row_position, 7, QtWidgets.QTableWidgetItem(departamento.nro_dormitorios))
        self.ui.tb_departamentos.setItem(row_position, 8, QtWidgets.QTableWidgetItem(departamento.amueblado))
        self.ui.tb_departamentos.setItem(row_position, 9, QtWidgets.QTableWidgetItem(departamento.habitado))
        self.ui.tb_departamentos.setItem(row_position, 10, QtWidgets.QTableWidgetItem(departamento.precio_ars))
        self.ui.tb_departamentos.setItem(row_position, 11, QtWidgets.QTableWidgetItem(departamento.precio_uds))

    def mostrar(self):
        if self.isHidden():
            self.show()


    def refresh(self, inmuebles):
        self.ui.tb_casas.setRowCount(0)
        self.ui.tb_departamentos.setRowCount(0)

        for inmueble in inmuebles:
            if inmueble.alquilado:
                if isinstance(inmueble, Casa):
                    self.agregar_casa_a_lista(inmueble)
                else:
                    self.agregar_departamento_a_lista(inmueble)
