#!/usr/bin/env python3

import argparse
import os
import sys
import signal
from PyQt6.QtWidgets import (QApplication, QMainWindow, QDialogButtonBox,
                               QDialog, QListView, QButtonGroup)
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt, QTranslator, QLocale, QLibraryInfo
from shutil import copy2
from sway_input_config.utils import (list_inputs_by_type, get_data_dir,
                                     get_sway_version,
                                     get_config_home,
                                     load_json, save_json,
                                     save_list_to_text_file,
                                     load_text_file, reload_sway_config)
from sway_input_config.ui_mainwindow import Ui_MainWindow
from sway_input_config.ui_about import Ui_about
from sway_input_config.ui_error_message import Ui_ErrorMessage
from sway_input_config.devices.keyboard import KeyboardSettings

app_version = "1.4.3"

if os.getenv("SWAYSOCK"):
    sway_version = get_sway_version()
    data_dir = ""
    config_home = get_config_home()
    sway_config = os.path.join(config_home, "sway", "config")

dir_name = os.path.dirname(__file__)
default_settings = os.path.join(dir_name, "data/defaults.json")

# Buttons array used for on_button_down scroll method
scroll_buttons = {
    "Disabled": "disable",
    "Left button": "BTN_LEFT",
    "Right button": "BTN_RIGHT",
    "Middle button": "BTN_MIDDLE",
    "Side button": "BTN_SIDE",
    "Extra button": "BTN_EXTRA"
    }


class ErrorMessage(QDialog):
    def __init__(self):
        super(ErrorMessage, self).__init__()
        self.ui = Ui_ErrorMessage()
        self.ui.setupUi(self)

        self.btnOk = self.ui.buttonBox.button(QDialogButtonBox.StandardButton.Ok)
        self.btnOk.clicked.connect(self.on_clicked_ok)

    def on_clicked_ok(self):
        self.close()


