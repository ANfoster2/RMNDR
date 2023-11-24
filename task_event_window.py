# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designergXprjC.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_frm_task_event(object):
    def setupUi(self, frm_task_event):
        if not frm_task_event.objectName():
            frm_task_event.setObjectName(u"frm_task_event")
        frm_task_event.resize(130, 90)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(frm_task_event.sizePolicy().hasHeightForWidth())
        frm_task_event.setSizePolicy(sizePolicy)
        frm_task_event.setMinimumSize(QSize(70, 70))
        frm_task_event.setMaximumSize(QSize(130, 90))
        self.verticalLayout = QVBoxLayout(frm_task_event)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(frm_task_event)
        self.frame.setObjectName(u"frame")
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_new_task = QPushButton(self.frame)
        self.btn_new_task.setObjectName(u"btn_new_task")
        sizePolicy.setHeightForWidth(self.btn_new_task.sizePolicy().hasHeightForWidth())
        self.btn_new_task.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.btn_new_task)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(frm_task_event)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_new_event = QPushButton(self.frame_2)
        self.btn_new_event.setObjectName(u"btn_new_event")
        sizePolicy.setHeightForWidth(self.btn_new_event.sizePolicy().hasHeightForWidth())
        self.btn_new_event.setSizePolicy(sizePolicy)

        self.verticalLayout_3.addWidget(self.btn_new_event)


        self.verticalLayout.addWidget(self.frame_2)


        self.retranslateUi(frm_task_event)

        QMetaObject.connectSlotsByName(frm_task_event)
    # setupUi

    def retranslateUi(self, frm_task_event):
        frm_task_event.setWindowTitle(QCoreApplication.translate("frm_task_event", u"Form", None))
        self.btn_new_task.setText(QCoreApplication.translate("frm_task_event", u"Task", None))
        self.btn_new_event.setText(QCoreApplication.translate("frm_task_event", u"Event", None))
    # retranslateUi

