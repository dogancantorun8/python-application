
#kullanıcıdan girdi almak için aşağıdaki şekilde dizayn edebilirim 


import sys

from PyQt5.QtWidgets import *
from PyQt5.Qt import *

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.labelName = QLabel('Adi Soyadı', self)
        self.labelName.move(20, 10)

        self.lineEditName = QLineEdit(self)
        self.lineEditName.setGeometry(20, 25, 200, 20)
        self.lineEditName.setPlaceholderText('Adinizi ve soyadinizi giriniz.')


        self.labelNo = QLabel('No', self)
        self.labelNo.move(20, 50)

        self.lineEditNo = QLineEdit(self)
        self.lineEditNo.setGeometry(20, 65, 200, 20)

        self.pushButtonOk = QPushButton('Ok', self)
        self.pushButtonOk.move(140, 110)
        self.pushButtonOk.clicked.connect(self.buttonOkHandler)

        self.pushButtonCancel = QPushButton('Cancel', self)
        self.pushButtonCancel.move(230, 110)
        self.pushButtonCancel.clicked.connect(lambda: self.close()) #cancel butona basıldıgında pencereyi kapatıyor
        
    def buttonOkHandler(self):
        print(self.lineEditName.text()) #edit boxa yazılanı alıyorum
        print(self.lineEditNo.text())   #edit boxa yazılanı alıyorum
        #QMessageBox.information(None, 'Info', self.lineEditName.text() + '\n' + self.lineEditNo.text())
        self.lineEditName.setCursorPosition(len(self.lineEditName.text()))
        self.lineEditName.insert('xxxxx') # lineedite yazı insert etmek için kullanıyorum =>>

app = QApplication(sys.argv)
mainWindow = MainWindow()
mainWindow.show()
app.exec()