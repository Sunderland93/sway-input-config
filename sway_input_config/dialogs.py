from PyQt6.QtWidgets import QDialog, QListWidgetItem
from PyQt6.QtCore import Qt
from sway_input_config.ui_selectlayout import Ui_SelectKeyboardLayoutDialog

class SelectKeyboardLayout(QDialog):
    def __init__(self, layouts, variants, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Add Keyboard Layout")
        self.setModal(True)

        self.select_layout = Ui_SelectKeyboardLayoutDialog()
        self.select_layout.setupUi(self)

        self.layout_code = ""
        self.variant_code = ""

        none_item = QListWidgetItem()
        none_item.setData(Qt.ItemDataRole.UserRole, "")
        none_item.setData(Qt.ItemDataRole.DisplayRole, "")
        self.select_layout.variants.addItem(none_item)

        for key, value in layouts:
            item = QListWidgetItem(value)
            item.setData(Qt.ItemDataRole.UserRole, key)
            item.setData(Qt.ItemDataRole.DisplayRole, value)
            self.select_layout.layouts.addItem(item)

        self.layouts = layouts
        self.variants = variants

        self.select_layout.layouts.setCurrentItem(self.select_layout.layouts.item(0))
        self.select_layout.variants.setCurrentItem(self.select_layout.variants.item(0))

        self.select_layout.layouts.currentItemChanged.connect(self.on_layout_changed)
        self.select_layout.buttonBox.rejected.connect(self.reject)
        self.select_layout.buttonBox.accepted.connect(self.on_add_layout)

    def on_layout_changed(self):
        item = self.select_layout.layouts.currentItem()
        self.select_layout.variants.clear()
        none_item = QListWidgetItem()
        none_item.setData(Qt.ItemDataRole.UserRole, "")
        none_item.setData(Qt.ItemDataRole.DisplayRole, "")
        self.select_layout.variants.addItem(none_item)
        for key, values in self.variants:
            value = values.split(":")[0]
            description = values.split(":")[1]
            if value in item.data(Qt.ItemDataRole.UserRole):
                if "custom" not in item.data(Qt.ItemDataRole.UserRole):
                    vitem = QListWidgetItem(description)
                    vitem.setData(Qt.ItemDataRole.UserRole, key)
                    vitem.setData(Qt.ItemDataRole.DisplayRole, description)
                    self.select_layout.variants.addItem(vitem)
        self.select_layout.variants.setCurrentItem(self.select_layout.variants.item(0))

    def on_add_layout(self):
        layout_item = self.select_layout.layouts.currentItem()
        variant_item = self.select_layout.variants.currentItem()
        self.layout_code = layout_item.data(Qt.ItemDataRole.UserRole)
        self.variant_code = variant_item.data(Qt.ItemDataRole.UserRole) if variant_item else ""
        self.accept()