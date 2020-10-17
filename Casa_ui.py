# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Casa.ui'
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


class Ui_Casa(object):
    def setupUi(self, Casa):
        if not Casa.objectName():
            Casa.setObjectName(u"Casa")
        Casa.resize(430, 389)
        Casa.setMinimumSize(QSize(430, 389))
        Casa.setMaximumSize(QSize(430, 389))
        self.centralwidget = QWidget(Casa)
        self.centralwidget.setObjectName(u"centralwidget")
        self.formLayoutWidget = QWidget(self.centralwidget)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(0, 0, 421, 337))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.lb_direccion = QLabel(self.formLayoutWidget)
        self.lb_direccion.setObjectName(u"lb_direccion")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lb_direccion)

        self.lb_codigo_postal = QLabel(self.formLayoutWidget)
        self.lb_codigo_postal.setObjectName(u"lb_codigo_postal")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lb_codigo_postal)

        self.lb_pisos = QLabel(self.formLayoutWidget)
        self.lb_pisos.setObjectName(u"lb_pisos")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.lb_pisos)

        self.lb_metros_cuadrados = QLabel(self.formLayoutWidget)
        self.lb_metros_cuadrados.setObjectName(u"lb_metros_cuadrados")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.lb_metros_cuadrados)

        self.lb_dormitorios = QLabel(self.formLayoutWidget)
        self.lb_dormitorios.setObjectName(u"lb_dormitorios")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.lb_dormitorios)

        self.lb_banios = QLabel(self.formLayoutWidget)
        self.lb_banios.setObjectName(u"lb_banios")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.lb_banios)

        self.lb_amueblada = QLabel(self.formLayoutWidget)
        self.lb_amueblada.setObjectName(u"lb_amueblada")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.lb_amueblada)

        self.lb_habitada = QLabel(self.formLayoutWidget)
        self.lb_habitada.setObjectName(u"lb_habitada")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.lb_habitada)

        self.lb_precio_ars = QLabel(self.formLayoutWidget)
        self.lb_precio_ars.setObjectName(u"lb_precio_ars")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.lb_precio_ars)

        self.lb_precio_uds = QLabel(self.formLayoutWidget)
        self.lb_precio_uds.setObjectName(u"lb_precio_uds")

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.lb_precio_uds)

        self.lb_imagenes = QLabel(self.formLayoutWidget)
        self.lb_imagenes.setObjectName(u"lb_imagenes")

        self.formLayout.setWidget(10, QFormLayout.LabelRole, self.lb_imagenes)

        self.le_direccion = QLineEdit(self.formLayoutWidget)
        self.le_direccion.setObjectName(u"le_direccion")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.le_direccion)

        self.le_codigo_postal = QLineEdit(self.formLayoutWidget)
        self.le_codigo_postal.setObjectName(u"le_codigo_postal")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.le_codigo_postal)

        self.le_metros_cuadrados = QLineEdit(self.formLayoutWidget)
        self.le_metros_cuadrados.setObjectName(u"le_metros_cuadrados")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.le_metros_cuadrados)

        self.le_precio_ars = QLineEdit(self.formLayoutWidget)
        self.le_precio_ars.setObjectName(u"le_precio_ars")

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.le_precio_ars)

        self.le_precio_uds = QLineEdit(self.formLayoutWidget)
        self.le_precio_uds.setObjectName(u"le_precio_uds")

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.le_precio_uds)

        self.le_imagenes = QLineEdit(self.formLayoutWidget)
        self.le_imagenes.setObjectName(u"le_imagenes")

        self.formLayout.setWidget(10, QFormLayout.FieldRole, self.le_imagenes)

        self.cb_pisos = QComboBox(self.formLayoutWidget)
        self.cb_pisos.setObjectName(u"cb_pisos")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.cb_pisos)

        self.cb_dormitorios = QComboBox(self.formLayoutWidget)
        self.cb_dormitorios.setObjectName(u"cb_dormitorios")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.cb_dormitorios)

        self.cb_banios = QComboBox(self.formLayoutWidget)
        self.cb_banios.setObjectName(u"cb_banios")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.cb_banios)

        self.cb_amueblada = QComboBox(self.formLayoutWidget)
        self.cb_amueblada.setObjectName(u"cb_amueblada")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.cb_amueblada)

        self.cb_habitada = QComboBox(self.formLayoutWidget)
        self.cb_habitada.setObjectName(u"cb_habitada")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.cb_habitada)

        self.pb_volver = QPushButton(self.centralwidget)
        self.pb_volver.setObjectName(u"pb_volver")
        self.pb_volver.setGeometry(QRect(330, 340, 89, 25))
        self.pb_volver.setMaximumSize(QSize(330, 340))
        Casa.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(Casa)
        self.statusbar.setObjectName(u"statusbar")
        Casa.setStatusBar(self.statusbar)

        self.retranslateUi(Casa)
        self.pb_volver.clicked.connect(Casa.volver_slot)

        QMetaObject.connectSlotsByName(Casa)
    # setupUi

    def retranslateUi(self, Casa):
        Casa.setWindowTitle(QCoreApplication.translate("Casa", u"Casa", None))
        self.lb_direccion.setText(QCoreApplication.translate("Casa", u"Direccion", None))
        self.lb_codigo_postal.setText(QCoreApplication.translate("Casa", u"Codigo Postal", None))
        self.lb_pisos.setText(QCoreApplication.translate("Casa", u"Pisos", None))
        self.lb_metros_cuadrados.setText(QCoreApplication.translate("Casa", u"Metros Cuadrados", None))
        self.lb_dormitorios.setText(QCoreApplication.translate("Casa", u"Dormitorios", None))
        self.lb_banios.setText(QCoreApplication.translate("Casa", u"Ba\u00f1os", None))
        self.lb_amueblada.setText(QCoreApplication.translate("Casa", u"Amueblada", None))
        self.lb_habitada.setText(QCoreApplication.translate("Casa", u"Habitada", None))
        self.lb_precio_ars.setText(QCoreApplication.translate("Casa", u"Precio ARS", None))
        self.lb_precio_uds.setText(QCoreApplication.translate("Casa", u"Precio UDS", None))
        self.lb_imagenes.setText(QCoreApplication.translate("Casa", u"Imagenes", None))
        self.pb_volver.setText(QCoreApplication.translate("Casa", u"Volver", None))
    # retranslateUi

