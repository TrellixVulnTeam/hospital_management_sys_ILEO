# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ayo_btn.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_window(object):
    def setupUi(self, window):
        window.setObjectName("window")
        window.resize(400, 300)
        window.setToolTip("")
        window.setToolTipDuration(1)
        window.setAutoFillBackground(False)
        window.setStyleSheet(".QWidget#window {background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #95CD41, stop:1 #F6D860)}")
        self.pushButton = QtWidgets.QPushButton(window)
        self.pushButton.setGeometry(QtCore.QRect(120, 140, 121, 51))
        self.pushButton.setStyleSheet("backgound-color: default")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(window)
        self.label.setGeometry(QtCore.QRect(120, 60, 121, 41))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(window)
        QtCore.QMetaObject.connectSlotsByName(window)

    def retranslateUi(self, window):
        _translate = QtCore.QCoreApplication.translate
        window.setWindowTitle(_translate("window", "MyWindow"))
        self.pushButton.setText(_translate("window", "Click Moi"))
        self.label.setText(_translate("window", "Ayo is a beech"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QWidget()
    ui = Ui_window()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())