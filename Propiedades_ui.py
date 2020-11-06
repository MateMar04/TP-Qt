# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Propiedades.ui'
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
        MainWindow.resize(574, 606)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(6, 40, 561, 41))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pb_departamento = QPushButton(self.horizontalLayoutWidget)
        self.pb_departamento.setObjectName(u"pb_departamento")

        self.horizontalLayout.addWidget(self.pb_departamento)

        self.pb_casa = QPushButton(self.horizontalLayoutWidget)
        self.pb_casa.setObjectName(u"pb_casa")

        self.horizontalLayout.addWidget(self.pb_casa)

        self.pb_lista = QPushButton(self.horizontalLayoutWidget)
        self.pb_lista.setObjectName(u"pb_lista")

        self.horizontalLayout.addWidget(self.pb_lista)

        self.formLayoutWidget = QWidget(self.centralwidget)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 90, 561, 436))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.lb_direccion = QLabel(self.formLayoutWidget)
        self.lb_direccion.setObjectName(u"lb_direccion")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lb_direccion)

        self.lb_metros_cuadrados = QLabel(self.formLayoutWidget)
        self.lb_metros_cuadrados.setObjectName(u"lb_metros_cuadrados")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.lb_metros_cuadrados)

        self.lb_cant_piso = QLabel(self.formLayoutWidget)
        self.lb_cant_piso.setObjectName(u"lb_cant_piso")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.lb_cant_piso)

        self.lb_n_piso = QLabel(self.formLayoutWidget)
        self.lb_n_piso.setObjectName(u"lb_n_piso")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.lb_n_piso)

        self.lb_codigo_postal = QLabel(self.formLayoutWidget)
        self.lb_codigo_postal.setObjectName(u"lb_codigo_postal")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lb_codigo_postal)

        self.lb_nro_departamento = QLabel(self.formLayoutWidget)
        self.lb_nro_departamento.setObjectName(u"lb_nro_departamento")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.lb_nro_departamento)

        self.lb_nro_ambientes = QLabel(self.formLayoutWidget)
        self.lb_nro_ambientes.setObjectName(u"lb_nro_ambientes")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.lb_nro_ambientes)

        self.lb_nro_dormitorios = QLabel(self.formLayoutWidget)
        self.lb_nro_dormitorios.setObjectName(u"lb_nro_dormitorios")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.lb_nro_dormitorios)

        self.lb_n_banios = QLabel(self.formLayoutWidget)
        self.lb_n_banios.setObjectName(u"lb_n_banios")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.lb_n_banios)

        self.lb_amueblado = QLabel(self.formLayoutWidget)
        self.lb_amueblado.setObjectName(u"lb_amueblado")

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.lb_amueblado)

        self.lb_habitado = QLabel(self.formLayoutWidget)
        self.lb_habitado.setObjectName(u"lb_habitado")

        self.formLayout.setWidget(10, QFormLayout.LabelRole, self.lb_habitado)

        self.lb_precio_ars = QLabel(self.formLayoutWidget)
        self.lb_precio_ars.setObjectName(u"lb_precio_ars")

        self.formLayout.setWidget(11, QFormLayout.LabelRole, self.lb_precio_ars)

        self.lb_precio_uds = QLabel(self.formLayoutWidget)
        self.lb_precio_uds.setObjectName(u"lb_precio_uds")

        self.formLayout.setWidget(12, QFormLayout.LabelRole, self.lb_precio_uds)

        self.lb_imagenes = QLabel(self.formLayoutWidget)
        self.lb_imagenes.setObjectName(u"lb_imagenes")

        self.formLayout.setWidget(13, QFormLayout.LabelRole, self.lb_imagenes)

        self.le_direccion = QLineEdit(self.formLayoutWidget)
        self.le_direccion.setObjectName(u"le_direccion")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.le_direccion)

        self.le_codigo_postal = QLineEdit(self.formLayoutWidget)
        self.le_codigo_postal.setObjectName(u"le_codigo_postal")
        self.le_codigo_postal.setLayoutDirection(Qt.LeftToRight)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.le_codigo_postal)

        self.le_metros_cuadrados = QLineEdit(self.formLayoutWidget)
        self.le_metros_cuadrados.setObjectName(u"le_metros_cuadrados")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.le_metros_cuadrados)

        self.le_cant_pisos = QLineEdit(self.formLayoutWidget)
        self.le_cant_pisos.setObjectName(u"le_cant_pisos")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.le_cant_pisos)

        self.le_nro_piso = QLineEdit(self.formLayoutWidget)
        self.le_nro_piso.setObjectName(u"le_nro_piso")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.le_nro_piso)

        self.le_nro_departamento = QLineEdit(self.formLayoutWidget)
        self.le_nro_departamento.setObjectName(u"le_nro_departamento")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.le_nro_departamento)

        self.le_nro_ambientes = QLineEdit(self.formLayoutWidget)
        self.le_nro_ambientes.setObjectName(u"le_nro_ambientes")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.le_nro_ambientes)

        self.le_nro_dormitorios = QLineEdit(self.formLayoutWidget)
        self.le_nro_dormitorios.setObjectName(u"le_nro_dormitorios")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.le_nro_dormitorios)

        self.le_nro_banios = QLineEdit(self.formLayoutWidget)
        self.le_nro_banios.setObjectName(u"le_nro_banios")

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.le_nro_banios)

        self.le_precio_ars = QLineEdit(self.formLayoutWidget)
        self.le_precio_ars.setObjectName(u"le_precio_ars")

        self.formLayout.setWidget(11, QFormLayout.FieldRole, self.le_precio_ars)

        self.le_precio_uds = QLineEdit(self.formLayoutWidget)
        self.le_precio_uds.setObjectName(u"le_precio_uds")

        self.formLayout.setWidget(12, QFormLayout.FieldRole, self.le_precio_uds)

        self.le_imagenes = QLineEdit(self.formLayoutWidget)
        self.le_imagenes.setObjectName(u"le_imagenes")

        self.formLayout.setWidget(13, QFormLayout.FieldRole, self.le_imagenes)

        self.cb_amueblado = QComboBox(self.formLayoutWidget)
        self.cb_amueblado.addItem("")
        self.cb_amueblado.addItem("")
        self.cb_amueblado.setObjectName(u"cb_amueblado")

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.cb_amueblado)

        self.cb_habitado = QComboBox(self.formLayoutWidget)
        self.cb_habitado.addItem("")
        self.cb_habitado.addItem("")
        self.cb_habitado.setObjectName(u"cb_habitado")

        self.formLayout.setWidget(10, QFormLayout.FieldRole, self.cb_habitado)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(160, 10, 271, 20))
        self.horizontalLayoutWidget_2 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(10, 520, 561, 51))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pb_registrar = QPushButton(self.horizontalLayoutWidget_2)
        self.pb_registrar.setObjectName(u"pb_registrar")

        self.horizontalLayout_2.addWidget(self.pb_registrar)

        self.pb_borrar_todo = QPushButton(self.horizontalLayoutWidget_2)
        self.pb_borrar_todo.setObjectName(u"pb_borrar_todo")

        self.horizontalLayout_2.addWidget(self.pb_borrar_todo)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pb_registrar.clicked.connect(MainWindow.registrar_slot)
        self.pb_borrar_todo.clicked.connect(MainWindow.borrar_todo_slot)
        self.le_precio_ars.textChanged.connect(MainWindow.peso_change_slot)
        self.pb_departamento.clicked.connect(MainWindow.departamento_slot)
        self.pb_casa.clicked.connect(MainWindow.casa_slot)
        self.pb_lista.clicked.connect(MainWindow.lista_slot)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Propiedades", None))
        self.pb_departamento.setText(QCoreApplication.translate("MainWindow", u"Departamento", None))
        self.pb_casa.setText(QCoreApplication.translate("MainWindow", u"Casa", None))
        self.pb_lista.setText(QCoreApplication.translate("MainWindow", u"Lista", None))
        self.lb_direccion.setText(QCoreApplication.translate("MainWindow", u"Direccion", None))
        self.lb_metros_cuadrados.setText(QCoreApplication.translate("MainWindow", u"Metros Cuadrados", None))
        self.lb_cant_piso.setText(QCoreApplication.translate("MainWindow", u"Cantidad de Pisos", None))
        self.lb_n_piso.setText(QCoreApplication.translate("MainWindow", u"Nro de Piso", None))
        self.lb_codigo_postal.setText(QCoreApplication.translate("MainWindow", u"Codigo Postal", None))
        self.lb_nro_departamento.setText(QCoreApplication.translate("MainWindow", u"Nro de Departamento", None))
        self.lb_nro_ambientes.setText(QCoreApplication.translate("MainWindow", u"Nro de Ambientes", None))
        self.lb_nro_dormitorios.setText(QCoreApplication.translate("MainWindow", u"Nro de Dormitorios", None))
        self.lb_n_banios.setText(QCoreApplication.translate("MainWindow", u"Nro de ba\u00f1os", None))
        self.lb_amueblado.setText(QCoreApplication.translate("MainWindow", u"Amueblado", None))
        self.lb_habitado.setText(QCoreApplication.translate("MainWindow", u"Habitado", None))
        self.lb_precio_ars.setText(QCoreApplication.translate("MainWindow", u"Precio ARS", None))
        self.lb_precio_uds.setText(QCoreApplication.translate("MainWindow", u"Precio UDS", None))
        self.lb_imagenes.setText(QCoreApplication.translate("MainWindow", u"Imagenes (URL)", None))
        self.le_direccion.setInputMask("")
        self.le_codigo_postal.setInputMask(QCoreApplication.translate("MainWindow", u"9999", None))
        self.le_metros_cuadrados.setInputMask(QCoreApplication.translate("MainWindow", u"999", None))
        self.le_cant_pisos.setInputMask(QCoreApplication.translate("MainWindow", u"9", None))
        self.le_nro_piso.setInputMask(QCoreApplication.translate("MainWindow", u"99", None))
        self.le_nro_departamento.setInputMask(QCoreApplication.translate("MainWindow", u"9", None))
        self.le_nro_ambientes.setInputMask(QCoreApplication.translate("MainWindow", u"99", None))
        self.le_nro_dormitorios.setInputMask(QCoreApplication.translate("MainWindow", u"9", None))
        self.le_nro_banios.setInputMask(QCoreApplication.translate("MainWindow", u"9", None))
        self.le_precio_ars.setInputMask(QCoreApplication.translate("MainWindow", u"########", None))
        self.le_precio_uds.setInputMask("")
        self.cb_amueblado.setItemText(0, QCoreApplication.translate("MainWindow", u"Si", None))
        self.cb_amueblado.setItemText(1, QCoreApplication.translate("MainWindow", u"No", None))

        self.cb_habitado.setItemText(0, QCoreApplication.translate("MainWindow", u"Si", None))
        self.cb_habitado.setItemText(1, QCoreApplication.translate("MainWindow", u"No", None))

        self.label.setText(QCoreApplication.translate("MainWindow", u"\u00bfQue tipo de propiedad desea agregar?", None))
        self.pb_registrar.setText(QCoreApplication.translate("MainWindow", u"Registrar", None))
        self.pb_borrar_todo.setText(QCoreApplication.translate("MainWindow", u"Borrar Todo", None))
    # retranslateUi

