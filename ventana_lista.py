from PySide2 import QtWidgets
from PySide2.QtWidgets import QMainWindow, QMessageBox
from PySide2.QtCore import Slot

from Casa import Casa
from Lista_ui import Ui_Lista
from ventana_alquiler import HireWindow

from selenium import webdriver
import validators


class ListWindow(QMainWindow):
    def __init__(self, base_de_datos):
        super(ListWindow, self).__init__()
        self.base_de_datos = base_de_datos
        self.base_de_datos.add_listener(self.refresh)
        self.ui = Ui_Lista()
        self.ui.setupUi(self)
        self.hire_window = HireWindow(base_de_datos)

        self.ordenado_por_id = False
        self.ordenado_por_cp = False
        self.ordenado_por_nro_ambientes = False
        self.ordenado_por_m2 = False
        self.ordenado_por_dormitorios = False
        self.ordenado_por_precio = False

    @Slot()
    def volver_slot(self):
        self.window().close()

    @Slot()
    def alquilar_propiedad_slot(self):
        selected_house = self.ui.tb_casas.selectedItems()
        selected_flat = self.ui.tb_departamentos.selectedItems()
        ids = []

        for i in range(len(selected_house)):
            house_row = selected_house[i].row()
            ids.append(self.ui.tb_casas.item(house_row, 0).text())

        for i in range(len(selected_flat)):
            flat_row = selected_flat[i].row()
            ids.append(self.ui.tb_departamentos.item(flat_row, 0).text())

        self.base_de_datos.alquilar(ids)

        self.hire_window.mostrar()

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
    def ver_alquilados_slot(self):
        self.hire_window.mostrar()

    @Slot()
    def por_id(self):
        self.refresh(self.ordenar(self.base_de_datos.read(), self.ordenado_por_id, lambda p: p.id))
        self.ordenado_por_id = not self.ordenado_por_id

    @Slot()
    def por_codigo_postal(self):
        self.refresh(self.ordenar(self.base_de_datos.read(), self.ordenado_por_cp, lambda p: p.codigo_postal))
        self.ordenado_por_cp = not self.ordenado_por_cp

    @Slot()
    def por_ambientes(self):
        self.refresh(self.ordenar(self.base_de_datos.read(), self.ordenado_por_nro_ambientes, lambda p: p.nro_ambientes))
        self.ordenado_por_nro_ambientes = not self.ordenado_por_nro_ambientes

    @Slot()
    def por_metros_cuadrados(self):
        self.refresh(self.ordenar(self.base_de_datos.read(), self.ordenado_por_m2, lambda p: p.m2))
        self.ordenado_por_m2 = not self.ordenado_por_m2

    @Slot()
    def por_dormitorios(self):
        self.refresh(self.ordenar(self.base_de_datos.read(), self.ordenado_por_dormitorios, lambda p: p.nro_dormitorios))
        self.ordenado_por_dormitorios = not self.ordenado_por_dormitorios

    @Slot()
    def por_precio(self):
        self.refresh(self.ordenar(self.base_de_datos.read(), self.ordenado_por_precio, lambda p: p.precio_ars))
        self.ordenado_por_precio = not self.ordenado_por_precio

    @Slot()
    def buscar_internet_slot(self):
        selected_house = self.ui.tb_casas.selectedItems()
        selected_flat = self.ui.tb_departamentos.selectedItems()
        links = []

        for i in range(len(selected_house)):
            house_row = selected_house[i].row()
            links.append(self.ui.tb_casas.item(house_row, 11).text())

        for i in range(len(selected_flat)):
            flat_row = selected_flat[i].row()
            links.append(self.ui.tb_departamentos.item(flat_row, 12).text())

        URLs = list(filter(lambda l: validators.url(l), links))

        if len(URLs) == 0:
            QMessageBox().critical(self, "URL no valida", "Las URLs no son validas")
        else:
            driver = webdriver.Chrome("./chromedriver")
            for i in range(len(URLs)):
                driver.get(URLs[i])
                if i < (len(URLs) - 1):
                    driver.execute_script("window.open('');")
                    driver.switch_to.window(driver.window_handles[i + 1])

    def refresh(self, inmuebles):
        self.ui.tb_casas.setRowCount(0)
        self.ui.tb_departamentos.setRowCount(0)

        for inmueble in inmuebles:
            if not inmueble.alquilado:
                if isinstance(inmueble, Casa):
                    self.agregar_casa_a_lista(inmueble)
                else:
                    self.agregar_departamento_a_lista(inmueble)

    def agregar_row_casa(self, casa):
        self.base_de_datos.add(casa)

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
        self.ui.tb_casas.setItem(row_position, 11, QtWidgets.QTableWidgetItem(casa.imagenes))

    def agregar_row_departamento(self, departamento):
        self.base_de_datos.add(departamento)

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
        self.ui.tb_departamentos.setItem(row_position, 12, QtWidgets.QTableWidgetItem(departamento.imagenes))

    def mostrar(self):
        if self.isHidden():
            self.show()

    def ordenar(self, elementos, modo, comparador):
        elementos.sort(reverse=modo, key=comparador)
        return elementos


