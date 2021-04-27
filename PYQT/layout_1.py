# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 12:55:12 2021

@author: dogancan 
"""

#Layout Nesneleri : 
#QHbox Layout= Horizontal yerleştirme yapıyor 
#QVboxLayout=Düşey yerleştirme yapıyor 
#QGridLayout =Satır sütun belirterek yerleştirme yapıyor 
#QStackedLayout ,QFormlayout  
#Önemli Not:Bİr pencereye tek bir layout nesnesi iliştirilebilir 

#Tüm layout nesnelerinin iki temel metodu var ; addWidget  ve addLayout  
#Layout nesnelerini self nesneleri ile tutmaya gerek yoktur. 

import sys
from PyQt5.Qt import *

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.labelName = QLabel('Adı Soyadı', self)
        self.lineEditName = QLineEdit(self)
        
        #Ad soyad labeli ve text boxunu HBox layout icerisine yerleştiriyorum
        hBoxLayout1 = QHBoxLayout()
        hBoxLayout1.addWidget(self.labelName)
        hBoxLayout1.addWidget(self.lineEditName)
        
        
        self.labelNo = QLabel('No            ', self)
        self.lineEditNo = QLineEdit(self)
        
        #NO labeli ve text boxunu HBox layout icerisine yerleştiriyorum
        hBoxLayout2 = QHBoxLayout()
        hBoxLayout2.addWidget(self.labelNo)
        hBoxLayout2.addWidget(self.lineEditNo)

        self.pushButtonOk = QPushButton('Ok', self)
        self.pushButtonOk.clicked.connect(self.okHandler)
        
        self.pushButtonCancel = QPushButton('Cancel', self)
        
        #OK ve Cancel butonlarını bir başka HBox layout icerisine yerleştiriyorum
        hBoxLayout3 = QHBoxLayout()
        hBoxLayout3.addWidget(self.pushButtonOk)
        hBoxLayout3.addWidget(self.pushButtonCancel)
        
        #Tüm yarattığım layout nesnelerimi VBoxLayot icerisine yerlestiriyorum
        vBoxLayout = QVBoxLayout()
        vBoxLayout.addLayout(hBoxLayout1)
        vBoxLayout.addLayout(hBoxLayout2)
        vBoxLayout.addLayout(hBoxLayout3)
        
        #Vbox layoutumu setLayout metoduyla set ediyorum 
        self.setLayout(vBoxLayout)
        
    def okHandler(self):
        a = int(self.lineEditNo.text())
        print(a ** 2)
        

app = QApplication(sys.argv)
mainWindow = MainWindow()
mainWindow.show()
app.exec()
