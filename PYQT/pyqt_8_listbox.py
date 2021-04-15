# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 19:30:25 2021

@author: Doğancan Torun
"""

## QListWidget sınıfının methodlarıyla işlem yapıyorum 

import sys

from PyQt5.QtWidgets import *
from PyQt5.Qt import *

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(640, 480)

        self.pushButtonOk = QPushButton('Ok', self)
        self.pushButtonOk.move(300, 450)
        self.pushButtonOk.clicked.connect(self.buttonOkHandler)

        self.listWidgetCities = QListWidget(self)
        self.listWidgetCities.setGeometry(20, 20, 200, 400)
        font = self.listWidgetCities.font()
        font.setPointSize(16)
        self.listWidgetCities.setFont(font)
        
        #dosyadan plakalar ve sehirleri okuyorum 
        with open('cities.txt', encoding='utf-8') as f:
            for line in f:
                city_info = line.split()
                self.listWidgetCities.addItem(city_info[1])

        
        lwi = self.listWidgetCities.findItems('Eskişehir', Qt.MatchExactly)
        if lwi:
            self.listWidgetCities.setCurrentItem(lwi[0])

        self.listWidgetCities.itemDoubleClicked.connect(self.listWidgetDoubleClickHandler) #iteme double click yapıldığında işlem yapacak 

    def buttonOkHandler(self):
        #listboxtan seçilen itemi message box ile gösteriyorum 
        QMessageBox.information(None, 'Message', self.listWidgetCities.currentItem().text())

    def listWidgetDoubleClickHandler(self, lwi): 
        QMessageBox.information(None, 'Test', lwi.text()) #itemin yazısını almak istiyorum .text ile alıyorum 




app = QApplication(sys.argv)
mainWindow = MainWindow()
mainWindow.show()
app.exec()

  


