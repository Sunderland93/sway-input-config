from PyQt6.QtWidgets import QListView, QButtonGroup
from PyQt6.QtCore import Qt
from sway_input_config.utils import list_inputs_by_type

# Buttons array used for on_button_down scroll method
scroll_buttons = {
    "Disabled": "disable",
    "Left button": "BTN_LEFT",
    "Right button": "BTN_RIGHT",
    "Middle button": "BTN_MIDDLE",
    "Side button": "BTN_SIDE",
    "Extra button": "BTN_EXTRA"
    }

class PointerSettings:
    def __init__(self, ui, settings):
        self.ui = ui
        self.settings = settings

    def init_ui(self, sway_version):
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

    def on_clicked_reset(self, defaults):
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