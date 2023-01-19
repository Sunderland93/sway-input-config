# Sway Input Configurator

Input devices configurator for [SwayWM](https://swaywm.org/), written in Python and Qt5/PySide2, inspired by [nwg-shell-config](https://github.com/nwg-piotr/nwg-shell-config). It uses standard [libinput](https://www.mankier.com/5/sway-input) options to configure keyboard, touchpad and pointer devices.

![Keyboard settings](https://github.com/Sunderland93/sway-input-config/blob/master/screenshot1.png?raw=true)

![Mouse settings](https://github.com/Sunderland93/sway-input-config/blob/master/screenshot2.png?raw=true)

![Touchpad settings](https://github.com/Sunderland93/sway-input-config/blob/master/screenshot3.png?raw=true)

## Installation:

#### Dependencies (Debian/Ubuntu):
* python3
* python3-pyside2.qtwidgets
* python3-pyside2.qtcore
* python3-pyside2.qtgui
* python3-setuptools
* python3-i3ipc

#### Dependencies (Arch Linux):
* python
* pyside2
* python-setuptools
* python-i3ipc

`git clone https://github.com/Sunderland93/sway-input-config.git`
`cd sway-input-config && python setup.py install`

Add the following lines to your Sway config (usually in `~/.config/sway/config`):

```text
include keyboard
include pointer
include touchpad   # if you don't have a touchpad, don't add this line
```

## Settings:

Configuration file is located in `~/.config/sway-input-config/settings`. It's a JSON-file:
```json
{
  "keyboard-layout": [
   "us"
  ],
  "keyboard-variant": [
   ""
  ],
  "keyboard-shortcut": "",
  "keyboard-identifier": "",
  "keyboard-model": "pc105",
  "keyboard-repeat-delay": 300,
  "keyboard-repeat-rate": 40,
  "keyboard-capslock": "disabled",
  "keyboard-numlock": "disabled",
  "pointer-identifier": "",
  "pointer-accel-profile": "flat",
  "pointer-pointer-accel": 0.0,
  "pointer-natural-scroll": "disabled",
  "pointer-scroll-factor": 1.0,
  "pointer-left-handed": "disabled",
  "touchpad-identifier": "",
  "touchpad-accel-profile": "flat",
  "touchpad-pointer-accel": 0.0,
  "touchpad-natural-scroll": "disabled",
  "touchpad-scroll-factor": 1.0,
  "touchpad-scroll-method": "two_finger",
  "touchpad-left-handed": "disabled",
  "touchpad-tap": "enabled",
  "touchpad-tap-button-map": "lrm",
  "touchpad-drag": "enabled",
  "touchpad-drag-lock": "disabled",
  "touchpad-dwt": "enabled",
  "touchpad-middle-emulation": "enabled"
}
```
If **settings** file is corrupted or missing, Sway Input Configurator will use the default settings and recreate **settings** file. Config files for keyboard, touchpad and mouse is located in `~/.config/sway/` (`keyboard`, `touchpad` and `pointer` respectively). 
