# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signup.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_signup_page(object):
    def setupUi(self, signup_page):
        signup_page.setObjectName("signup_page")
        signup_page.resize(449, 550)
        signup_page.setStyleSheet("background-color: rgb(241, 220, 255);")
        self.label = QtWidgets.QLabel(signup_page)
        self.label.setGeometry(QtCore.QRect(170, 40, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(signup_page)
        self.label_2.setGeometry(QtCore.QRect(120, 90, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.txt_signup_username = QtWidgets.QLineEdit(signup_page)
        self.txt_signup_username.setGeometry(QtCore.QRect(90, 170, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.txt_signup_username.setFont(font)
        self.txt_signup_username.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.txt_signup_username.setObjectName("txt_signup_username")
        self.txt_signup_password = QtWidgets.QLineEdit(signup_page)
        self.txt_signup_password.setGeometry(QtCore.QRect(90, 260, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.txt_signup_password.setFont(font)
        self.txt_signup_password.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.txt_signup_password.setObjectName("txt_signup_password")
        self.label_3 = QtWidgets.QLabel(signup_page)
        self.label_3.setGeometry(QtCore.QRect(90, 140, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(7, 7, 7);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(signup_page)
        self.label_4.setGeometry(QtCore.QRect(90, 230, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(7, 7, 7);")
        self.label_4.setObjectName("label_4")
        self.btn_create = QtWidgets.QPushButton(signup_page)
        self.btn_create.setGeometry(QtCore.QRect(90, 430, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.btn_create.setFont(font)
        self.btn_create.setStyleSheet("QPushButton{\n"
"    \n"
"    color: rgb(25, 25, 25);\n"
"    background-color: rgb(255, 255, 255);\n"
"    border: 0px solid;\n"
"    border-radius: 20px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(216, 211, 215);\n"
"}\n"
"QPushButton:checked{\n"
"background-color: rgb(216, 211, 215);\n"
"}")
        self.btn_create.setObjectName("btn_create")
        self.label_5 = QtWidgets.QLabel(signup_page)
        self.label_5.setGeometry(QtCore.QRect(90, 320, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(7, 7, 7);")
        self.label_5.setObjectName("label_5")
        self.txt_signup_password2 = QtWidgets.QLineEdit(signup_page)
        self.txt_signup_password2.setGeometry(QtCore.QRect(90, 350, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.txt_signup_password2.setFont(font)
        self.txt_signup_password2.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.txt_signup_password2.setObjectName("txt_signup_password2")

        self.retranslateUi(signup_page)
        QtCore.QMetaObject.connectSlotsByName(signup_page)

    def retranslateUi(self, signup_page):
        _translate = QtCore.QCoreApplication.translate
        signup_page.setWindowTitle(_translate("signup_page", "Dialog"))
        self.label.setText(_translate("signup_page", "Sign up"))
        self.label_2.setText(_translate("signup_page", "Sign up for a new account"))
        self.label_3.setText(_translate("signup_page", "Username"))
        self.label_4.setText(_translate("signup_page", "Password"))
        self.btn_create.setText(_translate("signup_page", "Create"))
        self.label_5.setText(_translate("signup_page", "Repeat Password"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    signup_page = QtWidgets.QDialog()
    ui = Ui_signup_page()
    ui.setupUi(signup_page)
    signup_page.show()
    sys.exit(app.exec_())
