"""
This module contains utility and helper methods for the
Flag Generator Application.
"""

import importlib
import pkgutil
from pathlib import Path
from typing import Dict, Iterator, List

from app.injector import Lab
from app.utils.config import load_configs
from app.utils.logger import setup_logger

logger = setup_logger(__name__)


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
        logger.info(f"Loaded plugin: {plugin_name}")
        if hasattr(plugin_module, 'create_lab'):
            lab = plugin_module.create_lab()
            labs.append(lab)
            logger.debug(
                f"Created lab: {lab.lab_id} with tasks: {[task.task_id for task in lab.get_tasks()]}")

    return labs


def load_all_configs(plugins: Dict[str, pkgutil.ModuleInfo]):
    """
    Loads the global and module level config files.

    Parameters:
        Dict[str, pkgutil.ModuleInfo]: A dictionary of plugins where the keys are
            plugin names and the values are the corresponding module objects.
    """

    configs = []
    configs.append(Path(__file__).parent.parent.joinpath(
        "config.ini"))  # global config
    for p in plugins.values():  # module level configs
        configs.append(Path(p.__file__).parent.joinpath("config.ini"))
    load_configs(configs)
