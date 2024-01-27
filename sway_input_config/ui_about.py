# Form implementation generated from reading ui file 'sway_input_config/ui/about.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_about(object):
    def setupUi(self, about):
        about.setObjectName("about")
        about.setWindowModality(QtCore.Qt.WindowModality.WindowModal)
        about.resize(450, 450)
        about.setMinimumSize(QtCore.QSize(450, 450))
        about.setMaximumSize(QtCore.QSize(450, 450))
        about.setModal(True)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(about)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pixmap = QtWidgets.QLabel(parent=about)
        self.pixmap.setText("")
        self.pixmap.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.pixmap.setOpenExternalLinks(True)
        self.pixmap.setObjectName("pixmap")
        self.verticalLayout.addWidget(self.pixmap)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(parent=about)
        self.label_2.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setOpenExternalLinks(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.version = QtWidgets.QLabel(parent=about)
        self.version.setText("")
        self.version.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.version.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.version.setWordWrap(True)
        self.version.setObjectName("version")
        self.verticalLayout.addWidget(self.version)
        self.label = QtWidgets.QLabel(parent=about)
        self.label.setText("<html><head/><body><p align=\"center\">Copyright: 2022-2023 Aleksey Samoilov</p><p align=\"center\">Licensed under the GNU GPLv3</p><p align=\"center\"><a href=\"https://github.com/Sunderland93/sway-input-config\"><span style=\" text-decoration: underline; color:#1397c3;\">Github</span></a></p></body></html>")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.buttonBox = QtWidgets.QDialogButtonBox(parent=about)
        self.buttonBox.setWhatsThis("")
        self.buttonBox.setAccessibleName("")
        self.buttonBox.setAccessibleDescription("")
        self.buttonBox.setLocale(QtCore.QLocale(QtCore.QLocale.Language.English, QtCore.QLocale.Country.UnitedStates))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout.addWidget(self.buttonBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(about)
        QtCore.QMetaObject.connectSlotsByName(about)

    def retranslateUi(self, about):
        _translate = QtCore.QCoreApplication.translate
        about.setWindowTitle(_translate("about", "About Sway Input Configurator"))
        self.label_2.setText(_translate("about", "A simple input device configurator for SwayWM, written in Python and Qt6. It uses standard libinput options to configure keyboard, touchpad and pointer devices"))
