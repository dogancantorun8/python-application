# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 18:18:11 2021

@author: dogancan Torun
"""


#Diyalog pencereleri iki şekilde olur #Arka tarafla etkileşemeyen,modal ,etkileşemeyen modless olarak adlandırılır 
#Bir Gui üzerinde modal ve modless tasarımı yapacağım  
#Ana menü üzerinde her iki  modeli inşa edeceğim 
#Qdialogdan sınıf türetip o sınıftan nesne yaratıp exec ile bunu çağırmalıyız. 
import sys

from PyQt5.Qt import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(640, 480)
        self.setFont(QFont('Arial', 12))

        dialogPopup = QMenu('Dialog', self)
        self.modalAction = dialogPopup.addAction('Modal...')
        self.modalAction.setFont(QFont('Arial', 12))
        self.modalAction.setShortcut('Ctrl+D')
        self.modalAction.triggered.connect(self.modalActionHandler)
        self.menuBar().addMenu(dialogPopup)

    def modalActionHandler(self):
        mmd = MyModalDialog(self)
        if mmd.exec() == QDialog.Accepted:
            name = mmd.lineEditName.text()
            no = mmd.lineEditNo.text()

            QMessageBox.information(self, 'Info', name + '\n' + no)

class MyModalDialog(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.resize(370, 120)

        self.labelName = QLabel('Adı Soyadı:', self)
        self.labelName.move(10, 10)
        self.labelName.move(10, 10)

        self.lineEditName = QLineEdit(self)
        self.lineEditName.move(100, 10)

        self.labelNo = QLabel('No:', self)
        self.labelNo.move(10, 40)

        self.lineEditNo = QLineEdit(self)
        self.lineEditNo.move(100, 40)

        self.pushButtonOk = QPushButton('Ok', self)
        self.pushButtonOk.clicked.connect(self.pushButtonOkHandler)
        self.pushButtonOk.setGeometry(150, 80, 70, 25)

        self.pushButtonCancel = QPushButton('Cancel', self)
        self.pushButtonCancel.clicked.connect(self.pushButtonCancelHandler)
        self.pushButtonCancel.setGeometry(230, 80, 70, 25)

    def pushButtonOkHandler(self):
        self.done(QDialog.Accepted)

    def pushButtonCancelHandler(self):
        self.done(QDialog.Rejected)

app = QApplication(sys.argv)
mainWindow = MainWindow()
mainWindow.show()
app.exec()