# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Menu.ui'
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


class Ui_Menu(object):
    def setupUi(self, Menu):
        if not Menu.objectName():
            Menu.setObjectName(u"Menu")
        Menu.resize(800, 243)
        self.centralwidget = QWidget(Menu)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 9, 791, 201))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.lb_menu = QLabel(self.verticalLayoutWidget)
        self.lb_menu.setObjectName(u"lb_menu")

        self.verticalLayout.addWidget(self.lb_menu)

        self.lb_accion = QLabel(self.verticalLayoutWidget)
        self.lb_accion.setObjectName(u"lb_accion")

        self.verticalLayout.addWidget(self.lb_accion)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pb_agregar_propiedad = QPushButton(self.verticalLayoutWidget)
        self.pb_agregar_propiedad.setObjectName(u"pb_agregar_propiedad")

        self.horizontalLayout.addWidget(self.pb_agregar_propiedad)

        self.pb_ver_propiedades = QPushButton(self.verticalLayoutWidget)
        self.pb_ver_propiedades.setObjectName(u"pb_ver_propiedades")

        self.horizontalLayout.addWidget(self.pb_ver_propiedades)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pb_ver_lista = QPushButton(self.verticalLayoutWidget)
        self.pb_ver_lista.setObjectName(u"pb_ver_lista")

        self.horizontalLayout_2.addWidget(self.pb_ver_lista)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        Menu.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(Menu)
        self.statusbar.setObjectName(u"statusbar")
        Menu.setStatusBar(self.statusbar)

        self.retranslateUi(Menu)
        self.pb_agregar_propiedad.clicked.connect(Menu.agregar_propiedades_slot)
        self.pb_ver_propiedades.clicked.connect(Menu.ver_propiedades_slot)
        self.pb_ver_lista.clicked.connect(Menu.ver_lista_slot)

        QMetaObject.connectSlotsByName(Menu)
    # setupUi

    def retranslateUi(self, Menu):
        Menu.setWindowTitle(QCoreApplication.translate("Menu", u"MainWindow", None))
        self.lb_menu.setText(QCoreApplication.translate("Menu", u"                                                                                                          MENU", None))
        self.lb_accion.setText(QCoreApplication.translate("Menu", u"                                                                                      \u00bfQue accion desea realizar?", None))
        self.pb_agregar_propiedad.setText(QCoreApplication.translate("Menu", u"Agregar propiedad", None))
        self.pb_ver_propiedades.setText(QCoreApplication.translate("Menu", u"Ver Propiedades", None))
        self.pb_ver_lista.setText(QCoreApplication.translate("Menu", u"Ver lista de guardados ", None))
    # retranslateUi

