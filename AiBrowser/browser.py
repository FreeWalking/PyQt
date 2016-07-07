# -*- coding: utf-8 -*-

"""
"""
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebKitWidgets import *
from PyQt5 import QtGui
from Ui_browser import Ui_BrowserForm
import sys
import os

class BrowserForm(QWebView,Ui_BrowserForm):
    _homesite = 'http://www.baidu.com'
    _website = None
    fi = None
    def __init__(self):
        super(BrowserForm, self).__init__()
        self.setupUi(self)
        # 页面跳转委托所有链接
        self.webView.page().setLinkDelegationPolicy(QWebPage.DelegateAllLinks)

        # self.gridLayout.addWidget(self.webView)
        # self.setLayout(self.gridLayout)   #全屏都是浏览框
        self.setWindowTitle("AiBrowser浏览器")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../logo.png"),QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)

        self.gohome()
        run_path = os.getcwd()
        self.fi = open("%s/browser.history"%run_path, "wb")

    def __del__(self):
        self.fi.close();

    def load(self):
        self.webView.load(QUrl(self._website))
        self.webView.show()

    def gohome(self):
        self._website = self._homesite
        self.load()

    def loadweb(self):
        self._website = self.lineEdit.text()
        self.load()

    def urlchange(self):
        url = self.webView.url().toString()
        self.lineEdit.setText(url)
        url = url + '\n'
        self.fi.write(url.encode('utf-8'))
        self.fi.flush()
        print ("----URL : %s"%url)

    def linkclicked(self, url):
        self.webView.load(url)
        self.webView.show()
        print ("----link URL : %s"%url)
        
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    screen = BrowserForm()
    screen.showMaximized()
    # screen.show()
    sys.exit(app.exec_())
