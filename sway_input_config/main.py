#!/usr/bin/env python3

import os
import sys
from PySide2.QtWidgets import (QApplication, QWidget, QVBoxLayout, QComboBox,
                               QDialog, QCheckBox, QHBoxLayout, QSpinBox,
                               QSlider, QPushButton, QDialogButtonBox,
                               QFormLayout, QRadioButton, QGridLayout,
                               QGroupBox, QLineEdit, QLabel,
                               QMainWindow, QTabWidget, QStyle)
from PySide2.QtCore import Qt
from PySide2.QtGui import QPixmap
from sway_input_config.utils import (get_data_dir, load_json, save_json,
                                     save_list_to_text_file, reload)

data_dir = ""
config_home = os.getenv('XDG_CONFIG_HOME') if os.getenv('XDG_CONFIG_HOME') else os.path.join(
    os.getenv("HOME"), ".config/")

data_home = os.getenv('XDG_DATA_HOME') if os.getenv('XDG_DATA_HOME') else os.path.join(
    os.getenv("HOME"), ".config/")

sway_config = os.path.join(config_home, "sway", "config")

dir_name = os.path.dirname(__file__)
shortcut_list = os.path.join(dir_name, "data/shortcuts.json")
kbd_model_list = os.path.join(dir_name, "data/kbd_model.json")
layouts_list = os.path.join(dir_name, "data/layouts.json")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(700, 650)
        self.mainWindow = QWidget()
        self.vbox = QVBoxLayout(self.mainWindow)
        self.hbox = QHBoxLayout()
        self.buttonBox = QDialogButtonBox()
        self.btnApply = QPushButton("Apply")
        self.btnApply.setIcon(self.style().standardIcon(QStyle.SP_DialogApplyButton))
        self.btnApply.clicked.connect(self.on_clicked_apply)
        self.btnCancel = QPushButton("Close")
        self.btnCancel.setIcon(self.style().standardIcon(QStyle.SP_DialogCloseButton))
        self.btnCancel.clicked.connect(self.cancel)
        self.buttonBox.addButton(self.btnApply, QDialogButtonBox.AcceptRole)
        self.buttonBox.addButton(self.btnCancel, QDialogButtonBox.RejectRole)
        self.btnAbout = QPushButton("About")
        self.btnAbout.setIcon(self.style().standardIcon(QStyle.SP_DialogHelpButton))
        self.btnAbout.clicked.connect(self.on_clicked_about)
        self.tabWidget = QTabWidget()
        self.tabWidget.addTab(KeyboardTab(), "Keyboard")
        self.tabWidget.addTab(MouseTab(), "Mouse")
        self.tabWidget.addTab(TouchpadTab(), "Touchpad")
        self.vbox.addWidget(self.tabWidget)
        self.hbox.addWidget(self.btnAbout)
        self.hbox.addWidget(self.buttonBox)
        self.vbox.addLayout(self.hbox)
        self.setLayout(self.vbox)
        self.setCentralWidget(self.mainWindow)
        self.show()

    def on_clicked_about(self):
        self.about = QDialog(self.mainWindow)
        self.about.setWindowTitle("About Sway Input Configurator")
        self.about.setFixedSize(400, 400)
        self.vLayout = QVBoxLayout()
        self.vLayout2 = QVBoxLayout()
        self.hLayout = QHBoxLayout()
        self.groupBox = QGroupBox()
        self.vLayout.addWidget(self.groupBox)

        self.closeBtn = QPushButton("Close")
        self.closeBtn.setIcon(self.style().standardIcon(QStyle.SP_DialogCloseButton))
        self.closeBtn.clicked.connect(self.about.reject)

        self.logo = QLabel()
        self.pixmap = QPixmap(os.path.join(dir_name, "data/logo_sic.png"))
        self.logo.setPixmap(self.pixmap)

        self.desc = QLabel()
        self.desc_text = ["\nA simple input devices configurator for SwayWM,\n"
                          "written in Python and Qt5/PySide2. "
                          "It uses standard\nlibinput options to configure "
                          "keyboard, touchpad\nand pointer devices"]
        self.desc.setText(self.desc_text[0])

        self.copyright = QLabel()
        self.copyright_text = ["Version: 1.1.0.\n"
                               "Licensed under the GNU GPLv3.\n"
                               "Copyright: 2022 Aleksey Samoilov"]
        self.copyright.setText(self.copyright_text[0])

        self.url = QLabel()
        self.urlLink = "<a href=\"https://github.com/Sunderland93/sway-input-config\">GitHub</a>"
        self.url.setText(self.urlLink)
        self.url.setOpenExternalLinks(True)

        self.hLayout.addWidget(self.closeBtn, 0, Qt.AlignRight)
        self.vLayout2.addWidget(self.logo, 0, Qt.AlignCenter)
        self.vLayout2.addWidget(self.desc, 0, Qt.AlignCenter)
        self.vLayout2.addWidget(self.copyright, 0, Qt.AlignCenter)
        self.vLayout2.addWidget(self.url, 0, Qt.AlignCenter)
        self.vLayout.addLayout(self.hLayout)
        self.groupBox.setLayout(self.vLayout2)
        self.about.setLayout(self.vLayout)
        self.about.exec()

    def on_clicked_apply(self):
        save_to_config()
        f = os.path.join(data_dir, "settings")
        print("Saving {}".format(f))
        save_json(settings, f)

    def cancel(self):
        self.close()


