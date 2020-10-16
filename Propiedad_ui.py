# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Propiedad.ui'
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


class Ui_Propiedad(object):
    def setupUi(self, Propiedad):
        if not Propiedad.objectName():
            Propiedad.setObjectName(u"Propiedad")
        Propiedad.resize(497, 179)
        Propiedad.setMinimumSize(QSize(497, 179))
        Propiedad.setMaximumSize(QSize(497, 179))
        self.centralwidget = QWidget(Propiedad)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 60, 491, 80))
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

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(130, 20, 261, 20))
        Propiedad.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(Propiedad)
        self.statusbar.setObjectName(u"statusbar")
        Propiedad.setStatusBar(self.statusbar)

        self.retranslateUi(Propiedad)
        self.pb_casa.clicked.connect(Propiedad.casa_slot)
        self.pb_departamento.clicked.connect(Propiedad.departamento_slot)
        self.pb_lista.clicked.connect(Propiedad.lista_slot)

        QMetaObject.connectSlotsByName(Propiedad)
    # setupUi

    def retranslateUi(self, Propiedad):
        Propiedad.setWindowTitle(QCoreApplication.translate("Propiedad", u"Propiedad", None))
        self.pb_departamento.setText(QCoreApplication.translate("Propiedad", u"Departamento", None))
        self.pb_casa.setText(QCoreApplication.translate("Propiedad", u"Casa", None))
        self.pb_lista.setText(QCoreApplication.translate("Propiedad", u"Lista", None))
        self.label.setText(QCoreApplication.translate("Propiedad", u"\u00bfQu\u00e9 tipo de propiedad desea a\u00f1adir?", None))
    # retranslateUi