class MainWindow(QMainWindow):
    def __init__(self, settings, data_dir):
        super(MainWindow, self).__init__()
        self.settings = settings
        self.data_dir = data_dir
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.keyboard = KeyboardSettings(self.ui, self.settings)

        self.keyboard.init_ui()

        # Dialog buttons
        self.ui.buttonBox.rejected.connect(self.cancel)
        self.btnApply = self.ui.buttonBox.button(QDialogButtonBox.StandardButton.Apply)
        self.btnApply.clicked.connect(self.on_clicked_apply)
        self.btnReset = self.ui.buttonBox.button(QDialogButtonBox.StandardButton.RestoreDefaults)
        self.btnReset.clicked.connect(self.on_clicked_reset)
        self.ui.buttonBox.helpRequested.connect(self.on_clicked_about)

        # Mouse Settings #

        # Use this settings
        if self.settings["pointer-use-settings"] == "true":
            self.ui.PointerUseSettings.setChecked(True)
        self.ui.PointerUseSettings.toggled.connect(self.pointer_use_settings)

        # Pointer ID #
        pointers = list_inputs_by_type(input_type="pointer")
        pointers_view = QListView(self.ui.pointerID)
        self.ui.pointerID.setView(pointers_view)
        self.ui.pointerID.addItem("")
        for item in pointers:
            self.ui.pointerID.addItem(item)
        pointers_view.setTextElideMode(Qt.TextElideMode.ElideNone)
        pointers_view.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.ui.pointerID.setCurrentText(self.settings["pointer-identifier"])
        self.ui.pointerID.activated.connect(self.set_pointer_identifier)

        # Left handed mode
        if self.settings["pointer-left-handed"] == "true":
            self.ui.pointerLeftHanded.setChecked(True)
        self.ui.pointerLeftHanded.toggled.connect(self.on_pointer_left_handed_checked)

        # Middle click emulation
        if self.settings["pointer-middle-emulation"] == "enabled":
            self.ui.pointerMiddle.setChecked(True)
        self.ui.pointerMiddle.toggled.connect(self.on_middle_checked)

        # Pointer speed
        pointerAccelValue = float(self.settings["pointer-pointer-accel"]) * 10
        self.ui.pointerAccel.setValue(int(pointerAccelValue))
        self.ui.pointerAccel.valueChanged.connect(self.on_accel_value_changed)

        # Acceleration profile
        self.pointerAccelButtonGroup = QButtonGroup()
        self.pointerAccelButtonGroup.addButton(self.ui.pointerFlat)
        self.pointerAccelButtonGroup.addButton(self.ui.pointerAdaptive)
        if self.settings["pointer-accel-profile"] == "flat":
            self.ui.pointerFlat.setChecked(True)
        else:
            self.ui.pointerAdaptive.setChecked(True)
        self.ui.pointerFlat.clicked.connect(self.on_accel_profile_changed)
        self.ui.pointerAdaptive.clicked.connect(self.on_accel_profile_changed)

        # Rotation angle (0.0 to 360.0) since Sway 1.9
        if sway_version >= "1.9":
            pointerRotationValue = float(self.settings["pointer-rotation-angle"])
            self.ui.pointerRotationAngleSlider.setValue(int(pointerRotationValue))
            self.ui.pointerRotationAngle.setValue(self.ui.pointerRotationAngleSlider.value())
            self.ui.pointerRotationAngleSlider.sliderMoved.connect(self.ui.pointerRotationAngle.setValue)
            self.ui.pointerRotationAngleSlider.valueChanged.connect(self.on_pointer_rotation_angle_value_changed)
        else:
            self.ui.pointerRotationAngleSlider.setDisabled(True)
            self.ui.pointerRotationAngle.setDisabled(True)
            self.ui.pointerRotationLabel.setDisabled(True)

        # Scrolling
        if self.settings["pointer-natural-scroll"] == "true":
            self.ui.pointerNatScroll.setChecked(True)
        self.ui.pointerNatScroll.toggled.connect(self.on_pointer_nat_scroll_checked)

        # Scrolling speed:
        pointerFactorValue = float(self.settings["pointer-scroll-factor"]) * 10
        self.ui.pointerScrollFactor.setValue(int(pointerFactorValue))
        self.ui.pointerScrollFactor.valueChanged.connect(self.on_pointer_scroll_value_changed)

        # Scrolling button (trackpoints only)
        for key, value in scroll_buttons.items():
            self.ui.scrollButtonList.addItem(key, value)
            if value == self.settings["pointer-scroll-button"]:
                self.ui.scrollButtonList.setCurrentText(key)
        self.ui.scrollButtonList.activated.connect(self.on_scroll_button_checked)

        # Scrolling button lock (since Sway 1.9)
        if sway_version >= "1.9":
            self.ui.scrollButtonLock.setEnabled(True)
            if self.settings["pointer-scroll-button-lock"] == "enabled":
                self.ui.scrollButtonLock.setChecked(True)
            self.ui.scrollButtonLock.clicked.connect(self.on_scroll_button_lock_checked)

        # Touchapd Settings #

        # Use this settings
        if self.settings["touchpad-use-settings"] == "true":
            self.ui.TouchPadUseSettings.setChecked(True)
        self.ui.TouchPadUseSettings.toggled.connect(self.touchpad_use_settings)

        # Touchpad ID #
        touchpads = list_inputs_by_type(input_type="touchpad")
        touchpads_view = QListView(self.ui.touchpadID)
        self.ui.touchpadID.setView(touchpads_view)
        if not touchpads:
            self.ui.touchpadID.addItem("Not found")
            self.ui.tabWidget.widget(2).setEnabled(False)
        else:
            self.ui.touchpadID.addItem("")
            for item in touchpads:
                self.ui.touchpadID.addItem(item)
                touchpads_view.setTextElideMode(Qt.TextElideMode.ElideNone)
                touchpads_view.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
                self.ui.touchpadID.setCurrentText(self.settings["touchpad-identifier"])
                self.ui.touchpadID.activated.connect(self.set_touchpad_identifier)

        # Touchapd send events mode:
        self.eventsButtonGroup = QButtonGroup()
        self.eventsButtonGroup.addButton(self.ui.touchEventsEnabled)
        self.eventsButtonGroup.addButton(self.ui.touchEventsDisabled)
        self.eventsButtonGroup.addButton(self.ui.touchEventsOnExternalMouse)
        if self.settings["touchpad-events"] == "disabled":
            self.ui.touchEventsDisabled.setChecked(True)
        elif self.settings["touchpad-events"] == "disabled_on_external_mouse":
            self.ui.touchEventsOnExternalMouse.setChecked(True)
        else:
            self.ui.touchEventsEnabled.setChecked(True)
        self.ui.touchEventsEnabled.clicked.connect(self.on_touchpad_events_mode_changed)
        self.ui.touchEventsDisabled.clicked.connect(self.on_touchpad_events_mode_changed)
        self.ui.touchEventsOnExternalMouse.clicked.connect(self.on_touchpad_events_mode_changed)

        # Disable while typing
        if self.settings["touchpad-dwt"] == "enabled":
            self.ui.DWT.setChecked(True)
        self.ui.DWT.toggled.connect(self.on_dwt_checked)

        # Disable while trackpointing
        if sway_version >= "1.8":
            if self.settings["touchpad-dwtp"] == "enabled":
                self.ui.DWTP.setChecked(True)
            self.ui.DWTP.toggled.connect(self.on_dwtp_checked)
        else:
            self.ui.DWTP.setEnabled(False)

        # Left handed mode
        if self.settings["touchpad-left-handed"] == "enabled":
            self.ui.touchLeftHanded.setChecked(True)
        self.ui.touchLeftHanded.toggled.connect(self.on_touch_left_handed_checked)

        # Middle click emulation
        if self.settings["touchpad-middle-emulation"] == "enabled":
            self.ui.touchMiddle.setChecked(True)
        self.ui.touchMiddle.toggled.connect(self.on_touch_middle_emu_checked)

        # Pointer speed:
        touchAccelValue = float(self.settings["touchpad-pointer-accel"]) * 10
        self.ui.touchAccel.setValue(int(touchAccelValue))
        self.ui.touchAccel.valueChanged.connect(self.on_touch_accel_value_changed)

        # Acceleration profile
        self.touchAccelButtonGroup = QButtonGroup()
        self.touchAccelButtonGroup.addButton(self.ui.touchFlat)
        self.touchAccelButtonGroup.addButton(self.ui.touchAdaptive)
        if self.settings["touchpad-accel-profile"] == "flat":
            self.ui.touchFlat.setChecked(True)
        else:
            self.ui.touchAdaptive.setChecked(True)
        self.ui.touchFlat.clicked.connect(self.on_touch_accel_profile_changed)
        self.ui.touchAdaptive.clicked.connect(self.on_touch_accel_profile_changed)

        # Rotation angle (0.0 to 360.0) since Sway 1.9
        if sway_version >= "1.9":
            touchRotationValue = float(self.settings["touchpad-rotation-angle"])
            self.ui.touchRotationAngleSlider.setValue(int(touchRotationValue))
            self.ui.touchRotationAngle.setValue(self.ui.touchRotationAngleSlider.value())
            self.ui.touchRotationAngleSlider.sliderMoved.connect(self.ui.touchRotationAngle.setValue)
            self.ui.touchRotationAngleSlider.valueChanged.connect(self.on_touch_rotation_angle_value_changed)
        else:
            self.ui.touchRotationAngleSlider.setDisabled(True)
            self.ui.touchRotationAngle.setDisabled(True)
            self.ui.touchpadRotationLabel.setDisabled(True)

        # Tap-to-click
        if self.settings["touchpad-tap"] == "enabled":
            self.ui.tap_click.setChecked(True)
        self.ui.tap_click.toggled.connect(self.on_tap_click_checked)

        # Tap-and-drag
        if self.settings["touchpad-tap"] == "enabled":
            self.ui.drag.setEnabled(True)
        else:
            self.ui.drag.setEnabled(False)
        if self.settings["touchpad-drag"] == "enabled":
            self.ui.drag.setChecked(True)
        self.ui.drag.toggled.connect(self.on_tapdrag_checked)

        # Tap-and-drag lock
        if self.settings["touchpad-tap"] == "enabled":
            self.ui.drag_lock.setEnabled(True)
        else:
            self.ui.drag_lock.setEnabled(False)
        if self.settings["touchpad-drag-lock"] == "enabled":
            self.ui.drag_lock.setChecked(True)
        self.ui.drag_lock.toggled.connect(self.on_draglock_checked)

        # Tap button mapping:
        self.mappingButtonGroup = QButtonGroup()
        self.mappingButtonGroup.addButton(self.ui.lmr)
        self.mappingButtonGroup.addButton(self.ui.lrm)
        if self.settings["touchpad-tap"] == "enabled":
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

        # Click method
        self.clickMethodButtonGroup = QButtonGroup()
        self.clickMethodButtonGroup.addButton(self.ui.btn_BtnArea)
        self.clickMethodButtonGroup.addButton(self.ui.btn_ClickFinger)
        if self.settings["touchpad-click-method"] == "button_areas":
            self.ui.btn_BtnArea.setChecked(True)
        elif self.settings["touchpad-click-method"] == "clickfinger":
            self.ui.btn_ClickFinger.setChecked(True)
        self.ui.btn_BtnArea.clicked.connect(self.on_click_method_checked)
        self.ui.btn_ClickFinger.clicked.connect(self.on_click_method_checked)

        # Scrolling method
        self.scrollingButtonGroup = QButtonGroup()
        self.scrollingButtonGroup.addButton(self.ui.touchScrollNoScroll)
        self.scrollingButtonGroup.addButton(self.ui.touchScrollTwoFingers)
        self.scrollingButtonGroup.addButton(self.ui.touchScrollEdges)
        if self.settings["touchpad-scroll-method"] == "two_finger":
            self.ui.touchScrollTwoFingers.setChecked(True)
        elif self.settings["touchpad-scroll-method"] == "edge":
            self.ui.touchScrollEdges.setChecked(True)
        else:
            self.ui.touchScrollNoScroll.setChecked(True)

        self.ui.touchScrollNoScroll.clicked.connect(self.on_scroll_method_checked)
        self.ui.touchScrollTwoFingers.clicked.connect(self.on_scroll_method_checked)
        self.ui.touchScrollEdges.clicked.connect(self.on_scroll_method_checked)

        # Natural (inverted) scrolling:
        if self.settings["touchpad-natural-scroll"] == "enabled":
            self.ui.touchNatScroll.setChecked(True)
        self.ui.touchNatScroll.toggled.connect(self.on_touch_nat_scroll_checked)

        # Scrolling speed
        touchFactorValue = float(self.settings["touchpad-scroll-factor"]) * 10
        self.ui.touchScrollFactor.setValue(int(touchFactorValue))
        self.ui.touchScrollFactor.valueChanged.connect(self.on_touch_scroll_value_changed)

        # Tablet Settings #

        # Use this settings
        if self.settings["tablet-use-settings"] == "true":
            self.ui.TabletUseSettings.setChecked(True)
        self.ui.TabletUseSettings.clicked.connect(self.tablet_use_settings)

        # Tablet ID
        tablet_tools = list_inputs_by_type(input_type="tablet_tool")
        tablet_view = QListView(self.ui.tabletID)
        self.ui.tabletID.setView(tablet_view)
        if not tablet_tools:
            self.ui.tabletID.addItem("Not found")
            self.ui.tabWidget.widget(3).setEnabled(False)
        else:
            self.ui.tabletID.addItem("")
            for item in tablet_tools:
                self.ui.tabletID.addItem(item)
                tablet_view.setTextElideMode(Qt.TextElideMode.ElideNone)
                tablet_view.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
                self.ui.tabletID.setCurrentText(self.settings["tablet-identifier"])

        # Left handed mode (invert tablet's input)
        if self.settings["tablet-left-handed"] == "enabled":
            self.ui.tabletLeftHanded.setChecked(True)
        self.ui.tabletLeftHanded.clicked.connect(self.on_tablet_left_handed_checked)

        # Tablet tool mode ("pen", "eraser", "brush", "pencil", "airbrush", and the wildcard *, which matches all tools)
        mode = ["*", "pen", "eraser", "brush", "pencil", "airbrush"]
        for item in mode:
            self.ui.toolModeList.addItem(item)
        self.ui.toolModeList.setCurrentText(self.settings["tablet-tool-mode"][0])
        self.ui.toolModeList.activated.connect(self.on_tablet_set_tool_mode)

        # Tablet tool movement (absolute or relative)
        self.toolMoveButtonGroup = QButtonGroup()
        self.toolMoveButtonGroup.addButton(self.ui.toolMoveAbsolute)
        self.toolMoveButtonGroup.addButton(self.ui.toolMoveRelative)
        if self.settings["tablet-tool-mode"][1] == "absolute":
            self.ui.toolMoveAbsolute.setChecked(True)
        else:
            self.ui.toolMoveRelative.setChecked(True)
        self.ui.toolMoveAbsolute.clicked.connect(self.on_tablet_set_tool_mode)
        self.ui.toolMoveRelative.clicked.connect(self.on_tablet_set_tool_mode)

    def on_clicked_reset(self):
        defaults = load_json(default_settings)
        self.keyboard.on_clicked_reset(defaults)

        self.ui.pointerID.setCurrentText(defaults["pointer-identifier"])
        self.ui.pointerLeftHanded.setChecked(False)
        self.ui.pointerMiddle.setChecked(False)

        pointerAccelValue = float(defaults["pointer-pointer-accel"]) * 10
        self.ui.pointerAccel.setValue(int(pointerAccelValue))

        pointerRotationAngleValue = float(defaults["pointer-rotation-angle"])
        self.ui.pointerRotationAngleSlider.setValue(int(pointerRotationAngleValue))
        self.ui.pointerRotationAngle.setValue(self.ui.pointerRotationAngleSlider.value())

        for key, value in scroll_buttons.items():
            if value == defaults["pointer-scroll-button"]:
                self.ui.scrollButtonList.setCurrentText(key)

        self.ui.pointerFlat.setChecked(True)
        self.ui.pointerNatScroll.setChecked(False)
        self.ui.scrollButtonLock.setChecked(False)
        self.ui.scrollButtonList.setCurrentText(defaults["pointer-scroll-button"])

        pointerFactorValue = float(defaults["pointer-scroll-factor"]) * 10
        self.ui.pointerScrollFactor.setValue(int(pointerFactorValue))

        touchpads = list_inputs_by_type(input_type="touchpad")
        if touchpads:
            self.ui.touchpadID.setCurrentText(defaults["touchpad-identifier"])
            self.ui.touchEventsEnabled.setChecked(True)
            self.ui.DWT.setChecked(True)
            self.ui.DWTP.setChecked(False)
            self.ui.touchLeftHanded.setChecked(False)
            self.ui.touchMiddle.setChecked(True)

            touchAccelValue = float(defaults["touchpad-pointer-accel"]) * 10
            self.ui.touchAccel.setValue(int(touchAccelValue))

            touchpadRotationAngleValue = float(defaults["touchpad-rotation-angle"])
            self.ui.touchRotationAngleSlider.setValue(int(touchpadRotationAngleValue))
            self.ui.touchRotationAngle.setValue(self.ui.touchRotationAngleSlider.value())

            self.ui.touchFlat.setChecked(True)
            self.ui.tap_click.setChecked(True)
            self.ui.drag.setEnabled(True)
            self.ui.drag.setChecked(True)
            self.ui.drag_lock.setChecked(False)
            self.ui.lrm.setEnabled(True)
            self.ui.lmr.setEnabled(True)
            self.ui.touchScrollNoScroll.setChecked(True)
            self.ui.btn_BtnArea.setChecked(True)
            self.ui.touchNatScroll.setChecked(False)

            touchFactorValue = float(defaults["touchpad-scroll-factor"]) * 10
            self.ui.touchScrollFactor.setValue(int(touchFactorValue))

        tablet_tools = list_inputs_by_type(input_type="tablet_tool")
        if tablet_tools:
            self.ui.tabletID.setCurrentText(defaults["tablet-identifier"])
            self.ui.tabletLeftHanded.setChecked(False)

            self.ui.toolModeList.setCurrentText(defaults["tablet-tool-mode"][0])
            self.ui.toolMoveAbsolute.setChecked(True)

    def pointer_use_settings(self):
        if self.ui.PointerUseSettings.isChecked() is True:
            self.settings["pointer-use-settings"] = "true"
        else:
            self.settings["pointer-use-settings"] = "false"

    def set_pointer_identifier(self):
        self.settings["pointer-identifier"] = self.ui.pointerID.currentText()

    def on_pointer_left_handed_checked(self):
        if self.ui.pointerLeftHanded.isChecked() is True:
            self.settings["pointer-left-handed"] = "true"
        else:
            self.settings["pointer-left-handed"] = "false"

    def on_middle_checked(self):
        if self.ui.pointerMiddle.isChecked():
            self.settings["pointer-middle-emulation"] = "enabled"
        else:
            self.settings["pointer-middle-emulation"] = "disabled"

    def on_accel_value_changed(self):
        self.settings["pointer-pointer-accel"] = self.ui.pointerAccel.value() / 10

    def on_accel_profile_changed(self):
        if self.ui.pointerFlat.isChecked():
            self.settings["pointer-accel-profile"] = "flat"
        else:
            self.settings["pointer-accel-profile"] = "adaptive"

    def on_pointer_rotation_angle_value_changed(self):
        self.settings["pointer-rotation-angle"] = float(self.ui.pointerRotationAngle.value())

    def on_scroll_button_checked(self):
        self.settings["pointer-scroll-button"] = self.ui.scrollButtonList.currentData()

    def on_scroll_button_lock_checked(self):
        if self.ui.scrollButtonLock.isChecked() is True:
            self.settings["pointer-scroll-button-lock"] = "enabled"
        else:
            self.settings["pointer-scroll-button-lock"] = "disabled"

    def on_pointer_nat_scroll_checked(self):
        if self.ui.pointerNatScroll.isChecked() is True:
            self.settings["pointer-natural-scroll"] = "true"
        else:
            self.settings["pointer-natural-scroll"] = "false"

    def on_pointer_scroll_value_changed(self):
        self.settings["pointer-scroll-factor"] = self.ui.pointerScrollFactor.value() / 10

    def touchpad_use_settings(self):
        if self.ui.TouchPadUseSettings.isChecked() is True:
            self.settings["touchpad-use-settings"] = "true"
        else:
            self.settings["touchpad-use-settings"] = "false"

    def set_touchpad_identifier(self):
        self.settings["touchpad-identifier"] = self.ui.touchpadID.currentText()

    def on_touchpad_events_mode_changed(self):
        if self.ui.touchEventsDisabled.isChecked() is True:
            self.settings["touchpad-events"] = "disabled"
        elif self.ui.touchEventsOnExternalMouse.isChecked() is True:
            self.settings["touchpad-events"] = "disabled_on_external_mouse"
        else:
            self.settings["touchpad-events"] = "enabled"

    def on_dwt_checked(self):
        if self.ui.DWT.isChecked():
            self.settings["touchpad-dwt"] = "enabled"
        else:
            self.settings["touchpad-dwt"] = "disabled"

    def on_dwtp_checked(self):
        if self.ui.DWTP.isChecked():
            self.settings["touchpad-dwtp"] = "enabled"
        else:
            self.settings["touchpad-dwtp"] = "disabled"

    def on_touch_left_handed_checked(self):
        if self.ui.touchLeftHanded.isChecked():
            self.settings["touchpad-left-handed"] = "enabled"
        else:
            self.settings["touchpad-left-handed"] = "disabled"

    def on_touch_middle_emu_checked(self):
        if self.ui.touchMiddle.isChecked():
            self.settings["touchpad-middle-emulation"] = "enabled"
        else:
            self.settings["touchpad-middle-emulation"] = "disabled"

    def on_touch_accel_value_changed(self):
        self.settings["touchpad-pointer-accel"] = self.ui.touchAccel.value() / 10

    def on_touch_accel_profile_changed(self):
        if self.ui.touchFlat.isChecked():
            self.settings["touchpad-accel-profile"] = "flat"
        else:
            self.settings["touchpad-accel-profile"] = "adaptive"

    def on_touch_rotation_angle_value_changed(self):
        self.settings["touchpad-rotation-angle"] = float(self.ui.touchRotationAngle.value())

    def on_tap_click_checked(self):
        if self.ui.tap_click.isChecked():
            self.settings["touchpad-tap"] = "enabled"
            self.ui.drag.setEnabled(True)
            self.ui.drag_lock.setEnabled(True)
            self.ui.lrm.setEnabled(True)
            self.ui.lmr.setEnabled(True)
        else:
            self.settings["touchpad-tap"] = "disabled"
            self.ui.drag.setEnabled(False)
            self.ui.drag_lock.setEnabled(False)
            self.ui.lrm.setEnabled(False)
            self.ui.lmr.setEnabled(False)

    def on_tapdrag_checked(self):
        if self.ui.drag.isChecked():
            self.settings["touchpad-drag"] = "enabled"
        else:
            self.settings["touchpad-drag"] = "disabled"

    def on_draglock_checked(self):
        if self.ui.drag_lock.isChecked():
            self.settings["touchpad-drag-lock"] = "enabled"
        else:
            self.settings["touchpad-drag-lock"] = "disabled"

    def on_multi_tap_checked(self):
        if self.ui.lrm.isChecked():
            self.settings["touchpad-tap-button-map"] = "lrm"
        else:
            self.settings["touchpad-tap-button-map"] = "lmr"

    def on_click_method_checked(self):
        if self.ui.btn_ClickFinger.isChecked():
            self.settings["touchpad-click-method"] = "clickfinger"
        else:
            self.settings["touchpad-click-method"] = "button_areas"

    def on_scroll_method_checked(self):
        if self.ui.touchScrollTwoFingers.isChecked() is True:
            self.settings["touchpad-scroll-method"] = "two_finger"
        elif self.ui.touchScrollEdges.isChecked() is True:
            self.settings["touchpad-scroll-method"] = "edge"
        else:
            self.settings["touchpad-scroll-method"] = "none"


    def on_touch_nat_scroll_checked(self):
        if self.ui.touchNatScroll.isChecked() is True:
            self.settings["touchpad-natural-scroll"] = "enabled"
        else:
            self.settings["touchpad-natural-scroll"] = "disabled"

    def on_touch_scroll_value_changed(self):
        self.settings["touchpad-scroll-factor"] = self.ui.touchScrollFactor.value() / 10

    def tablet_use_settings(self):
        if self.ui.TabletUseSettings.isChecked() is True:
            self.settings["tablet-use-settings"] = "true"
        else:
            self.settings["tablet-use-settings"] = "false"

    def set_tablet_identifier(self):
        self.settings["tablet-identifier"] = self.ui.tabletID.currentText()

    def on_tablet_left_handed_checked(self):
        if self.ui.tabletLeftHanded.isChecked():
            self.settings["tablet-left-handed"] = "enabled"
        else:
            self.settings["tablet-left-handed"] = "disabled"

    def on_tablet_set_tool_mode(self):
        if self.ui.toolMoveAbsolute.isChecked() is True:
            self.settings["tablet-tool-mode"][1] = "absolute"
        else:
            self.settings["tablet-tool-mode"][1] = "relative"
        self.settings["tablet-tool-mode"][0] = self.ui.toolModeList.currentText()

    def on_clicked_about(self):
        self.about = AboutDialog()
        self.about.show()

    def on_clicked_apply(self):
        self.keyboard.set_keyboard_layout()
        save_to_config(self.settings)
        f = os.path.join(self.data_dir, "settings")
        print("Saving {}".format(f))
        save_json(self.settings, f)
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

        self.aboutDialog.version.setText(self.tr("Version: ") + app_version)

        self.aboutDialog.buttonBox.rejected.connect(self.cancel)

    def cancel(self):
        self.close()


