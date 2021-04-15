# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 20:07:12 2021

@author: dogancan
"""

#kalem değiştirme ve özellik ekleme 

import sys
from PyQt5.Qt import *

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(640, 480)

    def paintEvent(self, pe):
        painter = QPainter(self)
        pen = QPen(Qt.red, 5, Qt.SolidLine)
        painter.setPen(pen)
        painter.drawLine(100, 100, 500, 100)

        pen.setColor(Qt.blue)
        painter.setPen(pen)

        painter.drawEllipse(100, 150, 100, 100)

        brush = QBrush(Qt.yellow)
        painter.fillRect(100, 300, 100, 100, brush)
        painter.drawRect(100, 300, 100, 100)

app = QApplication(sys.argv)
mainWindow = MainWindow()
mainWindow.show()
app.exec()

