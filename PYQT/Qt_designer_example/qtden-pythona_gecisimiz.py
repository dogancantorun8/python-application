# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 18:23:05 2021

@author: dogancan
"""

import sys
import qtdesign 
import fruitsdialog

from PyQt5.Qt import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        
        self.uiTest = qtdesign.Ui_MainWindow() #designer dosyamdan nesnemi yaratıyorum
        self.uiTest.setupUi(self) #yarattığım nesneme selfi veriyorum 
        
        self.uiTest.pushButtonOk.clicked.connect(self.pushButtonOkHandler)
        self.uiTest.listWidgetCities.doubleClicked.connect(self.listWidgetDoubleClickedHandler)

    def pushButtonOkHandler(self):
        print(self.uiTest.lineEditName.text())
        print(self.uiTest.lineEditNo.text())

    def listWidgetDoubleClickedHandler(self):
        print(self.uiTest.listWidgetCities.currentItem().text())
    
    def pushButtonCancelClickedHandler(self):
        print('Canceled')

    def openHandler(self):
        print('Open selected')

    def closeHandler(self):
        self.close()

    def fruitsDialogHandler(self):
        fd = FruitsDialog(self)
        if fd.exec() == QDialog.Accepted:
            print('Ok')

class FruitsDialog(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.uiDialog = fruitsdialog.Ui_Dialog()
        self.uiDialog.setupUi(self)

app = QApplication(sys.argv)
mainWindow = MainWindow()
mainWindow.show()
app.exec()

