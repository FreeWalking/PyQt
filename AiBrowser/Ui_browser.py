# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'browser.ui'
#
# Created: Thu Jul  7 11:22:50 2016
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_BrowserForm(object):
    def setupUi(self, BrowserForm):
        BrowserForm.setObjectName("BrowserForm")
        BrowserForm.setEnabled(True)
        BrowserForm.resize(1375, 705)
        self.loadButton = QtWidgets.QPushButton(BrowserForm)
        self.loadButton.setGeometry(QtCore.QRect(900, 10, 75, 23))
        self.loadButton.setMinimumSize(QtCore.QSize(75, 0))
        self.loadButton.setObjectName("loadButton")
        self.label = QtWidgets.QLabel(BrowserForm)
        self.label.setGeometry(QtCore.QRect(251, 11, 36, 16))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(BrowserForm)
        self.lineEdit.setGeometry(QtCore.QRect(290, 10, 591, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.webView = QtWebKitWidgets.QWebView(BrowserForm)
        self.webView.setGeometry(QtCore.QRect(-10, 40, 1371, 651))
        self.webView.setUrl(QtCore.QUrl("about:blank"))
        self.webView.setObjectName("webView")
        self.pushButton = QtWidgets.QPushButton(BrowserForm)
        self.pushButton.setGeometry(QtCore.QRect(980, 10, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(BrowserForm)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 10, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(BrowserForm)
        self.pushButton_3.setGeometry(QtCore.QRect(90, 10, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(BrowserForm)
        self.pushButton_4.setGeometry(QtCore.QRect(1060, 10, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(BrowserForm)
        self.pushButton_5.setGeometry(QtCore.QRect(170, 10, 75, 23))
        self.pushButton_5.setObjectName("pushButton_5")

        self.retranslateUi(BrowserForm)
        self.loadButton.clicked.connect(BrowserForm.loadweb)
        self.webView.urlChanged['QUrl'].connect(BrowserForm.urlchange)
        self.pushButton.clicked.connect(self.webView.stop)
        self.pushButton_4.clicked.connect(self.webView.reload)
        self.pushButton_2.clicked.connect(self.webView.back)
        self.pushButton_3.clicked.connect(self.webView.forward)
        self.pushButton_5.clicked.connect(BrowserForm.gohome)
        self.lineEdit.returnPressed.connect(BrowserForm.loadweb)
        self.webView.linkClicked['QUrl'].connect(BrowserForm.linkclicked)
        QtCore.QMetaObject.connectSlotsByName(BrowserForm)

    def retranslateUi(self, BrowserForm):
        _translate = QtCore.QCoreApplication.translate
        BrowserForm.setWindowTitle(_translate("BrowserForm", "Dialog"))
        self.loadButton.setText(_translate("BrowserForm", "Load"))
        self.label.setText(_translate("BrowserForm", "网址："))
        self.pushButton.setText(_translate("BrowserForm", "Stop"))
        self.pushButton_2.setText(_translate("BrowserForm", "Back"))
        self.pushButton_3.setText(_translate("BrowserForm", "Forward "))
        self.pushButton_4.setText(_translate("BrowserForm", "Reload"))
        self.pushButton_5.setText(_translate("BrowserForm", "Home"))

from PyQt5 import QtWebKitWidgets
