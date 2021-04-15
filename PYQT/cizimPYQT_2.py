# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 19:22:45 2021

@author: dogancan
"""


#sinüs eğrisini çizmek istersek; 
import sys
from PyQt5.Qt import *
import math

XORG = 640 // 2
YORG = 480 // 2
XSCALE = 50
YSCALE = 100

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(640, 480)

    def paintEvent(self, pe):
        painter = QPainter(self)
        painter.drawLine(320, 0, 320, 480)
        painter.drawLine(0, 240, 640, 240)

        poly = QPolygon()

        x = -2 * math.pi
        while x < 2 * math.pi:
            y = math.sin(x)
            poly.append(QPoint(XORG + int(x * XSCALE), YORG - int(y * YSCALE)))
            x += 0.1

        painter.drawPolyline(poly)

app = QApplication(sys.argv)
mainWindow = MainWindow()
mainWindow.show()
app.exec()
