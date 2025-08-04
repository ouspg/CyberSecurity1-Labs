"""
Main script for the Flag Generator application.
"""

import importlib
import pkgutil

from app import labs

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
    plugins = discover_plugins()
    print(plugins)
    for plugin_name, plugin_module in plugins.items():
        print(f"Loaded plugin: {plugin_name}")
        if hasattr(plugin_module, 'group_tasks'):
            plugin_module.group_tasks()

if __name__ == "__main__":
    main()