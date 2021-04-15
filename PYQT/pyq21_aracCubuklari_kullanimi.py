# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 17:07:54 2021

@author: dogancan 
"""

#araccubukları QToolbar sınıfından yaratılıyor. 
#yani ana pencere üzerinde yeni bir pencere ekliyoruz  
#burada daha önce menü barda oluşturduğumuz actionları toolbarımıza ekleyebiliriz  
#toolbarı is Visible ile görünmez yapabiliyorum 
import sys

from PyQt5.Qt import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(640, 480)

        self.menuBar().setFont(QFont('Arial', 12))

        self.filePopup = QMenu('&File', self)
        self.menuBar().addMenu(self.filePopup)
        self.filePopup.setFont(QFont('Arial', 12))

        self.editPopup = self.menuBar().addMenu('&Edit')
        self.editPopup.setFont(QFont('Arial', 12))
        self.editPopup.setToolTipsVisible(True)

        self.openAction = self.filePopup.addAction('&Open')
        self.openAction.setIcon(QIcon('Icons/Open.png'))
        self.openAction.triggered.connect(self.openActionHandler)
        self.openAction.setShortcut('Ctrl+O')

        self.closeAction = self.filePopup.addAction(QIcon('Icons/Close.png'), '&Close')
        self.closeAction.triggered.connect(self.closeActionHandler)
        self.closeAction.setEnabled(False)

        self.cutAction = self.editPopup.addAction(QIcon('Icons/Cut.png'), '&Cut', self.cutActionHandler, 'Ctrl+X')
        self.copyAction = self.editPopup.addAction(QIcon('Icons/Copy.png'), 'C&opy', self.copyActionHandler, 'Ctrl+C')
        self.copyAction.setToolTip('Copies into clipboard')
        self.pasteAction = self.editPopup.addAction(QIcon('Icons/Paste.png'), '&Paste', self.pasteActionHandler, 'Ctrl+V')

        self.cutAction.setCheckable(True)
        self.cutAction.setToolTip('Cut and save in clipboard')

        self.editPopup.addSeparator()
        self.fruitPopup = QMenu('Fruit', self)
        self.editPopup.addMenu(self.fruitPopup)
        self.fruitPopup.setFont(QFont('Arial', 12))

        self.bananaAction = self.fruitPopup.addAction('Banana', lambda: print('Banana'))
        self.cherryAction = self.fruitPopup.addAction('Cherry', lambda: print('Cherry'))

        self.bananaAction.setCheckable(True)
        self.bananaAction.setChecked(True)

        self.toolBar = QToolBar('Main Toolbar', self)
        self.addToolBar(self.toolBar)
        self.toolBar.addAction(self.openAction)
        self.toolBar.addAction(self.closeAction)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.cutAction)
        self.toolBar.addAction(self.copyAction)
        self.toolBar.addAction(self.pasteAction)
        self.toolBar.setIconSize(QSize(40, 40))

        self.viewPopup = QMenu('View', self)
        self.menuBar().addMenu(self.viewPopup)
        self.toolBarAction = self.viewPopup.addAction('Toolbar', self.toolBarActionHandler)
        self.toolBarAction.setCheckable(True)
        self.toolBarAction.setChecked(True)

        self.mainWidget = QWidget(self)
        self.mainWidget.setGeometry(0, self.menuBar().height() + self.toolBar.height() + 12, self.width(), self.height() - (self.menuBar().height() + self.toolBar.height() + 12))
        self.buttonOk = QPushButton('Ok', self.mainWidget)
        self.buttonOk.move(0, 0)

    def openActionHandler(self):
        self.closeAction.setEnabled(True)
        self.openAction.setEnabled(False)

    def closeActionHandler(self):
        self.closeAction.setEnabled(False)
        self.openAction.setEnabled(True)

    def cutActionHandler(self):
        print('Cut')

    def copyActionHandler(self):
        print('Copy')

    def pasteActionHandler(self):
        print('Paste')

    def toolBarActionHandler(self):
        self.toolBar.setVisible(not self.toolBar.isVisible())

app = QApplication(sys.argv)
mainWindow = MainWindow()
mainWindow.show()
app.exec()
