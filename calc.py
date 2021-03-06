# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calc.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(310, 485)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(12, 12, 12);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.push_2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.push_2.sizePolicy().hasHeightForWidth())
        self.push_2.setSizePolicy(sizePolicy)
        self.push_2.setStyleSheet("QPushButton{\n"
"font: 57 20pt \"MathJax_Vector-Bold\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(191, 191, 191);\n"
"border-radius:30px;\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"    background-color: rgb(238, 238, 238);\n"
"}\n"
"QPushButton{\n"
"background-color: rgb(208, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.push_2.setObjectName("push_2")
        self.gridLayout.addWidget(self.push_2, 2, 1, 1, 1)
        self.push_9 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.push_9.sizePolicy().hasHeightForWidth())
        self.push_9.setSizePolicy(sizePolicy)
        self.push_9.setStyleSheet("QPushButton{\n"
"font: 57 20pt \"MathJax_Vector-Bold\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(191, 191, 191);\n"
"border-radius:30px;\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"    background-color: rgb(238, 238, 238);\n"
"}\n"
"QPushButton{\n"
"background-color: rgb(208, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.push_9.setObjectName("push_9")
        self.gridLayout.addWidget(self.push_9, 4, 2, 1, 1)
        self.push_6 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.push_6.sizePolicy().hasHeightForWidth())
        self.push_6.setSizePolicy(sizePolicy)
        self.push_6.setStyleSheet("QPushButton{\n"
"font: 57 20pt \"MathJax_Vector-Bold\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(191, 191, 191);\n"
"border-radius:30px;\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"    background-color: rgb(238, 238, 238);\n"
"}\n"
"QPushButton{\n"
"background-color: rgb(208, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.push_6.setObjectName("push_6")
        self.gridLayout.addWidget(self.push_6, 3, 2, 1, 1)
        self.push_tochka = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.push_tochka.sizePolicy().hasHeightForWidth())
        self.push_tochka.setSizePolicy(sizePolicy)
        self.push_tochka.setStyleSheet("QPushButton{\n"
"font: 57 20pt \"MathJax_Vector-Bold\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(191, 191, 191);\n"
"border-radius:30px;\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"    background-color: rgb(238, 238, 238);\n"
"}\n"
"QPushButton{\n"
"background-color: rgb(208, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.push_tochka.setObjectName("push_tochka")
        self.gridLayout.addWidget(self.push_tochka, 5, 2, 1, 1)
        self.push_ayir = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.push_ayir.sizePolicy().hasHeightForWidth())
        self.push_ayir.setSizePolicy(sizePolicy)
        self.push_ayir.setStyleSheet("QPushButton{\n"
"font: 57 36pt \"MathJax_Vector-Bold\";\n"
"    color: rgb(255, 255, 255);\n"
"    \n"
"    background-color: rgb(225, 225, 112);\n"
"border-radius:30px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: rgb(255, 255, 127);\n"
"    background-color: rgb(12, 12, 12);\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(208, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.push_ayir.setObjectName("push_ayir")
        self.gridLayout.addWidget(self.push_ayir, 2, 3, 1, 1)
        self.push_boluv = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.push_boluv.sizePolicy().hasHeightForWidth())
        self.push_boluv.setSizePolicy(sizePolicy)
        self.push_boluv.setStyleSheet("QPushButton{\n"
"font: 57 36pt \"MathJax_Vector-Bold\";\n"
"    color: rgb(255, 255, 255);\n"
"    \n"
"    background-color: rgb(225, 225, 112);\n"
"border-radius:30px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: rgb(255, 255, 127);\n"
"    background-color: rgb(12, 12, 12);\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(208, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.push_boluv.setObjectName("push_boluv")
        self.gridLayout.addWidget(self.push_boluv, 4, 3, 1, 1)
        self.push_3 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.push_3.sizePolicy().hasHeightForWidth())
        self.push_3.setSizePolicy(sizePolicy)
        self.push_3.setStyleSheet("QPushButton{\n"
"font: 57 20pt \"MathJax_Vector-Bold\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(191, 191, 191);\n"
"border-radius:30px;\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"    background-color: rgb(238, 238, 238);\n"
"}\n"
"QPushButton{\n"
"background-color: rgb(208, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.push_3.setObjectName("push_3")
        self.gridLayout.addWidget(self.push_3, 2, 2, 1, 1)
        self.push_kopay = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.push_kopay.sizePolicy().hasHeightForWidth())
        self.push_kopay.setSizePolicy(sizePolicy)
        self.push_kopay.setStyleSheet("QPushButton{\n"
"font: 57 36pt \"MathJax_Vector-Bold\";\n"
"    color: rgb(255, 255, 255);\n"
"    \n"
"    background-color: rgb(225, 225, 112);\n"
"border-radius:30px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: rgb(255, 255, 127);\n"
"    background-color: rgb(12, 12, 12);\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(208, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.push_kopay.setObjectName("push_kopay")
        self.gridLayout.addWidget(self.push_kopay, 3, 3, 1, 1)
        self.push_8 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.push_8.sizePolicy().hasHeightForWidth())
        self.push_8.setSizePolicy(sizePolicy)
        self.push_8.setStyleSheet("QPushButton{\n"
"font: 57 20pt \"MathJax_Vector-Bold\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(191, 191, 191);\n"
"border-radius:30px;\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"    background-color: rgb(238, 238, 238);\n"
"}\n"
"QPushButton{\n"
"background-color: rgb(208, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.push_8.setObjectName("push_8")
        self.gridLayout.addWidget(self.push_8, 4, 1, 1, 1)
        self.push_1 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.push_1.sizePolicy().hasHeightForWidth())
        self.push_1.setSizePolicy(sizePolicy)
        self.push_1.setStyleSheet("QPushButton{\n"
"font: 57 20pt \"MathJax_Vector-Bold\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(191, 191, 191);\n"
"border-radius:30px;\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"    background-color: rgb(238, 238, 238);\n"
"}\n"
"QPushButton{\n"
"background-color: rgb(208, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.push_1.setObjectName("push_1")
        self.gridLayout.addWidget(self.push_1, 2, 0, 1, 1)
        self.push_ochir = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.push_ochir.sizePolicy().hasHeightForWidth())
        self.push_ochir.setSizePolicy(sizePolicy)
        self.push_ochir.setStyleSheet("QPushButton{\n"
"font: 57 20pt \"MathJax_Vector-Bold\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(191, 191, 191);\n"
"border-radius:30px;\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"    background-color: rgb(238, 238, 238);\n"
"}\n"
"QPushButton{\n"
"background-color: rgb(208, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.push_ochir.setObjectName("push_ochir")
        self.gridLayout.addWidget(self.push_ochir, 1, 2, 1, 1)
        self.push_barobar = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.push_barobar.sizePolicy().hasHeightForWidth())
        self.push_barobar.setSizePolicy(sizePolicy)
        self.push_barobar.setStyleSheet("QPushButton{\n"
"font: 57 36pt \"MathJax_Vector-Bold\";\n"
"    color: rgb(255, 255, 255);\n"
"    \n"
"    background-color: rgb(225, 225, 112);\n"
"border-radius:30px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: rgb(255, 255, 127);\n"
"    background-color: rgb(12, 12, 12);\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(208, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.push_barobar.setObjectName("push_barobar")
        self.gridLayout.addWidget(self.push_barobar, 5, 3, 1, 1)
        self.push_qosh = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.push_qosh.sizePolicy().hasHeightForWidth())
        self.push_qosh.setSizePolicy(sizePolicy)
        self.push_qosh.setStyleSheet("QPushButton{\n"
"font: 57 36pt \"MathJax_Vector-Bold\";\n"
"    color: rgb(255, 255, 255);\n"
"    \n"
"    background-color: rgb(225, 225, 112);\n"
"border-radius:30px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: rgb(255, 255, 127);\n"
"    background-color: rgb(12, 12, 12);\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(208, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.push_qosh.setIconSize(QtCore.QSize(27, 28))
        self.push_qosh.setAutoRepeatDelay(0)
        self.push_qosh.setAutoRepeatInterval(0)
        self.push_qosh.setObjectName("push_qosh")
        self.gridLayout.addWidget(self.push_qosh, 1, 3, 1, 1)
        self.push_4 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.push_4.sizePolicy().hasHeightForWidth())
        self.push_4.setSizePolicy(sizePolicy)
        self.push_4.setStyleSheet("QPushButton{\n"
"font: 57 20pt \"MathJax_Vector-Bold\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(191, 191, 191);\n"
"border-radius:30px;\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"    background-color: rgb(238, 238, 238);\n"
"}\n"
"QPushButton{\n"
"background-color: rgb(208, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.push_4.setObjectName("push_4")
        self.gridLayout.addWidget(self.push_4, 3, 0, 1, 1)
        self.push_7 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.push_7.sizePolicy().hasHeightForWidth())
        self.push_7.setSizePolicy(sizePolicy)
        self.push_7.setStyleSheet("QPushButton{\n"
"font: 57 20pt \"MathJax_Vector-Bold\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(191, 191, 191);\n"
"border-radius:30px;\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"    background-color: rgb(238, 238, 238);\n"
"}\n"
"QPushButton{\n"
"background-color: rgb(208, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.push_7.setObjectName("push_7")
        self.gridLayout.addWidget(self.push_7, 4, 0, 1, 1)
        self.push_5 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.push_5.sizePolicy().hasHeightForWidth())
        self.push_5.setSizePolicy(sizePolicy)
        self.push_5.setStyleSheet("QPushButton{\n"
"font: 57 20pt \"MathJax_Vector-Bold\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(191, 191, 191);\n"
"border-radius:30px;\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"    background-color: rgb(238, 238, 238);\n"
"}\n"
"QPushButton{\n"
"background-color: rgb(208, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.push_5.setObjectName("push_5")
        self.gridLayout.addWidget(self.push_5, 3, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(14)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet("font: 57 28pt \"MathJax_Vector-Bold\";\n"
"color: rgb(255, 255, 255);")
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 4)
        self.push_tozala = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.push_tozala.sizePolicy().hasHeightForWidth())
        self.push_tozala.setSizePolicy(sizePolicy)
        self.push_tozala.setStyleSheet("QPushButton{\n"
"font: 57 20pt \"MathJax_Vector-Bold\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(191, 191, 191);\n"
"border-radius:30px;\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"    background-color: rgb(238, 238, 238);\n"
"}\n"
"QPushButton{\n"
"background-color: rgb(208, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.push_tozala.setObjectName("push_tozala")
        self.gridLayout.addWidget(self.push_tozala, 1, 0, 1, 2)
        self.push_0 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.push_0.sizePolicy().hasHeightForWidth())
        self.push_0.setSizePolicy(sizePolicy)
        self.push_0.setStyleSheet("QPushButton{\n"
"font: 57 20pt \"MathJax_Vector-Bold\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(191, 191, 191);\n"
"border-radius:30px;\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"    background-color: rgb(238, 238, 238);\n"
"}\n"
"QPushButton{\n"
"background-color: rgb(208, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.push_0.setObjectName("push_0")
        self.gridLayout.addWidget(self.push_0, 5, 0, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 310, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.push_1.clicked.connect(self.method_1)
        self.push_2.clicked.connect(self.method_2)
        self.push_3.clicked.connect(self.method_3)
        self.push_4.clicked.connect(self.method_4)
        self.push_5.clicked.connect(self.method_5)
        self.push_6.clicked.connect(self.method_6)
        self.push_7.clicked.connect(self.method_7)
        self.push_8.clicked.connect(self.method_8)
        self.push_9.clicked.connect(self.method_9)
        self.push_0.clicked.connect(self.method_0)
        self.push_tochka.clicked.connect(self.method_tochka)
        self.push_qosh.clicked.connect(self.method_qosh)
        self.push_ayir.clicked.connect(self.method_ayir)
        self.push_kopay.clicked.connect(self.method_kopay)
        self.push_boluv.clicked.connect(self.method_boluv)
        self.push_barobar.clicked.connect(self.method_barobar)
        self.push_tozala.clicked.connect(self.method_tozala)
        self.push_ochir.clicked.connect(self.method_ochir)



    def method_1(self):
        text=self.label.text()
        self.label.setText(text+"1")

    def method_2(self):
        text=self.label.text()
        self.label.setText(text+"2")

    def method_3(self):
        text=self.label.text()
        self.label.setText(text+"3")

    def method_4(self):
        text=self.label.text()
        self.label.setText(text+"4")

    def method_5(self):
        text=self.label.text()
        self.label.setText(text+"5")

    def method_6(self):
        text=self.label.text()
        self.label.setText(text+"6")

    def method_7(self):
        text=self.label.text()
        self.label.setText(text+"7")

    def method_8(self):
        text=self.label.text()
        self.label.setText(text+"8")

    def method_9(self):
        text=self.label.text()
        self.label.setText(text+"9")
        
    def method_0(self):
        text=self.label.text()
        self.label.setText(text+"0")

    def method_tochka(self):
        text=self.label.text()
        self.label.setText(text+".")

    def method_qosh(self):
        text=self.label.text()
        self.label.setText(text+"+")

    def method_ayir(self):
        text=self.label.text()
        self.label.setText(text+"-")

    def method_kopay(self):
        text=self.label.text()
        self.label.setText(text+"*")

    def method_boluv(self):
        text=self.label.text()
        self.label.setText(text+"/")

    def method_tozala(self):
        self.label.setText("")

    def method_ochir(self):
        text=self.label.text()
        self.label.setText(text[:len(text)-1])

    def method_barobar(self):
        text=self.label.text()

        try:
            ans=eval(text)
            self.label.setText(str(ans))
        except:
            self.label.setText("Noto'gri Kiritish")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Kalkulyator"))
        self.push_2.setText(_translate("MainWindow", "2"))
        self.push_2.setShortcut(_translate("MainWindow", "2"))
        self.push_9.setText(_translate("MainWindow", "9"))
        self.push_9.setShortcut(_translate("MainWindow", "9"))
        self.push_6.setText(_translate("MainWindow", "6"))
        self.push_6.setShortcut(_translate("MainWindow", "6"))
        self.push_tochka.setText(_translate("MainWindow", "."))
        self.push_tochka.setShortcut(_translate("MainWindow", "."))
        self.push_ayir.setText(_translate("MainWindow", "-"))
        self.push_ayir.setShortcut(_translate("MainWindow", "-"))
        self.push_boluv.setText(_translate("MainWindow", "??"))
        self.push_boluv.setShortcut(_translate("MainWindow", "/"))
        self.push_3.setText(_translate("MainWindow", "3"))
        self.push_3.setShortcut(_translate("MainWindow", "3"))
        self.push_kopay.setText(_translate("MainWindow", "x"))
        self.push_kopay.setShortcut(_translate("MainWindow", "*"))
        self.push_8.setText(_translate("MainWindow", "8"))
        self.push_8.setShortcut(_translate("MainWindow", "8"))
        self.push_1.setText(_translate("MainWindow", "1"))
        self.push_1.setShortcut(_translate("MainWindow", "1"))
        self.push_ochir.setText(_translate("MainWindow", "Del"))
        self.push_ochir.setShortcut(_translate("MainWindow", "Backspace"))
        self.push_barobar.setText(_translate("MainWindow", "="))
        self.push_barobar.setShortcut(_translate("MainWindow", "Enter"))
        self.push_qosh.setText(_translate("MainWindow", "+"))
        self.push_qosh.setShortcut(_translate("MainWindow", "+"))
        self.push_4.setText(_translate("MainWindow", "4"))
        self.push_4.setShortcut(_translate("MainWindow", "4"))
        self.push_7.setText(_translate("MainWindow", "7"))
        self.push_7.setShortcut(_translate("MainWindow", "7"))
        self.push_5.setText(_translate("MainWindow", "5"))
        self.push_5.setShortcut(_translate("MainWindow", "5"))
        self.push_tozala.setText(_translate("MainWindow", "Tozalash"))
        self.push_tozala.setShortcut(_translate("MainWindow", "Del"))
        self.push_0.setText(_translate("MainWindow", "0"))
        self.push_0.setShortcut(_translate("MainWindow", "0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
