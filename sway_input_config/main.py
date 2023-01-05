#!/usr/bin/env python3

import os
import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QDialogButtonBox, QDialog
from PySide2.QtGui import QPixmap
from sway_input_config.utils import (get_data_dir, load_json, save_json,
                                     save_list_to_text_file, reload)
from ui_mainwindow import Ui_MainWindow
from ui_about import Ui_about
from ui_selectlayout import Ui_SelectKeyboardLayoutDialog

data_dir = ""
config_home = os.getenv('XDG_CONFIG_HOME') if os.getenv('XDG_CONFIG_HOME') else os.path.join(
    os.getenv("HOME"), ".config/")

data_home = os.getenv('XDG_DATA_HOME') if os.getenv('XDG_DATA_HOME') else os.path.join(
    os.getenv("HOME"), ".config/")

sway_config = os.path.join(config_home, "sway", "config")

dir_name = os.path.dirname(__file__)
shortcut_list = os.path.join(dir_name, "data/shortcuts.json")
kbd_model_list = os.path.join(dir_name, "data/kbd_model.json")
layout_list = os.path.join(dir_name, "data/layouts.json")


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Dialog buttons
        self.ui.buttonBox.rejected.connect(self.cancel)
        self.btnApply = self.ui.buttonBox.button(QDialogButtonBox.Apply)
        self.btnApply.clicked.connect(self.on_clicked_apply)
        self.ui.buttonBox.helpRequested.connect(self.on_clicked_about)

        #### Keyboard Settings ####

        # Use this settings
        if settings["keyboard-use-settings"] == "true":
            self.ui.KeyBoardUseSettings.setChecked(True)
        self.ui.KeyBoardUseSettings.toggled.connect(self.keyboard_use_settings)

        # Add layout
        self.ui.addBtn.clicked.connect(self.select_keyboard_layout)

        # Keyboard shortcut option
        shortcut_data = load_json(shortcut_list)
        for item in shortcut_data:
            self.ui.shortcutName.addItem(item)
        for key, value in shortcut_data.items():
            if value == settings["keyboard-shortcut"]:
                self.ui.shortcutName.setCurrentText(key)
        self.ui.shortcutName.activated.connect(self.set_shortcut)

        # Keyboard model option
        model_list = load_json(kbd_model_list)
        for item in model_list:
            self.ui.kbdModel.addItem(item)
        for key, value in model_list.items():
            if value == settings["keyboard-model"]:
                self.ui.kbdModel.setCurrentText(key)
        self.ui.kbdModel.activated.connect(self.set_model)

        # Repeat delay
        self.ui.repeatDelaySlider.setValue(settings["keyboard-repeat-delay"])
        self.ui.repeatDelay.setValue(self.ui.repeatDelaySlider.value())
        self.ui.repeatDelay.valueChanged.connect(self.ui.repeatDelaySlider.setValue)
        self.ui.repeatDelaySlider.sliderMoved.connect(self.ui.repeatDelay.setValue)
        self.ui.repeatDelaySlider.valueChanged.connect(self.on_repeat_delay_value_changed)

        # Repeat rate
        self.ui.repeatRateSlider.setValue(settings["keyboard-repeat-rate"])
        self.ui.repeatRate.setValue(self.ui.repeatRateSlider.value())
        self.ui.repeatRate.valueChanged.connect(self.ui.repeatRateSlider.setValue)
        self.ui.repeatRateSlider.sliderMoved.connect(self.ui.repeatRate.setValue)
        self.ui.repeatRateSlider.valueChanged.connect(self.on_repeat_rate_value_changed)

        # Enable Caps Lock option
        if settings["keyboard-capslock"] == "enabled":
            self.ui.caps_lock.setChecked(True)
        self.ui.caps_lock.toggled.connect(self.on_caps_lock_checked)

        # Enable Num Lock option
        if settings["keyboard-numlock"] == "enabled":
            self.ui.num_lock.setChecked(True)
        self.ui.num_lock.toggled.connect(self.on_num_lock_checked)

        #### Mouse Settings ####

        # Use this settings
        if settings["pointer-use-settings"] == "true":
            self.ui.PointerUseSettings.setChecked(True)
        self.ui.PointerUseSettings.toggled.connect(self.pointer_use_settings)

        # Left handed mode
        if settings["pointer-left-handed"] == "true":
            self.ui.pointerLeftHanded.setChecked(True)
        self.ui.pointerLeftHanded.toggled.connect(self.on_pointer_left_handed_checked)

        # Middle click emulation
        if settings["pointer-middle-emulation"] == "enabled":
            self.ui.pointerMiddle.setChecked(True)
        self.ui.pointerMiddle.toggled.connect(self.on_middle_checked)

        # Pointer speed
        self.ui.pointerAccel.setValue(float(settings["pointer-pointer-accel"]) * 10)
        self.ui.pointerAccel.valueChanged.connect(self.on_accel_value_changed)

        # Acceleration profile
        if settings["pointer-accel-profile"] == "flat":
            self.ui.pointerFlat.setChecked(True)
        else:
            self.ui.pointerAdaptive.setChecked(True)
        self.ui.pointerFlat.clicked.connect(self.on_accel_profile_changed)
        self.ui.pointerAdaptive.clicked.connect(self.on_accel_profile_changed)

        # Scrolling
        if settings["pointer-natural-scroll"] == "true":
            self.ui.pointerNatScroll.setChecked(True)
        self.ui.pointerNatScroll.toggled.connect(self.on_pointer_nat_scroll_checked)

        # Scrolling speed:
        self.ui.pointerScrollFactor.setValue(float(settings["pointer-scroll-factor"]) * 10)
        self.ui.pointerScrollFactor.valueChanged.connect(self.on_pointer_scroll_value_changed)

        #### Touchapd Settings ####

        # Use this settings
        if settings["touchpad-use-settings"] == "true":
            self.ui.TouchPadUseSettings.setChecked(True)
        self.ui.TouchPadUseSettings.toggled.connect(self.touchpad_use_settings)

        # Disable while typing
        if settings["touchpad-dwt"] == "enabled":
            self.ui.DWT.setChecked(True)
        self.ui.DWT.toggled.connect(self.on_dwt_checked)

        # Disable while trackpointing
        if settings["touchpad-dwtp"] == "enabled":
            self.ui.DWTP.setChecked(True)
        self.ui.DWTP.toggled.connect(self.on_dwtp_checked)

        # Left handed mode
        if settings["touchpad-left-handed"] == "enabled":
            self.ui.touchLeftHanded.setChecked(True)
        self.ui.touchLeftHanded.toggled.connect(self.on_touch_left_handed_checked)

        # Middle click emulation
        if settings["touchpad-middle-emulation"] == "enabled":
            self.ui.touchMiddle.setChecked(True)
        self.ui.touchMiddle.toggled.connect(self.on_touch_middle_emu_checked)

        # Pointer speed:
        self.ui.touchAccel.setValue(float(settings["touchpad-pointer-accel"]) * 10)
        self.ui.touchAccel.valueChanged.connect(self.on_touch_accel_value_changed)

        # Acceleration profile
        if settings["touchpad-accel-profile"] == "flat":
            self.ui.touchFlat.setChecked(True)
        else:
            self.ui.touchAdaptive.setChecked(True)
        self.ui.touchFlat.clicked.connect(self.on_touch_accel_profile_changed)
        self.ui.touchAdaptive.clicked.connect(self.on_touch_accel_profile_changed)

        # Tap-to-click
        if settings["touchpad-tap"] == "enabled":
            self.ui.tap_click.setChecked(True)
        self.ui.tap_click.toggled.connect(self.on_tap_click_checked)

        # Tap-and-drag
        if settings["touchpad-tap"] == "enabled":
            self.ui.drag.setEnabled(True)
        else:
            self.ui.drag.setEnabled(False)
        if settings["touchpad-drag"] == "enabled":
            self.ui.drag.setChecked(True)
        self.ui.drag.toggled.connect(self.on_tapdrag_checked)

        # Tap-and-drag lock
        if settings["touchpad-tap"] == "enabled":
            self.ui.drag_lock.setEnabled(True)
        else:
            self.ui.drag_lock.setEnabled(False)
        if settings["touchpad-drag-lock"] == "enabled":
            self.ui.drag_lock.setChecked(True)
        self.ui.drag_lock.toggled.connect(self.on_draglock_checked)

        # Two-finger tap
        if settings["touchpad-tap"] == "enabled":
            self.ui.lrm.setEnabled(True)
            self.ui.lmr.setEnabled(True)
        else:
            self.ui.lrm.setEnabled(False)
            self.ui.lmr.setEnabled(False)
        if settings["touchpad-tap-button-map"] == "lrm":
            self.ui.lrm.setChecked(True)
        else:
            self.ui.lmr.setChecked(True)
        self.ui.lrm.clicked.connect(self.on_multi_tap_checked)
        self.ui.lmr.clicked.connect(self.on_multi_tap_checked)

        # Scrolling method
        if settings["touchpad-scroll-method"] == "two_finger":
            self.ui.method1.setChecked(True)
        elif settings["touchpad-scroll-method"] == "edge":
            self.ui.method2.setChecked(True)
        elif settings["touchpad-scroll-method"] == "on_button_down":
            self.ui.method3.setChecked(True)
        else:
            self.ui.method4.setChecked(True)
        self.ui.method1.clicked.connect(self.on_scroll_method_checked)
        self.ui.method2.clicked.connect(self.on_scroll_method_checked)
        self.ui.method3.clicked.connect(self.on_scroll_method_checked)
        self.ui.method4.clicked.connect(self.on_scroll_method_checked)

        # Scrolling:
        if settings["touchpad-natural-scroll"] == "enabled":
            self.ui.touchNatScroll.setChecked(True)
        self.ui.touchNatScroll.toggled.connect(self.on_touch_nat_scroll_checked)

        # Scrolling speed
        self.ui.touchScrollFactor.setValue(float(settings["touchpad-scroll-factor"]) * 10)
        self.ui.touchScrollFactor.valueChanged.connect(self.on_touch_scroll_value_changed)

    def keyboard_use_settings(self):
        if self.ui.KeyBoardUseSettings.isChecked() is True:
            settings["keyboard-use-settings"] = "true"
        else:
            settings["keyboard-use-settings"] = "false"

    def select_keyboard_layout(self):
        self.select_dialog = SelectKeyboardLayout()
        self.select_dialog.show()

    def set_shortcut(self):
        data = load_json("data/shortcut.json")
        for key in data.keys():
            settings["keyboard-shortcut"] = data[self.ui.shortcutName.currentText()]

    def set_model(self):
        model_data = load_json("data/kbd_model.json")
        for key in model_data.keys():
            settings["keyboard-model"] = model_data[self.ui.kbdModel.currentText()]

    def on_repeat_delay_value_changed(self):
        settings["keyboard-repeat-delay"] = self.ui.repeatDelay.value()

    def on_repeat_rate_value_changed(self):
        settings["keyboard-repeat-rate"] = self.ui.repeatRate.value()

    def on_caps_lock_checked(self):
        if self.ui.caps_lock.isChecked():
            settings["keyboard-capslock"] = "enabled"
        else:
            settings["keyboard-capslock"] = "disabled"

    def on_num_lock_checked(self):
        if self.ui.num_lock.isChecked():
            settings["keyboard-numlock"] = "enabled"
        else:
            settings["keyboard-numlock"] = "disabled"

    def pointer_use_settings(self):
        if self.ui.PointerUseSettings.isChecked() is True:
            settings["pointer-use-settings"] = "true"
        else:
            settings["pointer-use-settings"] = "false"

    def on_pointer_left_handed_checked(self):
        if self.ui.pointerLeftHanded.isChecked() is True:
            settings["pointer-left-handed"] = "true"
        else:
            settings["pointer-left-handed"] = "false"

    def on_middle_checked(self):
        if self.ui.pointerMiddle.isChecked():
            settings["pointer-middle-emulation"] = "enabled"
        else:
            settings["pointer-middle-emulation"] = "disabled"

    def on_accel_value_changed(self):
        settings["pointer-pointer-accel"] = self.ui.pointerAccel.value() / 10

    def on_accel_profile_changed(self):
        if self.ui.pointerFlat.isChecked():
            settings["pointer-accel-profile"] = "flat"
        else:
            settings["pointer-accel-profile"] = "adaptive"

    def on_pointer_nat_scroll_checked(self):
        if self.ui.pointerNatScroll.isChecked() is True:
            settings["pointer-natural-scroll"] = "true"
        else:
            settings["pointer-natural-scroll"] = "false"

    def on_pointer_scroll_value_changed(self):
        settings["pointer-scroll-factor"] = self.ui.pointerScrollFactor.value() / 10

    def touchpad_use_settings(self):
        if self.ui.TouchPadUseSettings.isChecked() is True:
            settings["touchpad-use-settings"] = "true"
        else:
            settings["touchpad-use-settings"] = "false"

    def on_dwt_checked(self):
        if self.ui.DWT.isChecked():
            settings["touchpad-dwt"] = "enabled"
        else:
            settings["touchpad-dwt"] = "disabled"

    def on_dwtp_checked(self):
        if self.ui.DWTP.isChecked():
            settings["touchpad-dwtp"] = "enabled"
        else:
            settings["touchpad-dwtp"] = "disabled"

    def on_touch_left_handed_checked(self):
        if self.ui.touchLeftHanded.isChecked():
            settings["touchpad-left-handed"] = "enabled"
        else:
            settings["touchpad-left-handed"] = "disabled"

    def on_touch_middle_emu_checked(self):
        if self.ui.touchMiddle.isChecked():
            settings["touchpad-middle-emulation"] = "enabled"
        else:
            settings["touchpad-middle-emulation"] = "disabled"

    def on_touch_accel_value_changed(self):
        settings["touchpad-pointer-accel"] = self.ui.touchAccel.value() / 10

    def on_touch_accel_profile_changed(self):
        if self.ui.touchFlat.isChecked():
            settings["touchpad-accel-profile"] = "flat"
        else:
            settings["touchpad-accel-profile"] = "adaptive"

    def on_tap_click_checked(self):
        if self.ui.tap_click.isChecked():
            settings["touchpad-tap"] = "enabled"
            self.ui.drag.setEnabled(True)
            self.ui.drag_lock.setEnabled(True)
            self.ui.lrm.setEnabled(True)
            self.ui.lmr.setEnabled(True)
        else:
            settings["touchpad-tap"] = "disabled"
            self.ui.drag.setEnabled(False)
            self.ui.drag_lock.setEnabled(False)
            self.ui.lrm.setEnabled(False)
            self.ui.lmr.setEnabled(False)

    def on_tapdrag_checked(self):
        if self.ui.drag.isChecked():
            settings["touchpad-drag"] = "enabled"
        else:
            settings["touchpad-drag"] = "disabled"

    def on_draglock_checked(self):
        if self.ui.drag_lock.isChecked():
            settings["touchpad-drag-lock"] = "enabled"
        else:
            settings["touchpad-drag-lock"] = "disabled"

    def on_multi_tap_checked(self):
        if self.ui.lrm.isChecked():
            settings["touchpad-tap-button-map"] = "lrm"
        else:
            settings["touchpad-tap-button-map"] = "lmr"

    def on_scroll_method_checked(self):
        if self.ui.method1.isChecked() is True:
            settings["touchpad-scroll-method"] = "two_finger"
        elif self.ui.method2.isChecked() is True:
            settings["touchpad-scroll-method"] = "edge"
        elif self.ui.method3.isChecked() is True:
            settings["touchpad-scroll-method"] = "on_button_down"
        else:
            settings["touchpad-scroll-method"] = "none"

    def on_touch_nat_scroll_checked(self):
        if self.ui.touchNatScroll.isChecked() is True:
            settings["touchpad-natural-scroll"] = "enabled"
        else:
            settings["touchpad-natural-scroll"] = "disabled"

    def on_touch_scroll_value_changed(self):
        settings["touchpad-scroll-factor"] = self.ui.touchScrollFactor.value() / 10

    def on_clicked_about(self):
        self.about = AboutDialog()
        self.about.show()

    def on_clicked_apply(self):
        save_to_config()
        f = os.path.join(data_dir, "settings")
        print("Saving {}".format(f))
        save_json(settings, f)

    def cancel(self):
        self.close()


class AboutDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.aboutDialog = Ui_about()
        self.aboutDialog.setupUi(self)

        self.pixmap = QPixmap(os.path.join(dir_name, "data/logo_sic.png"))
        self.aboutDialog.pixmap.setPixmap(self.pixmap)

        self.aboutDialog.buttonBox.rejected.connect(self.cancel)

    def cancel(self):
        self.close()



class SelectKeyboardLayout(QDialog):
    def __init__(self):
        super().__init__()
        self.select_layout = Ui_SelectKeyboardLayoutDialog()
        self.select_layout.setupUi(self)

        layout = load_json(layout_list)
        for item in layout:
            self.select_layout.layouts.addItem(item)

        self.select_layout.buttonBox.rejected.connect(self.cancel)

    def cancel(self):
        self.close()

def save_to_config():
    if settings["keyboard-use-settings"] == "true":

        lines = ['input "type:keyboard" {']
        if settings["keyboard-layout"]:
            lines.append('  xkb_layout {}'.format(settings["keyboard-layout"]))
        if settings["keyboard-variant"]:
            lines.append('  xkb_variant {}'.format(settings["keyboard-variant"]))
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
                 '  dwtp {}'.format(settings["touchpad-dwtp"]),
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
