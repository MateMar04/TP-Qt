# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Lista.ui'
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


class Ui_Lista(object):
    def setupUi(self, Lista):
        if not Lista.objectName():
            Lista.setObjectName(u"Lista")
        Lista.resize(1350, 498)
        Lista.setMinimumSize(QSize(1350, 498))
        Lista.setMaximumSize(QSize(1350, 498))
        self.actionCasas = QAction(Lista)
        self.actionCasas.setObjectName(u"actionCasas")
        self.actionPor_ID_2 = QAction(Lista)
        self.actionPor_ID_2.setObjectName(u"actionPor_ID_2")
        self.actionPor_Piso = QAction(Lista)
        self.actionPor_Piso.setObjectName(u"actionPor_Piso")
        self.actionPor_N_de_Departamento = QAction(Lista)
        self.actionPor_N_de_Departamento.setObjectName(u"actionPor_N_de_Departamento")
        self.actionPor_Codigo_Postal = QAction(Lista)
        self.actionPor_Codigo_Postal.setObjectName(u"actionPor_Codigo_Postal")
        self.actionPor_Metros_Cuadrados = QAction(Lista)
        self.actionPor_Metros_Cuadrados.setObjectName(u"actionPor_Metros_Cuadrados")
        self.actionPor_Ambientes = QAction(Lista)
        self.actionPor_Ambientes.setObjectName(u"actionPor_Ambientes")
        self.actionPor_Dormitorios = QAction(Lista)
        self.actionPor_Dormitorios.setObjectName(u"actionPor_Dormitorios")
        self.actionPor_Precio = QAction(Lista)
        self.actionPor_Precio.setObjectName(u"actionPor_Precio")
        self.centralwidget = QWidget(Lista)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(180, 0, 1161, 471))
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

        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(20, 0, 139, 371))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lb_departamentos = QLabel(self.verticalLayoutWidget_2)
        self.lb_departamentos.setObjectName(u"lb_departamentos")

        self.verticalLayout_2.addWidget(self.lb_departamentos)

        self.lb_casas = QLabel(self.verticalLayoutWidget_2)
        self.lb_casas.setObjectName(u"lb_casas")

        self.verticalLayout_2.addWidget(self.lb_casas)

        self.verticalLayoutWidget_3 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(0, 340, 171, 131))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.pushButton_4 = QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.verticalLayout_3.addWidget(self.pushButton_4)

        self.pushButton_2 = QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_3.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.verticalLayoutWidget_3)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_3.addWidget(self.pushButton)

        self.pushButton_3 = QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout_3.addWidget(self.pushButton_3)

        self.pb_volver = QPushButton(self.verticalLayoutWidget_3)
        self.pb_volver.setObjectName(u"pb_volver")

        self.verticalLayout_3.addWidget(self.pb_volver)

        Lista.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(Lista)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 1350, 22))
        self.menuOrdenar = QMenu(self.menuBar)
        self.menuOrdenar.setObjectName(u"menuOrdenar")
        Lista.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menuOrdenar.menuAction())
        self.menuOrdenar.addAction(self.actionPor_ID_2)
        self.menuOrdenar.addAction(self.actionPor_Codigo_Postal)
        self.menuOrdenar.addAction(self.actionPor_Ambientes)
        self.menuOrdenar.addAction(self.actionPor_Metros_Cuadrados)
        self.menuOrdenar.addAction(self.actionPor_Dormitorios)
        self.menuOrdenar.addAction(self.actionPor_Precio)

        self.retranslateUi(Lista)
        self.pb_volver.clicked.connect(Lista.volver_slot)
        self.pushButton.clicked.connect(Lista.alquilar_propiedad_slot)
        self.pushButton_2.clicked.connect(Lista.eliminar_propiedad_slot)
        self.pushButton_3.clicked.connect(Lista.ver_alquilados_slot)
        self.actionPor_ID_2.triggered.connect(Lista.por_id)
        self.actionPor_Codigo_Postal.triggered.connect(Lista.por_codigo_postal)
        self.actionPor_Ambientes.triggered.connect(Lista.por_ambientes)
        self.actionPor_Metros_Cuadrados.triggered.connect(Lista.por_metros_cuadrados)
        self.actionPor_Dormitorios.triggered.connect(Lista.por_dormitorios)
        self.actionPor_Precio.triggered.connect(Lista.por_precio)
        self.pushButton_4.clicked.connect(Lista.buscar_internet_slot)

        QMetaObject.connectSlotsByName(Lista)
    # setupUi

    def retranslateUi(self, Lista):
        Lista.setWindowTitle(QCoreApplication.translate("Lista", u"Lista de Propiedades", None))
        self.actionCasas.setText(QCoreApplication.translate("Lista", u"Casas", None))
        self.actionPor_ID_2.setText(QCoreApplication.translate("Lista", u"Por ID", None))
        self.actionPor_Piso.setText(QCoreApplication.translate("Lista", u"Por Piso", None))
        self.actionPor_N_de_Departamento.setText(QCoreApplication.translate("Lista", u"Por N\u00b0 de Departamento", None))
        self.actionPor_Codigo_Postal.setText(QCoreApplication.translate("Lista", u"Por Codigo Postal", None))
        self.actionPor_Metros_Cuadrados.setText(QCoreApplication.translate("Lista", u"Por Metros Cuadrados", None))
        self.actionPor_Ambientes.setText(QCoreApplication.translate("Lista", u"Por Ambientes", None))
        self.actionPor_Dormitorios.setText(QCoreApplication.translate("Lista", u"Por Dormitorios", None))
        self.actionPor_Precio.setText(QCoreApplication.translate("Lista", u"Por Precio", None))
        ___qtablewidgetitem = self.tb_departamentos.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Lista", u"ID", None));
        ___qtablewidgetitem1 = self.tb_departamentos.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Lista", u"Direccion", None));
        ___qtablewidgetitem2 = self.tb_departamentos.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Lista", u"Piso", None));
        ___qtablewidgetitem3 = self.tb_departamentos.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Lista", u"N\u00b0 Departamento", None));
        ___qtablewidgetitem4 = self.tb_departamentos.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Lista", u"Codigo Postal", None));
        ___qtablewidgetitem5 = self.tb_departamentos.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Lista", u"Metros Cuadrados", None));
        ___qtablewidgetitem6 = self.tb_departamentos.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Lista", u"Ambientes", None));
        ___qtablewidgetitem7 = self.tb_departamentos.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Lista", u"Dormitorios", None));
        ___qtablewidgetitem8 = self.tb_departamentos.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Lista", u"Amueblado", None));
        ___qtablewidgetitem9 = self.tb_departamentos.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Lista", u"Habitado", None));
        ___qtablewidgetitem10 = self.tb_departamentos.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Lista", u"Precio ARS", None));
        ___qtablewidgetitem11 = self.tb_departamentos.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Lista", u"Precio UDS", None));
        ___qtablewidgetitem12 = self.tb_departamentos.horizontalHeaderItem(12)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("Lista", u"Imagenes", None));
        ___qtablewidgetitem13 = self.tb_casas.horizontalHeaderItem(0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("Lista", u"ID", None));
        ___qtablewidgetitem14 = self.tb_casas.horizontalHeaderItem(1)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("Lista", u"Direccion", None));
        ___qtablewidgetitem15 = self.tb_casas.horizontalHeaderItem(2)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("Lista", u"Pisos", None));
        ___qtablewidgetitem16 = self.tb_casas.horizontalHeaderItem(3)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("Lista", u"Codigo Postal", None));
        ___qtablewidgetitem17 = self.tb_casas.horizontalHeaderItem(4)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("Lista", u"Metros Cuadrados", None));
        ___qtablewidgetitem18 = self.tb_casas.horizontalHeaderItem(5)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("Lista", u"Dormitorios", None));
        ___qtablewidgetitem19 = self.tb_casas.horizontalHeaderItem(6)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("Lista", u"Ba\u00f1os", None));
        ___qtablewidgetitem20 = self.tb_casas.horizontalHeaderItem(7)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("Lista", u"Amueblado", None));
        ___qtablewidgetitem21 = self.tb_casas.horizontalHeaderItem(8)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("Lista", u"Habitado", None));
        ___qtablewidgetitem22 = self.tb_casas.horizontalHeaderItem(9)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("Lista", u"Precio ARS", None));
        ___qtablewidgetitem23 = self.tb_casas.horizontalHeaderItem(10)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("Lista", u"Precio UDS", None));
        ___qtablewidgetitem24 = self.tb_casas.horizontalHeaderItem(11)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("Lista", u"Imagenes", None));
        self.lb_departamentos.setText(QCoreApplication.translate("Lista", u"Departamentos", None))
        self.lb_casas.setText(QCoreApplication.translate("Lista", u"Casas", None))
        self.pushButton_4.setText(QCoreApplication.translate("Lista", u"Buscar en Internet", None))
        self.pushButton_2.setText(QCoreApplication.translate("Lista", u"Eliminar Propiedad", None))
        self.pushButton.setText(QCoreApplication.translate("Lista", u"Alquilar Propiedad", None))
        self.pushButton_3.setText(QCoreApplication.translate("Lista", u"Ver Alquiladas", None))
        self.pb_volver.setText(QCoreApplication.translate("Lista", u"Volver", None))
        self.menuOrdenar.setTitle(QCoreApplication.translate("Lista", u"Ordenar", None))
    # retranslateUi

