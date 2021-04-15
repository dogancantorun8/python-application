# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 18:33:17 2021

@author: dogancan
"""


#QAction nesnelerini oluşturma ve kulanma :Bir menü elemanı seçildiğinde bir işlem yapmak istersek Qaction Eventleriyle işlem yapabiliriz 


import sys
from PyQt5.QtWidgets import *
from PyQt5.Qt import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(640, 480)

        self.filePopup = QMenu('File', self)
        self.menuBar().addMenu(self.filePopup)

        self.editPopup = self.menuBar().addMenu('Edit')

        self.openAction = self.filePopup.addAction('&Open')
        self.openAction.triggered.connect(self.openActionHandler)

        self.closeAction = self.filePopup.addAction('&Close')
        self.closeAction.triggered.connect(self.closeActionHandler)

        self.cutAction = self.editPopup.addAction('&Cut')
        self.copyAction = self.editPopup.addAction('&Copy')
        self.pasteAction = self.editPopup.addAction('&Paste')

    def openActionHandler(self):
        print('Open')

    def closeActionHandler(self):
        self.close()

app = QApplication(sys.argv)
mainWindow = MainWindow()
mainWindow.show()
app.exec()