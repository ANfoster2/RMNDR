# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from signup import Ui_signup_page


class Ui_login_page(object):
    def setupUi(self, login_page):
        login_page.setObjectName("login_page")
        login_page.resize(449, 550)
        login_page.setStyleSheet("background-color: rgb(241, 220, 255);")
        self.label = QtWidgets.QLabel(login_page)
        self.label.setGeometry(QtCore.QRect(190, 60, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(login_page)
        self.label_2.setGeometry(QtCore.QRect(100, 110, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.txt_login_username = QtWidgets.QLineEdit(login_page)
        self.txt_login_username.setGeometry(QtCore.QRect(90, 190, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.txt_login_username.setFont(font)
        self.txt_login_username.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.txt_login_username.setObjectName("txt_login_username")
        self.txt_login_password = QtWidgets.QLineEdit(login_page)
        self.txt_login_password.setGeometry(QtCore.QRect(90, 290, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.txt_login_password.setFont(font)
        self.txt_login_password.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.txt_login_password.setObjectName("txt_login_password")
        self.label_3 = QtWidgets.QLabel(login_page)
        self.label_3.setGeometry(QtCore.QRect(90, 160, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(7, 7, 7);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(login_page)
        self.label_4.setGeometry(QtCore.QRect(90, 260, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(7, 7, 7);")
        self.label_4.setObjectName("label_4")
        self.frame = QtWidgets.QFrame(login_page)
        self.frame.setGeometry(QtCore.QRect(120, 340, 193, 41))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_5 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.btn_signup = QtWidgets.QPushButton(self.frame)
        self.btn_signup.clicked.connect(self.clickHandler)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(True)
        self.btn_signup.setFont(font)
        self.btn_signup.setStyleSheet("border: 0px")
        self.btn_signup.setObjectName("btn_signup")
        self.horizontalLayout.addWidget(self.btn_signup)
        self.btn_login = QtWidgets.QPushButton(login_page)
        self.btn_login.setGeometry(QtCore.QRect(90, 410, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.btn_login.setFont(font)
        self.btn_login.setStyleSheet("QPushButton{\n"
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
        self.btn_login.setObjectName("btn_login")

        self.retranslateUi(login_page)
        QtCore.QMetaObject.connectSlotsByName(login_page)

    def retranslateUi(self, login_page):
        _translate = QtCore.QCoreApplication.translate
        login_page.setWindowTitle(_translate("login_page", "Dialog"))
        self.label.setText(_translate("login_page", "Login"))
        self.label_2.setText(_translate("login_page", "Sign in to your existing account"))
        self.label_3.setText(_translate("login_page", "Username"))
        self.label_4.setText(_translate("login_page", "Password"))
        self.label_5.setText(_translate("login_page", "New to RMNDR?"))
        self.btn_signup.setText(_translate("login_page", "Sign up"))
        self.btn_login.setText(_translate("login_page", "Login"))

    def clickHandler(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_signup_page()
        self.ui.setupUi(self.window)
        self.window.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    login_page = QtWidgets.QDialog()
    ui = Ui_login_page()
    ui.setupUi(login_page)
    login_page.show()
    sys.exit(app.exec_())