# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 17:40:46 2021

@author: doğancan
"""

#combobox ile csvden okuduklarımı comboboxa ekliyorum 

import sys

from PyQt5.Qt import *
import csv

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(640, 480)
        
       
        self.cb = QComboBox(self)  #combox yaratıyorum
        self.cb.setGeometry(10, 10, 300, 30) #konumunu set ediyorum
        self.cb.setFont(QFont('Arial', 14))

        
        with open('Countries.csv', encoding='UTF-8') as f:
            for line in csv.reader(f):
                self.cb.addItem(line[-1]) #her okuduğum elemanı comboboxa ekliyorum

app = QApplication(sys.argv)
mainWindow = MainWindow()
mainWindow.show()
app.exec() 
