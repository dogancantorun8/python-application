# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 18:53:44 2021

@author: dogancan
"""
#İki sekilde icon set edilebilir : 
#Eleman yaratılırken set edilir yada aksiyon kısmındada set islemi olur 


import sys

from PyQt5.QtWidgets import *
from PyQt5.Qt import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(640, 480)

        self.filePopup = QMenu('&File', self)
        self.menuBar().addMenu(self.filePopup)

        self.editPopup = self.menuBar().addMenu('&Edit')

        self.openAction = self.filePopup.addAction('&Open')
        self.openAction.setIcon(QIcon('Icons/Open.png')) 
        self.openAction.triggered.connect(self.openActionHandler)

        self.closeAction = self.filePopup.addAction(QIcon('Icons/Close.png'), '&Close')
        self.closeAction.triggered.connect(self.closeActionHandler)

        self.cutAction = self.editPopup.addAction(QIcon('Icons/Cut.png'), '&Cut', self.cutActionHandler)
        self.copyAction = self.editPopup.addAction(QIcon('Icons/Copy.png'), 'C&opy', self.copyActionHandler)
        self.pasteAction = self.editPopup.addAction(QIcon('Icons/Paste.png'), '&Paste', self.pasteActionHandler)

    def openActionHandler(self):
        print('Open')

    def closeActionHandler(self):
        self.close()

    def cutActionHandler(self):
        print('Cut')

    def copyActionHandler(self):
        print('Copy')

    def pasteActionHandler(self):
        print('Paste')

app = QApplication(sys.argv)
mainWindow = MainWindow()
mainWindow.show()
app.exec()
