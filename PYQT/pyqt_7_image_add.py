# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 19:17:21 2021

@author: Dogancan Torun
"""


#Resim ekleme islemi:QPixmap sınıfının kullanıyorum 
import sys

from PyQt5.QtWidgets import *
from PyQt5.Qt import *

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.labelName = QLabel('Adı Soyadı', self)
        self.labelName.move(20, 10)

        self.lineEditName = QLineEdit(self)
        self.lineEditName.setGeometry(20, 25, 200, 20)
        self.lineEditName.textChanged.connect(self.nameTextChangedHandler)

        self.labelNo = QLabel('No', self)
        self.labelNo.move(20, 50)

        self.lineEditNo = QLineEdit(self)
        self.lineEditNo.setGeometry(20, 65, 200, 20)

        self.labelImage = QLabel(self)
        self.labelImage.setGeometry(240, 10, 100, 90)
        self.labelImage.setStyleSheet('background-color: yellow')

        pm = QPixmap('images.jpg') #resmi okuyorum
        scaledPm = pm.scaled(100, 90) #imgemle aynı boyutlarda scale ediyorum
        self.labelImage.setPixmap(scaledPm) #♦fotoğrafı arayuzume set ediyorum

        self.pushButtonOk = QPushButton('Ok', self)
        self.pushButtonOk.move(140, 110)
        self.pushButtonOk.clicked.connect(self.buttonOkHandler)

        self.pushButtonCancel = QPushButton('Cancel', self)
        self.pushButtonCancel.move(230, 110)
        self.pushButtonCancel.clicked.connect(lambda: self.close())

    def buttonOkHandler(self):
        print(self.lineEditName.text())
        print(self.lineEditNo.text())
        self.lineEditName.setCursorPosition(len(self.lineEditName.text()))

# =============================================================================
#     def nameTextChangedHandler(self, s):
#         if len(s) > 10:
#             self.lineEditName.resize(300, 25)
# =============================================================================

app = QApplication(sys.argv)
mainWindow = MainWindow()
mainWindow.show()
app.exec()