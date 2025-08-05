"""
This module contains utility and helper methods for the
Flag Generator Application.
"""

import importlib
import pkgutil
from typing import Dict, Iterator


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
