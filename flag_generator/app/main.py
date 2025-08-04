"""
Main script for the Flag Generator application.
"""

import importlib
import pkgutil
import os

from app import labs
from app.generator import FlagGenerator

def iter_namespace(ns_pkg):
    # Specifying the second argument (prefix) to iter_modules makes the
    # returned name an absolute name instead of a relative one. This allows
    # import_module to work without having to do additional modification to
    # the name.
    return pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + ".")

def discover_plugins():
    """
    Discover and load plugins for the Flag Generator application.
    """
    discovered_plugins = {
        name: importlib.import_module(name)
        for finder, name, ispkg
        in iter_namespace(labs)
    }
    return discovered_plugins


def main():
    secret = os.environ.get("FLAG_SECRET")
    email = "student@student.oulu.fi"
    plugins = discover_plugins()
    print(plugins)
    labs = {}
    for plugin_name, plugin_module in plugins.items():
        print(f"Loaded plugin: {plugin_name}")
        # if hasattr(plugin_module, 'group_tasks'):
            # plugin_module.group_tasks()
        if hasattr(plugin_module, 'get_lab_data'):
            lab_data = plugin_module.get_lab_data()
            labs.update(lab_data)
    
    print("Labs data:", labs)
    gen = FlagGenerator(secret, labs)
    flags = gen.generate_flags(email)
    print("Generated flags:", flags)

if __name__ == "__main__":
    main()