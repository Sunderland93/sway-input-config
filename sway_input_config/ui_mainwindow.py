# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.3
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
        MainWindow.resize(615, 715)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(615, 715))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        MainWindow.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QSize(615, 715))
        self.centralwidget.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"combobox-popup: 0")
        self.KeyboardTab = QWidget()
        self.KeyboardTab.setObjectName(u"KeyboardTab")
        self.verticalLayout_4 = QVBoxLayout(self.KeyboardTab)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.groupBox = QGroupBox(self.KeyboardTab)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.layouts = QTreeWidget(self.groupBox)
        self.layouts.setObjectName(u"layouts")
        self.layouts.setDragEnabled(True)
        self.layouts.setDragDropMode(QAbstractItemView.InternalMove)
        self.layouts.setRootIsDecorated(False)
        self.layouts.setItemsExpandable(False)
        self.layouts.setColumnCount(2)

        self.horizontalLayout_2.addWidget(self.layouts)


        self.gridLayout_2.addLayout(self.horizontalLayout_2, 0, 0, 1, 4)

        self.num_lockLabel = QLabel(self.groupBox)
        self.num_lockLabel.setObjectName(u"num_lockLabel")

        self.gridLayout_2.addWidget(self.num_lockLabel, 7, 0, 1, 1)

        self.repeatDelayLabel = QLabel(self.groupBox)
        self.repeatDelayLabel.setObjectName(u"repeatDelayLabel")

        self.gridLayout_2.addWidget(self.repeatDelayLabel, 4, 0, 1, 1)

        self.repeatRate = QSpinBox(self.groupBox)
        self.repeatRate.setObjectName(u"repeatRate")
        self.repeatRate.setMinimum(1)
        self.repeatRate.setMaximum(4000)

        self.gridLayout_2.addWidget(self.repeatRate, 5, 2, 1, 1)

        self.shortcutName = QComboBox(self.groupBox)
        self.shortcutName.setObjectName(u"shortcutName")
        self.shortcutName.setStyleSheet(u"combobox-popup: 0;")

        self.gridLayout_2.addWidget(self.shortcutName, 3, 1, 1, 1)

        self.repeatDelay = QSpinBox(self.groupBox)
        self.repeatDelay.setObjectName(u"repeatDelay")
        self.repeatDelay.setMinimum(1)
        self.repeatDelay.setMaximum(6000)

        self.gridLayout_2.addWidget(self.repeatDelay, 4, 2, 1, 1)

        self.caps_lockLabel = QLabel(self.groupBox)
        self.caps_lockLabel.setObjectName(u"caps_lockLabel")

        self.gridLayout_2.addWidget(self.caps_lockLabel, 6, 0, 1, 1)

        self.kbdModel_label = QLabel(self.groupBox)
        self.kbdModel_label.setObjectName(u"kbdModel_label")

        self.gridLayout_2.addWidget(self.kbdModel_label, 2, 0, 1, 1)

        self.num_lock = QCheckBox(self.groupBox)
        self.num_lock.setObjectName(u"num_lock")

        self.gridLayout_2.addWidget(self.num_lock, 7, 1, 1, 1)

        self.kbdID_label = QLabel(self.groupBox)
        self.kbdID_label.setObjectName(u"kbdID_label")

        self.gridLayout_2.addWidget(self.kbdID_label, 1, 0, 1, 1)

        self.caps_lock = QCheckBox(self.groupBox)
        self.caps_lock.setObjectName(u"caps_lock")

        self.gridLayout_2.addWidget(self.caps_lock, 6, 1, 1, 1)

        self.kbdModel = QComboBox(self.groupBox)
        self.kbdModel.setObjectName(u"kbdModel")
        self.kbdModel.setStyleSheet(u"combobox-popup: 0;")

        self.gridLayout_2.addWidget(self.kbdModel, 2, 1, 1, 1)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.addBtn = QPushButton(self.groupBox)
        self.addBtn.setObjectName(u"addBtn")

        self.verticalLayout_5.addWidget(self.addBtn)

        self.rmBtn = QPushButton(self.groupBox)
        self.rmBtn.setObjectName(u"rmBtn")

        self.verticalLayout_5.addWidget(self.rmBtn)

        self.upBtn = QPushButton(self.groupBox)
        self.upBtn.setObjectName(u"upBtn")

        self.verticalLayout_5.addWidget(self.upBtn)

        self.downBtn = QPushButton(self.groupBox)
        self.downBtn.setObjectName(u"downBtn")

        self.verticalLayout_5.addWidget(self.downBtn)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)


        self.gridLayout_2.addLayout(self.verticalLayout_5, 0, 4, 1, 1)

        self.repeatRateLabel = QLabel(self.groupBox)
        self.repeatRateLabel.setObjectName(u"repeatRateLabel")

        self.gridLayout_2.addWidget(self.repeatRateLabel, 5, 0, 1, 1)

        self.shortcutLabel = QLabel(self.groupBox)
        self.shortcutLabel.setObjectName(u"shortcutLabel")

        self.gridLayout_2.addWidget(self.shortcutLabel, 3, 0, 1, 1)

        self.repeatDelaySlider = QSlider(self.groupBox)
        self.repeatDelaySlider.setObjectName(u"repeatDelaySlider")
        self.repeatDelaySlider.setMinimum(1)
        self.repeatDelaySlider.setMaximum(6000)
        self.repeatDelaySlider.setPageStep(50)
        self.repeatDelaySlider.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.repeatDelaySlider, 4, 1, 1, 1)

        self.kbdID = QComboBox(self.groupBox)
        self.kbdID.setObjectName(u"kbdID")
        self.kbdID.setStyleSheet(u"combobox-popup: 0")

        self.gridLayout_2.addWidget(self.kbdID, 1, 1, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.KeyBoardUseSettings = QCheckBox(self.groupBox)
        self.KeyBoardUseSettings.setObjectName(u"KeyBoardUseSettings")
        self.KeyBoardUseSettings.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_3.addWidget(self.KeyBoardUseSettings)


        self.gridLayout_2.addLayout(self.horizontalLayout_3, 9, 0, 1, 5)

        self.repeatRateSlider = QSlider(self.groupBox)
        self.repeatRateSlider.setObjectName(u"repeatRateSlider")
        self.repeatRateSlider.setMinimum(1)
        self.repeatRateSlider.setMaximum(4000)
        self.repeatRateSlider.setPageStep(50)
        self.repeatRateSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.repeatRateSlider, 5, 1, 1, 1)


        self.verticalLayout_4.addWidget(self.groupBox)

        self.tabWidget.addTab(self.KeyboardTab, "")
        self.MouseTab = QWidget()
        self.MouseTab.setObjectName(u"MouseTab")
        self.verticalLayout_6 = QVBoxLayout(self.MouseTab)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.groupBox_2 = QGroupBox(self.MouseTab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_7 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label)

        self.pointerMiddle = QCheckBox(self.groupBox_2)
        self.pointerMiddle.setObjectName(u"pointerMiddle")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.pointerMiddle)

        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_2)

        self.pointerAccel = QSlider(self.groupBox_2)
        self.pointerAccel.setObjectName(u"pointerAccel")
        self.pointerAccel.setMinimum(-10)
        self.pointerAccel.setMaximum(10)
        self.pointerAccel.setPageStep(1)
        self.pointerAccel.setOrientation(Qt.Horizontal)
        self.pointerAccel.setTickPosition(QSlider.TicksBelow)
        self.pointerAccel.setTickInterval(1)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.pointerAccel)

        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_3)

        self.pointerFlat = QRadioButton(self.groupBox_2)
        self.pointerFlat.setObjectName(u"pointerFlat")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.pointerFlat)

        self.pointerAdaptive = QRadioButton(self.groupBox_2)
        self.pointerAdaptive.setObjectName(u"pointerAdaptive")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.pointerAdaptive)

        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_4)

        self.pointerNatScroll = QCheckBox(self.groupBox_2)
        self.pointerNatScroll.setObjectName(u"pointerNatScroll")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.pointerNatScroll)

        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_5)

        self.pointerScrollFactor = QSlider(self.groupBox_2)
        self.pointerScrollFactor.setObjectName(u"pointerScrollFactor")
        self.pointerScrollFactor.setMinimum(1)
        self.pointerScrollFactor.setMaximum(100)
        self.pointerScrollFactor.setPageStep(1)
        self.pointerScrollFactor.setOrientation(Qt.Horizontal)
        self.pointerScrollFactor.setTickPosition(QSlider.TicksBelow)
        self.pointerScrollFactor.setTickInterval(9)

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.pointerScrollFactor)

        self.pointerLeftHanded = QCheckBox(self.groupBox_2)
        self.pointerLeftHanded.setObjectName(u"pointerLeftHanded")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.pointerLeftHanded)

        self.pointerID_label = QLabel(self.groupBox_2)
        self.pointerID_label.setObjectName(u"pointerID_label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.pointerID_label)

        self.pointerID = QComboBox(self.groupBox_2)
        self.pointerID.setObjectName(u"pointerID")
        self.pointerID.setStyleSheet(u"combobox-popup: 0")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.pointerID)


        self.horizontalLayout_6.addLayout(self.formLayout)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")

        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)


        self.verticalLayout_7.addLayout(self.horizontalLayout_6)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.PointerUseSettings = QCheckBox(self.groupBox_2)
        self.PointerUseSettings.setObjectName(u"PointerUseSettings")

        self.horizontalLayout_4.addWidget(self.PointerUseSettings)


        self.verticalLayout_7.addLayout(self.horizontalLayout_4)


        self.verticalLayout_6.addWidget(self.groupBox_2)

        self.tabWidget.addTab(self.MouseTab, "")
        self.TouchpadTab = QWidget()
        self.TouchpadTab.setObjectName(u"TouchpadTab")
        self.verticalLayout_8 = QVBoxLayout(self.TouchpadTab)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.groupBox_3 = QGroupBox(self.TouchpadTab)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_9 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_5)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_6 = QLabel(self.groupBox_3)
        self.label_6.setObjectName(u"label_6")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_6)

        self.DWT = QCheckBox(self.groupBox_3)
        self.DWT.setObjectName(u"DWT")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.DWT)

        self.touchLeftHanded = QCheckBox(self.groupBox_3)
        self.touchLeftHanded.setObjectName(u"touchLeftHanded")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.touchLeftHanded)

        self.touchMiddle = QCheckBox(self.groupBox_3)
        self.touchMiddle.setObjectName(u"touchMiddle")

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.touchMiddle)

        self.label_7 = QLabel(self.groupBox_3)
        self.label_7.setObjectName(u"label_7")

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.label_7)

        self.touchAccel = QSlider(self.groupBox_3)
        self.touchAccel.setObjectName(u"touchAccel")
        self.touchAccel.setMinimum(-10)
        self.touchAccel.setMaximum(10)
        self.touchAccel.setPageStep(1)
        self.touchAccel.setOrientation(Qt.Horizontal)
        self.touchAccel.setTickPosition(QSlider.TicksBelow)
        self.touchAccel.setTickInterval(1)

        self.formLayout_2.setWidget(5, QFormLayout.FieldRole, self.touchAccel)

        self.label_8 = QLabel(self.groupBox_3)
        self.label_8.setObjectName(u"label_8")

        self.formLayout_2.setWidget(6, QFormLayout.LabelRole, self.label_8)

        self.touchFlat = QRadioButton(self.groupBox_3)
        self.touchFlat.setObjectName(u"touchFlat")

        self.formLayout_2.setWidget(6, QFormLayout.FieldRole, self.touchFlat)

        self.touchAdaptive = QRadioButton(self.groupBox_3)
        self.touchAdaptive.setObjectName(u"touchAdaptive")

        self.formLayout_2.setWidget(7, QFormLayout.FieldRole, self.touchAdaptive)

        self.label_9 = QLabel(self.groupBox_3)
        self.label_9.setObjectName(u"label_9")

        self.formLayout_2.setWidget(8, QFormLayout.LabelRole, self.label_9)

        self.tap_click = QCheckBox(self.groupBox_3)
        self.tap_click.setObjectName(u"tap_click")

        self.formLayout_2.setWidget(8, QFormLayout.FieldRole, self.tap_click)

        self.drag = QCheckBox(self.groupBox_3)
        self.drag.setObjectName(u"drag")

        self.formLayout_2.setWidget(9, QFormLayout.FieldRole, self.drag)

        self.drag_lock = QCheckBox(self.groupBox_3)
        self.drag_lock.setObjectName(u"drag_lock")

        self.formLayout_2.setWidget(10, QFormLayout.FieldRole, self.drag_lock)

        self.label_10 = QLabel(self.groupBox_3)
        self.label_10.setObjectName(u"label_10")

        self.formLayout_2.setWidget(11, QFormLayout.LabelRole, self.label_10)

        self.lrm = QRadioButton(self.groupBox_3)
        self.lrm.setObjectName(u"lrm")

        self.formLayout_2.setWidget(11, QFormLayout.FieldRole, self.lrm)

        self.lmr = QRadioButton(self.groupBox_3)
        self.lmr.setObjectName(u"lmr")

        self.formLayout_2.setWidget(12, QFormLayout.FieldRole, self.lmr)

        self.label_11 = QLabel(self.groupBox_3)
        self.label_11.setObjectName(u"label_11")

        self.formLayout_2.setWidget(13, QFormLayout.LabelRole, self.label_11)

        self.method1 = QRadioButton(self.groupBox_3)
        self.method1.setObjectName(u"method1")

        self.formLayout_2.setWidget(13, QFormLayout.FieldRole, self.method1)

        self.method2 = QRadioButton(self.groupBox_3)
        self.method2.setObjectName(u"method2")

        self.formLayout_2.setWidget(14, QFormLayout.FieldRole, self.method2)

        self.method3 = QRadioButton(self.groupBox_3)
        self.method3.setObjectName(u"method3")

        self.formLayout_2.setWidget(15, QFormLayout.FieldRole, self.method3)

        self.method4 = QRadioButton(self.groupBox_3)
        self.method4.setObjectName(u"method4")

        self.formLayout_2.setWidget(16, QFormLayout.FieldRole, self.method4)

        self.touchNatScroll = QCheckBox(self.groupBox_3)
        self.touchNatScroll.setObjectName(u"touchNatScroll")

        self.formLayout_2.setWidget(17, QFormLayout.FieldRole, self.touchNatScroll)

        self.label_12 = QLabel(self.groupBox_3)
        self.label_12.setObjectName(u"label_12")

        self.formLayout_2.setWidget(18, QFormLayout.LabelRole, self.label_12)

        self.touchScrollFactor = QSlider(self.groupBox_3)
        self.touchScrollFactor.setObjectName(u"touchScrollFactor")
        self.touchScrollFactor.setMinimum(1)
        self.touchScrollFactor.setMaximum(100)
        self.touchScrollFactor.setPageStep(1)
        self.touchScrollFactor.setOrientation(Qt.Horizontal)
        self.touchScrollFactor.setTickPosition(QSlider.TicksBelow)
        self.touchScrollFactor.setTickInterval(9)

        self.formLayout_2.setWidget(18, QFormLayout.FieldRole, self.touchScrollFactor)

        self.DWTP = QCheckBox(self.groupBox_3)
        self.DWTP.setObjectName(u"DWTP")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.DWTP)

        self.touchpadID_label = QLabel(self.groupBox_3)
        self.touchpadID_label.setObjectName(u"touchpadID_label")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.touchpadID_label)

        self.touchpadID = QComboBox(self.groupBox_3)
        self.touchpadID.setObjectName(u"touchpadID")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.touchpadID)


        self.horizontalLayout_8.addLayout(self.formLayout_2)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_6)


        self.verticalLayout_9.addLayout(self.horizontalLayout_8)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_3)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_7)

        self.TouchPadUseSettings = QCheckBox(self.groupBox_3)
        self.TouchPadUseSettings.setObjectName(u"TouchPadUseSettings")

        self.horizontalLayout_7.addWidget(self.TouchPadUseSettings)


        self.verticalLayout_9.addLayout(self.horizontalLayout_7)


        self.verticalLayout_8.addWidget(self.groupBox_3)

        self.tabWidget.addTab(self.TouchpadTab, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.buttonBox = QDialogButtonBox(self.centralwidget)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Apply|QDialogButtonBox.Close|QDialogButtonBox.Help|QDialogButtonBox.RestoreDefaults)

        self.verticalLayout.addWidget(self.buttonBox)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Sway Input Configurator", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Keyboard Settings", None))
        ___qtreewidgetitem = self.layouts.headerItem()
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"Variant", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"Layout", None));
        self.num_lockLabel.setText(QCoreApplication.translate("MainWindow", u"NumLock:", None))
        self.repeatDelayLabel.setText(QCoreApplication.translate("MainWindow", u"Repeat delay:", None))
