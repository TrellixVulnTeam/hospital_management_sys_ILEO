# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'label_lineedit.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(668, 385)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setObjectName("groupBox")
        self.click_btn = QtWidgets.QPushButton(self.groupBox)
        self.click_btn.setGeometry(QtCore.QRect(30, 120, 93, 28))
        self.click_btn.setObjectName("click_btn")
        self.click_btn.clicked.connect(self.btn_click)
        self.widget = QtWidgets.QWidget(self.groupBox)
        self.widget.setGeometry(QtCore.QRect(30, 30, 183, 24))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.name_label = QtWidgets.QLabel(self.widget)
        self.name_label.setObjectName("name_label")
        self.horizontalLayout.addWidget(self.name_label)
        self.name_field = QtWidgets.QLineEdit(self.widget)
        self.name_field.setObjectName("name_field")
        self.horizontalLayout.addWidget(self.name_field)
        self.widget1 = QtWidgets.QWidget(self.groupBox)
        self.widget1.setGeometry(QtCore.QRect(30, 70, 181, 24))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.email_label = QtWidgets.QLabel(self.widget1)
        self.email_label.setObjectName("email_label")
        self.horizontalLayout_2.addWidget(self.email_label)
        self.email_field = QtWidgets.QLineEdit(self.widget1)
        self.email_field.setObjectName("email_field")
        self.horizontalLayout_2.addWidget(self.email_field)
        self.horizontalLayout_3.addWidget(self.groupBox)
        self.output_label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(10)
        self.output_label.setFont(font)
        self.output_label.setAlignment(QtCore.Qt.AlignCenter)
        self.output_label.setObjectName("output_label")
        self.horizontalLayout_3.addWidget(self.output_label)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "User details"))
        self.click_btn.setText(_translate("Form", "Click"))
        self.name_label.setText(_translate("Form", "Name:"))
        self.email_label.setText(_translate("Form", "Email:"))
        self.output_label.setText(_translate("Form", "TextLabel"))

    def btn_click(self):
        name = self.name_field.text()
        email = self.email_field.text()

        if (name != '') and (email != ''):
            out_text = f'{name} has email {email}'
            self.output_label.setText(out_text)
            self.name_field.setText('')
            self.email_field.setText('')
            self.name_field.setFocus()
        elif name=='':
            self.name_field.setFocus()
        elif email == '':
            self.email_field.setFocus()




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())