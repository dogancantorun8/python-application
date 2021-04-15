# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 18:27:19 2021

@author: doğancan
"""


#slider kullanımı:slider ses verme işleminde sağa sola çekip sesi yükselttiğimiz komponent 
#slider default oryantasyon olarak düşeydedir. 


###basic bir slider tanımlama
import sys

from PyQt5.Qt import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(640, 480)

        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.move(50, 50)
        self.slider.resize(200, 30)


app = QApplication(sys.argv)
mainWindow = MainWindow()
mainWindow.show()
app.exec()

###Slider ve buton kullanımı :value ile slider değerini alabiliyoruz slider üstünde visible hale getiriyoruz
#slider bir aralığı 100 parçaya böler her zaman  
import sys

from PyQt5.Qt import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(640, 480)

        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.move(50, 50)
        self.slider.resize(400, 30)
        self.slider.setTickPosition(QSlider.TicksBothSides)
        self.slider.setTickInterval(5)

        self.pushButtonOk = QPushButton('Ok', self)
        self.pushButtonOk.setGeometry(300, 350, 100, 100)
        self.pushButtonOk.clicked.connect(self.pushButtonOkHandler)


    def pushButtonOkHandler(self):
        print(self.slider.value())


app = QApplication(sys.argv)
mainWindow = MainWindow()
mainWindow.show()
app.exec()

####slider sinyalini alıp işleme :  
#slideri bıraktığımız yerde alıp işleme yada slider hareketliyken sinyali işleme şeklinde 2 eventi işleyebiliriz 

import sys

from PyQt5.Qt import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(640, 480)

        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.move(50, 50)
        self.slider.resize(400, 30)
        self.slider.setTickPosition(QSlider.TicksBothSides)
        self.slider.setTickInterval(5)
        self.slider.setMaximum(200)
        self.slider.setMinimum(50)
        self.slider.sliderMoved.connect(self.sliderMovedHandler)
        self.slider.valueChanged.connect(self.sliderValueChangedHandler)
        self.slider.sliderReleased.connect(self.sliderReleasedHandler)

        self.pushButtonOk = QPushButton('Ok', self)
        self.pushButtonOk.setGeometry(300, 350, 100, 100)
        self.pushButtonOk.clicked.connect(self.pushButtonOkHandler)

    def pushButtonOkHandler(self):
        print(self.slider.value())

    def sliderMovedHandler(self):
        print('SLIDER MOVED')

    def sliderValueChangedHandler(self):
        print('VALUE CHANGED')

    def sliderReleasedHandler(self): #sliderin bırakıldığı yerdeki değerini almak için bu handler kullanılıyor
        print('SLIDER RELEASED')

app = QApplication(sys.argv)
mainWindow = MainWindow()
mainWindow.show()
app.exec()