class KeyboardTab(QWidget):
    def __init__(self):
        super().__init__()
        self.vbox = QVBoxLayout()
        self.gridLayout = QGridLayout()
        self.groupBox = QGroupBox("Keyboard settings")
        self.vbox.addWidget(self.groupBox)

        self.KeyBoardUseSettings = QCheckBox("Use this settings")
        if settings["keyboard-use-settings"] == "true":
            self.KeyBoardUseSettings.setChecked(True)
        self.KeyBoardUseSettings.toggled.connect(self.keyboard_use_settings)

        self.layoutList = QComboBox()
        self.layoutList.setStyleSheet("QComboBox { combobox-popup: 0; }")
        layout = load_json(layouts_list)
        for key, value in layout.items():
            self.layoutList.addItem(key)

        self.layoutName = QLineEdit()
        self.layoutLabel = QLabel("Layout:")
        layout = load_json(layouts_list)
        layout_list = []
        for key, value in layout.items():
            layout_list.append('{}'.format(','.join(settings["keyboard-layout"])))
        self.layoutName.setText(layout_list[0])

        self.addBtn = QPushButton("Add")
        self.addBtn.setToolTip("Add selected layout to the list")
        self.addBtn.clicked.connect(self.add_layout)

        self.variantName = QLineEdit()
        self.labelVariant = QLabel("Variant:")
        self.variantName.setToolTip("Variant of the keyboard like 'dvorak' or 'colemak'.")
        self.variantName.setMaxLength(30)
        variant_list = []
        variant_list.append('{}'.format(','.join(settings["keyboard-variant"])))
        self.variantName.setText(variant_list[0])
        self.variantName.textChanged.connect(self.on_variant_changed)

        self.shortcutName = QComboBox()
        self.shortcutName.setToolTip("Keyboard shortcut for switch between layouts.")
        self.shortcutName.setStyleSheet("QComboBox { combobox-popup: 0; }")
        self.shortcutLabel = QLabel("Shortcut:")
        shortcut_data = load_json(shortcut_list)
        for item in shortcut_data:
            self.shortcutName.addItem(item)
        for key, value in shortcut_data.items():
            if value == settings["keyboard-shortcut"]:
                self.shortcutName.setCurrentText(key)
        self.shortcutName.activated.connect(self.set_shortcut)

        self.kbdModel = QComboBox()
        self.kbdModel.setStyleSheet("QComboBox { combobox-popup: 0; }")
        self.kbdModel_label = QLabel("Keyboard model:")
        model_list = load_json(kbd_model_list)
        for item in model_list:
            self.kbdModel.addItem(item)
        for key, value in model_list.items():
            if value == settings["keyboard-model"]:
                self.kbdModel.setCurrentText(key)
        self.kbdModel.activated.connect(self.set_model)

        self.repeatDelaySlider = QSlider(Qt.Orientation.Horizontal)
        self.repeatDelaySlider.setRange(1, 6000)
        self.repeatDelaySlider.setPageStep(50)
        self.repeatDelaySlider.setValue(settings["keyboard-repeat-delay"])

        self.repeatDelay = QSpinBox()
        self.repeatDelayLabel = QLabel("Repeat delay:")
        self.repeatDelay.setToolTip("Amount of time a key must be held before it starts repeating.")
        self.repeatDelay.setRange(1, 6000)
        self.repeatDelay.setSingleStep(1)
        self.repeatDelay.setSuffix(" ms")
        self.repeatDelay.setValue(self.repeatDelaySlider.value())
        self.repeatDelay.valueChanged.connect(self.repeatDelaySlider.setValue)
        self.repeatDelaySlider.sliderMoved.connect(self.repeatDelay.setValue)
        self.repeatDelaySlider.valueChanged.connect(self.on_repeat_delay_value_changed)

        self.repeatRateSlider = QSlider(Qt.Orientation.Horizontal)
        self.repeatRateSlider.setRange(1, 4000)
        self.repeatRateSlider.setPageStep(50)
        self.repeatRateSlider.setValue(settings["keyboard-repeat-rate"])

        self.repeatRate = QSpinBox()
        self.repeatRateLabel = QLabel("Repeat rate:")
        self.repeatRate.setToolTip("Frequency of key repeats once the repeat_delay has passed.")
        self.repeatRate.setRange(1, 4000)
        self.repeatRate.setSingleStep(1)
        self.repeatRate.setSuffix(" repeats/s")
        self.repeatRate.setValue(self.repeatRateSlider.value())
        self.repeatRate.valueChanged.connect(self.repeatRateSlider.setValue)
        self.repeatRateSlider.sliderMoved.connect(self.repeatRate.setValue)
        self.repeatRateSlider.valueChanged.connect(self.on_repeat_rate_value_changed)

        self.caps_lock = QCheckBox()
        self.caps_lockLabel = QLabel("CapsLock:")
        if settings["keyboard-capslock"] == "enabled":
            self.caps_lock.setChecked(True)
        self.caps_lock.setToolTip("Initially enables or disables CapsLock on startup.")
        self.caps_lock.toggled.connect(self.on_caps_lock_checked)

        self.num_lock = QCheckBox()
        self.num_lockLabel = QLabel("NumLock:")
        if settings["keyboard-numlock"] == "enabled":
            self.num_lock.setChecked(True)
        self.num_lock.setToolTip("Initially enables or disables NumLock on startup.")
        self.num_lock.toggled.connect(self.on_num_lock_checked)

        self.vbox2 = QVBoxLayout()

        self.gridLayout.addWidget(self.layoutLabel, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.layoutName, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.layoutList, 0, 2, 1, 1)
        self.gridLayout.addWidget(self.addBtn, 0, 3, 1, 1)
        self.gridLayout.addWidget(self.labelVariant, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.variantName, 1, 1, 1, 1)
        self.gridLayout.addWidget(self.shortcutLabel, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.shortcutName, 2, 1, 1, 1)
        self.gridLayout.addWidget(self.kbdModel_label, 3, 0, 1, 1)
        self.gridLayout.addWidget(self.kbdModel, 3, 1, 1, 1)
        self.gridLayout.addWidget(self.repeatDelayLabel, 4, 0, 1, 1)
        self.gridLayout.addWidget(self.repeatDelaySlider, 4, 1, 1, 1)
        self.gridLayout.addWidget(self.repeatDelay, 4, 2, 1, 1)
        self.gridLayout.addWidget(self.repeatRateLabel, 5, 0, 1, 1)
        self.gridLayout.addWidget(self.repeatRateSlider, 5, 1, 1, 1)
        self.gridLayout.addWidget(self.repeatRate, 5, 2, 1, 1)
        self.gridLayout.addWidget(self.caps_lockLabel, 6, 0, 1, 1)
        self.gridLayout.addWidget(self.caps_lock, 6, 1, 1, 1)
        self.gridLayout.addWidget(self.num_lockLabel, 7, 0, 1, 1)
        self.gridLayout.addWidget(self.num_lock, 7, 1, 1, 1)
        self.vbox2.addLayout(self.gridLayout)
        self.vbox2.addStretch()
        self.vbox2.addWidget(self.KeyBoardUseSettings, 0, Qt.AlignRight)
        self.groupBox.setLayout(self.vbox2)
        self.setLayout(self.vbox)

    def keyboard_use_settings(self):
        if self.KeyBoardUseSettings.isChecked() is True:
            settings["keyboard-use-settings"] = "true"
        else:
            settings["keyboard-use-settings"] = "false"

    def set_shortcut(self):
        data = load_json(shortcut_list)
        for key in data.keys():
            settings["keyboard-shortcut"] = data[self.shortcutName.currentText()]

    def set_model(self):
        model_data = load_json(kbd_model_list)
        for key in model_data.keys():
            settings["keyboard-model"] = model_data[self.kbdModel.currentText()]

    def add_layout(self):
        layout_data = load_json(layouts_list)
        layout = self.layoutList.currentText()
        for key, value in layout_data.items():
            if key in layout:
                self.layoutName.insert(",")
                self.layoutName.insert(value)
        settings["keyboard-layout"] = self.layoutName.text()

    def on_variant_changed(self):
        settings["keyboard-variant"] = self.variantName.text()

    def on_repeat_delay_value_changed(self):
        settings["keyboard-repeat-delay"] = self.repeatDelay.value()

    def on_repeat_rate_value_changed(self):
        settings["keyboard-repeat-rate"] = self.repeatRate.value()

    def on_caps_lock_checked(self):
        if self.caps_lock.isChecked():
            settings["keyboard-capslock"] = "enabled"
        else:
            settings["keyboard-capslock"] = "disabled"

    def on_num_lock_checked(self):
        if self.num_lock.isChecked():
            settings["keyboard-numlock"] = "enabled"
        else:
            settings["keyboard-numlock"] = "disabled"


