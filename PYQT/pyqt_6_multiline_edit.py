# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 18:09:44 2021

@author: Asus
"""

#Multiline Text edit ile girdi alabiliyorum 

import sys

from PyQt5.QtWidgets import *
from PyQt5.Qt import *

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(640, 480)

        self.labelName = QLabel('Adı Soyadı', self)
        self.labelName.move(20, 10)

        self.textEdit = QTextEdit(self)
        self.textEdit.setGeometry(5, 5, 630, 430)
        self.textEdit.setFont(QFont('Arial', 16))
        self.textEdit.setStyleSheet('color: red; background-color:yellow')

        self.pushButtonOk = QPushButton('Ok', self)
        self.pushButtonOk.move(300, 450)
        self.pushButtonOk.clicked.connect(self.buttonOkHandler)

    def buttonOkHandler(self):
        with open('pyqt_6_multiline_edit.py') as f:
           self.textEdit.setPlainText(f.read()) 
        #print(self.textEdit.toPlainText())  #edit boxun icine yazılanı almak istersem bu sekilde alabilirim 

app = QApplication(sys.argv)
mainWindow = MainWindow()
mainWindow.show()
app.exec() 


########################### Line edit ve text edit kullanımı 
import sys

from PyQt5.QtWidgets import *
from PyQt5.Qt import *

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(640, 480)

        self.labelName = QLabel('Adı Soyadı', self)
        self.labelName.move(20, 10)

        self.textEdit = QTextEdit(self)
        self.textEdit.setGeometry(5, 5, 630, 350)
        self.textEdit.setFont(QFont('Arial', 16))
        #self.textEdit.setStyleSheet('color: red; background-color:yellow')
        self.textEdit.setLineWrapMode(QTextEdit.NoWrap)

        self.lineEdit = QLineEdit(self)
        self.lineEdit.setGeometry(5, 380, 630, 25)
        self.lineEdit.setFont(QFont('Arial', 16))

        self.pushButtonOk = QPushButton('Ok', self)
        self.pushButtonOk.move(300, 450)
        self.pushButtonOk.clicked.connect(self.buttonOkHandler)

        self.lineEdit.setFocus()

    def buttonOkHandler(self):
        tq = self.textEdit.textCursor()
        tq.movePosition(QTextCursor.End)
        self.textEdit.setTextCursor(tq)
        self.textEdit.insertPlainText(self.lineEdit.text() + '\n')
        self.lineEdit.setFocus()
        self.lineEdit.clear()

app = QApplication(sys.argv)
mainWindow = MainWindow()
mainWindow.show()
app.exec()