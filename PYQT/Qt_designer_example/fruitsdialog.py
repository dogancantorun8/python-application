# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fruitsdialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(402, 319)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.toolButtonApple = QtWidgets.QToolButton(Dialog)
        self.toolButtonApple.setGeometry(QtCore.QRect(10, 30, 91, 51))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Icons/Apple.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButtonApple.setIcon(icon)
        self.toolButtonApple.setIconSize(QtCore.QSize(64, 64))
        self.toolButtonApple.setCheckable(True)
        self.toolButtonApple.setObjectName("toolButtonApple")
        self.toolButtonCherry = QtWidgets.QToolButton(Dialog)
        self.toolButtonCherry.setGeometry(QtCore.QRect(120, 30, 91, 51))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../Icons/Cherry.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButtonCherry.setIcon(icon1)
        self.toolButtonCherry.setIconSize(QtCore.QSize(64, 64))
        self.toolButtonCherry.setCheckable(True)
        self.toolButtonCherry.setObjectName("toolButtonCherry")
        self.toolButtonGreppe = QtWidgets.QToolButton(Dialog)
        self.toolButtonGreppe.setGeometry(QtCore.QRect(230, 30, 91, 51))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../Icons/Grape.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButtonGreppe.setIcon(icon2)
        self.toolButtonGreppe.setIconSize(QtCore.QSize(64, 64))
        self.toolButtonGreppe.setCheckable(True)
        self.toolButtonGreppe.setObjectName("toolButtonGreppe")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.toolButtonApple.setText(_translate("Dialog", "..."))
        self.toolButtonCherry.setText(_translate("Dialog", "..."))
        self.toolButtonGreppe.setText(_translate("Dialog", "..."))
