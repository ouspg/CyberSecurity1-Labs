"""
Main script for the Flag Generator application.
"""

from app import labs as plugin
from app.generator import FlagGenerator
from app.utils.config import get_config
from app.utils.helpers import create_all_labs, discover_plugins
from app.utils.logger import setup_logger

logger = setup_logger(__name__)

email = "student@student.oulu.fi"

if __name__ == "__main__":
    plugins = discover_plugins(plugin)
    logger.debug(f"Discovered plugins: {plugins}")

    labs = create_all_labs(plugins)
    logger.debug(f"Labs created: {labs}")

    gen = FlagGenerator(get_config(env_var="secret"), labs)
    flags = gen.generate_flags(email)

    logger.info(f"Generated flags: {flags}")
    for lab in labs:
        lab.inject_all()
        logger.info(f"Injected flags for lab {lab.lab_id}")
