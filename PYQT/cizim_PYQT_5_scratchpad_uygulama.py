# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 17:28:19 2021

@author: dogancan
"""

#Scratchpad uygulaması: 
import sys
from PyQt5.Qt import *

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1024, 768)
        self.currentLine = None
        self.lines = []
        self.drawFlag = False

    def paintEvent(self, pe):
        painter = QPainter(self)
        painter.setRenderHints(QPainter.Antialiasing)

        pen = QPen()
        pen.setWidth(3)
        painter.setPen(pen)

        for line in self.lines:
            painter.drawPolyline(line)

        if self.currentLine != None:
            painter.drawPolyline(self.currentLine)

    def mousePressEvent(self, me):
        self.drawFlag = True
        self.currentLine = QPolygon()
        self.currentLine.append(me.pos())
        self.update()

    def mouseReleaseEvent(self, me):
        self.drawFlag = False
        self.lines.append(self.currentLine)

    def mouseMoveEvent(self, me):
        self.currentLine.append(me.pos())
        self.update()


app = QApplication(sys.argv)
mainWindow = MainWindow()
mainWindow.show()
app.exec() 
