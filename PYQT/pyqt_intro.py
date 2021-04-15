# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 19:17:16 2021

@author: Dogancan Torun
"""


#QT bir C++ kütüphanesidir. 
#QT crossplatform bir librarydir.[PYQT de crossplatform çalışabiliyors]
# from PyQt5.QtWidgets import * =>bu anatosyonla Q ile başlayan sınıfların QT sınıfı olduğunu anlayabiliriz
#Arayüz elemanlarının hepsi QWidgettan türemiş.

##İskelet programım
import sys
from PyQt5.QtWidgets import * # * kullanmak bana "." operatörünü kullanmadan erişmek için yazdım.
class MainWindow(QWidget): #Qwidgetten bir sınıf türetip methodlarımı ondan oluşturuyorum
    def __init__(self):
        super().__init__()

app = QApplication(sys.argv) #QApplication sınıfından nesne mutlaka yaratmalıyız.bunu yaratırken komut satırı argümanlarınıda alabilmesi için içine yazıyoruz
mainWindow = MainWindow() #^Mesaj döngüsüne girmeden ana penceremi her zaman yaratmalıyım
mainWindow.show()
app.exec() #mesaj döngüsünü "exec" içerisinde koşturuyoruz."exec" metodu QApplication sınıfının bir metodudur.PyQt kodu ana pencere kapanırsa biter yani kapanana kadar kod execdedir

###Eğer bir push button yaratmak istersem:
import sys

from PyQt5.QtWidgets import *

class MainWindow(QWidget):
    def __init__(self): #buradaki self=mainwindow demek yani herşeyi mainwindow üzerine kuruyorum 
        super().__init__()
        self.pushButtonOk = QPushButton('Ok', self) #burada self yazarak butonun üst penceresini main window yapmıs oldum
        self.pushButtonOk.move(50,50) #konum ayarını yapıyorum

        #2.butonum
        self.pushButtonCancel = QPushButton('Cancel', self)
        self.pushButtonCancel.move(150, 50)


app = QApplication(sys.argv)
mainWindow = MainWindow()
mainWindow.show()
app.exec() 

##Push buton konumlandırmak istersem:Pos ile nesne şeklinde konumu alabiliyorum
##Componentin width-height almak istersem size kullanabilirim ama dönüşte bir nesne alırım her ikisinide almış olurum.
import sys

from PyQt5.QtWidgets import *

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.pushButtonOk = QPushButton('Ok', self)
        self.pushButtonOk.move(50, 50)

        print(self.pushButtonOk.x(), self.pushButtonOk.y())
        print(self.pushButtonOk.pos())

        print(self.pushButtonOk.width())
        print(self.pushButtonOk.height())

        print(self.pushButtonOk.size())


app = QApplication(sys.argv)
mainWindow = MainWindow()
mainWindow.show()
app.exec()

##Frame size bulmak :Borderlar dahil penceremizin alanını veriyor
import sys

from PyQt5.QtWidgets import *

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.pushButtonOk = QPushButton('Ok', self)
        self.pushButtonOk.move(50, 50)

        print(self.width(), self.height())

        print(self.frameSize().width(), self.frameSize().height())


app = QApplication(sys.argv)
mainWindow = MainWindow()
mainWindow.show()
app.exec()


##Geometry kullanımı: 
import sys
from PyQt5.QtWidgets import *
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.pushButtonOk = QPushButton('Ok', self)
        self.pushButtonOk.move(50, 50)

        result = self.pushButtonOk.frameGeometry()
        print(result.x(), result.y(), result.width(), result.height())
        print(type(result))

app = QApplication(sys.argv)
mainWindow = MainWindow()
mainWindow.show()
app.exec()

##Bir butonun boyutunu değiştirmek  istersem: 
import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.pushButonOk = QPushButton('Ok', self)
        self.pushButonOk.move(QPoint(100, 50))
        self.pushButonOk.resize(100, 100) #resize ile butonumun boyutlarını değiştireceğim 


app = QApplication(sys.argv)
mainWindow = MainWindow()
mainWindow.show()
app.exec()

###QSize yardımıyla buton boyutunu değiştirmek ve buton ismini-anapencere ismini değiştirmek : 

import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class MainWindow(QWidget):
    def __init__(self):
        super().__init__() 
        
        self.setWindowTitle('Sample Window') #anapencere ismini değiştirmek
        print(self.windowTitle()) #anapencere ismini almak istersem

        
        self.pushButtonOk = QPushButton('Ok', self)
        self.pushButtonOk.move(100, 100)
        self.pushButtonOk.resize(QSize(100, 100)) 
        
        text = self.pushButtonOk.text() ##Bir butonun üzerindeki yazıyı değiştirmek istersem set ile yapıyorum 
        print(text)
        self.pushButtonOk.setText('New Text')



app = QApplication(sys.argv)
mainWindow = MainWindow()
mainWindow.show()
app.exec()


