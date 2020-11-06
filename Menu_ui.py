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
        Menu.resize(800, 600)
        self.centralwidget = QWidget(Menu)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 9, 791, 201))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton = QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_3 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_2.addWidget(self.pushButton_3)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        Menu.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(Menu)
        self.statusbar.setObjectName(u"statusbar")
        Menu.setStatusBar(self.statusbar)

        self.retranslateUi(Menu)
        self.pushButton.clicked.connect(Menu.agregar_propiedades_slot)
        self.pushButton_2.clicked.connect(Menu.ver_propiedades_slot)
        self.pushButton_3.clicked.connect(Menu.ver_lista_slot)

        QMetaObject.connectSlotsByName(Menu)
    # setupUi

    def retranslateUi(self, Menu):
        Menu.setWindowTitle(QCoreApplication.translate("Menu", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("Menu", u"                                                                                                          MENU", None))
        self.label_2.setText(QCoreApplication.translate("Menu", u"                                                                                      \u00bfQue accion desea realizar?", None))
        self.pushButton.setText(QCoreApplication.translate("Menu", u"Agregar propiedad", None))
        self.pushButton_2.setText(QCoreApplication.translate("Menu", u"Ver Propiedades", None))
        self.pushButton_3.setText(QCoreApplication.translate("Menu", u"Ver lista de guardados ", None))
    # retranslateUi

