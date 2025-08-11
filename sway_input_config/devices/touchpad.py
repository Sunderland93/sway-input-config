from PyQt6.QtWidgets import QListView, QButtonGroup
from PyQt6.QtCore import Qt
from sway_input_config.utils import list_inputs_by_type

class TouchpadSettings:
    def __init__(self, ui, settings):
        self.ui = ui
        self.settings = settings

    def init_ui(self, sway_version):
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
        if self.settings["touchpad-tap-button-map"] == "lrm":
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

    def on_clicked_reset(self, defaults):
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