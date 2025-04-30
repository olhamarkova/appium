from configparser import ConfigParser
import os


def get_config_property(config_group, prop):
    config = ConfigParser()
    path = os.path.join(os.path.dirname(__file__), "..", "config.ini")
    config.read(path)
    return config.get(config_group, prop)
