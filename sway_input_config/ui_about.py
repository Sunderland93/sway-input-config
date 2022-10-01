# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'about.ui'
##
## Created by: Qt User Interface Compiler version 5.15.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_about(object):
    def setupUi(self, about):
        if not about.objectName():
            about.setObjectName(u"about")
        about.resize(450, 450)
        about.setMinimumSize(QSize(450, 450))
        about.setMaximumSize(QSize(450, 450))
        about.setModal(True)
        self.verticalLayout_2 = QVBoxLayout(about)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pixmap = QLabel(about)
        self.pixmap.setObjectName(u"pixmap")
        self.pixmap.setAlignment(Qt.AlignCenter)
        self.pixmap.setMargin(0)
        self.pixmap.setOpenExternalLinks(True)

        self.verticalLayout.addWidget(self.pixmap)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.label_2 = QLabel(about)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setOpenExternalLinks(True)

        self.verticalLayout.addWidget(self.label_2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.label = QLabel(about)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.buttonBox = QDialogButtonBox(about)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Close)

        self.horizontalLayout.addWidget(self.buttonBox)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.retranslateUi(about)

        QMetaObject.connectSlotsByName(about)
    # setupUi

    def retranslateUi(self, about):
        about.setWindowTitle(QCoreApplication.translate("about", u"About Sway Input Config", None))
        self.pixmap.setText("")
        self.label_2.setText(QCoreApplication.translate("about", u"<html><head/><body><p align=\"center\">A simple input devices configurator for SwayWM, written in Python </p><p align=\"center\">and Qt5/PySide2. It uses standard libinput options to configure </p><p align=\"center\">keyboard, touchpad and pointer devices</p></body></html>", None))
        self.label.setText(QCoreApplication.translate("about", u"<html><head/><body><p align=\"center\">Version: 1.2.0.</p><p align=\"center\">Licensed under the GNU GPLv3.</p><p align=\"center\">Copyright: 2022 Aleksey Samoilov<br/></p><p align=\"center\"><a href=\"https://github.com/Sunderland93/sway-input-config\"><span style=\" text-decoration: underline; color:#1d99f3;\">GitHub</span></a></p></body></html>", None))
    # retranslateUi

