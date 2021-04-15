import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.checkBox = QCheckBox('Printer', self)
        self.checkBox.move(150, 50)
        self.checkBox.setFont(QFont('Times New Roman', 16))
        self.checkBox.setCursor(Qt.CursorShape.SizeAllCursor)
        self.checkBox.clicked.connect(self.checkBoxClickedHandler)
        self.checkBox.setTristate(True)
        self.checkBox.setCheckState(Qt.CheckState.PartiallyChecked)

        self.pushButtonOk = QPushButton('Ok', self)
        self.pushButtonOk.move(100, 100)
        self.pushButtonOk.resize(QSize(100, 100))
        self.pushButtonOk.clicked.connect(self.buttonOkHandler)
        self.pushButtonOk.setFont(QFont('Times New Roman', 16))
        self.pushButtonOk.setCursor(Qt.CursorShape.IBeamCursor)

    def buttonOkHandler(self):
        state = self.checkBox.checkState()
        if state == Qt.CheckState.Checked:
            print('Checked')
        elif state == Qt.CheckState.Unchecked:
            print('Unchecked')
        elif state == Qt.CheckState.PartiallyChecked:
            print('Indeterminate')




    def checkBoxClickedHandler(self):
        print('Clicked')

app = QApplication(sys.argv)
mainWindow = MainWindow()
mainWindow.show()
app.exec()