import platform
import re
from PyQt6.QtWidgets import QTreeWidgetItem, QListView
from PyQt6.QtCore import Qt
from sway_input_config.dialogs import SelectKeyboardLayout
from sway_input_config.utils import list_inputs_by_type, load_text_file

os_name = platform.system()
if os_name == "Linux":
    XKB_BASE_LIST = load_text_file("/usr/share/X11/xkb/rules/base.lst").splitlines()
elif os_name == "FreeBSD":
    XKB_BASE_LIST = load_text_file("/usr/local/share/X11/xkb/rules/base.lst").splitlines()

models   =  []
layouts  =  []
variants =  []
options  =  []

for line in XKB_BASE_LIST:
    if not line:
        continue
    match = re.match(r'^!\s*(\w+)\s*$', line)
    if match:
        category = match.group(1)
    else:
        match = re.match(r'^\s*(\w+:\w+|\w+-\w+|\w+)\s*(.*)$', line)
        if not match:
            continue
        key = match.group(1)
        value = match.group(2)
        if category == 'model':
            models.append((key, value))
        elif category == 'layout':
            layouts.append((key, value))
        elif category == 'variant':
            variants.append((key, value))
        elif category == 'option':
            options.append((key, value))


class KeyboardSettings:
    def __init__(self, ui, settings):
        self.ui = ui
        self.settings = settings

    def init_ui(self):
        # Use this settings
        if self.settings["keyboard-use-settings"] == "true":
             self.ui.KeyBoardUseSettings.setChecked(True)
        self.ui.KeyBoardUseSettings.toggled.connect(self.keyboard_use_settings)

        # Keyboard layout
        for key, value in layouts:
             if key in self.settings["keyboard-layout"]:
                  self.layout_item = QTreeWidgetItem(self.ui.layouts)
                  self.layout_item.setData(0, Qt.ItemDataRole.DisplayRole, value)
                  self.layout_item.setData(0, Qt.ItemDataRole.UserRole, key)
                  self.ui.layouts.addTopLevelItem(self.layout_item)
                  for key, values in variants:
                       value = values.split(":")[0]
                       description = values.split(":")[1]
                       if value in self.layout_item.data(0, Qt.ItemDataRole.UserRole):
                            # Workaround to prevent custom layout from using variants for English(US)
                            if "custom" not in self.layout_item.data(0, Qt.ItemDataRole.UserRole):
                                 if key in self.settings["keyboard-variant"]:
                                      self.layout_item.setData(1, Qt.ItemDataRole.DisplayRole, description)
                                      self.layout_item.setData(1, Qt.ItemDataRole.UserRole, key)

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
        kbd_view.setTextElideMode(Qt.TextElideMode.ElideNone)
        kbd_view.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.ui.kbdID.setCurrentText(self.settings["keyboard-identifier"])
        self.ui.kbdID.activated.connect(self.set_kbd_identifier)

        # Keyboard model option
        model_view = QListView(self.ui.kbdModel)
        self.ui.kbdModel.setView(model_view)
        model_view.setTextElideMode(Qt.TextElideMode.ElideNone)
        model_view.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        for key, value in models:
             self.ui.kbdModel.addItem(value, key)
             if key == self.settings["keyboard-model"]:
                  self.ui.kbdModel.setCurrentText(value)
        self.ui.kbdModel.activated.connect(self.set_model)

        # Keyboard shortcut option
        shortcut_view = QListView(self.ui.shortcutName)
        self.ui.shortcutName.setView(shortcut_view)
        self.ui.shortcutName.addItem("")
        for key, value in options:
            if "grp:" in key:
                  self.ui.shortcutName.addItem(value, key)
            if key == self.settings["keyboard-shortcut"]:
                 self.ui.shortcutName.setCurrentText(value)
        shortcut_view.setTextElideMode(Qt.TextElideMode.ElideNone)
        shortcut_view.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.ui.shortcutName.activated.connect(self.set_shortcut)

        # Repeat delay
        self.ui.repeatDelaySlider.setValue(self.settings["keyboard-repeat-delay"])
        self.ui.repeatDelay.setValue(self.ui.repeatDelaySlider.value())
        self.ui.repeatDelay.valueChanged.connect(self.ui.repeatDelaySlider.setValue)
        self.ui.repeatDelaySlider.sliderMoved.connect(self.ui.repeatDelay.setValue)
        self.ui.repeatDelaySlider.valueChanged.connect(self.on_repeat_delay_value_changed)
        
        # Repeat rate
        self.ui.repeatRateSlider.setValue(self.settings["keyboard-repeat-rate"])
        self.ui.repeatRate.setValue(self.ui.repeatRateSlider.value())
        self.ui.repeatRate.valueChanged.connect(self.ui.repeatRateSlider.setValue)
        self.ui.repeatRateSlider.sliderMoved.connect(self.ui.repeatRate.setValue)
        self.ui.repeatRateSlider.valueChanged.connect(self.on_repeat_rate_value_changed)

        # Enable Caps Lock option
        if self.settings["keyboard-capslock"] == "enabled":
            self.ui.caps_lock.setChecked(True)
        self.ui.caps_lock.toggled.connect(self.on_caps_lock_checked)
        
        # Enable Num Lock option
        if self.settings["keyboard-numlock"] == "enabled":
            self.ui.num_lock.setChecked(True)
        self.ui.num_lock.toggled.connect(self.on_num_lock_checked)

    def keyboard_use_settings(self):
        if self.ui.KeyBoardUseSettings.isChecked() is True:
            self.settings["keyboard-use-settings"] = "true"
        else:
            self.settings["keyboard-use-settings"] = "false"

    def on_add_keyboard_layout(self):
        self.dlg = SelectKeyboardLayout(self.layouts, self.variants)
        if self.dlg.exec() == 1:
            lay_key = self.dlg.select_layout.layouts.currentItem().data(Qt.ItemDataRole.DisplayRole)
            lay_value = self.dlg.select_layout.layouts.currentItem().data(Qt.ItemDataRole.UserRole)
            var_key = self.dlg.select_layout.variants.currentItem().data(Qt.ItemDataRole.DisplayRole)
            var_value = self.dlg.select_layout.variants.currentItem().data(Qt.ItemDataRole.UserRole)
            self.item = QTreeWidgetItem(self.ui.layouts)
            self.item.setData(0, Qt.ItemDataRole.DisplayRole, lay_key)
            self.item.setData(0, Qt.ItemDataRole.UserRole, lay_value)
            self.item.setData(1, Qt.ItemDataRole.DisplayRole, var_key)
            self.item.setData(1, Qt.ItemDataRole.UserRole, var_value)
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
                if item.data(1, Qt.ItemDataRole.UserRole) is None:
                    variants.append(str(""))
                else:
                    variants.append(item.data(1, Qt.ItemDataRole.UserRole))
                layouts.append(item.data(0, Qt.ItemDataRole.UserRole))
                row += 1
        self.settings["keyboard-layout"] = layouts
        self.settings["keyboard-variant"] = variants

    def set_kbd_identifier(self):
        self.settings["keyboard-identifier"] = self.ui.kbdID.currentText()

    def set_model(self):
        self.settings["keyboard-model"] = self.ui.kbdModel.currentData()

    def set_shortcut(self):
        self.settings["keyboard-shortcut"] = self.ui.shortcutName.currentData()

    def on_repeat_delay_value_changed(self):
        self.settings["keyboard-repeat-delay"] = self.ui.repeatDelay.value()

    def on_repeat_rate_value_changed(self):
        self.settings["keyboard-repeat-rate"] = self.ui.repeatRate.value()

    def on_caps_lock_checked(self):
        if self.ui.caps_lock.isChecked():
            self.settings["keyboard-capslock"] = "enabled"
        else:
            self.settings["keyboard-capslock"] = "disabled"

    def on_num_lock_checked(self):
        if self.ui.num_lock.isChecked():
            self.settings["keyboard-numlock"] = "enabled"
        else:
            self.settings["keyboard-numlock"] = "disabled"

    def on_clicked_reset(self, defaults):
        self.ui.layouts.clear()
        for key, values in layouts:
            if key in defaults["keyboard-layout"]:
                self.layout_item = QTreeWidgetItem(self.ui.layouts)
                self.layout_item.setData(0, Qt.ItemDataRole.DisplayRole, values)
                self.layout_item.setData(0, Qt.ItemDataRole.UserRole, key)
                self.ui.layouts.addTopLevelItem(self.layout_item)
                for key, values in variants:
                    value = values.split(":")[0]
                    description = values.split(":")[1]
                    if value in self.layout_item.data(0, Qt.ItemDataRole.UserRole):
                        # Workaround to prevent custom layout from using variants for English(US)
                        if "custom" not in self.layout_item.data(0, Qt.ItemDataRole.UserRole):
                            if key in defaults["keyboard-variant"]:
                                self.layout_item.setData(1, Qt.ItemDataRole.DisplayRole, description)
                                self.layout_item.setData(1, Qt.ItemDataRole.UserRole, key)
        for key, value in models:
            if key == defaults["keyboard-model"]:
                self.ui.kbdModel.setCurrentText(value)
        self.ui.shortcutName.setCurrentText(defaults["keyboard-shortcut"])
        self.ui.kbdID.setCurrentText(defaults["keyboard-identifier"])
        self.ui.repeatDelaySlider.setValue(defaults["keyboard-repeat-delay"])
        self.ui.repeatDelay.setValue(self.ui.repeatDelaySlider.value())
        self.ui.repeatRateSlider.setValue(defaults["keyboard-repeat-rate"])
        self.ui.repeatRate.setValue(self.ui.repeatRateSlider.value())
        self.ui.caps_lock.setChecked(False)
        self.ui.num_lock.setChecked(False)