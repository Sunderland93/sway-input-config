#!/usr/bin/env bash

path=$(python3 -c 'import site; print(site.getsitepackages()[0])')
rm -r $path/sway_input_config*
rm /usr/local/bin/sway-input-config
rm /usr/share/applications/sway-input-config.desktop
rm /usr/share/pixmaps/sway-input-config.svg
