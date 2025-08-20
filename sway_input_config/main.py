#!/usr/bin/env python3

import argparse
import os
import sys
import signal
from PyQt6.QtWidgets import (QApplication, QMainWindow, QDialogButtonBox, QDialog)
from PyQt6.QtCore import QTranslator, QLocale, QLibraryInfo
from PyQt6.QtGui import QPixmap
from shutil import copy2
from sway_input_config.utils import (get_data_dir,
                                     get_sway_version,
                                     get_config_home,
                                     load_json, save_json,
                                     save_list_to_text_file,
                                     load_text_file, reload_sway_config)
from sway_input_config.ui_mainwindow import Ui_MainWindow
from sway_input_config.ui_about import Ui_about
from sway_input_config.ui_error_message import Ui_ErrorMessage
from sway_input_config.devices.keyboard import KeyboardSettings
from sway_input_config.devices.pointer import PointerSettings
from sway_input_config.devices.tablet import TabletSettings
from sway_input_config.devices.touchpad import TouchpadSettings

app_version = "1.4.4"

if os.getenv("SWAYSOCK"):
    sway_version = get_sway_version()
    data_dir = ""
    config_home = get_config_home()
    sway_config = os.path.join(config_home, "sway", "config")

dir_name = os.path.dirname(__file__)
default_settings = os.path.join(dir_name, "data/defaults.json")


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


class MainWindow(QMainWindow):
    def __init__(self, settings, data_dir):
        super(MainWindow, self).__init__()
        self.settings = settings
        self.data_dir = data_dir
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.keyboard = KeyboardSettings(self.ui, self.settings)
        self.pointer = PointerSettings(self.ui, self.settings)
        self.tablet = TabletSettings(self.ui, self.settings)
        self.touchpad = TouchpadSettings(self.ui, self.settings)

        self.keyboard.init_ui()
        self.pointer.init_ui(sway_version)
        self.tablet.init_ui()
        self.touchpad.init_ui(sway_version)

        # Dialog buttons
        self.ui.buttonBox.rejected.connect(self.cancel)
        self.btnApply = self.ui.buttonBox.button(QDialogButtonBox.StandardButton.Apply)
        self.btnApply.clicked.connect(self.on_clicked_apply)
        self.btnReset = self.ui.buttonBox.button(QDialogButtonBox.StandardButton.RestoreDefaults)
        self.btnReset.clicked.connect(self.on_clicked_reset)
        self.ui.buttonBox.helpRequested.connect(self.on_clicked_about)

    def on_clicked_reset(self):
        defaults = load_json(default_settings)
        self.keyboard.on_clicked_reset(defaults)
        self.pointer.on_clicked_reset(defaults)
        self.tablet.on_clicked_reset(defaults)
        self.touchpad.on_clicked_reset(defaults)

    def on_clicked_about(self):
        self.about = AboutDialog(dir_name, app_version)
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
