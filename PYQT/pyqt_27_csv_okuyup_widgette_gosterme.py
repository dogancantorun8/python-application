# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 17:22:23 2021

@author: dogancan 
"""


#bir dosyadan veri okuyup arayüzde anlamlandırma 
#table widget 
import sys
import csv

from PyQt5.Qt import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(640, 480)
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setGeometry(10, 10, 620, 400)
        self.tableWidget.setColumnCount(3)

        #self.tableWidget.setHorizontalHeaderLabels(['Yıl', 'Ülke', 'Şampiyon'])

        font = QFont('Arial', 12)
        font.setBold(True)

        header0 = QTableWidgetItem('Yıl')
        header0.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, header0)

        header1 = QTableWidgetItem('Ülke')
        header1.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, header1)

        header2= QTableWidgetItem('Şampiyon')
        header2.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, header2)
        self.tableWidget.cellDoubleClicked.connect(self.cellDoubleClickedHandler)

        with open('WorldCups.csv') as f:
            reader = csv.reader(f)
            next(reader)
            for index, row in enumerate(reader):
                self.tableWidget.insertRow(index)

                twi1 = QTableWidgetItem(row[0])
                twi1.setForeground(QBrush(QColor(255, 0, 0)))
                twi1.setFont(QFont('Arial', 12))

                twi2 = QTableWidgetItem(row[1])
                twi2.setFont(QFont('Arial', 12))
                twi2.setForeground(QBrush(QColor(0, 0, 255)))
                twi2.setBackground(QBrush(QColor(255, 255, 0)))

                twi3 = QTableWidgetItem(row[2])
                twi3.setFont(QFont('Arial', 12))
                twi3.setForeground(QBrush(QColor(0, 255, 0)))


                self.tableWidget.setItem(index, 0, twi1)
                self.tableWidget.setItem(index, 1, twi2)
                self.tableWidget.setItem(index, 2, twi3)

    def cellDoubleClickedHandler(self, row, col):
        twi = self.tableWidget.item(row, col)
        print(twi.text())




app = QApplication(sys.argv)
mainWindow = MainWindow()
mainWindow.show()
app.exec()