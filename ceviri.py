# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ceviri.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 600)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 600))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 600))
        MainWindow.setStyleSheet("QMainWindow::selection{\n"
"    background-color: orange;\n"
"}\n"
"#centralwidget{\n"
"    background-color: #000;\n"
"}\n"
"QPushButton{\n"
"    width: 200px;\n"
"    height: 50px;\n"
"    font-size: 18px;\n"
"    background-color:orangered;\n"
"    color: #fff;\n"
"    border-radius: 6px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:#d12c03;\n"
"}\n"
"QLabel{\n"
"    border:none;\n"
"    font-size: 18px;\n"
"    color:#fff;\n"
"}\n"
"QLineEdit{\n"
"    background-color:#000;\n"
"    border:none;\n"
"    color: #fff;\n"
"    font-size: 18px;\n"
"    border-bottom:2px solid orangered;\n"
"}\n"
"QLineEdit:focus{\n"
"    border-bottom: 2px solid orange;\n"
"}\n"
"QRadioButton{\n"
"    background-color: orangered;\n"
"    color:#fff;\n"
"    font-size: 18px;\n"
"    border-radius: 6px;\n"
"}\n"
"QRadioButton:hover{\n"
"    background-color:rgb(196, 57, 7);\n"
"}\n"
"QRadioButton:focus{\n"
"    background-color: orange;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_ceviri = QtWidgets.QLabel(self.centralwidget)
        self.lbl_ceviri.setGeometry(QtCore.QRect(20, 340, 781, 111))
        self.lbl_ceviri.setStyleSheet("font-size:18px;\n"
"color:#fff;")
        self.lbl_ceviri.setText("")
        self.lbl_ceviri.setObjectName("lbl_ceviri")
        self.btn_cevir = QtWidgets.QPushButton(self.centralwidget)
        self.btn_cevir.setGeometry(QtCore.QRect(260, 420, 431, 101))
        self.btn_cevir.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_cevir.setStyleSheet("")
        self.btn_cevir.setObjectName("btn_cevir")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(110, 70, 711, 171))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.lbl_en = QtWidgets.QLabel(self.layoutWidget)
        self.lbl_en.setMinimumSize(QtCore.QSize(200, 50))
        self.lbl_en.setStyleSheet("")
        self.lbl_en.setObjectName("lbl_en")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lbl_en)
        self.txt_en = QtWidgets.QLineEdit(self.layoutWidget)
        self.txt_en.setMinimumSize(QtCore.QSize(0, 50))
        self.txt_en.setObjectName("txt_en")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txt_en)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setMinimumSize(QtCore.QSize(200, 50))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.txt_tr = QtWidgets.QLineEdit(self.layoutWidget)
        self.txt_tr.setMinimumSize(QtCore.QSize(0, 50))
        self.txt_tr.setObjectName("txt_tr")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txt_tr)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(180, 250, 601, 52))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.rd_entr = QtWidgets.QRadioButton(self.widget)
        self.rd_entr.setMinimumSize(QtCore.QSize(100, 50))
        self.rd_entr.setMaximumSize(QtCore.QSize(200, 100))
        self.rd_entr.setStyleSheet("")
        self.rd_entr.setObjectName("rd_entr")
        self.horizontalLayout.addWidget(self.rd_entr)
        self.rd_tren = QtWidgets.QRadioButton(self.widget)
        self.rd_tren.setMinimumSize(QtCore.QSize(100, 50))
        self.rd_tren.setMaximumSize(QtCore.QSize(200, 100))
        self.rd_tren.setStyleSheet("")
        self.rd_tren.setObjectName("rd_tren")
        self.horizontalLayout.addWidget(self.rd_tren)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_cevir.setText(_translate("MainWindow", "Çevir"))
        self.lbl_en.setText(_translate("MainWindow", "İngilizce Metin : "))
        self.label_2.setText(_translate("MainWindow", "Türkçe  Metin : "))
        self.rd_entr.setText(_translate("MainWindow", "İngilizce-Türkçe "))
        self.rd_tren.setText(_translate("MainWindow", "Türkçe-İngilizce"))
