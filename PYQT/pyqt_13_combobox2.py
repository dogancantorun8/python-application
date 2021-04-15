# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 17:56:12 2021

@author: doğancan 
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
    
        self.buttonOk = QPushButton('Ok', self)
        self.buttonOk.move(350, 10)
        self.buttonOk.clicked.connect(self.buttonOkHandler)

        with open('Countries.csv', encoding='UTF-8') as f:
            for line in csv.reader(f):
                self.cb.addItem(line[-1])

    def buttonOkHandler(self):
        print(self.cb.currentText()) #o anda hangi eleman seçilmişse onu .Yani comboxtaki yazımı alıyorum 
        print(self.cb.currentIndex()) # o anda hangi eleman seçilmişse onun indexini veriyor.

app = QApplication(sys.argv)
mainWindow = MainWindow()
mainWindow.show()
app.exec()
