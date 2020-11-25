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
        Lista.resize(1285, 480)
        Lista.setMinimumSize(QSize(1285, 480))
        Lista.setMaximumSize(QSize(1285, 480))
        self.centralwidget = QWidget(Lista)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(180, 0, 1111, 471))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.tb_departamentos = QTableWidget(self.verticalLayoutWidget)
        if (self.tb_departamentos.columnCount() < 12):
            self.tb_departamentos.setColumnCount(12)
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
        self.tb_departamentos.setObjectName(u"tb_departamentos")

        self.verticalLayout.addWidget(self.tb_departamentos)

        self.tb_casas = QTableWidget(self.verticalLayoutWidget)
        if (self.tb_casas.columnCount() < 11):
            self.tb_casas.setColumnCount(11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tb_casas.setHorizontalHeaderItem(0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tb_casas.setHorizontalHeaderItem(1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tb_casas.setHorizontalHeaderItem(2, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tb_casas.setHorizontalHeaderItem(3, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tb_casas.setHorizontalHeaderItem(4, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tb_casas.setHorizontalHeaderItem(5, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tb_casas.setHorizontalHeaderItem(6, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tb_casas.setHorizontalHeaderItem(7, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tb_casas.setHorizontalHeaderItem(8, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tb_casas.setHorizontalHeaderItem(9, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tb_casas.setHorizontalHeaderItem(10, __qtablewidgetitem22)
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
        self.verticalLayoutWidget_3.setGeometry(QRect(0, 350, 171, 121))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
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

        self.retranslateUi(Lista)
        self.pb_volver.clicked.connect(Lista.volver_slot)
        self.pushButton.clicked.connect(Lista.alquilar_propiedad_slot)
        self.pushButton_2.clicked.connect(Lista.eliminar_propiedad_slot)
        self.pushButton_3.clicked.connect(Lista.ver_alquilados_slot)

        QMetaObject.connectSlotsByName(Lista)
    # setupUi

    def retranslateUi(self, Lista):
        Lista.setWindowTitle(QCoreApplication.translate("Lista", u"Lista de Propiedades", None))
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
        ___qtablewidgetitem12 = self.tb_casas.horizontalHeaderItem(0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("Lista", u"ID", None));
        ___qtablewidgetitem13 = self.tb_casas.horizontalHeaderItem(1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("Lista", u"Direccion", None));
        ___qtablewidgetitem14 = self.tb_casas.horizontalHeaderItem(2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("Lista", u"Pisos", None));
        ___qtablewidgetitem15 = self.tb_casas.horizontalHeaderItem(3)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("Lista", u"Codigo Postal", None));
        ___qtablewidgetitem16 = self.tb_casas.horizontalHeaderItem(4)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("Lista", u"Metros Cuadrados", None));
        ___qtablewidgetitem17 = self.tb_casas.horizontalHeaderItem(5)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("Lista", u"Dormitorios", None));
        ___qtablewidgetitem18 = self.tb_casas.horizontalHeaderItem(6)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("Lista", u"Ba\u00f1os", None));
        ___qtablewidgetitem19 = self.tb_casas.horizontalHeaderItem(7)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("Lista", u"Amueblado", None));
        ___qtablewidgetitem20 = self.tb_casas.horizontalHeaderItem(8)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("Lista", u"Habitado", None));
        ___qtablewidgetitem21 = self.tb_casas.horizontalHeaderItem(9)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("Lista", u"Precio ARS", None));
        ___qtablewidgetitem22 = self.tb_casas.horizontalHeaderItem(10)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("Lista", u"Precio UDS", None));
        self.lb_departamentos.setText(QCoreApplication.translate("Lista", u"Departamentos", None))
        self.lb_casas.setText(QCoreApplication.translate("Lista", u"Casas", None))
        self.pushButton_2.setText(QCoreApplication.translate("Lista", u"Eliminar Propiedad", None))
        self.pushButton.setText(QCoreApplication.translate("Lista", u"Alquilar Propiedad", None))
        self.pushButton_3.setText(QCoreApplication.translate("Lista", u"Ver Alquiladas", None))
        self.pb_volver.setText(QCoreApplication.translate("Lista", u"Volver", None))
    # retranslateUi

