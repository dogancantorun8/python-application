import sys

from PyQt5.QtWidgets import *
from PyQt5.Qt import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(640, 480)

        self.filePopup = QMenu('File', self)  #File pop  ekliyorum
        self.menuBar().addMenu(self.filePopup)

        self.editPopup = self.menuBar().addMenu('Edit') #2. yöntem Edit popup  ekliyorum 

        self.filePopup.addAction('&Open')
        self.filePopup.addAction('&Close')

        self.editPopup.addAction('&Cut')
        self.editPopup.addAction('&Copy')
        self.editPopup.addAction('&Paste')

app = QApplication(sys.argv)
mainWindow = MainWindow()
mainWindow.show()
app.exec()

