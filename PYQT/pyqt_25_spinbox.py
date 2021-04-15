# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 20:42:57 2021

@author: dogancan
"""


#spinbox yaratma ve spinboxta seçilen değeri alma: 
import sys

from PyQt5.Qt import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(640, 480)
        self.setFont(QFont('Arial', 14))

        self.spinBox = QSpinBox(self)
        self.spinBox.setGeometry(50, 50, 100, 30) 
        self.spinBox.setMaximum(10)
        
        self.pushButtonOk = QPushButton('Ok', self)
        self.pushButtonOk.move(50, 100)
        self.pushButtonOk.clicked.connect(self.pushButtonOkHandler)

    def pushButtonOkHandler(self):
        print(self.spinBox.value()) #spinboxtaki değeri alabiliyorum 


app = QApplication(sys.argv)
mainWindow = MainWindow()
mainWindow.show()
app.exec()

####Date formatında spinbox ile işlem yapıp değerini alma islemi: 
import sys

from PyQt5.Qt import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(640, 480)
        self.setFont(QFont('Arial', 14))

        self.dateTimeEdit = QDateTimeEdit(self)
        self.dateTimeEdit.move(50, 50)
        self.dateTimeEdit.resize(200, 30)

        self.pushButtonOk = QPushButton('Ok', self)
        self.pushButtonOk.move(50, 100)
        self.pushButtonOk.clicked.connect(self.pushButtonOkHandler)

    def pushButtonOkHandler(self):
        qdate = self.dateTimeEdit.date()
        print('{}/{}/{}'.format(qdate.day(), qdate.month(), qdate.year()))


app = QApplication(sys.argv)
mainWindow = MainWindow()
mainWindow.show()
app.exec()
####tarihi alıp yazdırmak :
import sys

from PyQt5.Qt import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(640, 480)
        self.setFont(QFont('Arial', 14))

        self.dateTimeEdit = QDateTimeEdit(self)
        self.dateTimeEdit.move(50, 50)
        self.dateTimeEdit.resize(200, 30)
        #self.dateTimeEdit.setDate(QDate.currentDate())
        #self.dateTimeEdit.setTime(QTime.currentTime())
        self.dateTimeEdit.setDateTime(QDateTime(2010, 12, 24, 12, 43, 54))

        self.pushButtonOk = QPushButton('Ok', self)
        self.pushButtonOk.move(50, 100)
        self.pushButtonOk.clicked.connect(self.pushButtonOkHandler)

    def pushButtonOkHandler(self):
        qdate = self.dateTimeEdit.date()
        print('{}/{}/{}'.format(qdate.day(), qdate.month(), qdate.year()))
        print(qdate.toString())

app = QApplication(sys.argv)
mainWindow = MainWindow()
mainWindow.show()
app.exec()