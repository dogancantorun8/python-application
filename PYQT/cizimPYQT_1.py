# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 18:36:06 2021

@author: dogancan
"""
 
##Tüm çizim elemanları Qpainter sınıfında herhangi bir çizim için Qpainter kullanmalıyız 
 


import sys
from PyQt5.Qt import *

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

    def paintEvent(self, pe):
        painter = QPainter(self)
        painter.drawLine(0, 0, 50, 50)
        painter.drawEllipse(200, 200, 100, 100)
        painter.drawPie(200, 50, 100, 100, 0, 16 * 90)
        painter.drawArc(320, 50, 100, 100, 0, 16 * 90)
        painter.drawRect(430, 50, 200, 100)

        poly = QPolygon()
        poly.append(QPoint(100, 100))
        poly.append(QPoint(200, 150))
        poly.append(QPoint(200, 350))
        painter.drawPolygon(poly)


app = QApplication(sys.argv)
mainWindow = MainWindow()
mainWindow.show()
app.exec()

##########3