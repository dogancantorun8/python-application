# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 17:27:32 2021

@author: Doğancan
"""

#bazi sinyaller sinyal slot mekanizmasıyla işlenmez.Bunun için kendimiz fonksiyon yazmalıyız. 
#örneğin pencere boyutunu büyütmek istersek resizeEvent ile yazmalıyız  


import sys

from PyQt5.QtWidgets import *
from PyQt5.Qt import *

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(640, 480)

        self.cb = QComboBox(self)
        self.cb.setGeometry(10, 10, 300, 30)




app = QApplication(sys.argv)
mainWindow = MainWindow()
mainWindow.show()
app.exec()