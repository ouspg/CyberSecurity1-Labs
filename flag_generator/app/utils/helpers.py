"""
This module contains utility and helper methods for the
Flag Generator Application.
"""

import importlib
import os
import pkgutil
from configparser import ConfigParser
from typing import Dict, Iterator, List

from app.injector import Lab


def iter_namespace(ns_pkg) -> Iterator[pkgutil.ModuleInfo]:
    # Specifying the second argument (prefix) to iter_modules makes the
    # returned name an absolute name instead of a relative one. This allows
    # import_module to work without having to do additional modification to
    # the name.

    return pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + ".")


def discover_plugins(ns_pkg) -> Dict[str, pkgutil.ModuleInfo]:
    """
    Discover and load plugins for the Flag Generator application.
    This function iterates through the labs package and imports all modules
    that are defined as plugins. It returns a dictionary where the keys are
    the plugin names and the values are the corresponding module objects.

    Returns:
        Dict[str, pkgutil.ModuleInfo]: A dictionary of discovered plugins where the keys are
            plugin names and the values are the corresponding module objects.
    """

    discovered_plugins = {
        name: importlib.import_module(name)
        for finder, name, ispkg
        in iter_namespace(ns_pkg)
    }
    return discovered_plugins


def create_all_labs(plugins) -> List[Lab]:
    """
    Creates all the labs by calling the `<module>.create_lab` method.

    Parameters:
        plugins (Dict[str, pkgutil.ModuleInfo]): The discovered plugins dictionary where the keys are
            the plugin names and the values are the corresponding module objects.

    Returns:
        List[Lab]: The list of Lab objects  
    """

    labs = []
    for plugin_name, plugin_module in plugins.items():
        print(f"Loaded plugin: {plugin_name}")
        if hasattr(plugin_module, 'create_lab'):
            lab = plugin_module.create_lab()
            labs.append(lab)
            print(
                f"Created lab: {lab.lab_id} with tasks: {[task.task_id for task in lab.get_tasks()]}")

    return labs


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
        config.read(os.path.dirname(__file__) + "/config.ini")
        config_value = config[section][key]
    else:
        config_value = os.environ.get(env_var)

    return config_value
