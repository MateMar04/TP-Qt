# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Departamento.ui'
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


class Ui_Departamento(object):
    def setupUi(self, Departamento):
        if not Departamento.objectName():
            Departamento.setObjectName(u"Departamento")
        Departamento.resize(514, 426)
        Departamento.setMinimumSize(QSize(514, 426))
        Departamento.setMaximumSize(QSize(514, 426))
        self.centralwidget = QWidget(Departamento)
        self.centralwidget.setObjectName(u"centralwidget")
        self.formLayoutWidget = QWidget(self.centralwidget)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(0, 10, 511, 368))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.lb_direccion = QLabel(self.formLayoutWidget)
        self.lb_direccion.setObjectName(u"lb_direccion")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lb_direccion)

        self.lb_piso = QLabel(self.formLayoutWidget)
        self.lb_piso.setObjectName(u"lb_piso")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lb_piso)

        self.lb__n_departamento = QLabel(self.formLayoutWidget)
        self.lb__n_departamento.setObjectName(u"lb__n_departamento")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.lb__n_departamento)

        self.lb_codigo_postal = QLabel(self.formLayoutWidget)
        self.lb_codigo_postal.setObjectName(u"lb_codigo_postal")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.lb_codigo_postal)

        self.lb_metros = QLabel(self.formLayoutWidget)
        self.lb_metros.setObjectName(u"lb_metros")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.lb_metros)

        self.lb_ambientes = QLabel(self.formLayoutWidget)
        self.lb_ambientes.setObjectName(u"lb_ambientes")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.lb_ambientes)

        self.lb_dormitorios = QLabel(self.formLayoutWidget)
        self.lb_dormitorios.setObjectName(u"lb_dormitorios")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.lb_dormitorios)

        self.lb_amueblado = QLabel(self.formLayoutWidget)
        self.lb_amueblado.setObjectName(u"lb_amueblado")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.lb_amueblado)

        self.lb_habitado = QLabel(self.formLayoutWidget)
        self.lb_habitado.setObjectName(u"lb_habitado")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.lb_habitado)

        self.lb_precios_ars = QLabel(self.formLayoutWidget)
        self.lb_precios_ars.setObjectName(u"lb_precios_ars")

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.lb_precios_ars)

        self.lb_precios_uds = QLabel(self.formLayoutWidget)
        self.lb_precios_uds.setObjectName(u"lb_precios_uds")

        self.formLayout.setWidget(10, QFormLayout.LabelRole, self.lb_precios_uds)

        self.lb_imagenes = QLabel(self.formLayoutWidget)
        self.lb_imagenes.setObjectName(u"lb_imagenes")

        self.formLayout.setWidget(11, QFormLayout.LabelRole, self.lb_imagenes)

        self.cb_habitado = QComboBox(self.formLayoutWidget)
        self.cb_habitado.addItem("")
        self.cb_habitado.addItem("")
        self.cb_habitado.setObjectName(u"cb_habitado")

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.cb_habitado)

        self.cb_amueblado = QComboBox(self.formLayoutWidget)
        self.cb_amueblado.addItem("")
        self.cb_amueblado.addItem("")
        self.cb_amueblado.setObjectName(u"cb_amueblado")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.cb_amueblado)

        self.cb_ambientes = QComboBox(self.formLayoutWidget)
        self.cb_ambientes.addItem("")
        self.cb_ambientes.addItem("")
        self.cb_ambientes.addItem("")
        self.cb_ambientes.addItem("")
        self.cb_ambientes.addItem("")
        self.cb_ambientes.setObjectName(u"cb_ambientes")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.cb_ambientes)

        self.cb_dormitorios = QComboBox(self.formLayoutWidget)
        self.cb_dormitorios.addItem("")
        self.cb_dormitorios.addItem("")
        self.cb_dormitorios.addItem("")
        self.cb_dormitorios.setObjectName(u"cb_dormitorios")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.cb_dormitorios)

        self.le_direccion = QLineEdit(self.formLayoutWidget)
        self.le_direccion.setObjectName(u"le_direccion")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.le_direccion)

        self.le_piso = QLineEdit(self.formLayoutWidget)
        self.le_piso.setObjectName(u"le_piso")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.le_piso)

        self.le_n_departamento = QLineEdit(self.formLayoutWidget)
        self.le_n_departamento.setObjectName(u"le_n_departamento")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.le_n_departamento)

        self.le_codigo_postal = QLineEdit(self.formLayoutWidget)
        self.le_codigo_postal.setObjectName(u"le_codigo_postal")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.le_codigo_postal)

        self.le_metros_cuadrados = QLineEdit(self.formLayoutWidget)
        self.le_metros_cuadrados.setObjectName(u"le_metros_cuadrados")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.le_metros_cuadrados)

        self.le_precio_ars = QLineEdit(self.formLayoutWidget)
        self.le_precio_ars.setObjectName(u"le_precio_ars")

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.le_precio_ars)

        self.le_precios_uds = QLineEdit(self.formLayoutWidget)
        self.le_precios_uds.setObjectName(u"le_precios_uds")

        self.formLayout.setWidget(10, QFormLayout.FieldRole, self.le_precios_uds)

        self.le_imagenes = QLineEdit(self.formLayoutWidget)
        self.le_imagenes.setObjectName(u"le_imagenes")

        self.formLayout.setWidget(11, QFormLayout.FieldRole, self.le_imagenes)

        Departamento.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(Departamento)
        self.statusbar.setObjectName(u"statusbar")
        Departamento.setStatusBar(self.statusbar)

        self.retranslateUi(Departamento)

        QMetaObject.connectSlotsByName(Departamento)
    # setupUi

    def retranslateUi(self, Departamento):
        Departamento.setWindowTitle(QCoreApplication.translate("Departamento", u"MainWindow", None))
        self.lb_direccion.setText(QCoreApplication.translate("Departamento", u"Direccion", None))
        self.lb_piso.setText(QCoreApplication.translate("Departamento", u"Piso", None))
        self.lb__n_departamento.setText(QCoreApplication.translate("Departamento", u"N\u00b0 Departamento", None))
        self.lb_codigo_postal.setText(QCoreApplication.translate("Departamento", u"Codigo Postal", None))
        self.lb_metros.setText(QCoreApplication.translate("Departamento", u"Metros Cuadrados", None))
        self.lb_ambientes.setText(QCoreApplication.translate("Departamento", u"N\u00b0 Ambientes", None))
        self.lb_dormitorios.setText(QCoreApplication.translate("Departamento", u"N\u00b0 Dormitorios", None))
        self.lb_amueblado.setText(QCoreApplication.translate("Departamento", u"Amueblado", None))
        self.lb_habitado.setText(QCoreApplication.translate("Departamento", u"Habitado", None))
        self.lb_precios_ars.setText(QCoreApplication.translate("Departamento", u"Precio ARS", None))
        self.lb_precios_uds.setText(QCoreApplication.translate("Departamento", u"Precio UDS", None))
        self.lb_imagenes.setText(QCoreApplication.translate("Departamento", u"Imagenes (Ingrese URL)", None))
        self.cb_habitado.setItemText(0, QCoreApplication.translate("Departamento", u"No", None))
        self.cb_habitado.setItemText(1, QCoreApplication.translate("Departamento", u"Si", None))

        self.cb_amueblado.setItemText(0, QCoreApplication.translate("Departamento", u"No", None))
        self.cb_amueblado.setItemText(1, QCoreApplication.translate("Departamento", u"Si", None))

        self.cb_ambientes.setItemText(0, QCoreApplication.translate("Departamento", u"Monoambiente", None))
        self.cb_ambientes.setItemText(1, QCoreApplication.translate("Departamento", u"2", None))
        self.cb_ambientes.setItemText(2, QCoreApplication.translate("Departamento", u"3", None))
        self.cb_ambientes.setItemText(3, QCoreApplication.translate("Departamento", u"4", None))
        self.cb_ambientes.setItemText(4, QCoreApplication.translate("Departamento", u"5", None))

        self.cb_dormitorios.setItemText(0, QCoreApplication.translate("Departamento", u"1", None))
        self.cb_dormitorios.setItemText(1, QCoreApplication.translate("Departamento", u"2", None))
        self.cb_dormitorios.setItemText(2, QCoreApplication.translate("Departamento", u"3", None))

        self.le_piso.setInputMask(QCoreApplication.translate("Departamento", u"99", None))
        self.le_n_departamento.setInputMask(QCoreApplication.translate("Departamento", u"99", None))
        self.le_codigo_postal.setInputMask(QCoreApplication.translate("Departamento", u"9999", None))
        self.le_metros_cuadrados.setInputMask(QCoreApplication.translate("Departamento", u"999", None))
        self.le_precio_ars.setInputMask(QCoreApplication.translate("Departamento", u"99999999", None))
        self.le_precios_uds.setInputMask(QCoreApplication.translate("Departamento", u"99999", None))
    # retranslateUi

