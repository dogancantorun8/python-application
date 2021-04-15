# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 19:18:28 2021

@author: doğancan
"""

import sys

from PyQt5.Qt import *

#3 tane slider yerleştirdim 
#3 tane label yerleştirdim 
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(640, 480)
        
        #REd slider tanımlıyorum
        self.sliderRed = QSlider(Qt.Horizontal, self)
        self.sliderRed.setGeometry(20, 20, 300, 30)
        self.sliderRed.setMaximum(255)
        self.sliderRed.setTickPosition(QSlider.TicksBothSides)
        self.sliderRed.valueChanged.connect(self.sliderRedValueChangedHandler)

        font = QFont('Arial', 20)
        
        
        self.labelRed = QLabel('Red 0', self)
        self.labelRed.move(340, 20)
        self.labelRed.resize(150, 30)
        self.labelRed.setFont(font)

        self.sliderGreen = QSlider(Qt.Horizontal, self)
        self.sliderGreen.setGeometry(20, 80, 300, 30)
        self.sliderGreen.setMaximum(255)
        self.sliderGreen.setTickPosition(QSlider.TicksBothSides)
        self.sliderGreen.valueChanged.connect(self.sliderGreenValueChangedHandler)

        self.labelGreen = QLabel('Green 0', self)
        self.labelGreen.move(340, 80)
        self.labelGreen.resize(150, 30)
        self.labelGreen.setFont(font)

        self.sliderBlue = QSlider(Qt.Horizontal, self)
        self.sliderBlue.setGeometry(20, 140, 300, 30)
        self.sliderBlue.setMaximum(255)
        self.sliderBlue.setTickPosition(QSlider.TicksBothSides)

        self.labelBlue = QLabel('Blue 0   ', self)
        self.labelBlue.move(340, 140)
        self.labelBlue.resize(150, 30)
        self.labelBlue.setFont(font)
        self.sliderBlue.valueChanged.connect(self.sliderBlueValueChangedHandler)

        self.labelColor = QLabel(self)
        self.labelColor.setGeometry(200, 230, 200, 200)
        self.labelColor.setStyleSheet('background-color: rgb(0, 0, 0)')

    def sliderRedValueChangedHandler(self, value):
        self.labelRed.setText(f'Red {value}')
        self.labelColor.setStyleSheet(f'background-color: rgb({self.sliderRed.value()}, {self.sliderGreen.value()}, {self.sliderBlue.value()})')

    def sliderGreenValueChangedHandler(self, value):
        self.labelGreen.setText(f'Green {value}')
        self.labelColor.setStyleSheet(f'background-color: rgb({self.sliderRed.value()}, {self.sliderGreen.value()}, {self.sliderBlue.value()})')

    def sliderBlueValueChangedHandler(self, value):
        self.labelBlue.setText(f'Blue {value}')
        self.labelColor.setStyleSheet(f'background-color: rgb({self.sliderRed.value()}, {self.sliderGreen.value()}, {self.sliderBlue.value()})')

app = QApplication(sys.argv)
mainWindow = MainWindow()
mainWindow.show()
app.exec()