class MouseTab(QWidget):
    def __init__(self):
        super().__init__()

        self.gridLayout = QGridLayout()
        self.formLayout = QFormLayout()
        self.vbox = QVBoxLayout()
        self.vbox2 = QVBoxLayout()
        self.groupBox = QGroupBox("Pointer device settings")
        self.vbox.addWidget(self.groupBox)

        self.PointerUseSettings = QCheckBox("Use this settings")
        if settings["pointer-use-settings"] == "true":
            self.PointerUseSettings.setChecked(True)
        self.PointerUseSettings.toggled.connect(self.pointer_use_settings)

        # Acceleration
        self.accel = QSlider(Qt.Orientation.Horizontal)
        self.accel.setToolTip("Changes the pointer acceleration. [<-1|1>]")
        self.accel_label = QLabel("Pointer speed:")
        self.accel.setTickPosition(QSlider.TicksBelow)
        self.accel.setRange(-10, 10)
        self.accel.setSingleStep(1)
        self.accel.setPageStep(1)
        self.accel.setTickInterval(1)
        self.accel.setValue(float(settings["pointer-pointer-accel"]) * 10)
        self.accel.valueChanged.connect(self.on_accel_value_changed)

        # Acceleration profile
        self.Flat = QRadioButton("Flat")
        self.Flat.setToolTip("Cursor moves the same distance as the mouse movement.")
        self.profile_label = QLabel("Acceleration profile:")
        self.Adaptive = QRadioButton("Adaptive")
        self.Adaptive.setToolTip("Cursor travel distance depends on the mouse movement speed.")
        if settings["pointer-accel-profile"] == "flat":
            self.Flat.setChecked(True)
        else:
            self.Adaptive.setChecked(True)
        self.Flat.clicked.connect(self.on_accel_profile_changed)
        self.Adaptive.clicked.connect(self.on_accel_profile_changed)

        # Natural scrolling
        self.natScroll = QCheckBox("Invert scroll direction")
        self.natScroll.setToolTip("Touchscreen like scrolling.")
        self.natScroll_label = QLabel("Natural scroll:")
        if settings["pointer-natural-scroll"] == "true":
            self.natScroll.setChecked(True)
        self.natScroll.toggled.connect(self.on_nat_scroll_checked)

        # Scrolling speed
        self.scrollFactor = QSlider(Qt.Orientation.Horizontal)
        self.scrollFactor.setToolTip("Scroll speed will be scaled by the given value.")
        self.scrollFactor_label = QLabel("Scrolling speed:")
        self.scrollFactor.setTickPosition(QSlider.TicksBelow)
        self.scrollFactor.setTickInterval(9)
        self.scrollFactor.setRange(1, 100)
        self.scrollFactor.setSingleStep(1)
        self.scrollFactor.setValue(float(settings["pointer-scroll-factor"]) * 10)
        self.scrollFactor.valueChanged.connect(self.on_scroll_value_changed)

        # Left handed mode
        self.leftHanded = QCheckBox("Left handed mode")
        self.leftHanded.setToolTip("Enables or disables left handed mode.")
        if settings["pointer-left-handed"] == "true":
            self.leftHanded.setChecked(True)
        self.leftHanded.toggled.connect(self.on_left_handed_checked)

        # Middle click by pressing left and right
        self.middle = QCheckBox("Press left and right buttons for middle click")
        self.middle.setToolTip("Enables or disables middle click emulation.")
        if settings["pointer-middle-emulation"] == "enabled":
            self.middle.setChecked(True)
        self.middle.toggled.connect(self.on_middle_checked)

        self.formLayout.addRow(QLabel("General:"), self.leftHanded)
        self.formLayout.addRow(QLabel(), self.middle)
        self.formLayout.addRow(QLabel("Pointer speed:"), self.accel)
        self.formLayout.addRow(QLabel("Acceleration profile:"), self.Flat)
        self.formLayout.addRow(QLabel(), self.Adaptive)
        self.formLayout.addRow(QLabel("Scrolling:"), self.natScroll)
        self.formLayout.addRow(QLabel("Scrolling speed:"), self.scrollFactor)

        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.addLayout(self.formLayout, 0, 1, 1, 1)
        self.gridLayout.setColumnStretch(2, 1)
        self.vbox2.addLayout(self.gridLayout)
        self.vbox2.addStretch()
        self.vbox2.addWidget(self.PointerUseSettings, 0, Qt.AlignRight)
        self.groupBox.setLayout(self.vbox2)
        self.setLayout(self.vbox)

    def pointer_use_settings(self):
        if self.PointerUseSettings.isChecked() is True:
            settings["pointer-use-settings"] = "true"
        else:
            settings["pointer-use-settings"] = "false"

    def on_accel_profile_changed(self):
        if self.Flat.isChecked():
            settings["pointer-accel-profile"] = "flat"
        else:
            settings["pointer-accel-profile"] = "adaptive"

    def on_accel_value_changed(self):
        settings["pointer-pointer-accel"] = self.accel.value() / 10

    def on_nat_scroll_checked(self):
        if self.natScroll.isChecked() is True:
            settings["pointer-natural-scroll"] = "true"
        else:
            settings["pointer-natural-scroll"] = "false"

    def on_scroll_value_changed(self):
        settings["pointer-scroll-factor"] = self.scrollFactor.value() / 10

    def on_left_handed_checked(self):
        if self.leftHanded.isChecked() is True:
            settings["pointer-left-handed"] = "true"
        else:
            settings["pointer-left-handed"] = "false"

    def on_middle_checked(self):
        if self.middle.isChecked():
            settings["pointer-middle-emulation"] = "enabled"
        else:
            settings["pointer-middle-emulation"] = "disabled"


