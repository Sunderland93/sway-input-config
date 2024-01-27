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

pylupdate6 --no-obsolete \
    $sources \
    --ts "$langs"/"lang_$lang.ts"
