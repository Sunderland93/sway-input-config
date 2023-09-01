# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'error_message.ui'
##
## Created by: Qt User Interface Compiler version 5.15.8
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore


class Ui_ErrorMessage(object):
    def setupUi(self, ErrorMessage):
        if not ErrorMessage.objectName():
            ErrorMessage.setObjectName(u"ErrorMessage")
        ErrorMessage.setWindowModality(Qt.WindowModal)
        ErrorMessage.resize(670, 115)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ErrorMessage.sizePolicy().hasHeightForWidth())
        ErrorMessage.setSizePolicy(sizePolicy)
        ErrorMessage.setMinimumSize(QSize(670, 115))
        ErrorMessage.setMaximumSize(QSize(670, 115))
        self.verticalLayout = QVBoxLayout(ErrorMessage)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(ErrorMessage)
        self.label.setObjectName(u"label")
        self.label.setTextFormat(Qt.AutoText)
        self.label.setWordWrap(True)

        self.horizontalLayout.addWidget(self.label)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.buttonBox = QDialogButtonBox(ErrorMessage)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Ok)

        self.horizontalLayout_3.addWidget(self.buttonBox)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.retranslateUi(ErrorMessage)

        QMetaObject.connectSlotsByName(ErrorMessage)
    # setupUi

    def retranslateUi(self, ErrorMessage):
        ErrorMessage.setWindowTitle(QCoreApplication.translate("ErrorMessage", u"Sway socket not found!", None))
        self.label.setText(QCoreApplication.translate("ErrorMessage", u"<html><head/><body><p><span style=\" font-size:10pt;\">Sway Input Configurator only supports Sway. You are probably using an unsupported window manager or there are problems with your Sway configuration.</span></p></body></html>", None))
    # retranslateUi

