#!/usr/bin/env python3

import os
import sys
from PySide2.QtWidgets import (QApplication, QWidget, QVBoxLayout, QComboBox,
                               QDialog, QCheckBox, QHBoxLayout, QSpinBox,
                               QPushButton, QDialogButtonBox, QFormLayout,
                               QGridLayout, QGroupBox, QLineEdit, QLabel,
                               QMainWindow, QTabWidget, QDoubleSpinBox, QStyle)
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

layout_list = ["af", "al", "am", "ara", "at", "au", "az", "ba", "bd", "be", "bg",
               "br", "brai", "bt", "bw", "by", "ca", "cd", "ch", "cm", "cn", "cz",
               "de", "dk", "dz", "ee", "epo", "es", "et", "fi", "fo", "fr", "gb",
               "ge", "gh", "gn", "gr", "hr", "hu", "id", "ie", "il", "in", "iq", "ir",
               "is", "it", "jp", "jv", "ke", "kg", "kh", "kr", "kz", "la", "latam",
               "lk", "lt", "lv", "ma", "mao", "md", "me", "mk", "ml", "mm", "mn", "mt",
               "mv", "my", "ng", "nl", "no", "np", "ph", "pk", "pl", "pt", "ro", "rs",
               "ru", "se", "si", "sk", "sn", "sy", "tg", "th", "tj", "tm", "tr", "tw",
               "tz", "ua", "us", "uz", "vn", "za"]


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(620, 400)
        self.mainWindow = QWidget()
        self.vbox = QVBoxLayout(self.mainWindow)
        self.hbox = QHBoxLayout()
        self.buttonBox = QDialogButtonBox()
        self.btnApply = QPushButton("Apply")
        self.btnApply.setIcon(self.style().standardIcon(QStyle.SP_DialogApplyButton))
        self.btnApply.clicked.connect(self.on_clicked_apply)
        self.btnCancel = QPushButton("Cancel")
        self.btnCancel.setIcon(self.style().standardIcon(QStyle.SP_DialogCancelButton))
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
        self.copyright_text = ["Version: 1.0.0.\n"
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
        for item in layout_list:
            self.layoutList.addItem(item)

        self.layoutName = QLineEdit()
        self.layoutLabel = QLabel("Layout:")
        self.layoutName.setText(settings["keyboard-layout"])

        self.addBtn = QPushButton("Add")
        self.addBtn.setToolTip("Add selected layout to the list")
        self.addBtn.clicked.connect(self.add_layout)

        self.variantName = QLineEdit()
        self.labelVariant = QLabel("Variant:")
        self.variantName.setToolTip("Variant of the keyboard like 'dvorak' or 'colemak'.")
        self.variantName.setMaxLength(30)
        self.variantName.setText(settings["keyboard-variant"])
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

        self.repeatDelay = QSpinBox()
        self.repeatDelayLabel = QLabel("Repeat delay:")
        self.repeatDelay.setToolTip("Amount of time a key must be held before it starts repeating.")
        self.repeatDelay.setRange(1, 6000)
        self.repeatDelay.setSingleStep(1)
        self.repeatDelay.setValue(settings["keyboard-repeat-delay"])
        self.repeatDelay.valueChanged.connect(self.on_repeat_delay_value_changed)

        self.repeatRate = QSpinBox()
        self.repeatRateLabel = QLabel("Repeat rate:")
        self.repeatRate.setToolTip("Frequency of key repeats once the repeat_delay has passed.")
        self.repeatRate.setRange(1, 4000)
        self.repeatDelay.setSingleStep(1)
        self.repeatRate.setValue(settings["keyboard-repeat-rate"])
        self.repeatRate.valueChanged.connect(self.on_repeat_rate_value_changed)

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
        self.gridLayout.addWidget(self.repeatDelayLabel, 3, 0, 1, 1)
        self.gridLayout.addWidget(self.repeatDelay, 3, 1, 1, 1)
        self.gridLayout.addWidget(self.repeatRateLabel, 4, 0, 1, 1)
        self.gridLayout.addWidget(self.repeatRate, 4, 1, 1, 1)
        self.gridLayout.addWidget(self.caps_lockLabel, 5, 0, 1, 1)
        self.gridLayout.addWidget(self.caps_lock, 5, 1, 1, 1)
        self.gridLayout.addWidget(self.num_lockLabel, 6, 0, 1, 1)
        self.gridLayout.addWidget(self.num_lock, 6, 1, 1, 1)
        self.vbox2.addLayout(self.gridLayout)
        self.vbox2.addWidget(self.KeyBoardUseSettings, 0, Qt.AlignRight)
        self.groupBox.setLayout(self.vbox2)
        self.setLayout(self.vbox)

    def keyboard_use_settings(self):
        if self.KeyBoardUseSettings.isChecked() == True:
            settings["keyboard-use-settings"] = "true"
        else:
            settings["keyboard-use-settings"] = "false"

    def set_shortcut(self):
        data = load_json("data/shortcut.json")
        for key in data.keys():
            settings["keyboard-shortcut"] = data[self.shortcutName.currentText()]

    def add_layout(self):
        layout = self.layoutList.currentText()
        self.layoutName.insert(",")
        self.layoutName.insert(layout)
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

        self.formLayout = QFormLayout()
        self.groupBox = QGroupBox("Pointer device settings")
        self.vbox = QVBoxLayout()
        self.vbox2 = QVBoxLayout()
        self.vbox.addWidget(self.groupBox)

        self.PointerUseSettings = QCheckBox("Use this settings")
        if settings["pointer-use-settings"] == "true":
            self.PointerUseSettings.setChecked(True)
        self.PointerUseSettings.toggled.connect(self.pointer_use_settings)

        self.accelProfile = QComboBox()
        self.accelProfile.setToolTip("Sets the pointer acceleration profile.")
        for item in ["flat", "adaptive"]:
            self.accelProfile.addItem(item)
        self.accelProfile.activated.connect(self.on_accel_profile_text_changed)

        self.accel = QDoubleSpinBox(decimals=1)
        self.accel.setToolTip("Changes the pointer acceleration. [<-1|1>]")
        self.accel.setRange(-1, 1)
        self.accel.setSingleStep(0.1)
        self.accel.setValue(settings["pointer-pointer-accel"])
        self.accel.valueChanged.connect(self.on_accel_value_changed)

        self.natScroll = QComboBox()
        self.natScroll.setToolTip("Enables or disables natural (inverted) scrolling.")
        for item in ["disabled", "enabled"]:
            self.natScroll.addItem(item)
        self.natScroll.activated.connect(self.on_nat_scroll_text_changed)

        self.scrollFactor = QDoubleSpinBox(decimals=1)
        self.scrollFactor.setToolTip("Scroll speed will be scaled by the given value.")
        self.scrollFactor.setRange(0.1, 10)
        self.scrollFactor.setSingleStep(0.1)
        self.scrollFactor.setValue(settings["pointer-scroll-factor"])
        self.scrollFactor.valueChanged.connect(self.on_scroll_value_changed)

        self.leftHanded = QComboBox()
        self.leftHanded.setToolTip("Enables or disables left handed mode.")
        for item in ["disabled", "enabled"]:
            self.leftHanded.addItem(item)
        self.leftHanded.activated.connect(self.on_left_handed_text_changed)

        self.formLayout.addRow(QLabel("Acceleration profile:"), self.accelProfile)
        self.formLayout.addRow(QLabel("Acceleration:"), self.accel)
        self.formLayout.addRow(QLabel("Natural scroll:"), self.natScroll)
        self.formLayout.addRow(QLabel("Scroll factor:"), self.scrollFactor)
        self.formLayout.addRow(QLabel("Left handed:"), self.leftHanded)

        self.vbox2.addLayout(self.formLayout)
        self.vbox2.addWidget(self.PointerUseSettings, 0, Qt.AlignRight)
        self.groupBox.setLayout(self.vbox2)
        self.setLayout(self.vbox)

    def pointer_use_settings(self):
        if self.PointerUseSettings.isChecked() == True:
            settings["pointer-use-settings"] = "true"
        else:
            settings["pointer-use-settings"] = "false"

    def on_accel_profile_text_changed(self):
        settings["pointer-accel-profile"] = self.accelProfile.currentText()

    def on_accel_value_changed(self):
        settings["pointer-pointer-accel"] = self.accel.value()

    def on_nat_scroll_text_changed(self):
        settings["pointer-natural-scroll"] = self.natScroll.currentText()

    def on_scroll_value_changed(self):
        settings["pointer-scroll-factor"] = self.scrollFactor.value()

    def on_left_handed_text_changed(self):
        settings["pointer-left-handed"] = self.leftHanded.currentText()


class TouchpadTab(QWidget):
    def __init__(self):
        super().__init__()

        self.gridLayout = QGridLayout()
        self.formLayout2 = QFormLayout()
        self.formLayout3 = QFormLayout()
        self.vbox = QVBoxLayout()
        self.vbox2 = QVBoxLayout()
        self.groupBox = QGroupBox("Touchpad settings")
        self.vbox.addWidget(self.groupBox)

        self.TouchPadUseSettings = QCheckBox("Use this settings")
        if settings["touchpad-use-settings"] == "true":
            self.TouchPadUseSettings.setChecked(True)
        self.TouchPadUseSettings.toggled.connect(self.touchpad_use_settings)

        self.accelProfile = QComboBox()
        self.accelProfile.setToolTip("Sets the pointer acceleration profile.")
        for item in ["flat", "adaptive"]:
            self.accelProfile.addItem(item)
        self.accelProfile.setCurrentText(settings["touchpad-accel-profile"])
        self.accelProfile.activated.connect(self.on_accel_profile_text_changed)

        self.accel = QDoubleSpinBox(decimals=1)
        self.accel.setToolTip("Changes the pointer acceleration. [<-1|1>]")
        self.accel.setRange(-1, 1)
        self.accel.setSingleStep(0.1)
        self.accel.setValue(settings["touchpad-pointer-accel"])
        self.accel.valueChanged.connect(self.on_accel_value_changed)

        self.scrollFactor = QDoubleSpinBox(decimals=1)
        self.scrollFactor.setToolTip("Scroll speed will be scaled by the given value.")
        self.scrollFactor.setRange(0.1, 10)
        self.scrollFactor.setSingleStep(0.1)
        self.scrollFactor.setValue(settings["touchpad-scroll-factor"])
        self.scrollFactor.valueChanged.connect(self.on_scroll_factor_changed)

        self.natScroll = QComboBox()
        self.natScroll.setToolTip("Enables or disables natural (inverted) scrolling.")
        for item in ["disabled", "enabled"]:
            self.natScroll.addItem(item)
        self.natScroll.setCurrentText(settings["touchpad-natural-scroll"])
        self.natScroll.activated.connect(self.on_nat_scroll_text_changed)

        self.scrollMethod = QComboBox()
        self.scrollMethod.setToolTip("Changes the scroll method.")
        for item in ["two_finger", "edge", "on_button_down", "none"]:
            self.scrollMethod.addItem(item)
        self.scrollMethod.setCurrentText(settings["touchpad-scroll-method"])

        self.leftHanded = QComboBox()
        self.leftHanded.setToolTip("Enables or disables left handed mode.")
        for item in ["disabled", "enabled"]:
            self.leftHanded.addItem(item)
        self.leftHanded.setCurrentText(settings["touchpad-left-handed"])
        self.leftHanded.activated.connect(self.on_left_handed_text_changed)

        self.tap = QComboBox()
        self.tap.setToolTip("Enables or disables tap-to-click.")
        for item in ["enabled", "disabled"]:
            self.tap.addItem(item)
        self.tap.setCurrentText(settings["touchpad-tap"])
        self.tap.activated.connect(self.on_tap_text_changed)

        self.tapBtnMap = QComboBox()
        self.tapBtnMap.setToolTip("'lrm' treats 1 finger as left click, 2 fingers as right click, "
                                  "and 3 fingers as middle click.\n'lmr' treats 1 finger as left click, "
                                  "2 fingers as middle click, and 3 fingers as right click.")
        for item in ["lrm", "lmr"]:
            self.tapBtnMap.addItem(item)
        self.tapBtnMap.setCurrentText(settings["touchpad-tap-button-map"])
        self.tapBtnMap.activated.connect(self.on_tap_btn_map_text_changed)

        self.middleEmu = QComboBox()
        self.middleEmu.setToolTip("Enables or disables middle click emulation.")
        for item in ["enabled", "disable"]:
            self.middleEmu.addItem(item)
        self.middleEmu.setCurrentText(settings["touchpad-middle-emulation"])
        self.middleEmu.activated.connect(self.on_middle_emu_text_changed)

        self.drag = QComboBox()
        self.drag.setToolTip("Enables or disables tap-and-drag.")
        for item in ["enabled", "disabled"]:
            self.drag.addItem(item)
        self.drag.setCurrentText(settings["touchpad-drag"])
        self.drag.activated.connect(self.on_drag_text_changed)

        self.dragLock = QComboBox()
        self.dragLock.setToolTip("Enables or disables drag lock.")
        for item in ["disabled", "enabled"]:
            self.dragLock.addItem(item)
        self.dragLock.setCurrentText(settings["touchpad-drag-lock"])
        self.dragLock.activated.connect(self.on_draglock_text_changed)

        self.DWT = QComboBox()
        self.DWT.setToolTip("Enables or disables disable-while-typing.")
        for item in ["enabled", "disabled"]:
            self.DWT.addItem(item)
        self.DWT.setCurrentText(settings["touchpad-dwt"])
        self.DWT.activated.connect(self.on_dwt_text_changed)

        self.formLayout2.addRow(QLabel("Acceleration profile:"), self.accelProfile)
        self.formLayout2.addRow(QLabel("Acceleration:"), self.accel)
        self.formLayout2.addRow(QLabel("Scroll factor:"), self.scrollFactor)
        self.formLayout2.addRow(QLabel("Natural scroll:"), self.natScroll)
        self.formLayout2.addRow(QLabel("Scroll method:"), self.scrollMethod)
        self.formLayout2.addRow(QLabel("Left handed:"), self.leftHanded)

        self.formLayout3.addRow(QLabel("Tap:"), self.tap)
        self.formLayout3.addRow(QLabel("Tap button map:"), self.tapBtnMap)
        self.formLayout3.addRow(QLabel("Middle emulation:"), self.middleEmu)
        self.formLayout3.addRow(QLabel("Drag:"), self.drag)
        self.formLayout3.addRow(QLabel("Drag lock:"), self.dragLock)
        self.formLayout3.addRow(QLabel("DWT:"), self.DWT)

        self.gridLayout.addLayout(self.formLayout2, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.formLayout3, 0, 1, 1, 1)
        self.vbox2.addLayout(self.gridLayout)
        self.vbox2.addWidget(self.TouchPadUseSettings, 0, Qt.AlignRight)
        self.groupBox.setLayout(self.vbox2)
        self.setLayout(self.vbox)

    def touchpad_use_settings(self):
        if self.TouchPadUseSettings.isChecked() == True:
            settings["touchpad-use-settings"] = "true"
        else:
            settings["touchpad-use-settings"] = "false"

    def on_accel_value_changed(self):
        settings["touchpad-pointer-accel"] = self.accel.value()

    def on_scroll_factor_changed(self):
        settings["touchpad-scroll-factor"] = self.scrollFactor.value()

    def on_accel_profile_text_changed(self):
        settings["touchpad-accel-profile"] = self.accelProfile.currentText()

    def on_nat_scroll_text_changed(self):
        settings["touchpad-natural-scroll"] = self.natScroll.currentText()

    def on_scroll_method_text_changed(self):
        settings["touchpad-scroll-method"] = self.scrollMethod.currentText()

    def on_left_handed_text_changed(self):
        settings["touchpad-left-handed"] = self.leftHanded.currentText()

    def on_tap_text_changed(self):
        settings["touchpad-tap"] = self.tap.currentText()

    def on_tap_btn_map_text_changed(self):
        settings["touchpad-tap-button-map"] = self.tapBtnMap.currentText()

    def on_middle_emu_text_changed(self):
        settings["touchpad-middle-emulation"] = self.middleEmu.currentText()

    def on_drag_text_changed(self):
        settings["touchpad-drag"] = self.drag.currentText()

    def on_draglock_text_changed(self):
        settings["touchpad-drag-lock"] = self.dragLock.currentText()

    def on_dwt_text_changed(self):
        settings["touchpad-dwt"] = self.DWT.currentText()


def save_to_config():
    if settings["keyboard-use-settings"] == "true":

        lines = ['input "type:keyboard" {']
        if settings["keyboard-layout"]:
            lines.append('  xkb_layout {}'.format(settings["keyboard-layout"]))
        if settings["keyboard-variant"]:
            lines.append('  xkb_variant {}'.format(settings["keyboard-variant"]))
        if settings["keyboard-shortcut"]:
            lines.append('  xkb_options {}'.format(settings["keyboard-shortcut"]))
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
                 '  left_handed {}'.format(settings["pointer-left-handed"])]
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

    global data_dir
    data_dir = get_data_dir()

    load_settings()

    win = MainWindow()
    win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