#if QT_CONFIG(tooltip)
        self.repeatRate.setToolTip(QCoreApplication.translate("MainWindow", u"Frequency of key repeats once the repeat_delay has passed.", None))
#endif // QT_CONFIG(tooltip)
        self.repeatRate.setSuffix(QCoreApplication.translate("MainWindow", u" repeats/s", None))
#if QT_CONFIG(tooltip)
        self.shortcutName.setToolTip(QCoreApplication.translate("MainWindow", u"Keyboard shortcut to switch between layouts.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.repeatDelay.setToolTip(QCoreApplication.translate("MainWindow", u"Amount of time a key must be held before it starts repeating.", None))
#endif // QT_CONFIG(tooltip)
        self.repeatDelay.setSuffix(QCoreApplication.translate("MainWindow", u" ms", None))
        self.caps_lockLabel.setText(QCoreApplication.translate("MainWindow", u"CapsLock:", None))
        self.kbdModel_label.setText(QCoreApplication.translate("MainWindow", u"Keyboard model:", None))
#if QT_CONFIG(tooltip)
        self.num_lock.setToolTip(QCoreApplication.translate("MainWindow", u"Initially enables or disables NumLock on startup.", None))
#endif // QT_CONFIG(tooltip)
        self.num_lock.setText("")
        self.kbdID_label.setText(QCoreApplication.translate("MainWindow", u"Keyboard identifier:", None))
#if QT_CONFIG(tooltip)
        self.caps_lock.setToolTip(QCoreApplication.translate("MainWindow", u"Initially enables or disables CapsLock on startup.", None))
#endif // QT_CONFIG(tooltip)
        self.caps_lock.setText("")
#if QT_CONFIG(tooltip)
        self.addBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Add layout to the list", None))
#endif // QT_CONFIG(tooltip)
        self.addBtn.setText(QCoreApplication.translate("MainWindow", u"Add", None))
#if QT_CONFIG(tooltip)
        self.rmBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Remove layout from the list.", None))
#endif // QT_CONFIG(tooltip)
        self.rmBtn.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
#if QT_CONFIG(tooltip)
        self.upBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Move selected layout up.", None))
#endif // QT_CONFIG(tooltip)
        self.upBtn.setText(QCoreApplication.translate("MainWindow", u"Up", None))
#if QT_CONFIG(tooltip)
        self.downBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Move selected layout down.", None))
#endif // QT_CONFIG(tooltip)
        self.downBtn.setText(QCoreApplication.translate("MainWindow", u"Down", None))
        self.repeatRateLabel.setText(QCoreApplication.translate("MainWindow", u"Repeat rate:", None))
        self.shortcutLabel.setText(QCoreApplication.translate("MainWindow", u"Keyboard shortcut:", None))
        self.KeyBoardUseSettings.setText(QCoreApplication.translate("MainWindow", u"Use this settings", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.KeyboardTab), QCoreApplication.translate("MainWindow", u"Keyboard", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Pointer device settings", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"General:", None))
#if QT_CONFIG(tooltip)
        self.pointerMiddle.setToolTip(QCoreApplication.translate("MainWindow", u"Enables or disables middle click emulation.", None))
#endif // QT_CONFIG(tooltip)
        self.pointerMiddle.setText(QCoreApplication.translate("MainWindow", u"Press left and right buttons for middle click", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Pointer speed:", None))
#if QT_CONFIG(tooltip)
        self.pointerAccel.setToolTip(QCoreApplication.translate("MainWindow", u"Changes the pointer acceleration.", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Acceleration profile:", None))
#if QT_CONFIG(tooltip)
        self.pointerFlat.setToolTip(QCoreApplication.translate("MainWindow", u"Cursor moves the same distance as the mouse movement.", None))
#endif // QT_CONFIG(tooltip)
        self.pointerFlat.setText(QCoreApplication.translate("MainWindow", u"Flat", None))
#if QT_CONFIG(tooltip)
        self.pointerAdaptive.setToolTip(QCoreApplication.translate("MainWindow", u"Cursor travel distance depends on the mouse movement speed.", None))
#endif // QT_CONFIG(tooltip)
        self.pointerAdaptive.setText(QCoreApplication.translate("MainWindow", u"Adaptive", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Scrolling:", None))
#if QT_CONFIG(tooltip)
        self.pointerNatScroll.setToolTip(QCoreApplication.translate("MainWindow", u"Touchscreen like scrolling.", None))
#endif // QT_CONFIG(tooltip)
        self.pointerNatScroll.setText(QCoreApplication.translate("MainWindow", u"Invert scroll direction", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Scrolling speed:", None))
#if QT_CONFIG(tooltip)
        self.pointerScrollFactor.setToolTip(QCoreApplication.translate("MainWindow", u"Scroll speed will be scaled by the given value.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pointerLeftHanded.setToolTip(QCoreApplication.translate("MainWindow", u"Enables or disables left handed mode.", None))
#endif // QT_CONFIG(tooltip)
        self.pointerLeftHanded.setText(QCoreApplication.translate("MainWindow", u"Left handed mode", None))
        self.pointerID_label.setText(QCoreApplication.translate("MainWindow", u"Pointer device identifier:", None))
        self.PointerUseSettings.setText(QCoreApplication.translate("MainWindow", u"Use this settings", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.MouseTab), QCoreApplication.translate("MainWindow", u"Mouse", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Touchpad Settings", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"General:", None))
        self.DWT.setText(QCoreApplication.translate("MainWindow", u"Disable while typing", None))
        self.touchLeftHanded.setText(QCoreApplication.translate("MainWindow", u"Left handed mode", None))
        self.touchMiddle.setText(QCoreApplication.translate("MainWindow", u"Press left and right buttons for middle click", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Pointer speed:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Acceleration profile:", None))
        self.touchFlat.setText(QCoreApplication.translate("MainWindow", u"Flat", None))
        self.touchAdaptive.setText(QCoreApplication.translate("MainWindow", u"Adaptive", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Tapping:", None))
        self.tap_click.setText(QCoreApplication.translate("MainWindow", u"Tap-to-click", None))
        self.drag.setText(QCoreApplication.translate("MainWindow", u"Tap-and-drag", None))
        self.drag_lock.setText(QCoreApplication.translate("MainWindow", u"Tap-and-drag lock", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Two-finger tap:", None))
        self.lrm.setText(QCoreApplication.translate("MainWindow", u"Two-type right, three middle", None))
        self.lmr.setText(QCoreApplication.translate("MainWindow", u"Two-tap middle, three right", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Scrolling", None))
        self.method1.setText(QCoreApplication.translate("MainWindow", u"Two fingers", None))
        self.method2.setText(QCoreApplication.translate("MainWindow", u"Touchpad edges", None))
        self.method3.setText(QCoreApplication.translate("MainWindow", u"On button down", None))
        self.method4.setText(QCoreApplication.translate("MainWindow", u"No scroll", None))
        self.touchNatScroll.setText(QCoreApplication.translate("MainWindow", u"Invert scroll direction", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Scrolling speed:", None))
        self.DWTP.setText(QCoreApplication.translate("MainWindow", u"Disable while trackpointing", None))
        self.touchpadID_label.setText(QCoreApplication.translate("MainWindow", u"Touchpad identifier:", None))
        self.TouchPadUseSettings.setText(QCoreApplication.translate("MainWindow", u"Use this settings", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.TouchpadTab), QCoreApplication.translate("MainWindow", u"Touchpad", None))
    # retranslateUi

