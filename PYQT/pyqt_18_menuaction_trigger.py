# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 18:47:15 2021

@author: dogancan
"""


#Menu barda her action ile oluşan sinyalimi trigger ile yakalayacağım  
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
        self.openAction.triggered.connect(self.openActionHandler) #Open aksiyonu icin trigger connect  oluşturdum 

        self.closeAction = self.filePopup.addAction('&Close')
        self.closeAction.triggered.connect(self.closeActionHandler)

        self.cutAction = self.editPopup.addAction('&Cut', self.cutActionHandler)
        self.copyAction = self.editPopup.addAction('&Copy', self.copyActionHandler)
        self.pasteAction = self.editPopup.addAction('&Paste', self.pasteActionHandler)

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