from configparser import ConfigParser

config = ConfigParser()

def get_config_property(config_group, prop):
    config.read("config.ini")
    return config.get(config_group, prop)
