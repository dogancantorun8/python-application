# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 18:17:49 2021

@author: dogancan
"""

##Bir menü yaratmak için önce Qmenübar nesnesi yaratmalıyım 
#2.olarak QMenü nesnelerini yaratacağım 3.olarakta QAction nesnelerini yaratacağım. 
#Menü ve toolbar yaratırken ana penceremi QMainwindowdan türetmeliyim

import sys

from PyQt5.QtWidgets import *
from PyQt5.Qt import *

class MainWindow(QMainWindow): #Menu bar zaten icinde, QWidget kullansaydik menu bari kendimiz yaratacaktik
    def __init__(self):
        super().__init__()
        self.resize(640, 480)

app = QApplication(sys.argv)
mainWindow = MainWindow()
mainWindow.show()
app.exec()