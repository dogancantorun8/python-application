# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 17:00:59 2021

@author: Doğancan 
"""


#Qt de Sinyal Slot mantığı: Sinyal =Olay ,Slot=Olay gerçekleştiğinde yapılacak aksiyon(fonksiyon)
#Bir sinyale slotta bağlanabilir,bir sinyale sinyalde bağlanabilir 

##Sinyale slot bağlamak: 

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.pushButtonOk = QPushButton('Ok', self)
        self.pushButtonOk.move(100, 100)
        self.pushButtonOk.resize(QSize(100, 100))

        self.pushButtonOk.clicked.connect(self.buttonOkHandler) #connect metoduyla butonumu bağladım 

    def buttonOkHandler(self):
        print('Ok')


app = QApplication(sys.argv)
mainWindow = MainWindow()
mainWindow.show()
app.exec()
