# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 18:59:00 2021

@author: doğancan
"""

import sys

from PyQt5.QtWidgets import *
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

        self.openAction = self.filePopup.addAction('&Open')
        self.openAction.setIcon(QIcon('Icons/Open.png'))
        self.openAction.triggered.connect(self.openActionHandler)
        self.openAction.setShortcut('Ctrl+O')


        self.closeAction = self.filePopup.addAction(QIcon('Icons/Close.png'), '&Close')
        self.closeAction.triggered.connect(self.closeActionHandler) 
        self.closeAction.setEnabled(False)

        self.cutAction = self.editPopup.addAction(QIcon('Icons/Cut.png'), '&Cut', self.cutActionHandler, 'Ctrl+X')
        self.copyAction = self.editPopup.addAction(QIcon('Icons/Copy.png'), 'C&opy', self.copyActionHandler, 'Ctrl+C')
        
        self.copyAction.setToolTip('Copies into clipboard') #toolun görevini belirtmek istersek
        self.pasteAction = self.editPopup.addAction(QIcon('Icons/Paste.png'), '&Paste', self.pasteActionHandler, 'Ctrl+V')
        
        self.cutAction.setCheckable(True)
        self.cutAction.setToolTip('Cut and save in clipboard')
        
        ##QMenüden bir alt menü oluşturup daha önceleri action eklediğim popupa menü ekliyorum
        self.fruitPopup = QMenu('Fruit', self)
        self.editPopup.addMenu(self.fruitPopup)
        self.fruitPopup.setFont(QFont('Arial', 12))
        
        #Fruit popupa action ekledim 
        self.bananaAction = self.fruitPopup.addAction('Banana', lambda: print('Banana'))
        self.cherryAction = self.fruitPopup.addAction('Cherry', lambda: print('Cherry'))
        
        #actionun check durumunun gösteriyor
        self.bananaAction.setCheckable(True)
        self.bananaAction.setChecked(True)


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

app = QApplication(sys.argv)
mainWindow = MainWindow()
mainWindow.show()
app.exec()