class TouchpadTab(QWidget):
    def __init__(self):
        super().__init__()

        self.gridLayout = QGridLayout()
        self.formLayout = QFormLayout()
        self.vbox = QVBoxLayout()
        self.vbox2 = QVBoxLayout()
        self.groupBox = QGroupBox("Touchpad settings")
        self.vbox.addWidget(self.groupBox)

        self.TouchPadUseSettings = QCheckBox("Use this settings")
        if settings["touchpad-use-settings"] == "true":
            self.TouchPadUseSettings.setChecked(True)
        self.TouchPadUseSettings.toggled.connect(self.touchpad_use_settings)

        # Acceleration profile
        self.Flat = QRadioButton("Flat")
        self.Flat.setToolTip("Cursor moves the same distance as the mouse movement.")
        self.Adaptive = QRadioButton("Adaptive")
        self.Adaptive.setToolTip("Cursor travel distance depends on the mouse movement speed.")
        if settings["touchpad-accel-profile"] == "flat":
            self.Flat.setChecked(True)
        else:
            self.Adaptive.setChecked(True)
        self.Flat.clicked.connect(self.on_accel_profile_changed)
        self.Adaptive.clicked.connect(self.on_accel_profile_changed)

        # Acceleration
        self.accel = QSlider(Qt.Orientation.Horizontal)
        self.accel.setToolTip("Changes the pointer acceleration. [<-1|1>]")
        self.accel.setTickPosition(QSlider.TicksBelow)
        self.accel.setRange(-10, 10)
        self.accel.setSingleStep(1)
        self.accel.setPageStep(1)
        self.accel.setTickInterval(1)
        self.accel.setValue(float(settings["touchpad-pointer-accel"]) * 10)
        self.accel.valueChanged.connect(self.on_accel_value_changed)

        # Scrolling speed
        self.scrollFactor = QSlider(Qt.Orientation.Horizontal)
        self.scrollFactor.setToolTip("Scroll speed will be scaled by the given value.")
        self.scrollFactor.setTickPosition(QSlider.TicksBelow)
        self.scrollFactor.setTickInterval(9)
        self.scrollFactor.setRange(1, 100)
        self.scrollFactor.setSingleStep(1)
        self.scrollFactor.setValue(float(settings["touchpad-scroll-factor"]) * 10)
        self.scrollFactor.valueChanged.connect(self.on_scroll_value_changed)

        # Natural scrolling
        self.natScroll = QCheckBox("Invert scroll direction")
        self.natScroll.setToolTip("Touchscreen like scrolling.")
        if settings["touchpad-natural-scroll"] == "enabled":
            self.natScroll.setChecked(True)
        self.natScroll.toggled.connect(self.on_nat_scroll_checked)

        # Scrolling method
        self.method1 = QRadioButton("Two fingers")
        self.method2 = QRadioButton("Touchpad edges")
        self.method3 = QRadioButton("On button down")
        self.method4 = QRadioButton("No scroll")
        if settings["touchpad-scroll-method"] == "two_finger":
            self.method1.setChecked(True)
        elif settings["touchpad-scroll-method"] == "edge":
            self.method2.setChecked(True)
        elif settings["touchpad-scroll-method"] == "on_button_down":
            self.method3.setChecked(True)
        else:
            self.method4.setChecked(True)
        self.method1.clicked.connect(self.on_scroll_method_checked)
        self.method2.clicked.connect(self.on_scroll_method_checked)
        self.method3.clicked.connect(self.on_scroll_method_checked)
        self.method4.clicked.connect(self.on_scroll_method_checked)

        # Left handed mode
        self.leftHanded = QCheckBox("Left handed mode")
        self.leftHanded.setToolTip("Enables or disables left handed mode.")
        if settings["touchpad-left-handed"] == "enabled":
            self.leftHanded.setChecked(True)
        self.leftHanded.toggled.connect(self.on_left_handed_checked)

        # Middle button emulation
        self.middleEmu = QCheckBox("Press left and right buttons for middle click")
        self.middleEmu.setToolTip("Enables or disables middle click emulation.")
        if settings["touchpad-middle-emulation"] == "enabled":
            self.middleEmu.setChecked(True)
        self.middleEmu.toggled.connect(self.on_middle_emu_checked)

        # Tap-to-click
        self.tap_click = QCheckBox("Tap-to-click")
        self.tap_click.setToolTip("Enables or disables tap-to-click.")
        if settings["touchpad-tap"] == "enabled":
            self.tap_click.setChecked(True)
        self.tap_click.toggled.connect(self.on_tap_click_checked)

        # Tap-and-drag
        self.drag = QCheckBox("Tap-and-drag")
        self.drag.setToolTip("Enables or disables tap-and-drag.")
        if settings["touchpad-tap"] == "enabled":
            self.drag.setEnabled(True)
        else:
            self.drag.setEnabled(False)
        if settings["touchpad-drag"] == "enabled":
            self.drag.setChecked(True)
        self.drag.toggled.connect(self.on_tapdrag_checked)

        # Tap-and-drag lock
        self.dragLock = QCheckBox("Tap-and-drag lock")
        self.dragLock.setToolTip("Enables or disables drag lock.")
        if settings["touchpad-tap"] == "enabled":
            self.dragLock.setEnabled(True)
        else:
            self.dragLock.setEnabled(False)
        if settings["touchpad-drag-lock"] == "enabled":
            self.dragLock.setChecked(True)
        self.dragLock.toggled.connect(self.on_draglock_checked)

        # Multi tapping
        self.lrm = QRadioButton("Two-tap right, three middle")
        self.lmr = QRadioButton("Two-tap middle, three right")
        if settings["touchpad-tap"] == "enabled":
            self.lrm.setEnabled(True)
            self.lmr.setEnabled(True)
        else:
            self.lrm.setEnabled(False)
            self.lmr.setEnabled(False)
        if settings["touchpad-tap-button-map"] == "lrm":
            self.lrm.setChecked(True)
        else:
            self.lmr.setChecked(True)
        self.lrm.clicked.connect(self.on_multi_tap_checked)
        self.lmr.clicked.connect(self.on_multi_tap_checked)

        # Disable while typing
        self.DWT = QCheckBox("Disable while typing")
        self.DWT.setToolTip("Enables or disables disable-while-typing.")
        if settings["touchpad-dwt"] == "enabled":
            self.DWT.setChecked(True)
        self.DWT.toggled.connect(self.on_dwt_checked)

        self.formLayout.addRow(QLabel("General:"), self.DWT)
        self.formLayout.addRow(QLabel(), self.leftHanded)
        self.formLayout.addRow(QLabel(), self.middleEmu)
        self.formLayout.addRow(QLabel("Pointer speed:"), self.accel)
        self.formLayout.addRow(QLabel("Acceleration profile:"), self.Flat)
        self.formLayout.addRow(QLabel(), self.Adaptive)
        self.formLayout.addRow(QLabel("Tapping:"), self.tap_click)
        self.formLayout.addRow(QLabel(), self.drag)
        self.formLayout.addRow(QLabel(), self.dragLock)
        self.formLayout.addRow(QLabel("Two-finger tap:"), self.lrm)
        self.formLayout.addRow(QLabel(), self.lmr)
        self.formLayout.addRow(QLabel("Scrolling:"), self.method1)
        self.formLayout.addRow(QLabel(), self.method2)
        self.formLayout.addRow(QLabel(), self.method3)
        self.formLayout.addRow(QLabel(), self.method4)
        self.formLayout.addRow(QLabel(), self.natScroll)
        self.formLayout.addRow(QLabel("Scrolling speed:"), self.scrollFactor)

        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.addLayout(self.formLayout, 0, 1, 1, 1)
        self.gridLayout.setColumnStretch(2, 1)
        self.vbox2.addLayout(self.gridLayout)
        self.vbox2.addStretch()
        self.vbox2.addWidget(self.TouchPadUseSettings, 0, Qt.AlignRight)
        self.groupBox.setLayout(self.vbox2)
        self.setLayout(self.vbox)

    def touchpad_use_settings(self):
        if self.TouchPadUseSettings.isChecked() is True:
            settings["touchpad-use-settings"] = "true"
        else:
            settings["touchpad-use-settings"] = "false"

    def on_accel_value_changed(self):
        settings["touchpad-pointer-accel"] = self.accel.value() / 10

    def on_scroll_value_changed(self):
        settings["touchpad-scroll-factor"] = self.scrollFactor.value() / 10

    def on_accel_profile_changed(self):
        if self.Flat.isChecked():
            settings["touchpad-accel-profile"] = "flat"
        else:
            settings["touchpad-accel-profile"] = "adaptive"

    def on_nat_scroll_checked(self):
        if self.natScroll.isChecked() is True:
            settings["touchpad-natural-scroll"] = "enabled"
        else:
            settings["touchpad-natural-scroll"] = "disabled"

    def on_scroll_method_checked(self):
        if self.method1.isChecked() is True:
            settings["touchpad-scroll-method"] = "two_finger"
        elif self.method2.isChecked() is True:
            settings["touchpad-scroll-method"] = "edge"
        elif self.method3.isChecked() is True:
            settings["touchpad-scroll-method"] = "on_button_down"
        else:
            settings["touchpad-scroll-method"] = "none"

    def on_left_handed_checked(self):
        if self.leftHanded.isChecked():
            settings["touchpad-left-handed"] = "enabled"
        else:
            settings["touchpad-left-handed"] = "disabled"

    def on_tap_click_checked(self):
        if self.tap_click.isChecked():
            settings["touchpad-tap"] = "enabled"
            self.drag.setEnabled(True)
            self.dragLock.setEnabled(True)
            self.lrm.setEnabled(True)
            self.lmr.setEnabled(True)
        else:
            settings["touchpad-tap"] = "disabled"
            self.drag.setEnabled(False)
            self.dragLock.setEnabled(False)
            self.lrm.setEnabled(False)
            self.lmr.setEnabled(False)

    def on_multi_tap_checked(self):
        if self.lrm.isChecked():
            settings["touchpad-tap-button-map"] = "lrm"
        else:
            settings["touchpad-tap-button-map"] = "lmr"

    def on_middle_emu_checked(self):
        if self.middleEmu.isChecked():
            settings["touchpad-middle-emulation"] = "enabled"
        else:
            settings["touchpad-middle-emulation"] = "disabled"

    def on_tapdrag_checked(self):
        if self.drag.isChecked():
            settings["touchpad-drag"] = "enabled"
        else:
            settings["touchpad-drag"] = "disabled"

    def on_draglock_checked(self):
        if self.dragLock.isChecked():
            settings["touchpad-drag-lock"] = "enabled"
        else:
            settings["touchpad-drag-lock"] = "disabled"

    def on_dwt_checked(self):
        if self.DWT.isChecked():
            settings["touchpad-dwt"] = "enabled"
        else:
            settings["touchpad-dwt"] = "disabled"


