# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 18:09:21 2021

@author: dogancan
"""

import sys
import csv
from PyQt5.Qt import *

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(640, 480)

        self.cb = QComboBox(self)
        self.cb.setGeometry(10, 10, 300, 30)
        self.cb.setFont(QFont('Arial', 14))
        self.cb.setMaxVisibleItems(15)
        self.cb.setEditable(True)

        self.buttonOk = QPushButton('Ok', self)
        self.buttonOk.move(350, 10)
        self.buttonOk.clicked.connect(self.buttonOkHandler)

        self.cb.currentIndexChanged.connect(self.currentIndexChangedHandler)

        with open('Countries.csv', encoding='UTF-8') as f:
            for line in csv.reader(f):
                self.cb.addItem(line[-1])

        self.cb.setItemIcon(0, QIcon('Icons/Cherry.png')) #0.elemana icon ekledim 
        self.cb.setItemIcon(5, QIcon('Icons/Strawberry.png')) #5.elemana icon ekledim 

        self.cb.setItemIcon(7, QIcon('Icons/Grape.png'))
        self.cb.setItemIcon(9, QIcon('Icons/Apple.png'))

    def buttonOkHandler(self):
        print(self.cb.currentText())
        print(self.cb.currentIndex())

    def currentIndexChangedHandler(self, cindex):
        print(cindex)

app = QApplication(sys.argv)
mainWindow = MainWindow()
mainWindow.show()
app.exec()
