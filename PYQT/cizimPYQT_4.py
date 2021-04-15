# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 17:10:29 2021

@author: dogancan
"""


#cizimlerde Antialising : kullanıcıya çizimlerin daha pürüzsüz gözükmesini istersek antialiasing yapacağız. 
import sys
from PyQt5.Qt import *

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

    def paintEvent(self, pe):
        painter = QPainter(self)
        pen = QPen()
        pen.setWidth(5)
        painter.setPen(pen)

        painter.drawLine(0, 0, 50, 50)
        painter.drawEllipse(100, 100, 100, 100)
        
        #antialiasing yapılmış nesnelerim 
        painter.setRenderHints(QPainter.Antialiasing)
        painter.drawLine(100, 0, 200, 100)
        painter.drawEllipse(200, 200, 100, 100)

app = QApplication(sys.argv)
mainWindow = MainWindow()
mainWindow.show()
app.exec()



