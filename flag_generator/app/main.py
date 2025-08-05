"""
Main script for the Flag Generator application.
"""


import os
from typing import List

from app import labs as plugin
from app.generator import FlagGenerator
from app.injector import Lab
from app.utils import create_all_labs, discover_plugins, get_config

email = "student@student.oulu.fi"

if __name__ == "__main__":
    plugins = discover_plugins(plugin)
    print(plugins)

    labs = create_all_labs(plugins)
    print("Labs created:", labs)

    gen = FlagGenerator(get_config(env_var="secret"), labs)
    flags = gen.generate_flags(email)

    print("Generated flags:", flags)
    for lab in labs:
        lab.inject_all()
        print(f"Injected flags for lab {lab.lab_id}")
