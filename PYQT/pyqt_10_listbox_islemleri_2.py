# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 17:49:48 2021

@author: Dogancan Torun 
"""

#listboxta ilgili elemana double click yapıldığında elemanı silebilirim    
#istediğim ile çift tıkladığımda silme işlemi yapabilirim
import sys
import pandas as pd

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

        self.df_cities = pd.read_csv('Cities.csv', delimiter=';', encoding='UTF-8')
        cities = self.df_cities['il'].to_list()
        cities = [city.replace('I', 'ı').capitalize()   for city in cities ]
        self.df_cities['il'] = cities

        self.listWidgetCities.addItems(cities)
        self.df_villages = pd.read_csv('Villages.csv', delimiter=';', encoding='UTF-8')
        villages = self.df_villages['ilce'].to_list()
        villages= [village.replace('I', 'ı').capitalize() for village in villages]
        self.df_villages['ilce'] = villages

        self.listWidgetCities.itemDoubleClicked.connect(self.listWidgetDoubleClickHandler)
        self.listWidgetCities.currentItemChanged.connect(self.listWidgetCurrentChangedHandler)

        self.listWidgetVillages = QListWidget(self)
        self.listWidgetVillages.setGeometry(240, 20, 200, 400)
        self.listWidgetVillages.setFont(font)

    def buttonOkHandler(self):
        QMessageBox.information(None, 'Message', self.listWidgetCities.currentItem().text())
        
        #çift tıklanıldıgında silme handleri tetikleniyor
    def listWidgetDoubleClickHandler(self, lwi):
        self.listWidgetCities.takeItem(self.listWidgetCities.currentRow())

    
    def listWidgetCurrentChangedHandler(self, lwiCurrent, lwiPrevious):
        self.listWidgetVillages.clear()
        id = self.df_cities[self.df_cities['il'] == lwiCurrent.text()].id.iloc[0]
        villages = self.df_villages[self.df_villages['il_id'] == id].ilce.to_list()
        self.listWidgetVillages.addItems(villages)

app = QApplication(sys.argv)
mainWindow = MainWindow()
mainWindow.show()
app.exec()

