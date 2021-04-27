# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 13:45:53 2021

@author doğancan
"""

#geometry yapısı olarak grid kullanırsam matrissel olarak bir yerleşim sağlıyor 
#dizilim hücresel olarak gerçekleşir 


import sys
from PyQt5.Qt import *

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.labelName = QLabel('Adı Soyadı', self)
        self.lineEditName = QLineEdit(self)

        self.labelNo = QLabel('No', self)
        self.lineEditNo = QLineEdit(self)

        self.pushButtonOk = QPushButton('Ok', self)
        self.pushButtonCancel = QPushButton('Cancel', self)

        gridLayout = QGridLayout() #Layout nesnesini yaratıyorum 
        gridLayout.addWidget(self.labelName, 0, 0)
        gridLayout.addWidget(self.lineEditName, 0, 1)
        gridLayout.addWidget(self.labelNo, 1, 0)
        gridLayout.addWidget(self.lineEditNo, 1, 1)
        
        #Butonlar için yarattığım HBox layout nesnemi gridlayout nesneme  set ediyorum
        hBoxLayout = QHBoxLayout()
        hBoxLayout.addSpacing(30)
        hBoxLayout.addWidget(self.pushButtonOk)
        hBoxLayout.addWidget(self.pushButtonCancel)

        gridLayout.addLayout(hBoxLayout, 2, 1) #ana pencereye grid layoutu bağlıyorum 

        self.setLayout(gridLayout)

app = QApplication(sys.argv)
mainWindow = MainWindow()
mainWindow.show()
app.exec()
