# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 18:26:00 2021

@author: Doğancan
"""

#Butona basıldığında message box çıksın istersem: 
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.pushButtonOk = QPushButton('Ok', self)
        self.pushButtonOk.move(100, 100)
        self.pushButtonOk.resize(QSize(100, 100))

        self.pushButtonOk.clicked.connect(self.buttonOkHandler)

    def buttonOkHandler(self):
        mb = QMessageBox(self) #QMessageBox(None) yazarsam alt pencereden bağımsız çıkar
        mb.setWindowTitle('Test')
        mb.setText('Are you sure?')
        mb.exec() #her message box için exec yazılmalı 

app = QApplication(sys.argv)
mainWindow = MainWindow()
mainWindow.show()
app.exec()

##diyalog penceresi çıktığında standart bazı butonlar çıksın istersem: 
import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.pushButtonOk = QPushButton('Ok', self)
        self.pushButtonOk.move(100, 100)
        self.pushButtonOk.resize(QSize(100, 100))

        self.pushButtonOk.clicked.connect(self.buttonOkHandler)

    def buttonOkHandler(self):
        mb = QMessageBox(None)
        mb.setWindowTitle('Test') #içteki pencere başlığı
        mb.setText('Are you sure?')#messageboxtaki iç yazı 
        mb.setStandardButtons(QMessageBox.Yes|QMessageBox.No|QMessageBox.Cancel)
        mb.setDefaultButton(QMessageBox.No) #defaultta hangisi seçili olsun istersem bu bloğu yazıyorum
        result = mb.exec() 
        #hangi butonla çıktığımı anlamak için bu if bloğunu yazdım
        if result == QMessageBox.Yes:
            print('Yes')
        elif result == QMessageBox.No:
            print('No')
        else:
            print('Cancel')


app = QApplication(sys.argv)
mainWindow = MainWindow()
mainWindow.show()
app.exec()

#Yukarıdaki messagebox için daha kolay bir yöntemi aşağıdaki gibi izleyebilirim 
import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.pushButtonOk = QPushButton('Ok', self)
        self.pushButtonOk.move(100, 100)
        self.pushButtonOk.resize(QSize(100, 100))

        self.pushButtonOk.clicked.connect(self.buttonOkHandler)

    def buttonOkHandler(self):
        result = QMessageBox.information(None, 'Test', 'Are youe sure?', QMessageBox.Yes|QMessageBox.No|QMessageBox.Cancel, QMessageBox.Cancel)
        if result == QMessageBox.Yes:
            print('Yes')
        elif result == QMessageBox.No:
            print('No')
        else:
            print('Cancel')

app = QApplication(sys.argv)
mainWindow = MainWindow()
mainWindow.show()
app.exec()



