# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 20:09:42 2021

@author: dogancan
"""

#Progressbar yaratma : 
import sys

from PyQt5.Qt import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(640, 480)

        self.progressBar = QProgressBar(self)
        self.progressBar.setGeometry(20, 20, 600, 30)

app = QApplication(sys.argv)
mainWindow = MainWindow()
mainWindow.show()
app.exec()

##push butona basıldıkça progressbarda ilerleme olsun istersek 
#düğmeye batığımda bir thread ile bunu koda veriyorum mesaj döngümün donmasını engellemek amacıyla  
import sys

import time
import threading
from PyQt5.Qt import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(640, 480)

        self.progressBar = QProgressBar(self)
        self.progressBar.setGeometry(20, 20, 600, 30)

        self.pushButtonOk = QPushButton('Download', self)
        self.pushButtonOk.move(300, 400)
        self.pushButtonOk.clicked.connect(self.pushButtonOkHandler)

    def pushButtonOkHandler(self):
        self.thread = threading.Thread(target=self.threadProc)
        self.thread.start()
        self.pushButtonOk.setEnabled(False)

    def threadProc(self):
        for i in range(101):
            self.progressBar.setValue(i)
            time.sleep(0.1)
        self.pushButtonOk.setEnabled(True)


app = QApplication(sys.argv)
mainWindow = MainWindow()
mainWindow.show()
app.exec()


