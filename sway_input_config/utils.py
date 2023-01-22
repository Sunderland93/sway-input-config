import json
import os
from i3ipc import Connection


def list_inputs_by_type(input_type=""):
    inputs = []

    i3 = Connection()
    all_inputs = i3.get_inputs()
    for i in all_inputs:
        if i.type == input_type or not input_type:
            inputs.append(i.identifier)

    return inputs


def get_data_dir():
    data_dir = ""
    home = os.getenv("HOME")
    xdg_data_home = os.getenv("XDG_DATA_HOME")

    if xdg_data_home:
        data_dir = os.path.join(xdg_data_home, "sway-input-config/")
    else:
        if home:
            data_dir = os.path.join(home, ".config/sway-input-config/")

    if not os.path.isdir(data_dir):
        print("Creating '{}'".format(data_dir))
        os.makedirs(data_dir, exist_ok=True)

    return data_dir


def load_text_file(path):
    try:
        with open(path, 'r') as file:
            data = file.read()
            return data
    except Exception as e:
        print(e)
        return None


def load_json(path):
    try:
        with open(path, 'r') as f:
            return json.load(f)
    except Exception as e:
        print("Error loading json: {}".format(e))
        return None


def save_json(src_dict, path):
    with open(path, 'w') as f:
        json.dump(src_dict, f, indent=2)


def save_list_to_text_file(data, file_path):
    text_file = open(file_path, "w")
    for line in data:
        text_file.write(line + "\n")
    text_file.close()


def reload_sway_config():
    i3 = Connection()
    i3.command('reload')
