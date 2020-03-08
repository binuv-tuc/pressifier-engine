import json
import os
from core import MODULE_DIR

CONFIG_FILE_PATH = f'{MODULE_DIR}/config.json'


def get_config():
    with open(CONFIG_FILE_PATH, mode='r') as file:
        config = json.load(file)
        return config


def save_config(config):
    if not os.path.exists(CONFIG_FILE_PATH):
        raise FileNotFoundError
    with open(CONFIG_FILE_PATH, mode='w') as file:
        json.dump(config, fp=file, ensure_ascii=False)