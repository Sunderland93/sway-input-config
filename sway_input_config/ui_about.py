# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'about.ui'
##
## Created by: Qt User Interface Compiler version 5.15.3
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
        about.setWindowModality(Qt.WindowModal)
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
        self.label_2.setTextFormat(Qt.PlainText)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setMargin(0)
        self.label_2.setOpenExternalLinks(True)

        self.verticalLayout.addWidget(self.label_2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.version = QLabel(about)
        self.version.setObjectName(u"version")
        self.version.setText(u"")
        self.version.setTextFormat(Qt.AutoText)
        self.version.setAlignment(Qt.AlignCenter)
        self.version.setWordWrap(True)

        self.verticalLayout.addWidget(self.version)

        self.label = QLabel(about)
        self.label.setObjectName(u"label")
        self.label.setText(u"<html><head/><body><p align=\"center\">Copyright: 2022-2023 Aleksey Samoilov</p><p align=\"center\">Licensed under the GNU GPLv3</p><p align=\"center\"><a href=\"https://github.com/Sunderland93/sway-input-config\"><span style=\" text-decoration: underline; color:#1397c3;\">Github</span></a></p></body></html>")

        self.verticalLayout.addWidget(self.label)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.buttonBox = QDialogButtonBox(about)
        self.buttonBox.setObjectName(u"buttonBox")
#if QT_CONFIG(whatsthis)
        self.buttonBox.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.buttonBox.setAccessibleName(u"")
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.buttonBox.setAccessibleDescription(u"")
#endif // QT_CONFIG(accessibility)
        self.buttonBox.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.buttonBox.setStandardButtons(QDialogButtonBox.Close)

        self.horizontalLayout.addWidget(self.buttonBox)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.retranslateUi(about)

        QMetaObject.connectSlotsByName(about)
    # setupUi

    def retranslateUi(self, about):
        about.setWindowTitle(QCoreApplication.translate("about", u"About Sway Input Configurator", None))
        self.pixmap.setText("")
        self.label_2.setText(QCoreApplication.translate("about", u"A simple input device configurator for SwayWM, written in Python and Qt5/PySide2. It uses standard libinput options to configure keyboard, touchpad and pointer devices", None))
    # retranslateUi

