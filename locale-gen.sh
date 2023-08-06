#!/bin/bash

set -e

# Check the script is not being run by root
if [ "$(id -u)" == "0" ]; then
   echo "This script must not be run as root!" > /dev/stderr
   exit 1
fi 

langs="$(pwd)"/sway_input_config/langs
sources="$(pwd)"/sway_input_config

if [ -n "$1" ]; then
    lang=$1
else
    lang=$(locale | grep LANG | cut -d= -f2 | cut -d. -f1)
fi

cd "$sources" || exit

if [[ -x /usr/bin/pylupdate5 ]]; then
    /usr/bin/pylupdate5 -noobsolete \
        main.py \
        ui_about.py \
        ui_mainwindow.py \
        ui_selectlayout.py \
        -ts "$langs"/"lang_$lang.ts"
else
    echo "Missing binary 'pylupdate5'."
    echo "On ubuntu you can install pyqt5-dev-tools"
    echo "For ArchLinux install python-pyqt5"
    exit 1
fi
