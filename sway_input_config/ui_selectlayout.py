# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'selectlayout.ui'
##
## Created by: Qt User Interface Compiler version 5.15.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_SelectKeyboardLayoutDialog(object):
    def setupUi(self, SelectKeyboardLayoutDialog):
        if not SelectKeyboardLayoutDialog.objectName():
            SelectKeyboardLayoutDialog.setObjectName(u"SelectKeyboardLayoutDialog")
        SelectKeyboardLayoutDialog.resize(480, 384)
        self.gridLayout = QGridLayout(SelectKeyboardLayoutDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(SelectKeyboardLayoutDialog)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(SelectKeyboardLayoutDialog)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)

        self.layouts = QListWidget(SelectKeyboardLayoutDialog)
        self.layouts.setObjectName(u"layouts")
        self.layouts.setSortingEnabled(True)

        self.gridLayout.addWidget(self.layouts, 1, 0, 1, 2)

        self.variants = QListWidget(SelectKeyboardLayoutDialog)
        self.variants.setObjectName(u"variants")

        self.gridLayout.addWidget(self.variants, 1, 2, 1, 1)

        self.buttonBox = QDialogButtonBox(SelectKeyboardLayoutDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 3)


        self.retranslateUi(SelectKeyboardLayoutDialog)

        QMetaObject.connectSlotsByName(SelectKeyboardLayoutDialog)
    # setupUi

    def retranslateUi(self, SelectKeyboardLayoutDialog):
        SelectKeyboardLayoutDialog.setWindowTitle(QCoreApplication.translate("SelectKeyboardLayoutDialog", u"Select a keyboard layout", None))
        self.label.setText(QCoreApplication.translate("SelectKeyboardLayoutDialog", u"Keyboard layout", None))
        self.label_2.setText(QCoreApplication.translate("SelectKeyboardLayoutDialog", u"Variant", None))
    # retranslateUi

