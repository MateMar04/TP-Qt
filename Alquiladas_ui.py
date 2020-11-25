# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Alquiladas.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1350, 498)
        MainWindow.setMinimumSize(QSize(1350, 498))
        MainWindow.setMaximumSize(QSize(1350, 498))
        self.actionPor_ID = QAction(MainWindow)
        self.actionPor_ID.setObjectName(u"actionPor_ID")
        self.actionPor_Codigo_Postal = QAction(MainWindow)
        self.actionPor_Codigo_Postal.setObjectName(u"actionPor_Codigo_Postal")
        self.actionPor_ambientes = QAction(MainWindow)
        self.actionPor_ambientes.setObjectName(u"actionPor_ambientes")
        self.actionPor_Metros_Cuadrados = QAction(MainWindow)
        self.actionPor_Metros_Cuadrados.setObjectName(u"actionPor_Metros_Cuadrados")
        self.actionPor_Dormitorios = QAction(MainWindow)
        self.actionPor_Dormitorios.setObjectName(u"actionPor_Dormitorios")
        self.actionPor_Precio = QAction(MainWindow)
        self.actionPor_Precio.setObjectName(u"actionPor_Precio")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(190, 10, 1301, 461))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.tb_departamentos = QTableWidget(self.verticalLayoutWidget)
        if (self.tb_departamentos.columnCount() < 13):
            self.tb_departamentos.setColumnCount(13)
        __qtablewidgetitem = QTableWidgetItem()
        self.tb_departamentos.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tb_departamentos.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tb_departamentos.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tb_departamentos.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tb_departamentos.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tb_departamentos.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tb_departamentos.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tb_departamentos.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tb_departamentos.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tb_departamentos.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tb_departamentos.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tb_departamentos.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tb_departamentos.setHorizontalHeaderItem(12, __qtablewidgetitem12)
        self.tb_departamentos.setObjectName(u"tb_departamentos")
        self.tb_departamentos.horizontalHeader().setDefaultSectionSize(100)

        self.verticalLayout.addWidget(self.tb_departamentos)

        self.tb_casas = QTableWidget(self.verticalLayoutWidget)
        if (self.tb_casas.columnCount() < 12):
            self.tb_casas.setColumnCount(12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tb_casas.setHorizontalHeaderItem(0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tb_casas.setHorizontalHeaderItem(1, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tb_casas.setHorizontalHeaderItem(2, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tb_casas.setHorizontalHeaderItem(3, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tb_casas.setHorizontalHeaderItem(4, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tb_casas.setHorizontalHeaderItem(5, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tb_casas.setHorizontalHeaderItem(6, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tb_casas.setHorizontalHeaderItem(7, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tb_casas.setHorizontalHeaderItem(8, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tb_casas.setHorizontalHeaderItem(9, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tb_casas.setHorizontalHeaderItem(10, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tb_casas.setHorizontalHeaderItem(11, __qtablewidgetitem24)
        self.tb_casas.setObjectName(u"tb_casas")

        self.verticalLayout.addWidget(self.tb_casas)

        self.lb_departamento = QLabel(self.centralwidget)
        self.lb_departamento.setObjectName(u"lb_departamento")
        self.lb_departamento.setGeometry(QRect(30, 110, 111, 20))
        self.lb_casas = QLabel(self.centralwidget)
        self.lb_casas.setObjectName(u"lb_casas")
        self.lb_casas.setGeometry(QRect(70, 320, 41, 17))
        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(10, 379, 160, 91))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pb_buscar = QPushButton(self.verticalLayoutWidget_2)
        self.pb_buscar.setObjectName(u"pb_buscar")

        self.verticalLayout_2.addWidget(self.pb_buscar)

        self.pb_eliminar_propiedad = QPushButton(self.verticalLayoutWidget_2)
        self.pb_eliminar_propiedad.setObjectName(u"pb_eliminar_propiedad")

        self.verticalLayout_2.addWidget(self.pb_eliminar_propiedad)

        self.pb_terminar_contrato = QPushButton(self.verticalLayoutWidget_2)
        self.pb_terminar_contrato.setObjectName(u"pb_terminar_contrato")

        self.verticalLayout_2.addWidget(self.pb_terminar_contrato)

        self.pb_volver = QPushButton(self.verticalLayoutWidget_2)
        self.pb_volver.setObjectName(u"pb_volver")

        self.verticalLayout_2.addWidget(self.pb_volver)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 1350, 22))
        self.menuOrdenar = QMenu(self.menuBar)
        self.menuOrdenar.setObjectName(u"menuOrdenar")
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menuOrdenar.menuAction())
        self.menuOrdenar.addAction(self.actionPor_ID)
        self.menuOrdenar.addAction(self.actionPor_Codigo_Postal)
        self.menuOrdenar.addAction(self.actionPor_ambientes)
        self.menuOrdenar.addAction(self.actionPor_Metros_Cuadrados)
        self.menuOrdenar.addAction(self.actionPor_Dormitorios)
        self.menuOrdenar.addAction(self.actionPor_Precio)

        self.retranslateUi(MainWindow)
        self.pb_eliminar_propiedad.clicked.connect(MainWindow.eliminar_propiedad_slot)
        self.pb_terminar_contrato.clicked.connect(MainWindow.terminar_contrato_slot)
        self.actionPor_Codigo_Postal.triggered.connect(MainWindow.por_codigo_postal)
        self.actionPor_Dormitorios.triggered.connect(MainWindow.por_dormitorios)
        self.actionPor_ID.triggered.connect(MainWindow.por_id)
        self.actionPor_Metros_Cuadrados.triggered.connect(MainWindow.por_metros_cuadrados)
        self.actionPor_Precio.triggered.connect(MainWindow.por_precio)
        self.actionPor_ambientes.triggered.connect(MainWindow.por_ambientes)
        self.pb_volver.clicked.connect(MainWindow.volver_slot)
        self.pb_buscar.clicked.connect(MainWindow.buscar_internet_slot)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Propiedades Alquiladas", None))
        self.actionPor_ID.setText(QCoreApplication.translate("MainWindow", u"Por ID", None))
        self.actionPor_Codigo_Postal.setText(QCoreApplication.translate("MainWindow", u"Por Codigo Postal", None))
        self.actionPor_ambientes.setText(QCoreApplication.translate("MainWindow", u"Por Ambientes", None))
        self.actionPor_Metros_Cuadrados.setText(QCoreApplication.translate("MainWindow", u"Por Metros Cuadrados", None))
        self.actionPor_Dormitorios.setText(QCoreApplication.translate("MainWindow", u"Por Dormitorios", None))
        self.actionPor_Precio.setText(QCoreApplication.translate("MainWindow", u"Por Precio", None))
        ___qtablewidgetitem = self.tb_departamentos.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.tb_departamentos.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Direccion", None));
        ___qtablewidgetitem2 = self.tb_departamentos.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Piso", None));
        ___qtablewidgetitem3 = self.tb_departamentos.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"N\u00b0 de Departamento", None));
        ___qtablewidgetitem4 = self.tb_departamentos.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Codigo Postal", None));
        ___qtablewidgetitem5 = self.tb_departamentos.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Metros Cuadrados", None));
        ___qtablewidgetitem6 = self.tb_departamentos.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Ambientes", None));
        ___qtablewidgetitem7 = self.tb_departamentos.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Dormitorios", None));
        ___qtablewidgetitem8 = self.tb_departamentos.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Amueblado", None));
        ___qtablewidgetitem9 = self.tb_departamentos.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Habitado", None));
        ___qtablewidgetitem10 = self.tb_departamentos.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Precio ARS", None));
        ___qtablewidgetitem11 = self.tb_departamentos.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Precio UDS", None));
        ___qtablewidgetitem12 = self.tb_departamentos.horizontalHeaderItem(12)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Imagenes", None));
        ___qtablewidgetitem13 = self.tb_casas.horizontalHeaderItem(0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem14 = self.tb_casas.horizontalHeaderItem(1)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Direccion", None));
        ___qtablewidgetitem15 = self.tb_casas.horizontalHeaderItem(2)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Pisos", None));
        ___qtablewidgetitem16 = self.tb_casas.horizontalHeaderItem(3)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Codigo Postal", None));
        ___qtablewidgetitem17 = self.tb_casas.horizontalHeaderItem(4)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Metros Cuadrados", None));
        ___qtablewidgetitem18 = self.tb_casas.horizontalHeaderItem(5)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Dormitorios", None));
        ___qtablewidgetitem19 = self.tb_casas.horizontalHeaderItem(6)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Ba\u00f1os", None));
        ___qtablewidgetitem20 = self.tb_casas.horizontalHeaderItem(7)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Amueblado", None));
        ___qtablewidgetitem21 = self.tb_casas.horizontalHeaderItem(8)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Habitado", None));
        ___qtablewidgetitem22 = self.tb_casas.horizontalHeaderItem(9)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Precio ARS", None));
        ___qtablewidgetitem23 = self.tb_casas.horizontalHeaderItem(10)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Precio UDS", None));
        ___qtablewidgetitem24 = self.tb_casas.horizontalHeaderItem(11)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"Imagenes", None));
        self.lb_departamento.setText(QCoreApplication.translate("MainWindow", u"Departamentos", None))
        self.lb_casas.setText(QCoreApplication.translate("MainWindow", u"Casas", None))
        self.pb_buscar.setText(QCoreApplication.translate("MainWindow", u"Buscar en Internet", None))
        self.pb_eliminar_propiedad.setText(QCoreApplication.translate("MainWindow", u"Eliminar Propiedad", None))
        self.pb_terminar_contrato.setText(QCoreApplication.translate("MainWindow", u"Terminar Contrato", None))
        self.pb_volver.setText(QCoreApplication.translate("MainWindow", u"Volver", None))
        self.menuOrdenar.setTitle(QCoreApplication.translate("MainWindow", u"Ordenar", None))
    # retranslateUi

