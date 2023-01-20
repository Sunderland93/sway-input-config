#!/usr/bin/env python3

import os
import sys
from PySide2.QtWidgets import (QApplication, QMainWindow, QDialogButtonBox,
                               QDialog, QTreeWidgetItem, QListWidgetItem,
                               QListView)
from PySide2.QtGui import QPixmap
from PySide2.QtCore import Qt
from sway_input_config.utils import (list_inputs_by_type, get_data_dir, load_json, save_json,
                                     save_list_to_text_file, reload_sway_config)
from sway_input_config.ui_mainwindow import Ui_MainWindow
from sway_input_config.ui_about import Ui_about
from sway_input_config.ui_selectlayout import Ui_SelectKeyboardLayoutDialog

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
variant_list = os.path.join(dir_name, "data/variants.json")
default_settings = os.path.join(dir_name, "data/defaults.json")


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Dialog buttons
        self.ui.buttonBox.rejected.connect(self.cancel)
        self.btnApply = self.ui.buttonBox.button(QDialogButtonBox.Apply)
        self.btnApply.clicked.connect(self.on_clicked_apply)
        self.btnReset = self.ui.buttonBox.button(QDialogButtonBox.RestoreDefaults)
        self.btnReset.clicked.connect(self.on_clicked_reset)
        self.ui.buttonBox.helpRequested.connect(self.on_clicked_about)

        # Keyboard Settings #

        # Use this settings
        if settings["keyboard-use-settings"] == "true":
            self.ui.KeyBoardUseSettings.setChecked(True)
        self.ui.KeyBoardUseSettings.toggled.connect(self.keyboard_use_settings)

        # Keyboard layout staff
        layouts_data = load_json(layout_list)
        variants_data = load_json(variant_list)
        for key, values in layouts_data.items():
            if values in settings["keyboard-layout"]:
                self.layout_item = QTreeWidgetItem(self.ui.layouts)
                self.layout_item.setData(0, Qt.DisplayRole, key)
                self.layout_item.setData(0, Qt.UserRole, values)
                self.ui.layouts.addTopLevelItem(self.layout_item)
                for key, values in variants_data.items():
                    if key in self.layout_item.data(0, Qt.DisplayRole):
                        for d in values:
                            for key, value in d.items():
                                if value in settings["keyboard-variant"]:
                                    self.layout_item.setData(1, Qt.DisplayRole, key)
                                    self.layout_item.setData(1, Qt.UserRole, value)

        self.ui.addBtn.clicked.connect(self.on_add_keyboard_layout)
        self.ui.rmBtn.clicked.connect(self.on_remove_layout)
        self.ui.upBtn.clicked.connect(self.on_move_up)
        self.ui.downBtn.clicked.connect(self.on_move_down)

        # Keyboard ID #
        keyboards = list_inputs_by_type(input_type="keyboard")
        kbd_view = QListView(self.ui.kbdID)
        self.ui.kbdID.setView(kbd_view)
        self.ui.kbdID.addItem("")
        for item in keyboards:
            self.ui.kbdID.addItem(item)
        kbd_view.setTextElideMode(Qt.ElideNone)
        kbd_view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.ui.kbdID.setCurrentText(settings["keyboard-identifier"])
        self.ui.kbdID.activated.connect(self.set_kbd_identifier)

        # Keyboard model option
        model_list = load_json(kbd_model_list)
        for item in model_list:
            model_view = QListView(self.ui.kbdModel)
            self.ui.kbdModel.setView(model_view)
            self.ui.kbdModel.addItem(item)
        for key, value in model_list.items():
            if value == settings["keyboard-model"]:
                self.ui.kbdModel.setCurrentText(key)
        model_view.setTextElideMode(Qt.ElideNone)
        model_view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.ui.kbdModel.activated.connect(self.set_model)

        # Keyboard shortcut option
        shortcut_data = load_json(shortcut_list)
        shortcut_view = QListView(self.ui.shortcutName)
        self.ui.shortcutName.setView(shortcut_view)
        self.ui.shortcutName.addItem("")
        for item in shortcut_data:
            self.ui.shortcutName.addItem(item)
        for key, value in shortcut_data.items():
            if value == settings["keyboard-shortcut"]:
                self.ui.shortcutName.setCurrentText(key)
        shortcut_view.setTextElideMode(Qt.ElideNone)
        shortcut_view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.ui.shortcutName.activated.connect(self.set_shortcut)

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

        # Mouse Settings #

        # Use this settings
        if settings["pointer-use-settings"] == "true":
            self.ui.PointerUseSettings.setChecked(True)
        self.ui.PointerUseSettings.toggled.connect(self.pointer_use_settings)

        # Pointer ID #
        pointers = list_inputs_by_type(input_type="pointer")
        pointers_view = QListView(self.ui.pointerID)
        self.ui.pointerID.setView(pointers_view)
        self.ui.pointerID.addItem("")
        for item in pointers:
            self.ui.pointerID.addItem(item)
        pointers_view.setTextElideMode(Qt.ElideNone)
        pointers_view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.ui.pointerID.setCurrentText(settings["pointer-identifier"])
        self.ui.pointerID.activated.connect(self.set_pointer_identifier)

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

        # Touchapd Settings #

        # Use this settings
        if settings["touchpad-use-settings"] == "true":
            self.ui.TouchPadUseSettings.setChecked(True)
        self.ui.TouchPadUseSettings.toggled.connect(self.touchpad_use_settings)

        # Toucpad ID #
        touchpads = list_inputs_by_type(input_type="touchpad")
        touchpads_view = QListView(self.ui.touchpadID)
        self.ui.touchpadID.setView(touchpads_view)
        self.ui.touchpadID.addItem("")
        for item in touchpads:
            self.ui.touchpadID.addItem(item)
        touchpads_view.setTextElideMode(Qt.ElideNone)
        touchpads_view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.ui.touchpadID.setCurrentText(settings["touchpad-identifier"])
        self.ui.touchpadID.activated.connect(self.set_touchpad_identifier)

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

    def on_clicked_reset(self):
        defaults = load_json(default_settings)
        layouts_data = load_json(layout_list)
        variants_data = load_json(variant_list)
        model_list = load_json(kbd_model_list)
        self.ui.layouts.clear()
        for key, values in layouts_data.items():
            if values in defaults["keyboard-layout"]:
                self.layout_item = QTreeWidgetItem(self.ui.layouts)
                self.layout_item.setData(0, Qt.DisplayRole, key)
                self.layout_item.setData(0, Qt.UserRole, values)
                self.ui.layouts.addTopLevelItem(self.layout_item)
                for key, values in variants_data.items():
                    if key in self.layout_item.data(0, Qt.DisplayRole):
                        for d in values:
                            for key, value in d.items():
                                if value in defaults["keyboard-variant"]:
                                    self.layout_item.setData(1, Qt.DisplayRole, key)
                                    self.layout_item.setData(1, Qt.UserRole, value)
        for key, value in model_list.items():
            if value == defaults["keyboard-model"]:
                self.ui.kbdModel.setCurrentText(key)
        self.ui.shortcutName.setCurrentText(defaults["keyboard-shortcut"])
        self.ui.kbdID.setCurrentText(defaults["keyboard-identifier"])
        self.ui.repeatDelaySlider.setValue(defaults["keyboard-repeat-delay"])
        self.ui.repeatDelay.setValue(self.ui.repeatDelaySlider.value())
        self.ui.repeatRateSlider.setValue(defaults["keyboard-repeat-rate"])
        self.ui.repeatRate.setValue(self.ui.repeatRateSlider.value())
        self.ui.caps_lock.setChecked(False)
        self.ui.num_lock.setChecked(False)

        self.ui.pointerID.setCurrentText(defaults["pointer-identifier"])
        self.ui.pointerLeftHanded.setChecked(False)
        self.ui.pointerMiddle.setChecked(False)
        self.ui.pointerAccel.setValue(float(defaults["pointer-pointer-accel"]) * 10)
        self.ui.pointerFlat.setChecked(True)
        self.ui.pointerNatScroll.setChecked(False)
        self.ui.pointerScrollFactor.setValue(float(defaults["pointer-scroll-factor"]) * 10)

        self.ui.touchpadID.setCurrentText(defaults["touchpad-identifier"])
        self.ui.DWT.setChecked(True)
        self.ui.DWTP.setChecked(True)
        self.ui.touchLeftHanded.setChecked(False)
        self.ui.touchMiddle.setChecked(True)
        self.ui.touchAccel.setValue(float(defaults["touchpad-pointer-accel"]) * 10)
        self.ui.touchFlat.setChecked(True)
        self.ui.tap_click.setChecked(True)
        self.ui.drag.setEnabled(True)
        self.ui.drag_lock.setChecked(False)
        self.ui.lrm.setEnabled(True)
        self.ui.lmr.setEnabled(True)
        self.ui.method1.setChecked(True)
        self.ui.touchNatScroll.setChecked(False)
        self.ui.touchScrollFactor.setValue(float(defaults["touchpad-scroll-factor"]) * 10)

    def on_add_keyboard_layout(self):
        self.dlg = SelectKeyboardLayout()
        if self.dlg.exec() == QDialog.Accepted:
            lay_key = self.dlg.select_layout.layouts.currentItem().data(Qt.DisplayRole)
            lay_value = self.dlg.select_layout.layouts.currentItem().data(Qt.UserRole)
            var_key = self.dlg.select_layout.variants.currentItem().data(Qt.DisplayRole)
            var_value = self.dlg.select_layout.variants.currentItem().data(Qt.UserRole)
            self.item = QTreeWidgetItem(self.ui.layouts)
            self.item.setData(0, Qt.DisplayRole, lay_key)
            self.item.setData(0, Qt.UserRole, lay_value)
            self.item.setData(1, Qt.DisplayRole, var_key)
            self.item.setData(1, Qt.UserRole, var_value)
            self.ui.layouts.addTopLevelItem(self.item)

    def on_remove_layout(self):
        if self.ui.layouts.topLevelItemCount() > 1:
            item = self.ui.layouts.currentItem()
            pos = self.ui.layouts.indexOfTopLevelItem(item)
            self.ui.layouts.takeTopLevelItem(pos)

    def on_move_up(self):
        item = self.ui.layouts.currentItem()
        pos = self.ui.layouts.indexOfTopLevelItem(item)
        if pos > 0:
            self.ui.layouts.takeTopLevelItem(pos)
            self.ui.layouts.insertTopLevelItem(pos - 1, item)
            self.ui.layouts.setCurrentItem(item)

    def on_move_down(self):
        item = self.ui.layouts.currentItem()
        pos = self.ui.layouts.indexOfTopLevelItem(item)
        if pos < self.ui.layouts.topLevelItemCount() - 1:
            self.ui.layouts.takeTopLevelItem(pos)
            self.ui.layouts.insertTopLevelItem(pos + 1, item)
            self.ui.layouts.setCurrentItem(item)

    def set_keyboard_layout(self):
        n = self.ui.layouts.topLevelItemCount()
        layouts = []
        variants = []
        row = 0
        if n > 0:
            while row < n:
                item = self.ui.layouts.topLevelItem(row)
                layouts.append(item.data(0, Qt.UserRole))
                variants.append(item.data(1, Qt.UserRole))
                row += 1
        settings["keyboard-layout"] = layouts
        settings["keyboard-variant"] = variants

    def set_kbd_identifier(self):
        settings["keyboard-identifier"] = self.ui.kbdID.currentText()

    def set_model(self):
        model_data = load_json(kbd_model_list)
        for key in model_data.keys():
            settings["keyboard-model"] = model_data[self.ui.kbdModel.currentText()]

    def set_shortcut(self):
        data = load_json(shortcut_list)
        for key in data.keys():
            settings["keyboard-shortcut"] = data[self.ui.shortcutName.currentText()]

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

    def set_pointer_identifier(self):
        settings["pointer-identifier"] = self.ui.pointerID.currentText()

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

    def set_touchpad_identifier(self):
        settings["touchpad-identifier"] = self.ui.touchpadID.currentText()

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
        self.set_keyboard_layout()
        save_to_config()
        f = os.path.join(data_dir, "settings")
        print("Saving {}".format(f))
        save_json(settings, f)
        reload_sway_config()

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
        for key, value in layout.items():
            item = QListWidgetItem(key)
            item.setData(Qt.UserRole, value)
            item.setData(Qt.DisplayRole, key)
            self.select_layout.layouts.addItem(item)
        custom_item = QListWidgetItem("A user defined custom layout")
        custom_item.setData(Qt.UserRole, "custom")
        custom_vitem = QListWidgetItem("None")
        custom_vitem.setData(Qt.UserRole, "")
        self.select_layout.layouts.addItem(custom_item)
        self.select_layout.variants.addItem(custom_vitem)
        self.select_layout.layouts.setCurrentItem(self.select_layout.layouts.item(0))
        self.select_layout.variants.setCurrentItem(self.select_layout.variants.item(0))

        self.select_layout.layouts.currentItemChanged.connect(self.on_layout_changed)
        self.select_layout.buttonBox.rejected.connect(self.cancel)
        self.select_layout.buttonBox.accepted.connect(self.on_add_layout)

    def on_layout_changed(self):
        item = self.select_layout.layouts.currentItem()
        self.select_layout.variants.clear()
        variant = load_json(variant_list)
        for key, value in variant.items():
            if key in item.data(Qt.DisplayRole):
                for v in value:
                    for key, value in v.items():
                        vitem = QListWidgetItem(key)
                        vitem.setData(Qt.UserRole, value)
                        self.select_layout.variants.addItem(vitem)
        self.select_layout.variants.setCurrentItem(self.select_layout.variants.item(0))

    def on_add_layout(self):
        self.accept()

    def cancel(self):
        self.close()


