# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainwindowfKRrzU.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 500)
        MainWindow.setMinimumSize(QSize(1000, 500))
        MainWindow.setStyleSheet(u"\n"
"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Top_Bar = QFrame(self.centralwidget)
        self.Top_Bar.setObjectName(u"Top_Bar")
        self.Top_Bar.setMaximumSize(QSize(16777215, 40))
        self.Top_Bar.setStyleSheet(u"\n"
"background-color: rgb(253, 243, 255);")
        self.Top_Bar.setFrameShape(QFrame.NoFrame)
        self.Top_Bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.Top_Bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.Top_Bar)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMaximumSize(QSize(70, 40))
        self.frame_toggle.setStyleSheet(u"background-color: rgb(249, 242, 255);")
        self.frame_toggle.setFrameShape(QFrame.StyledPanel)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn_toggle = QPushButton(self.frame_toggle)
        self.btn_toggle.setObjectName(u"btn_toggle")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_toggle.sizePolicy().hasHeightForWidth())
        self.btn_toggle.setSizePolicy(sizePolicy)
        self.btn_toggle.setStyleSheet(u"color: rgb(39, 39, 39);\n"
"border: 0px solid;")

        self.verticalLayout_2.addWidget(self.btn_toggle)


        self.horizontalLayout.addWidget(self.frame_toggle)

        self.frame_top = QFrame(self.Top_Bar)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_top.setFrameShape(QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_top)


        self.verticalLayout.addWidget(self.Top_Bar)

        self.Content = QFrame(self.centralwidget)
        self.Content.setObjectName(u"Content")
        self.Content.setFrameShape(QFrame.NoFrame)
        self.Content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Content)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.Content)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.frame)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        self.frame_left_menu.setMinimumSize(QSize(70, 0))
        self.frame_left_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(243, 225, 255);")
        self.frame_left_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_top_menus = QFrame(self.frame_left_menu)
        self.frame_top_menus.setObjectName(u"frame_top_menus")
        self.frame_top_menus.setFrameShape(QFrame.NoFrame)
        self.frame_top_menus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_top_menus)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btn_menu_1 = QPushButton(self.frame_top_menus)
        self.btn_menu_1.setObjectName(u"btn_menu_1")
        self.btn_menu_1.setMinimumSize(QSize(0, 40))
        self.btn_menu_1.setStyleSheet(u"QPushButton{\n"
"	\n"
"	color: rgb(25, 25, 25);\n"
"	background-color: rgb(243, 225, 255);\n"
"	border: 0px solid\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:checked{\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.btn_menu_1.setCheckable(True)

        self.verticalLayout_4.addWidget(self.btn_menu_1)

        self.btn_menu_2 = QPushButton(self.frame_top_menus)
        self.btn_menu_2.setObjectName(u"btn_menu_2")
        self.btn_menu_2.setMinimumSize(QSize(0, 40))
        self.btn_menu_2.setStyleSheet(u"QPushButton{\n"
"	\n"
"	color: rgb(25, 25, 25);\n"
"	background-color: rgb(243, 225, 255);\n"
"	border: 0px solid\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(255, 255, 255);\n"
"}")

        self.verticalLayout_4.addWidget(self.btn_menu_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.btn_menu_3 = QPushButton(self.frame_top_menus)
        self.btn_menu_3.setObjectName(u"btn_menu_3")
        self.btn_menu_3.setMinimumSize(QSize(0, 40))
        self.btn_menu_3.setStyleSheet(u"QPushButton{\n"
"	\n"
"	color: rgb(25, 25, 25);\n"
"	background-color: rgb(243, 225, 255);\n"
"	border: 0px solid\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(255, 255, 255);\n"
"}")

        self.verticalLayout_4.addWidget(self.btn_menu_3)


        self.verticalLayout_3.addWidget(self.frame_top_menus)


        self.horizontalLayout_3.addWidget(self.frame_left_menu)

        self.frame_pages = QFrame(self.frame)
        self.frame_pages.setObjectName(u"frame_pages")
        self.frame_pages.setFrameShape(QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_pages)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.pages_widget = QStackedWidget(self.frame_pages)
        self.pages_widget.setObjectName(u"pages_widget")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.verticalLayout_6 = QVBoxLayout(self.page_1)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_2 = QLabel(self.page_1)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(40)
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_2)

        self.pages_widget.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_7 = QVBoxLayout(self.page_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label = QLabel(self.page_2)
        self.label.setObjectName(u"label")
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label)

        self.pages_widget.addWidget(self.page_2)

        self.verticalLayout_5.addWidget(self.pages_widget)


        self.horizontalLayout_3.addWidget(self.frame_pages)


        self.horizontalLayout_2.addWidget(self.frame)


        self.verticalLayout.addWidget(self.Content)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.pages_widget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_toggle.setText(QCoreApplication.translate("MainWindow", u"MENU", None))
        self.btn_menu_1.setText(QCoreApplication.translate("MainWindow", u"Schedule", None))
        self.btn_menu_2.setText(QCoreApplication.translate("MainWindow", u"Notes", None))
        self.btn_menu_3.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Page 1", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Page 2", None))
    # retranslateUi

