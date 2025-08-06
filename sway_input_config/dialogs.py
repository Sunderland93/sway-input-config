import os
from PyQt6.QtWidgets import QDialog, QDialogButtonBox
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from sway_input_config.ui_about import Ui_about
from sway_input_config.ui_error_message import Ui_ErrorMessage

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