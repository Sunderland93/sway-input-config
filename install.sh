#!/usr/bin/env bash

python3 setup.py install --optimize=1
cp sway-input-config.desktop /usr/share/applications/
cp sway-input-config.svg /usr/share/pixmaps/
