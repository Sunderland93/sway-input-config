import os
from PyQt6.QtWidgets import QDialog, QListWidgetItem, QDialogButtonBox
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from sway_input_config.ui_about import Ui_about
from sway_input_config.ui_error_message import Ui_ErrorMessage
from sway_input_config.ui_selectlayout import Ui_SelectKeyboardLayoutDialog

class AboutDialog(QDialog):
    def __init__(self, dir_name, app_version):
        super().__init__()
        self.aboutDialog = Ui_about()
        self.aboutDialog.setupUi(self)

        self.pixmap = QPixmap(os.path.join(dir_name, "data/logo_sic.png"))
        self.aboutDialog.pixmap.setPixmap(self.pixmap)

        self.aboutDialog.version.setText(self.tr("Version: ") + app_version)

        self.aboutDialog.buttonBox.rejected.connect(self.cancel)

    def cancel(self):
        self.close()


class ErrorMessage(QDialog):
    def __init__(self):
        super(ErrorMessage, self).__init__()
        self.ui = Ui_ErrorMessage()
        self.ui.setupUi(self)

        self.btnOk = self.ui.buttonBox.button(QDialogButtonBox.StandardButton.Ok)
        self.btnOk.clicked.connect(self.on_clicked_ok)

    def on_clicked_ok(self):
        self.close()


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