def save_to_config():
    if settings["keyboard-use-settings"] == "true":

        lines = ['input "type:keyboard" {'] if not settings["keyboard-identifier"] else [
            'input "%s" {' % settings["keyboard-identifier"]]
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

        lines = ['input "type:pointer" {'] if not settings["pointer-identifier"] else [
            'input "%s" {' % settings["pointer-identifier"]]
        lines.append('  accel_profile {}'.format(settings["pointer-accel-profile"])),
        lines.append('  pointer_accel {}'.format(settings["pointer-pointer-accel"])),
        lines.append('  natural_scroll {}'.format(settings["pointer-natural-scroll"])),
        lines.append('  scroll_factor {}'.format(settings["pointer-scroll-factor"])),
        lines.append('  left_handed {}'.format(settings["pointer-left-handed"])),
        lines.append('  middle_emulation {}'.format(settings["pointer-middle-emulation"]))
        lines.append('}')

        save_list_to_text_file(lines, os.path.join(config_home, "sway/pointer"))

    if settings["touchpad-use-settings"] == "true":
        lines = ['input "type:touchpad" {'] if not settings["touchpad-identifier"] else [
            'input "%s" {' % settings["touchpad-identifier"]]
        lines.append('  accel_profile {}'.format(settings["touchpad-accel-profile"])),
        lines.append('  pointer_accel {}'.format(settings["touchpad-pointer-accel"])),
        lines.append('  natural_scroll {}'.format(settings["touchpad-natural-scroll"])),
        lines.append('  scroll_factor {}'.format(settings["touchpad-scroll-factor"])),
        lines.append('  scroll_method {}'.format(settings["touchpad-scroll-method"])),
        lines.append('  left_handed {}'.format(settings["touchpad-left-handed"])),
        lines.append('  tap {}'.format(settings["touchpad-tap"])),
        lines.append('  tap_button_map {}'.format(settings["touchpad-tap-button-map"])),
        lines.append('  drag {}'.format(settings["touchpad-drag"])),
        lines.append('  drag_lock {}'.format(settings["touchpad-drag-lock"])),
        lines.append('  dwt {}'.format(settings["touchpad-dwt"])),
        lines.append('  dwtp {}'.format(settings["touchpad-dwtp"])),
        lines.append('  middle_emulation {}'.format(settings["touchpad-middle-emulation"]))
        lines.append('}')

        save_list_to_text_file(lines, os.path.join(config_home, "sway/touchpad"))


def load_settings():
    settings_file = os.path.join(data_dir, "settings")
    global settings
    if os.path.isfile(settings_file):
        print("Loading settings from {}".format(settings_file))
        settings = load_json(settings_file)
        defaults = load_json(default_settings)
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