def save_to_config():
    if settings["keyboard-use-settings"] == "true":

        lines = ['input "type:keyboard" {']
        if settings["keyboard-layout"]:
            lines.append('  xkb_layout {}'.format(','.join(settings["keyboard-layout"])))
        if settings["keyboard-variant"]:
            lines.append('  xkb_variant {}'.format(','.join(settings["keyboard-variant"])))
        if settings["keyboard-shortcut"]:
            lines.append('  xkb_options {}'.format(settings["keyboard-shortcut"]))
        lines.append('  xkb_model {}'.format(settings["keyboard-model"]))
        lines.append('  repeat_delay {}'.format(settings["keyboard-repeat-delay"]))
        lines.append('  repeat_rate {}'.format(settings["keyboard-repeat-rate"]))
        lines.append('  xkb_capslock {}'.format(settings["keyboard-capslock"]))
        lines.append('  xkb_numlock {}'.format(settings["keyboard-numlock"]))
        lines.append('}')

        save_list_to_text_file(lines, os.path.join(config_home, "sway/keyboard"))

    if settings["pointer-use-settings"] == "true":

        lines = ['input "type:pointer" {', '  accel_profile {}'.format(settings["pointer-accel-profile"]),
                 '  pointer_accel {}'.format(settings["pointer-pointer-accel"]),
                 '  natural_scroll {}'.format(settings["pointer-natural-scroll"]),
                 '  scroll_factor {}'.format(settings["pointer-scroll-factor"]),
                 '  left_handed {}'.format(settings["pointer-left-handed"]),
                 '  middle_emulation {}'.format(settings["pointer-middle-emulation"])]
        lines.append('}')

        save_list_to_text_file(lines, os.path.join(config_home, "sway/pointer"))

    if settings["touchpad-use-settings"] == "true":
        lines = ['input "type:touchpad" {', '  accel_profile {}'.format(settings["touchpad-accel-profile"]),
                 '  pointer_accel {}'.format(settings["touchpad-pointer-accel"]),
                 '  natural_scroll {}'.format(settings["touchpad-natural-scroll"]),
                 '  scroll_factor {}'.format(settings["touchpad-scroll-factor"]),
                 '  scroll_method {}'.format(settings["touchpad-scroll-method"]),
                 '  left_handed {}'.format(settings["touchpad-left-handed"]),
                 '  tap {}'.format(settings["touchpad-tap"]),
                 '  tap_button_map {}'.format(settings["touchpad-tap-button-map"]),
                 '  drag {}'.format(settings["touchpad-drag"]), '  drag_lock {}'.format(settings["touchpad-drag-lock"]),
                 '  dwt {}'.format(settings["touchpad-dwt"]),
                 '  middle_emulation {}'.format(settings["touchpad-middle-emulation"])]
        lines.append('}')

        save_list_to_text_file(lines, os.path.join(config_home, "sway/touchpad"))

    reload()


def load_settings():
    defaults_file = os.path.join(dir_name, "data/defaults.json")
    settings_file = os.path.join(data_dir, "settings")
    global settings
    if os.path.isfile(settings_file):
        print("Loading settings from {}".format(settings_file))
        settings = load_json(settings_file)
        defaults = load_json(defaults_file)
        missing = 0
        for key in defaults:
            if key not in settings:
                settings[key] = defaults[key]
                print("'{}' key missing from settings, adding '{}'".format(key, defaults[key]))
                missing += 1
        if missing > 0:
            print("{} missing config key(s) substituted. Saving {}".format(missing, settings_file))
            save_json(settings, settings_file)
    else:
        print("Loading default settings")
        defaults = load_json(defaults_file)
        save_json(defaults, settings_file)
        settings = load_json(settings_file)


def main():
    app = QApplication(["Sway Input Configurator"])
    app.setDesktopFileName("sway-input-config")

    global data_dir
    data_dir = get_data_dir()

    load_settings()

    win = MainWindow()
    win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
