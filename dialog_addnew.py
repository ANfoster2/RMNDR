# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_addnew.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import ui_mainwindow




class Ui_dialog_addnew(object):
    def setupUi(self, dialog_addnew):
        dialog_addnew.setObjectName("dialog_addnew")
        dialog_addnew.resize(339, 458)
        self.txt_task_name = QtWidgets.QLineEdit(dialog_addnew)
        self.txt_task_name.setGeometry(QtCore.QRect(40, 90, 261, 31))
        self.txt_task_name.setText("")
        self.txt_task_name.setObjectName("txt_task_name")
        self.txt_task_description = QtWidgets.QTextEdit(dialog_addnew)
        self.txt_task_description.setGeometry(QtCore.QRect(40, 170, 261, 131))
        self.txt_task_description.setObjectName("txt_task_description")
        self.label = QtWidgets.QLabel(dialog_addnew)
        self.label.setGeometry(QtCore.QRect(40, 60, 91, 16))
        self.label.setStyleSheet("font: 10pt \"Microsoft YaHei UI\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(dialog_addnew)
        self.label_2.setGeometry(QtCore.QRect(40, 130, 151, 16))
        self.label_2.setStyleSheet("font: 10pt \"Microsoft YaHei UI\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(dialog_addnew)
        self.label_3.setGeometry(QtCore.QRect(20, 330, 161, 16))
        self.label_3.setStyleSheet("font: 9pt \"Microsoft YaHei UI\";")
        self.label_3.setObjectName("label_3")
        self.cb_estimated_time = QtWidgets.QComboBox(dialog_addnew)
        self.cb_estimated_time.setGeometry(QtCore.QRect(190, 330, 111, 31))
        self.cb_estimated_time.setObjectName("cb_estimated_time")
        self.cb_estimated_time.addItem("")
        self.cb_estimated_time.addItem("")
        self.cb_estimated_time.addItem("")
        self.cb_estimated_time.addItem("")
        self.cb_estimated_time.addItem("")
        self.cb_estimated_time.addItem("")
        self.cb_estimated_time.addItem("")
        self.cb_estimated_time.addItem("")
        self.btn_cancel = QtWidgets.QPushButton(dialog_addnew)
        self.btn_cancel.clicked.connect(lambda: dialog_addnew.close()) #close window
        self.btn_cancel.setGeometry(QtCore.QRect(40, 380, 101, 41))
        self.btn_cancel.setStyleSheet("\n"
"QPushButton{\n"
"    font: 10pt \"Microsoft YaHei UI\";\n"
"    color: rgb(25, 25, 25);\n"
"    background-color: rgb(243, 225, 255);\n"
"    \n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(228, 196, 255)\n"
"}\n"
"")
        self.btn_cancel.setObjectName("btn_cancel")
        self.btn_Create_task = QtWidgets.QPushButton(dialog_addnew)
        self.btn_Create_task.setGeometry(QtCore.QRect(190, 380, 111, 41))
        self.btn_Create_task.setStyleSheet("QPushButton{\n"
"    font: 10pt \"Microsoft YaHei UI\";\n"
"    color: rgb(25, 25, 25);\n"
"    background-color: rgb(243, 225, 255);\n"
"    \n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(228, 196, 255)\n"
"}\n"
"")
        self.btn_Create_task.setObjectName("btn_Create_task")
        self.btn_Create_task.clicked.connect(lambda: self.loadData()) #call load data function
        #self.btn_Create_task.clicked.connect(lambda: dialog_addnew.close())
        self.dateEdit_task = QtWidgets.QDateEdit(dialog_addnew)
        self.dateEdit_task.setDateTime(QtCore.QDateTime.currentDateTime())#set the dateEdit to current date
        self.dateEdit_task.dateChanged.connect(self.dateEditDateChanged)
        self.dateEdit_task.setGeometry(QtCore.QRect(110, 20, 121, 31))
        self.dateEdit_task.setStyleSheet("font: 10pt \"Microsoft YaHei\";")
        self.dateEdit_task.setAlignment(QtCore.Qt.AlignCenter)
        self.dateEdit_task.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.dateEdit_task.setObjectName("dateEdit_task")

        self.retranslateUi(dialog_addnew)
        QtCore.QMetaObject.connectSlotsByName(dialog_addnew)

    def dateEditDateChanged(self):
        #The calendar date was changed
        dateSelected = self.dateEdit_task.date().toPyDate() #format dateSelected to pyDate
       

    #load data into SQLite
    def loadData(self):
        dateSelected = self.dateEdit_task.date().toPyDate()
        weekday =dateSelected.isoweekday() #returns weekday as number (1-7)
        if weekday == 1:
            weekday = 'Monday'
        elif weekday ==2:
            weekday = 'Tuesday'
        elif weekday ==3:
            weekday = 'Wednesday'
        elif weekday ==4:
            weekday = 'Thursday'
        elif weekday ==5:
            weekday = 'Friday'
        elif weekday ==6:
            weekday = 'Saturday'
        elif weekday ==7:
            weekday = 'Sunday'
        
        taskName = self.txt_task_name.text()
        taskDescription = self.txt_task_description.toPlainText()
        estimatedTime = str(self.cb_estimated_time.currentText())

        conn = sqlite3.connect("tasks.db")
        cur = conn.cursor()
        user_info = [weekday, taskName, taskDescription, estimatedTime, dateSelected,]
        cur.execute('INSERT INTO task_info(Weekday, Task_Name, Task_Description, Estimated_Time, Date) VALUES(?, ?, ?, ?, ?)', user_info)

        conn.commit()
        print('Record inserted successfully')
        conn.close()
        # import ui_mainwindow
        # if weekday == 'Monday':
        #     self.ui.Ui_MainWindow.loadMonday()
        # elif weekday == 'Tuesday':
        #     self.ui.Ui_MainWindowloadTuesday()
        # elif weekday == 'Wednesday':
        #     self.ui.Ui_MainWindow.loadWednesday()
        # elif weekday == 'Thursday':
        #     self.ui.Ui_MainWindow.loadThursday()
        # elif weekday == 'Friday':
        #     self.ui.Ui_MainWindow.loadFriday()
        # elif weekday == 'Saturday':
        #     self.ui.Ui_MainWindow.loadSaturday()
        # elif weekday == 'Sunday':
        #     self.ui.Ui_MainWindow.loadSunday()

        
        
        
        


    def retranslateUi(self, dialog_addnew):
        _translate = QtCore.QCoreApplication.translate
        dialog_addnew.setWindowTitle(_translate("dialog_addnew", "Dialog"))
        self.txt_task_description.setHtml(_translate("dialog_addnew", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label.setText(_translate("dialog_addnew", "Task name"))
        self.label_2.setText(_translate("dialog_addnew", "Task description"))
        self.label_3.setText(_translate("dialog_addnew", "Schedule time blocks:"))
        self.cb_estimated_time.setItemText(0, _translate("dialog_addnew", "15 min"))
        self.cb_estimated_time.setItemText(1, _translate("dialog_addnew", "Estimated time"))
        self.cb_estimated_time.setItemText(2, _translate("dialog_addnew", "30 min"))
        self.cb_estimated_time.setItemText(3, _translate("dialog_addnew", "45 min"))
        self.cb_estimated_time.setItemText(4, _translate("dialog_addnew", "1 hour"))
        self.cb_estimated_time.setItemText(5, _translate("dialog_addnew", "1:30 hours"))
        self.cb_estimated_time.setItemText(6, _translate("dialog_addnew", "2:00 hours"))
        self.cb_estimated_time.setItemText(7, _translate("dialog_addnew", "3:00  hours"))
        self.btn_cancel.setText(_translate("dialog_addnew", "Cancel"))
        self.btn_Create_task.setText(_translate("dialog_addnew", "Create task"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialog_addnew = QtWidgets.QDialog()
    ui = Ui_dialog_addnew()
    ui.setupUi(dialog_addnew)
    dialog_addnew.show()
    sys.exit(app.exec_())
