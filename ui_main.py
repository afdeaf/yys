# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_main.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import slots


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(380, 190)
        MainWindow.setStyleSheet("#centralwidget{background-image: url(:/iamge/bg_main.png);}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.window = QtWidgets.QLabel(self.centralwidget)
        self.window.setGeometry(QtCore.QRect(53, 90, 61, 21))
        self.window.setObjectName("window")
        self.win_value_x = QtWidgets.QLineEdit(self.centralwidget)
        self.win_value_x.setGeometry(QtCore.QRect(110, 90, 31, 21))
        self.win_value_x.setObjectName("win_value_x")
        self.time = QtWidgets.QLabel(self.centralwidget)
        self.time.setGeometry(QtCore.QRect(50, 140, 61, 20))
        self.time.setObjectName("time")
        self.time_value = QtWidgets.QLineEdit(self.centralwidget)
        self.time_value.setGeometry(QtCore.QRect(110, 140, 91, 20))
        self.time_value.setObjectName("time_value")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 90, 16, 21))
        self.label.setObjectName("label")
        self.win_value_y = QtWidgets.QLineEdit(self.centralwidget)
        self.win_value_y.setGeometry(QtCore.QRect(170, 90, 31, 20))
        self.win_value_y.setObjectName("win_value_y")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(260, 90, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(110, 40, 91, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(53, 40, 61, 21))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(lambda: slots.pushButton_click(self))
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.window.setText(_translate("MainWindow", "窗口大小："))
        self.win_value_x.setText(_translate("MainWindow", "962"))
        self.time.setText(_translate("MainWindow", "一把时间："))
        self.label.setText(_translate("MainWindow", "X"))
        self.win_value_y.setText(_translate("MainWindow", "575"))
        self.pushButton.setText(_translate("MainWindow", "开始"))
        self.comboBox.setItemText(0, _translate("MainWindow", "御魂/觉醒"))
        self.comboBox.setItemText(1, _translate("MainWindow", "百鬼"))
        self.label_2.setText(_translate("MainWindow", "功能选择："))
import pic_rc
