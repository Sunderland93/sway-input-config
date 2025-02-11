import os
from abc import ABC, abstractmethod
from sway_input_config.utils import save_list_to_text_file, load_text_file


class InputBackend(ABC):
    @abstractmethod
    def save_keyboard_settings(self, settings):
        pass

    @abstractmethod
    def save_pointer_settings(self, settings):
        pass

    @abstractmethod
    def save_touchpad_settings(self, settings):
        pass

    @abstractmethod
    def save_tablet_settings(self, settings):
        pass


class SwayInputBackend(InputBackend):
    def __init__(self, config_home, sway_config, sway_version):
        self.config_home = config_home
        self.sway_config = sway_config
        self.sway_version = sway_version

    def save_keyboard_settings(self, settings):
        if settings["keyboard-use-settings"] == "true":
            lines = ['input "type:keyboard" {'] if not settings["keyboard-identifier"] else [
                'input "%s" {' % settings["keyboard-identifier"]]
            lines.append('  xkb_layout {}'.format(','.join(settings["keyboard-layout"])))
            lines.append('  xkb_variant {}'.format(','.join(settings["keyboard-variant"])))
            if settings["keyboard-shortcut"]:
                lines.append('  xkb_options {}'.format(settings["keyboard-shortcut"]))
            lines.append('  xkb_model {}'.format(settings["keyboard-model"]))
            lines.append('  repeat_delay {}'.format(settings["keyboard-repeat-delay"]))
            lines.append('  repeat_rate {}'.format(settings["keyboard-repeat-rate"]))
            lines.append('  xkb_capslock {}'.format(settings["keyboard-capslock"]))
            lines.append('  xkb_numlock {}'.format(settings["keyboard-numlock"]))
            lines.append('}')

            save_list_to_text_file(lines, os.path.join(self.config_home, "sway/keyboard"))

            config = load_text_file(self.sway_config).splitlines()
            new_config = []
            for line in config:
                if "include keyboard" not in line:
                    new_config.append(line)
            new_config.append("include keyboard")
            save_list_to_text_file(new_config, self.sway_config)
            
        else:
            config = load_text_file(self.sway_config).splitlines()
            old_config = []
            for line in config:
                old_config.append(line)
            if "include keyboard" in old_config:
                old_config.remove("include keyboard")
            save_list_to_text_file(old_config, self.sway_config)

            if os.path.exists(os.path.join(self.config_home, "sway/keyboard")):
                os.unlink(os.path.join(self.config_home, "sway/keyboard"))

    def save_pointer_settings(self, settings):
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
            if self.sway_version >= "1.9":
                lines.append('  rotation_angle {}'.format(settings["pointer-rotation-angle"]))
                lines.append('  scroll_button_lock {}'.format(settings["pointer-scroll-button-lock"])),
            lines.append('}')

            save_list_to_text_file(lines, os.path.join(self.config_home, "sway/pointer"))

            config = load_text_file(self.sway_config).splitlines()
            new_config = []
            for line in config:
                if "include pointer" not in line:
                    new_config.append(line)
            new_config.append("include pointer")
            save_list_to_text_file(new_config, self.sway_config)
        else:
            config = load_text_file(self.sway_config).splitlines()
            old_config = []
            for line in config:
                old_config.append(line)
            if "include pointer" in old_config:
                old_config.remove("include pointer")
            save_list_to_text_file(old_config, self.sway_config)
            
            if os.path.exists(os.path.join(self.config_home, "sway/pointer")):
                os.unlink(os.path.join(self.config_home, "sway/pointer"))

    def save_touchpad_settings(self, settings):
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
            if self.sway_version >= "1.8":
                lines.append('  dwtp {}'.format(settings["touchpad-dwtp"])),
            if self.sway_version >= "1.9":
                lines.append('  rotation_angle {}'.format(settings["touchpad-rotation-angle"])),
            lines.append('  middle_emulation {}'.format(settings["touchpad-middle-emulation"])),
            lines.append('  click_method {}'.format(settings["touchpad-click-method"]))
            lines.append('}')

            save_list_to_text_file(lines, os.path.join(self.config_home, "sway/touchpad"))

            config = load_text_file(self.sway_config).splitlines()
            new_config = []
            for line in config:
                if "include touchpad" not in line:
                    new_config.append(line)
            new_config.append("include touchpad")
            save_list_to_text_file(new_config, self.sway_config)
        else:
            config = load_text_file(self.sway_config).splitlines()
            old_config = []
            for line in config:
                old_config.append(line)
            if "include touchpad" in old_config:
                old_config.remove("include touchpad")
            save_list_to_text_file(old_config, self.sway_config)

            if os.path.exists(os.path.join(self.config_home, "sway/touchpad")):
                os.unlink(os.path.join(self.config_home, "sway/touchpad"))

    def save_tablet_settings(self, settings):
        if settings["tablet-use-settings"] == "true":
            lines = ['input "type:tablet_tool" {'] if not settings["tablet-identifier"] else [
                'input "%s" {' % settings["tablet-identifier"]]
            lines.append('  left_handed {}'.format(settings["tablet-left-handed"]))
            lines.append('  tool_mode {}'.format(' '.join(settings["tablet-tool-mode"])))
            lines.append('}')

            save_list_to_text_file(lines, os.path.join(self.config_home, "sway/tablet"))

            config = load_text_file(self.sway_config).splitlines()
            new_config = []
            for line in config:
                if "include tablet" not in line:
                    new_config.append(line)
            new_config.append("include tablet")
            save_list_to_text_file(new_config, self.sway_config)
        else:
            config = load_text_file(self.sway_config).splitlines()
            old_config = []
            for line in config:
                old_config.append(line)
            if "include tablet" in old_config:
                old_config.remove("include tablet")
            save_list_to_text_file(old_config, self.sway_config)
            
            if os.path.exists(os.path.join(self.config_home, "sway/tablet")):
                os.unlink(os.path.join(self.config_home, "sway/tablet"))