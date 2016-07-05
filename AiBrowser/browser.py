# -*- coding: utf-8 -*-

"""
"""
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebKitWidgets import *
from Ui_browser import Ui_BrowserForm

class BrowserForm(QWidget,Ui_BrowserForm):
    _homesite = 'http://www.baidu.com'
    _website = None
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(BrowserForm, self).__init__(parent)
        self.setupUi(self)

        # self.gridLayout.addWidget(self.webView)
        # self.setLayout(self.gridLayout)   #全屏都是浏览框
        self.setWindowTitle("AiBrowser浏览器")
        self.gohome()

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
        self.lineEdit.setText(self.webView.url().toString())

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    screen = BrowserForm()
    screen.showMaximized()
    # screen.show()
    sys.exit(app.exec_())