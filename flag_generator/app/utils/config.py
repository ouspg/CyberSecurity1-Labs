"""
This module sets up the config environment for the app by reading
the appropriate config
"""

import os
from configparser import ConfigParser


def get_config(section: str = "", key: str = "", env_var: str = "") -> str | None:
    """
    Read the config option from the config file.
    The configs are first read from the config file. If the config section and key
    are not provided then it tries to read it from the environemnt.

    Parameters:
        section (str): Option config file section
        key (str): Optional config file key
        env_var (str): Optional environment variable

    Returns:
        (str | None): The config value or None if no config sepcified
    """

    config_value = None

    if section and key:
        config = ConfigParser()
        config.read(os.path.dirname(__file__) + "/../config.ini")
        config_value = config[section][key]
    else:
        config_value = os.environ.get(env_var)

    return config_value
