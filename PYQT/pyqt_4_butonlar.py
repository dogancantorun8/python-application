# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 19:43:19 2021

@author:
"""

#Qwidget sınıfından türetilmiş=> QAbstractbutton  altından; 
    #CheckBox,RadioButton,PushButton buradan üretilir

#Push button kullanımı: 
import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.pushButtonOk = QPushButton('Ok', self)
        self.pushButtonOk.move(100, 100)
        self.pushButtonOk.resize(QSize(100, 100))
        self.pushButtonOk.clicked.connect(self.buttonOkHandler)
        self.pushButtonOk.setFont(QFont('Times New Roman', 16))


    def buttonOkHandler(self):
        mb = QMessageBox(None)
        mb.setWindowTitle('Test')
        mb.setText('Are you sure?')
        mb.setStandardButtons(QMessageBox.Yes|QMessageBox.No|QMessageBox.Cancel)
        mb.setDefaultButton(QMessageBox.Cancel)
        mb.setIcon(QMessageBox.Information)
        result = mb.exec()
        if result == QMessageBox.Yes:
            print('Yes')
        elif result == QMessageBox.No:
            print('No')
        else:
            print('Cancel')


app = QApplication(sys.argv)
mainWindow = MainWindow()
mainWindow.show()

#Checkbox ve beamcursor kullanımı(yani o componentin üzerine geldiğimizde cursorun şekli değişiyor)
import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.checkBox = QCheckBox('Printer', self)
        self.checkBox.move(150, 50)
        self.checkBox.setFont(QFont('Times New Roman', 16))
        self.checkBox.setCursor(Qt.CursorShape.SizeAllCursor)

        self.pushButtonOk = QPushButton('Ok', self)
        self.pushButtonOk.move(100, 100)
        self.pushButtonOk.resize(QSize(100, 100))
        self.pushButtonOk.clicked.connect(self.buttonOkHandler)
        self.pushButtonOk.setFont(QFont('Times New Roman', 16))
        self.pushButtonOk.setCursor(Qt.CursorShape.IBeamCursor) #pushbutton uzerine geldiğimizde cursor değişiyor

    def buttonOkHandler(self):
        QMessageBox.about(None, 'Info', 'Checked' if self.checkBox.isChecked() else 'Unchecked')

app = QApplication(sys.argv)
mainWindow = MainWindow()
mainWindow.show()
app.exec()

#Eger 3 konumlu bir checkboxum olsun istersem ve checkboxun durumuna göre işlem yapmak istediğimde aşağıdaki şekilde bir yol izleyebilirim 
import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.checkBox = QCheckBox('Printer', self)
        self.checkBox.move(150, 50)
        self.checkBox.setFont(QFont('Times New Roman', 16))
        self.checkBox.setCursor(Qt.CursorShape.SizeAllCursor)
        self.checkBox.clicked.connect(self.checkBoxClickedHandler)
        self.checkBox.setTristate(True)
        self.checkBox.setCheckState(Qt.CheckState.PartiallyChecked)

        self.pushButtonOk = QPushButton('Ok', self)
        self.pushButtonOk.move(100, 100)
        self.pushButtonOk.resize(QSize(100, 100))
        self.pushButtonOk.clicked.connect(self.buttonOkHandler)
        self.pushButtonOk.setFont(QFont('Times New Roman', 16))
        self.pushButtonOk.setCursor(Qt.CursorShape.IBeamCursor)

    def buttonOkHandler(self):
        state = self.checkBox.checkState()
        if state == Qt.CheckState.Checked:
            print('Checked')
        elif state == Qt.CheckState.Unchecked:
            print('Unchecked')
        elif state == Qt.CheckState.PartiallyChecked:
            print('Indeterminate')




    def checkBoxClickedHandler(self):
        print('Clicked')

app = QApplication(sys.argv)
mainWindow = MainWindow()
mainWindow.show()
app.exec()


#Radio Button Kullanımı
import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.resize(640, 480)

        self.labelTitle = QLabel('Radio Button Uygulaması', self)
        self.labelTitle.move(200, 10)
        self.labelTitle.setFont(QFont('Arial', 20))
        
        #Radio butonlarımı GroupBox üzerinde grupladım
        self.groupBox = QGroupBox('Seçenekler', self)
        self.groupBox.move(10, 10)

        self.radioButtonA = QRadioButton('A', self.groupBox)
        self.radioButtonA.move(20, 40)

        self.radioButtonB = QRadioButton('B', self.groupBox)
        self.radioButtonB.move(20, 65)

        self.radioButtonC = QRadioButton('C', self.groupBox)
        self.radioButtonC.move(20, 90)

        self.radioButtonD = QRadioButton('D', self.groupBox)
        self.radioButtonD.move(20, 115)

        self.radioButtonE = QRadioButton('E', self.groupBox)
        self.radioButtonE.move(20, 140)

        self.pushButtonOk = QPushButton('Ok', self)
        self.pushButtonOk.move(160, 40)
        self.pushButtonOk.resize(QSize(100, 100))
        self.pushButtonOk.clicked.connect(self.buttonOkHandler)
        self.pushButtonOk.setFont(QFont('Times New Roman', 16))

    def buttonOkHandler(self):
        if self.radioButtonA.isChecked():
            print('A')
        elif self.radioButtonB.isChecked():
            print('B')
        elif self.radioButtonC.isChecked():
            print('C')
        elif self.radioButtonD.isChecked():
            print('D')
        elif self.radioButtonE.isChecked():
            print('E')
        else:
            print('Hiçbiri')

app = QApplication(sys.argv)
mainWindow = MainWindow()
mainWindow.show()
app.exec()
