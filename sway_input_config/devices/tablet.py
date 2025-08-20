from PyQt6.QtWidgets import QListView, QButtonGroup
from PyQt6.QtCore import Qt
from sway_input_config.utils import list_inputs_by_type

class TabletSettings:
    def __init__(self, ui, settings):
        self.ui = ui
        self.settings = settings

    def init_ui(self):
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

    def on_clicked_reset(self, defaults):
        tablet_tools = list_inputs_by_type(input_type="tablet_tool")
        if tablet_tools:
            self.ui.tabletID.setCurrentText(defaults["tablet-identifier"])
            self.ui.tabletLeftHanded.setChecked(False)

            self.ui.toolModeList.setCurrentText(defaults["tablet-tool-mode"][0])
            self.ui.toolMoveAbsolute.setChecked(True)