def save_to_config(settings):
    if settings["keyboard-use-settings"] == "true":

        lines = ['input "type:keyboard" {'] if not settings["keyboard-identifier"] else [
            'input "%s" {' % settings["keyboard-identifier"]]
        lines.append('  xkb_layout {}'.format(','.join(settings["keyboard-layout"])))
        # Prevents adding empty xkb_variant option in config
        if settings["keyboard-variant"] and any(v.strip() for v in settings["keyboard-variant"]):
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

        config = load_text_file(sway_config).splitlines()
        new_config = []
        for line in config:
            if "include keyboard" not in line:
                new_config.append(line)
        new_config.append("include keyboard")
        save_list_to_text_file(new_config, sway_config)

    else:
        config = load_text_file(sway_config).splitlines()
        old_config = []
        for line in config:
            old_config.append(line)
        if "include keyboard" in old_config:
            old_config.remove("include keyboard")
        save_list_to_text_file(old_config, sway_config)

        if os.path.exists(os.path.join(config_home, "sway/keyboard")):
            os.unlink(os.path.join(config_home, "sway/keyboard"))

    if settings["pointer-use-settings"] == "true":

        lines = ['input "type:pointer" {'] if not settings["pointer-identifier"] else [
            'input "%s" {' % settings["pointer-identifier"]]
        lines.append('  accel_profile {}'.format(settings["pointer-accel-profile"])),
        lines.append('  pointer_accel {}'.format(settings["pointer-pointer-accel"])),
        lines.append('  natural_scroll {}'.format(settings["pointer-natural-scroll"])),
        lines.append('  scroll_factor {}'.format(settings["pointer-scroll-factor"])),
        lines.append('  scroll_button {}'.format(settings["pointer-scroll-button"])),
        lines.append('  left_handed {}'.format(settings["pointer-left-handed"])),
        lines.append('  middle_emulation {}'.format(settings["pointer-middle-emulation"])),
        if sway_version >= "1.9":
            lines.append('  rotation_angle {}'.format(settings["pointer-rotation-angle"]))
            lines.append('  scroll_button_lock {}'.format(settings["pointer-scroll-button-lock"])),
        lines.append('}')

        save_list_to_text_file(lines, os.path.join(config_home, "sway/pointer"))

        config = load_text_file(sway_config).splitlines()
        new_config = []
        for line in config:
            if "include pointer" not in line:
                new_config.append(line)
        new_config.append("include pointer")
        save_list_to_text_file(new_config, sway_config)

    else:
        config = load_text_file(sway_config).splitlines()
        old_config = []
        for line in config:
            old_config.append(line)
        if "include pointer" in old_config:
            old_config.remove("include pointer")
        save_list_to_text_file(old_config, sway_config)

        if os.path.exists(os.path.join(config_home, "sway/pointer")):
            os.unlink(os.path.join(config_home, "sway/pointer"))

    if settings["touchpad-use-settings"] == "true":
        lines = ['input "type:touchpad" {'] if not settings["touchpad-identifier"] else [
            'input "%s" {' % settings["touchpad-identifier"]]
        lines.append('  events {}'.format(settings["touchpad-events"])),
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
        if sway_version >= "1.8":
            lines.append('  dwtp {}'.format(settings["touchpad-dwtp"])),
        if sway_version >= "1.9":
            lines.append('  rotation_angle {}'.format(settings["touchpad-rotation-angle"])),
        lines.append('  middle_emulation {}'.format(settings["touchpad-middle-emulation"])),
        lines.append('  click_method {}'.format(settings["touchpad-click-method"]))
        lines.append('}')

        save_list_to_text_file(lines, os.path.join(config_home, "sway/touchpad"))

        config = load_text_file(sway_config).splitlines()
        new_config = []
        for line in config:
            if "include touchpad" not in line:
                new_config.append(line)
        new_config.append("include touchpad")
        save_list_to_text_file(new_config, sway_config)

    else:
        config = load_text_file(sway_config).splitlines()
        old_config = []
        for line in config:
            old_config.append(line)
        if "include touchpad" in old_config:
            old_config.remove("include touchpad")
        save_list_to_text_file(old_config, sway_config)

        if os.path.exists(os.path.join(config_home, "sway/touchpad")):
            os.unlink(os.path.join(config_home, "sway/touchpad"))

    if settings["tablet-use-settings"] == "true":
        lines = ['input "type:tablet_tool" {'] if not settings["tablet-identifier"] else [
            'input "%s" {' % settings["tablet-identifier"]]
        lines.append('  left_handed {}'.format(settings["tablet-left-handed"]))
        lines.append('  tool_mode {}'.format(' '.join(settings["tablet-tool-mode"])))
        lines.append('}')

        save_list_to_text_file(lines, os.path.join(config_home, "sway/tablet"))

        config = load_text_file(sway_config).splitlines()
        new_config = []
        for line in config:
            if "include tablet" not in line:
                new_config.append(line)
        new_config.append("include tablet")
        save_list_to_text_file(new_config, sway_config)

    else:
        config = load_text_file(sway_config).splitlines()
        old_config = []
        for line in config:
            old_config.append(line)
        if "include tablet" in old_config:
            old_config.remove("include tablet")
        save_list_to_text_file(old_config, sway_config)

        if os.path.exists(os.path.join(config_home, "sway/tablet")):
            os.unlink(os.path.join(config_home, "sway/tablet"))


