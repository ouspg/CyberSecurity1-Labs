"""
This module sets up the config environment for the app by reading
the appropriate config
"""

import os
from configparser import ConfigParser
from typing import List

CONFIG = None


def load_configs(config_files: List[str]):
    """
    Loads multiple config files into a single config object.
    Sets a global config variable to store config values globally

    Parameters:
        config_files (List[str]): List of config file locations
    """

    global CONFIG

    CONFIG = ConfigParser()
    for file in config_files:
        CONFIG.read(file)


def get_config(section: str, key: str, env_var: str) -> str | None:
    """
    Read the config option from the config file.
    The configs are first read from the config file. If the config section and key
    do not exist then it tries to read it from the environemnt.

    Parameters:
        section (str): config file section
        key (str): config file key
        env_var (str): environment variable

    Returns:
        (str | None): The config value or None if no config sepcified
    """

    config_value = None

    try:
        config_value = CONFIG[section][key]
    except KeyError:
        config_value = os.environ.get(env_var)

    return config_value
