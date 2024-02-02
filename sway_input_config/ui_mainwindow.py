# Form implementation generated from reading ui file 'sway_input_config/ui/mainwindow.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(910, 720)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(910, 720))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.Language.English, QtCore.QLocale.Country.UnitedStates))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(615, 715))
        self.centralwidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabWidget.setStyleSheet("combobox-popup: 0")
        self.tabWidget.setObjectName("tabWidget")
        self.KeyboardTab = QtWidgets.QWidget()
        self.KeyboardTab.setObjectName("KeyboardTab")
        self.gridLayout = QtWidgets.QGridLayout(self.KeyboardTab)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.layouts = QtWidgets.QTreeWidget(parent=self.KeyboardTab)
        self.layouts.setDragEnabled(True)
        self.layouts.setDragDropMode(QtWidgets.QAbstractItemView.DragDropMode.InternalMove)
        self.layouts.setRootIsDecorated(False)
        self.layouts.setItemsExpandable(False)
        self.layouts.setColumnCount(2)
        self.layouts.setObjectName("layouts")
        self.horizontalLayout_2.addWidget(self.layouts)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.addBtn = QtWidgets.QPushButton(parent=self.KeyboardTab)
        self.addBtn.setObjectName("addBtn")
        self.verticalLayout_5.addWidget(self.addBtn)
        self.rmBtn = QtWidgets.QPushButton(parent=self.KeyboardTab)
        self.rmBtn.setObjectName("rmBtn")
        self.verticalLayout_5.addWidget(self.rmBtn)
        self.upBtn = QtWidgets.QPushButton(parent=self.KeyboardTab)
        self.upBtn.setObjectName("upBtn")
        self.verticalLayout_5.addWidget(self.upBtn)
        self.downBtn = QtWidgets.QPushButton(parent=self.KeyboardTab)
        self.downBtn.setObjectName("downBtn")
        self.verticalLayout_5.addWidget(self.downBtn)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_5.addItem(spacerItem)
        self.gridLayout.addLayout(self.verticalLayout_5, 0, 1, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.caps_lock = QtWidgets.QCheckBox(parent=self.KeyboardTab)
        self.caps_lock.setText("")
        self.caps_lock.setObjectName("caps_lock")
        self.gridLayout_2.addWidget(self.caps_lock, 5, 1, 1, 1)
        self.shortcutLabel = QtWidgets.QLabel(parent=self.KeyboardTab)
        self.shortcutLabel.setObjectName("shortcutLabel")
        self.gridLayout_2.addWidget(self.shortcutLabel, 2, 0, 1, 1)
        self.repeatDelay = QtWidgets.QSpinBox(parent=self.KeyboardTab)
        self.repeatDelay.setMinimum(1)
        self.repeatDelay.setMaximum(6000)
        self.repeatDelay.setObjectName("repeatDelay")
        self.gridLayout_2.addWidget(self.repeatDelay, 3, 2, 1, 1)
        self.caps_lockLabel = QtWidgets.QLabel(parent=self.KeyboardTab)
        self.caps_lockLabel.setObjectName("caps_lockLabel")
        self.gridLayout_2.addWidget(self.caps_lockLabel, 5, 0, 1, 1)
        self.repeatRateSlider = QtWidgets.QSlider(parent=self.KeyboardTab)
        self.repeatRateSlider.setMinimum(1)
        self.repeatRateSlider.setMaximum(4000)
        self.repeatRateSlider.setPageStep(50)
        self.repeatRateSlider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.repeatRateSlider.setObjectName("repeatRateSlider")
        self.gridLayout_2.addWidget(self.repeatRateSlider, 4, 1, 1, 1)
        self.repeatRate = QtWidgets.QSpinBox(parent=self.KeyboardTab)
        self.repeatRate.setMinimum(1)
        self.repeatRate.setMaximum(4000)
        self.repeatRate.setObjectName("repeatRate")
        self.gridLayout_2.addWidget(self.repeatRate, 4, 2, 1, 1)
        self.kbdID = QtWidgets.QComboBox(parent=self.KeyboardTab)
        self.kbdID.setStyleSheet("combobox-popup: 0")
        self.kbdID.setObjectName("kbdID")
        self.gridLayout_2.addWidget(self.kbdID, 0, 1, 1, 1)
        self.repeatDelaySlider = QtWidgets.QSlider(parent=self.KeyboardTab)
        self.repeatDelaySlider.setMinimum(1)
        self.repeatDelaySlider.setMaximum(6000)
        self.repeatDelaySlider.setPageStep(50)
        self.repeatDelaySlider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.repeatDelaySlider.setObjectName("repeatDelaySlider")
        self.gridLayout_2.addWidget(self.repeatDelaySlider, 3, 1, 1, 1)
        self.repeatDelayLabel = QtWidgets.QLabel(parent=self.KeyboardTab)
        self.repeatDelayLabel.setObjectName("repeatDelayLabel")
        self.gridLayout_2.addWidget(self.repeatDelayLabel, 3, 0, 1, 1)
        self.kbdModel = QtWidgets.QComboBox(parent=self.KeyboardTab)
        self.kbdModel.setStyleSheet("combobox-popup: 0;")
        self.kbdModel.setObjectName("kbdModel")
        self.gridLayout_2.addWidget(self.kbdModel, 1, 1, 1, 1)
        self.kbdID_label = QtWidgets.QLabel(parent=self.KeyboardTab)
        self.kbdID_label.setObjectName("kbdID_label")
        self.gridLayout_2.addWidget(self.kbdID_label, 0, 0, 1, 1)
        self.repeatRateLabel = QtWidgets.QLabel(parent=self.KeyboardTab)
        self.repeatRateLabel.setObjectName("repeatRateLabel")
        self.gridLayout_2.addWidget(self.repeatRateLabel, 4, 0, 1, 1)
        self.num_lockLabel = QtWidgets.QLabel(parent=self.KeyboardTab)
        self.num_lockLabel.setObjectName("num_lockLabel")
        self.gridLayout_2.addWidget(self.num_lockLabel, 6, 0, 1, 1)
        self.num_lock = QtWidgets.QCheckBox(parent=self.KeyboardTab)
        self.num_lock.setText("")
        self.num_lock.setObjectName("num_lock")
        self.gridLayout_2.addWidget(self.num_lock, 6, 1, 1, 1)
        self.shortcutName = QtWidgets.QComboBox(parent=self.KeyboardTab)
        self.shortcutName.setStyleSheet("combobox-popup: 0;")
        self.shortcutName.setObjectName("shortcutName")
        self.gridLayout_2.addWidget(self.shortcutName, 2, 1, 1, 1)
        self.kbdModel_label = QtWidgets.QLabel(parent=self.KeyboardTab)
        self.kbdModel_label.setObjectName("kbdModel_label")
        self.gridLayout_2.addWidget(self.kbdModel_label, 1, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 1, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.KeyBoardUseSettings = QtWidgets.QCheckBox(parent=self.KeyboardTab)
        self.KeyBoardUseSettings.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.KeyBoardUseSettings.setObjectName("KeyBoardUseSettings")
        self.horizontalLayout_3.addWidget(self.KeyBoardUseSettings)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 2)
        self.tabWidget.addTab(self.KeyboardTab, "")
        self.PointerTab = QtWidgets.QWidget()
        self.PointerTab.setObjectName("PointerTab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.PointerTab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_5 = QtWidgets.QGroupBox(parent=self.PointerTab)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pointerID = QtWidgets.QComboBox(parent=self.groupBox_5)
        self.pointerID.setStyleSheet("combobox-popup: 0")
        self.pointerID.setObjectName("pointerID")
        self.gridLayout_3.addWidget(self.pointerID, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(parent=self.groupBox_5)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 1, 0, 1, 1)
        self.pointerID_label = QtWidgets.QLabel(parent=self.groupBox_5)
        self.pointerID_label.setToolTip("")
        self.pointerID_label.setObjectName("pointerID_label")
        self.gridLayout_3.addWidget(self.pointerID_label, 0, 0, 1, 1)
        self.pointerLeftHanded = QtWidgets.QCheckBox(parent=self.groupBox_5)
        self.pointerLeftHanded.setObjectName("pointerLeftHanded")
        self.gridLayout_3.addWidget(self.pointerLeftHanded, 1, 1, 1, 1)
        self.pointerMiddle = QtWidgets.QCheckBox(parent=self.groupBox_5)
        self.pointerMiddle.setObjectName("pointerMiddle")
        self.gridLayout_3.addWidget(self.pointerMiddle, 2, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_5)
        self.groupBox_6 = QtWidgets.QGroupBox(parent=self.PointerTab)
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox_6)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 0, 0, 1, 1)
        self.pointerAccel = QtWidgets.QSlider(parent=self.groupBox_6)
        self.pointerAccel.setMinimum(-10)
        self.pointerAccel.setMaximum(10)
        self.pointerAccel.setPageStep(1)
        self.pointerAccel.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.pointerAccel.setTickPosition(QtWidgets.QSlider.TickPosition.TicksBelow)
        self.pointerAccel.setTickInterval(1)
        self.pointerAccel.setObjectName("pointerAccel")
        self.gridLayout_4.addWidget(self.pointerAccel, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox_6)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 1, 0, 1, 1)
        self.pointerFlat = QtWidgets.QRadioButton(parent=self.groupBox_6)
        self.pointerFlat.setObjectName("pointerFlat")
        self.gridLayout_4.addWidget(self.pointerFlat, 1, 1, 1, 1)
        self.pointerAdaptive = QtWidgets.QRadioButton(parent=self.groupBox_6)
        self.pointerAdaptive.setObjectName("pointerAdaptive")
        self.gridLayout_4.addWidget(self.pointerAdaptive, 2, 1, 1, 1)
        self.pointerRotationLabel = QtWidgets.QLabel(parent=self.groupBox_6)
        self.pointerRotationLabel.setObjectName("pointerRotationLabel")
        self.gridLayout_4.addWidget(self.pointerRotationLabel, 3, 0, 1, 1)
        self.pointerRotationAngleSlider = QtWidgets.QSlider(parent=self.groupBox_6)
        self.pointerRotationAngleSlider.setMaximum(360)
        self.pointerRotationAngleSlider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.pointerRotationAngleSlider.setTickPosition(QtWidgets.QSlider.TickPosition.TicksBelow)
        self.pointerRotationAngleSlider.setTickInterval(10)
        self.pointerRotationAngleSlider.setObjectName("pointerRotationAngleSlider")
        self.gridLayout_4.addWidget(self.pointerRotationAngleSlider, 3, 1, 1, 1)
        self.pointerRotationAngle = QtWidgets.QSpinBox(parent=self.groupBox_6)
        self.pointerRotationAngle.setMaximum(360)
        self.pointerRotationAngle.setObjectName("pointerRotationAngle")
        self.gridLayout_4.addWidget(self.pointerRotationAngle, 3, 2, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_6)
        self.groupBox_7 = QtWidgets.QGroupBox(parent=self.PointerTab)
        self.groupBox_7.setObjectName("groupBox_7")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.groupBox_7)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox_7)
        self.label_4.setObjectName("label_4")
        self.gridLayout_10.addWidget(self.label_4, 0, 0, 1, 1)
        self.pointerScrollFactor = QtWidgets.QSlider(parent=self.groupBox_7)
        self.pointerScrollFactor.setMinimum(1)
        self.pointerScrollFactor.setMaximum(100)
        self.pointerScrollFactor.setPageStep(1)
        self.pointerScrollFactor.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.pointerScrollFactor.setTickPosition(QtWidgets.QSlider.TickPosition.TicksBelow)
        self.pointerScrollFactor.setTickInterval(9)
        self.pointerScrollFactor.setObjectName("pointerScrollFactor")
        self.gridLayout_10.addWidget(self.pointerScrollFactor, 1, 1, 1, 1)
        self.pointerNatScroll = QtWidgets.QCheckBox(parent=self.groupBox_7)
        self.pointerNatScroll.setObjectName("pointerNatScroll")
        self.gridLayout_10.addWidget(self.pointerNatScroll, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox_7)
        self.label_5.setObjectName("label_5")
        self.gridLayout_10.addWidget(self.label_5, 1, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_7)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.PointerUseSettings = QtWidgets.QCheckBox(parent=self.PointerTab)
        self.PointerUseSettings.setObjectName("PointerUseSettings")
        self.horizontalLayout_4.addWidget(self.PointerUseSettings)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.tabWidget.addTab(self.PointerTab, "")
        self.TouchpadTab = QtWidgets.QWidget()
        self.TouchpadTab.setObjectName("TouchpadTab")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.TouchpadTab)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem4 = QtWidgets.QSpacerItem(271, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.TouchPadUseSettings = QtWidgets.QCheckBox(parent=self.TouchpadTab)
        self.TouchPadUseSettings.setObjectName("TouchPadUseSettings")
        self.horizontalLayout.addWidget(self.TouchPadUseSettings)
        self.gridLayout_9.addLayout(self.horizontalLayout, 4, 0, 1, 2)
        self.touchButtonBox = QtWidgets.QGroupBox(parent=self.TouchpadTab)
        self.touchButtonBox.setObjectName("touchButtonBox")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.touchButtonBox)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.lrm = QtWidgets.QRadioButton(parent=self.touchButtonBox)
        self.lrm.setAutoExclusive(True)
        self.lrm.setObjectName("lrm")
        self.gridLayout_7.addWidget(self.lrm, 4, 1, 1, 1)
        self.touchLeftHanded = QtWidgets.QCheckBox(parent=self.touchButtonBox)
        self.touchLeftHanded.setObjectName("touchLeftHanded")
        self.gridLayout_7.addWidget(self.touchLeftHanded, 2, 1, 1, 1)
        self.tap_click = QtWidgets.QCheckBox(parent=self.touchButtonBox)
        self.tap_click.setObjectName("tap_click")
        self.gridLayout_7.addWidget(self.tap_click, 0, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(parent=self.touchButtonBox)
        self.label_13.setObjectName("label_13")
        self.gridLayout_7.addWidget(self.label_13, 6, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(parent=self.touchButtonBox)
        self.label_10.setObjectName("label_10")
        self.gridLayout_7.addWidget(self.label_10, 4, 0, 1, 1)
        self.btn_ClickFinger = QtWidgets.QRadioButton(parent=self.touchButtonBox)
        self.btn_ClickFinger.setObjectName("btn_ClickFinger")
        self.gridLayout_7.addWidget(self.btn_ClickFinger, 7, 1, 1, 1)
        self.DWT = QtWidgets.QCheckBox(parent=self.touchButtonBox)
        self.DWT.setObjectName("DWT")
        self.gridLayout_7.addWidget(self.DWT, 0, 1, 1, 1)
        self.drag_lock = QtWidgets.QCheckBox(parent=self.touchButtonBox)
        self.drag_lock.setObjectName("drag_lock")
        self.gridLayout_7.addWidget(self.drag_lock, 2, 0, 1, 1)
        self.DWTP = QtWidgets.QCheckBox(parent=self.touchButtonBox)
        self.DWTP.setObjectName("DWTP")
        self.gridLayout_7.addWidget(self.DWTP, 1, 1, 1, 1)
        self.drag = QtWidgets.QCheckBox(parent=self.touchButtonBox)
        self.drag.setObjectName("drag")
        self.gridLayout_7.addWidget(self.drag, 1, 0, 1, 1)
        self.touchMiddle = QtWidgets.QCheckBox(parent=self.touchButtonBox)
        self.touchMiddle.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.touchMiddle.setObjectName("touchMiddle")
        self.gridLayout_7.addWidget(self.touchMiddle, 3, 1, 1, 1)
        self.btn_BtnArea = QtWidgets.QRadioButton(parent=self.touchButtonBox)
        self.btn_BtnArea.setObjectName("btn_BtnArea")
        self.gridLayout_7.addWidget(self.btn_BtnArea, 6, 1, 1, 1)
        self.lmr = QtWidgets.QRadioButton(parent=self.touchButtonBox)
        self.lmr.setAutoExclusive(True)
        self.lmr.setObjectName("lmr")
        self.gridLayout_7.addWidget(self.lmr, 5, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_7.addItem(spacerItem5, 8, 0, 1, 2)
        self.gridLayout_9.addWidget(self.touchButtonBox, 0, 1, 2, 1)
        self.touchGeneralBox = QtWidgets.QGroupBox(parent=self.TouchpadTab)
        self.touchGeneralBox.setObjectName("touchGeneralBox")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.touchGeneralBox)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.touchpadID_label = QtWidgets.QLabel(parent=self.touchGeneralBox)
        self.touchpadID_label.setObjectName("touchpadID_label")
        self.gridLayout_6.addWidget(self.touchpadID_label, 0, 0, 1, 1)
        self.touchpadID = QtWidgets.QComboBox(parent=self.touchGeneralBox)
        self.touchpadID.setObjectName("touchpadID")
        self.gridLayout_6.addWidget(self.touchpadID, 0, 1, 1, 1)
        self.eventLabel = QtWidgets.QLabel(parent=self.touchGeneralBox)
        self.eventLabel.setObjectName("eventLabel")
        self.gridLayout_6.addWidget(self.eventLabel, 1, 0, 1, 1)
        self.touchEventsEnabled = QtWidgets.QRadioButton(parent=self.touchGeneralBox)
        self.touchEventsEnabled.setAutoExclusive(True)
        self.touchEventsEnabled.setObjectName("touchEventsEnabled")
        self.gridLayout_6.addWidget(self.touchEventsEnabled, 1, 1, 1, 1)
        self.touchEventsDisabled = QtWidgets.QRadioButton(parent=self.touchGeneralBox)
        self.touchEventsDisabled.setAutoExclusive(True)
        self.touchEventsDisabled.setObjectName("touchEventsDisabled")
        self.gridLayout_6.addWidget(self.touchEventsDisabled, 2, 1, 1, 1)
        self.touchEventsOnExternalMouse = QtWidgets.QRadioButton(parent=self.touchGeneralBox)
        self.touchEventsOnExternalMouse.setAutoExclusive(True)
        self.touchEventsOnExternalMouse.setObjectName("touchEventsOnExternalMouse")
        self.gridLayout_6.addWidget(self.touchEventsOnExternalMouse, 3, 1, 1, 1)
        self.gridLayout_9.addWidget(self.touchGeneralBox, 0, 0, 1, 1)
        self.touchPointerBox = QtWidgets.QGroupBox(parent=self.TouchpadTab)
        self.touchPointerBox.setObjectName("touchPointerBox")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.touchPointerBox)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_7 = QtWidgets.QLabel(parent=self.touchPointerBox)
        self.label_7.setObjectName("label_7")
        self.gridLayout_5.addWidget(self.label_7, 0, 0, 1, 1)
        self.touchAccel = QtWidgets.QSlider(parent=self.touchPointerBox)
        self.touchAccel.setMinimum(-10)
        self.touchAccel.setMaximum(10)
        self.touchAccel.setPageStep(1)
        self.touchAccel.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.touchAccel.setTickPosition(QtWidgets.QSlider.TickPosition.TicksBelow)
        self.touchAccel.setTickInterval(1)
        self.touchAccel.setObjectName("touchAccel")
        self.gridLayout_5.addWidget(self.touchAccel, 0, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(parent=self.touchPointerBox)
        self.label_8.setObjectName("label_8")
        self.gridLayout_5.addWidget(self.label_8, 1, 0, 1, 1)
        self.touchFlat = QtWidgets.QRadioButton(parent=self.touchPointerBox)
        self.touchFlat.setAutoExclusive(True)
        self.touchFlat.setObjectName("touchFlat")
        self.gridLayout_5.addWidget(self.touchFlat, 1, 1, 1, 1)
        self.touchAdaptive = QtWidgets.QRadioButton(parent=self.touchPointerBox)
        self.touchAdaptive.setAutoExclusive(True)
        self.touchAdaptive.setObjectName("touchAdaptive")
        self.gridLayout_5.addWidget(self.touchAdaptive, 2, 1, 1, 1)
        self.touchpadRotationLabel = QtWidgets.QLabel(parent=self.touchPointerBox)
        self.touchpadRotationLabel.setObjectName("touchpadRotationLabel")
        self.gridLayout_5.addWidget(self.touchpadRotationLabel, 3, 0, 1, 1)
        self.touchRotationAngleSlider = QtWidgets.QSlider(parent=self.touchPointerBox)
        self.touchRotationAngleSlider.setMaximum(360)
        self.touchRotationAngleSlider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.touchRotationAngleSlider.setTickPosition(QtWidgets.QSlider.TickPosition.TicksBelow)
        self.touchRotationAngleSlider.setTickInterval(10)
        self.touchRotationAngleSlider.setObjectName("touchRotationAngleSlider")
        self.gridLayout_5.addWidget(self.touchRotationAngleSlider, 3, 1, 1, 1)
        self.touchRotationAngle = QtWidgets.QSpinBox(parent=self.touchPointerBox)
        self.touchRotationAngle.setMaximum(360)
        self.touchRotationAngle.setObjectName("touchRotationAngle")
        self.gridLayout_5.addWidget(self.touchRotationAngle, 3, 2, 1, 1)
        self.gridLayout_9.addWidget(self.touchPointerBox, 1, 0, 1, 1)
        self.touchScrollingBox = QtWidgets.QGroupBox(parent=self.TouchpadTab)
        self.touchScrollingBox.setObjectName("touchScrollingBox")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.touchScrollingBox)
        self.gridLayout_8.setObjectName("gridLayout_8")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_8.addItem(spacerItem6, 0, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(parent=self.touchScrollingBox)
        self.label_12.setObjectName("label_12")
        self.gridLayout_8.addWidget(self.label_12, 0, 1, 1, 1)
        self.touchScrollFactor = QtWidgets.QSlider(parent=self.touchScrollingBox)
        self.touchScrollFactor.setMinimum(1)
        self.touchScrollFactor.setMaximum(100)
        self.touchScrollFactor.setPageStep(1)
        self.touchScrollFactor.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.touchScrollFactor.setTickPosition(QtWidgets.QSlider.TickPosition.TicksBelow)
        self.touchScrollFactor.setTickInterval(9)
        self.touchScrollFactor.setObjectName("touchScrollFactor")
        self.gridLayout_8.addWidget(self.touchScrollFactor, 0, 2, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_8.addItem(spacerItem7, 0, 4, 1, 1)
        self.label_6 = QtWidgets.QLabel(parent=self.touchScrollingBox)
        self.label_6.setObjectName("label_6")
        self.gridLayout_8.addWidget(self.label_6, 1, 1, 1, 1)
        self.touchNatScroll = QtWidgets.QCheckBox(parent=self.touchScrollingBox)
        self.touchNatScroll.setObjectName("touchNatScroll")
        self.gridLayout_8.addWidget(self.touchNatScroll, 1, 2, 1, 2)
        self.label_11 = QtWidgets.QLabel(parent=self.touchScrollingBox)
        self.label_11.setObjectName("label_11")
        self.gridLayout_8.addWidget(self.label_11, 2, 1, 1, 1)
        self.method4 = QtWidgets.QRadioButton(parent=self.touchScrollingBox)
        self.method4.setAutoExclusive(True)
        self.method4.setObjectName("method4")
        self.gridLayout_8.addWidget(self.method4, 2, 2, 1, 1)
        self.method1 = QtWidgets.QRadioButton(parent=self.touchScrollingBox)
        self.method1.setAutoExclusive(True)
        self.method1.setObjectName("method1")
        self.gridLayout_8.addWidget(self.method1, 3, 2, 1, 1)
        self.method2 = QtWidgets.QRadioButton(parent=self.touchScrollingBox)
        self.method2.setAutoExclusive(True)
        self.method2.setObjectName("method2")
        self.gridLayout_8.addWidget(self.method2, 4, 2, 1, 1)
        self.method3 = QtWidgets.QRadioButton(parent=self.touchScrollingBox)
        self.method3.setAutoExclusive(True)
        self.method3.setObjectName("method3")
        self.gridLayout_8.addWidget(self.method3, 5, 2, 1, 1)
        self.scrollButtonList = QtWidgets.QComboBox(parent=self.touchScrollingBox)
        self.scrollButtonList.setEnabled(False)
        self.scrollButtonList.setObjectName("scrollButtonList")
        self.gridLayout_8.addWidget(self.scrollButtonList, 5, 3, 1, 1)
        self.scrollButtonLock = QtWidgets.QCheckBox(parent=self.touchScrollingBox)
        self.scrollButtonLock.setEnabled(False)
        self.scrollButtonLock.setObjectName("scrollButtonLock")
        self.gridLayout_8.addWidget(self.scrollButtonLock, 5, 4, 1, 1)
        self.gridLayout_9.addWidget(self.touchScrollingBox, 2, 0, 1, 2)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_9.addItem(spacerItem8, 3, 0, 1, 2)
        self.tabWidget.addTab(self.TouchpadTab, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.buttonBox = QtWidgets.QDialogButtonBox(parent=self.centralwidget)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Apply|QtWidgets.QDialogButtonBox.StandardButton.Close|QtWidgets.QDialogButtonBox.StandardButton.Help|QtWidgets.QDialogButtonBox.StandardButton.RestoreDefaults)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sway Input Configurator"))
        self.layouts.headerItem().setText(0, _translate("MainWindow", "Layout"))
        self.layouts.headerItem().setText(1, _translate("MainWindow", "Variant"))
        self.addBtn.setToolTip(_translate("MainWindow", "Add layout to the list"))
        self.addBtn.setText(_translate("MainWindow", "Add"))
        self.rmBtn.setToolTip(_translate("MainWindow", "Remove layout from the list."))
        self.rmBtn.setText(_translate("MainWindow", "Remove"))
        self.upBtn.setToolTip(_translate("MainWindow", "Move selected layout up."))
        self.upBtn.setText(_translate("MainWindow", "Up"))
        self.downBtn.setToolTip(_translate("MainWindow", "Move selected layout down."))
        self.downBtn.setText(_translate("MainWindow", "Down"))
        self.caps_lock.setToolTip(_translate("MainWindow", "Initially enables or disables CapsLock on startup."))
        self.shortcutLabel.setText(_translate("MainWindow", "Keyboard shortcut:"))
        self.repeatDelay.setToolTip(_translate("MainWindow", "Amount of time a key must be held before it starts repeating."))
        self.repeatDelay.setSuffix(_translate("MainWindow", " ms"))
        self.caps_lockLabel.setText(_translate("MainWindow", "CapsLock:"))
        self.repeatRate.setToolTip(_translate("MainWindow", "Frequency of key repeats once the repeat_delay has passed."))
        self.repeatRate.setSuffix(_translate("MainWindow", " repeats/s"))
        self.kbdID.setToolTip(_translate("MainWindow", "Keyboard identifier"))
        self.repeatDelayLabel.setText(_translate("MainWindow", "Repeat delay:"))
        self.kbdID_label.setText(_translate("MainWindow", "Keyboard ID:"))
        self.repeatRateLabel.setText(_translate("MainWindow", "Repeat rate:"))
        self.num_lockLabel.setText(_translate("MainWindow", "NumLock:"))
        self.num_lock.setToolTip(_translate("MainWindow", "Initially enables or disables NumLock on startup."))
        self.shortcutName.setToolTip(_translate("MainWindow", "Keyboard shortcut to switch between layouts."))
        self.kbdModel_label.setText(_translate("MainWindow", "Keyboard model:"))
        self.KeyBoardUseSettings.setText(_translate("MainWindow", "Use this settings"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.KeyboardTab), _translate("MainWindow", "Keyboard"))
        self.groupBox_5.setTitle(_translate("MainWindow", "General"))
        self.pointerID.setToolTip(_translate("MainWindow", "Pointer device identifier"))
        self.label.setText(_translate("MainWindow", "Buttons:"))
        self.pointerID_label.setText(_translate("MainWindow", "Pointer device ID:"))
        self.pointerLeftHanded.setToolTip(_translate("MainWindow", "Enables or disables left handed mode."))
        self.pointerLeftHanded.setText(_translate("MainWindow", "Left handed mode"))
        self.pointerMiddle.setToolTip(_translate("MainWindow", "Enables or disables middle click emulation."))
        self.pointerMiddle.setText(_translate("MainWindow", "Press left and right buttons for middle click"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Pointer"))
        self.label_2.setText(_translate("MainWindow", "Pointer speed:"))
        self.pointerAccel.setToolTip(_translate("MainWindow", "Changes the pointer acceleration."))
        self.label_3.setText(_translate("MainWindow", "Acceleration profile:"))
        self.pointerFlat.setToolTip(_translate("MainWindow", "Cursor moves the same distance as the mouse movement."))
        self.pointerFlat.setText(_translate("MainWindow", "Flat"))
        self.pointerAdaptive.setToolTip(_translate("MainWindow", "Cursor travel distance depends on the mouse movement speed."))
        self.pointerAdaptive.setText(_translate("MainWindow", "Adaptive"))
        self.pointerRotationLabel.setText(_translate("MainWindow", "Rotation angle:"))
        self.pointerRotationAngleSlider.setToolTip(_translate("MainWindow", "Sets the rotation angle of the device to the given angle, in degrees clockwise."))
        self.pointerRotationAngle.setToolTip(_translate("MainWindow", "Sets the rotation angle of the device to the given angle, in degrees clockwise."))
        self.groupBox_7.setTitle(_translate("MainWindow", "Scrolling"))
        self.label_4.setText(_translate("MainWindow", "Scrolling:"))
        self.pointerScrollFactor.setToolTip(_translate("MainWindow", "Scroll speed will be scaled by the given value."))
        self.pointerNatScroll.setToolTip(_translate("MainWindow", "Touchscreen like scrolling."))
        self.pointerNatScroll.setText(_translate("MainWindow", "Invert scroll direction"))
        self.label_5.setText(_translate("MainWindow", "Scrolling speed:"))
        self.PointerUseSettings.setText(_translate("MainWindow", "Use this settings"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.PointerTab), _translate("MainWindow", "Pointer device"))
        self.TouchPadUseSettings.setText(_translate("MainWindow", "Use this settings"))
        self.touchButtonBox.setTitle(_translate("MainWindow", "Touchpad buttons"))
        self.lrm.setText(_translate("MainWindow", "2 fingers - right click, 3 - middle"))
        self.touchLeftHanded.setToolTip(_translate("MainWindow", "Enables or disables left handed mode."))
        self.touchLeftHanded.setText(_translate("MainWindow", "Left handed mode"))
        self.tap_click.setText(_translate("MainWindow", "Tap-to-click"))
        self.label_13.setText(_translate("MainWindow", "Click method\n"
"(clickpads only):"))
        self.label_10.setText(_translate("MainWindow", "Tap button mapping:"))
        self.btn_ClickFinger.setToolTip(_translate("MainWindow", "Clicking with 1, 2, 3 fingers triggers a left, right, or middle click, respectively"))
        self.btn_ClickFinger.setText(_translate("MainWindow", "Click fingers"))
        self.DWT.setToolTip(_translate("MainWindow", "Disables touchpad while typing the text"))
        self.DWT.setText(_translate("MainWindow", "Disable while typing"))
        self.drag_lock.setText(_translate("MainWindow", "Tap-and-drag lock"))
        self.DWTP.setToolTip(_translate("MainWindow", "Disables touchpad while using trackpoint device"))
        self.DWTP.setText(_translate("MainWindow", "Disable while trackpointing"))
        self.drag.setText(_translate("MainWindow", "Tap-and-drag"))
        self.touchMiddle.setToolTip(_translate("MainWindow", "Enables or disables middle click emulation."))
        self.touchMiddle.setText(_translate("MainWindow", " Press left and right buttons for\n"
" middle click"))
        self.btn_BtnArea.setToolTip(_translate("MainWindow", "The bottom area of the touchpad is divided into a left, middle and right button area"))
        self.btn_BtnArea.setText(_translate("MainWindow", "Button area"))
        self.lmr.setText(_translate("MainWindow", "2 fingers - middle click, 3 - right"))
        self.touchGeneralBox.setTitle(_translate("MainWindow", "General"))
        self.touchpadID_label.setText(_translate("MainWindow", "Touchpad ID:"))
        self.touchpadID.setToolTip(_translate("MainWindow", "Touchpad identifier"))
        self.eventLabel.setText(_translate("MainWindow", "Touchpad events:"))
        self.touchEventsEnabled.setToolTip(_translate("MainWindow", "Send events normally"))
        self.touchEventsEnabled.setText(_translate("MainWindow", "Enable"))
        self.touchEventsDisabled.setToolTip(_translate("MainWindow", "Touchpad only stops sending events but not get fully disabled"))
        self.touchEventsDisabled.setText(_translate("MainWindow", "Disable"))
        self.touchEventsOnExternalMouse.setToolTip(_translate("MainWindow", "Disable touchpad while an external mouse is plugged in"))
        self.touchEventsOnExternalMouse.setText(_translate("MainWindow", "Disable when external mouse is plugged in"))
        self.touchPointerBox.setTitle(_translate("MainWindow", "Pointer"))
        self.label_7.setText(_translate("MainWindow", "Pointer speed:"))
        self.touchAccel.setToolTip(_translate("MainWindow", "Changes the pointer acceleration."))
        self.label_8.setText(_translate("MainWindow", "Acceleration profile:"))
        self.touchFlat.setToolTip(_translate("MainWindow", "Cursor moves the same distance as the mouse movement."))
        self.touchFlat.setText(_translate("MainWindow", "Flat"))
        self.touchAdaptive.setToolTip(_translate("MainWindow", "Cursor travel distance depends on the mouse movement speed."))
        self.touchAdaptive.setText(_translate("MainWindow", "Adaptive"))
        self.touchpadRotationLabel.setText(_translate("MainWindow", "Rotation angle:"))
        self.touchRotationAngleSlider.setToolTip(_translate("MainWindow", "Sets the rotation angle of the device to the given angle, in degrees clockwise."))
        self.touchRotationAngle.setToolTip(_translate("MainWindow", "Sets the rotation angle of the device to the given angle, in degrees clockwise."))
        self.touchScrollingBox.setTitle(_translate("MainWindow", "Scrolling"))
        self.label_12.setText(_translate("MainWindow", "Scrolling speed:"))
        self.touchScrollFactor.setToolTip(_translate("MainWindow", "Scroll speed will be scaled by the given value."))
        self.label_6.setText(_translate("MainWindow", "Scrolling:"))
        self.touchNatScroll.setToolTip(_translate("MainWindow", "Touchscreen like scrolling."))
        self.touchNatScroll.setText(_translate("MainWindow", "Invert scroll direction"))
        self.label_11.setText(_translate("MainWindow", "Scrolling method:"))
        self.method4.setText(_translate("MainWindow", "No scroll"))
        self.method1.setText(_translate("MainWindow", "Two fingers"))
        self.method2.setText(_translate("MainWindow", "Touchpad edges"))
        self.method3.setText(_translate("MainWindow", "On button down"))
        self.scrollButtonList.setToolTip(_translate("MainWindow", "Sets the button used for scroll_method on_button_down."))
        self.scrollButtonLock.setToolTip(_translate("MainWindow", "Enables or disables scroll button lock for specified input device."))
        self.scrollButtonLock.setText(_translate("MainWindow", "Scroll button lock"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.TouchpadTab), _translate("MainWindow", "Touchpad"))
