# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'general_in_tab.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(984, 641)
        #
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        #
        self.tab_one = QtWidgets.QWidget()
        self.tab_one.setObjectName("tab_one")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.tab_one)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.data_category = QtWidgets.QLabel(self.tab_one)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.data_category.setFont(font)
        self.data_category.setObjectName("data_category")
        self.verticalLayout.addWidget(self.data_category)
        self.data_category_list = QtWidgets.QListWidget(self.tab_one)
        self.data_category_list.setObjectName("data_category_list")
        item = QtWidgets.QListWidgetItem()
        self.data_category_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.data_category_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.data_category_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.data_category_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.data_category_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.data_category_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.data_category_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.data_category_list.addItem(item)
        self.verticalLayout.addWidget(self.data_category_list)
        self.horizontalLayout_7.addLayout(self.verticalLayout)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.data_category_options = QtWidgets.QLabel(self.tab_one)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.data_category_options.sizePolicy().hasHeightForWidth())
        self.data_category_options.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.data_category_options.setFont(font)
        self.data_category_options.setObjectName("data_category_options")
        self.verticalLayout_2.addWidget(self.data_category_options)
        self.data_category_options_list = QtWidgets.QListWidget(self.tab_one)
        self.data_category_options_list.setObjectName("data_category_options_list")
        item = QtWidgets.QListWidgetItem()
        self.data_category_options_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.data_category_options_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.data_category_options_list.addItem(item)
        self.verticalLayout_2.addWidget(self.data_category_options_list)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.data_id = QtWidgets.QLabel(self.tab_one)
        self.data_id.setMinimumSize(QtCore.QSize(100, 0))
        self.data_id.setMaximumSize(QtCore.QSize(100, 16777215))
        self.data_id.setObjectName("data_id")
        self.horizontalLayout.addWidget(self.data_id)
        self.data_id_entry = QtWidgets.QLineEdit(self.tab_one)
        self.data_id_entry.setObjectName("data_id_entry")
        self.horizontalLayout.addWidget(self.data_id_entry)
        self.edit_change_btn = QtWidgets.QPushButton(self.tab_one)
        self.edit_change_btn.setObjectName("edit_change_btn")
        self.horizontalLayout.addWidget(self.edit_change_btn)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.description = QtWidgets.QLabel(self.tab_one)
        self.description.setMinimumSize(QtCore.QSize(100, 0))
        self.description.setMaximumSize(QtCore.QSize(100, 16777215))
        self.description.setObjectName("description")
        self.horizontalLayout_2.addWidget(self.description)
        self.description_entry = QtWidgets.QLineEdit(self.tab_one)
        self.description_entry.setObjectName("description_entry")
        self.horizontalLayout_2.addWidget(self.description_entry)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.parent_data = QtWidgets.QLabel(self.tab_one)
        self.parent_data.setMinimumSize(QtCore.QSize(100, 0))
        self.parent_data.setMaximumSize(QtCore.QSize(100, 16777215))
        self.parent_data.setObjectName("parent_data")
        self.horizontalLayout_3.addWidget(self.parent_data)
        self.parent_data_options = QtWidgets.QComboBox(self.tab_one)
        self.parent_data_options.setObjectName("parent_data_options")
        self.horizontalLayout_3.addWidget(self.parent_data_options)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.status = QtWidgets.QLabel(self.tab_one)
        self.status.setMinimumSize(QtCore.QSize(100, 0))
        self.status.setMaximumSize(QtCore.QSize(100, 16777215))
        self.status.setObjectName("status")
        self.horizontalLayout_4.addWidget(self.status)
        self.status_options = QtWidgets.QComboBox(self.tab_one)
        self.status_options.setObjectName("status_options")
        self.horizontalLayout_4.addWidget(self.status_options)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.locked = QtWidgets.QLabel(self.tab_one)
        self.locked.setMinimumSize(QtCore.QSize(100, 0))
        self.locked.setMaximumSize(QtCore.QSize(100, 16777215))
        self.locked.setObjectName("locked")
        self.horizontalLayout_5.addWidget(self.locked)
        self.locked_options = QtWidgets.QComboBox(self.tab_one)
        self.locked_options.setObjectName("locked_options")
        self.horizontalLayout_5.addWidget(self.locked_options)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.save_btn = QtWidgets.QPushButton(self.tab_one)
        self.save_btn.setObjectName("save_btn")
        self.horizontalLayout_6.addWidget(self.save_btn)
        self.clear_btn = QtWidgets.QPushButton(self.tab_one)
        self.clear_btn.setObjectName("clear_btn")
        self.horizontalLayout_6.addWidget(self.clear_btn)
        self.close_btn = QtWidgets.QPushButton(self.tab_one)
        self.close_btn.setObjectName("close_btn")
        self.horizontalLayout_6.addWidget(self.close_btn)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.horizontalLayout_7.addLayout(self.verticalLayout_4)
        self.tabWidget.addTab(self.tab_one, "")
        self.tab_two = QtWidgets.QWidget()
        self.tab_two.setObjectName("tab_two")
        self.tabWidget.addTab(self.tab_two, "")
        self.verticalLayout_5.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 984, 26))
        self.menubar.setObjectName("menubar")
        self.menuDo = QtWidgets.QMenu(self.menubar)
        self.menuDo.setObjectName("menuDo")
        self.menuThat = QtWidgets.QMenu(self.menubar)
        self.menuThat.setObjectName("menuThat")
        self.menuStuff = QtWidgets.QMenu(self.menubar)
        self.menuStuff.setObjectName("menuStuff")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuDo.menuAction())
        self.menubar.addAction(self.menuThat.menuAction())
        self.menubar.addAction(self.menuStuff.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.data_category.setText(_translate("MainWindow", "Data Category"))
        __sortingEnabled = self.data_category_list.isSortingEnabled()
        self.data_category_list.setSortingEnabled(False)
        item = self.data_category_list.item(0)
        item.setText(_translate("MainWindow", "Account Status"))
        item = self.data_category_list.item(1)
        item.setText(_translate("MainWindow", "Admit Type"))
        item = self.data_category_list.item(2)
        item.setText(_translate("MainWindow", "Arrival Mode"))
        item = self.data_category_list.item(3)
        item.setText(_translate("MainWindow", "Bank Account Type"))
        item = self.data_category_list.item(4)
        item.setText(_translate("MainWindow", "Billing Method"))
        item = self.data_category_list.item(5)
        item.setText(_translate("MainWindow", "Block Details"))
        item = self.data_category_list.item(6)
        item.setText(_translate("MainWindow", "Blood Group"))
        item = self.data_category_list.item(7)
        item.setText(_translate("MainWindow", "Booking Mode"))
        self.data_category_list.setSortingEnabled(__sortingEnabled)
        self.data_category_options.setText(_translate("MainWindow", "Account Status"))
        __sortingEnabled = self.data_category_options_list.isSortingEnabled()
        self.data_category_options_list.setSortingEnabled(False)
        item = self.data_category_options_list.item(0)
        item.setText(_translate("MainWindow", "Active"))
        item = self.data_category_options_list.item(1)
        item.setText(_translate("MainWindow", "Inactive"))
        item = self.data_category_options_list.item(2)
        item.setText(_translate("MainWindow", "Discharged"))
        self.data_category_options_list.setSortingEnabled(__sortingEnabled)
        self.data_id.setText(_translate("MainWindow", "Data ID"))
        self.edit_change_btn.setText(_translate("MainWindow", "Edit"))
        self.description.setText(_translate("MainWindow", "Description"))
        self.parent_data.setText(_translate("MainWindow", "Parent Data"))
        self.status.setText(_translate("MainWindow", "Status"))
        self.locked.setText(_translate("MainWindow", "Locked"))
        self.save_btn.setText(_translate("MainWindow", "Save"))
        self.clear_btn.setText(_translate("MainWindow", "Clear"))
        self.close_btn.setText(_translate("MainWindow", "Close"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_one), _translate("MainWindow", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_two), _translate("MainWindow", "Tab 2"))
        self.menuDo.setTitle(_translate("MainWindow", "Do"))
        self.menuThat.setTitle(_translate("MainWindow", "That "))
        self.menuStuff.setTitle(_translate("MainWindow", "Stuff"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