def load_settings(data_dir):
    settings_file = os.path.join(data_dir, "settings")
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
        copy2(os.path.join(dir_name, "data/defaults.json"), os.path.join(data_dir, "settings"))
        settings = load_json(settings_file)
    return settings


def main():
    app = QApplication(["Sway Input Configurator"])
    app.setDesktopFileName("sway-input-config")

    if os.getenv("SWAYSOCK"):
        parser = argparse.ArgumentParser()
        parser.add_argument("-v",
                            "--version",
                            action="version",
                            version=app_version,
                            help="display application version")
        parser.add_argument("-l",
                            "--locale",
                            default=QLocale.system().name(),
                            help="force application locale")
        parser.add_argument("-r",
                            "--restore",
                            action="store_true",
                            help="restore default settings")
        args = parser.parse_args()

        locale = args.locale
        locale_ts = QTranslator()
        app_ts = QTranslator()
        locale_ts.load('qt_%s' % locale, QLibraryInfo.path(QLibraryInfo.LibraryPath.TranslationsPath))
        app_ts.load('lang_%s' % locale, os.path.join(dir_name, "langs"))
        app.installTranslator(locale_ts)
        app.installTranslator(app_ts)

        data_dir = get_data_dir()
        settings = load_settings(data_dir)

        if args.restore:
            if input("\nRestore default settings? y/N ").upper() == "Y":
                copy2(os.path.join(dir_name, "data/defaults.json"), os.path.join(data_dir, "settings"))
                sys.exit(0)

        win = MainWindow(settings, data_dir)
        win.show()
        sys.exit(app.exec())
    else:
        win = ErrorMessage()
        win.show()
        sys.exit(app.exec())


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    main()
