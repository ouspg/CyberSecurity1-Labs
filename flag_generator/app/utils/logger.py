"""
This module configures the loggers to be used in other modules
"""

import logging
from sys import stdout

from app.utils.config import get_config


def setup_logger(name: str) -> logging.Logger:
    """
    Setup module specific loggers.

    Paramters:
        name (str): Name of the logger

    Returns:
        logging.Logger: The logger object
    """

    logger = logging.getLogger(name)
    if logger.hasHandlers():
        return logger  # already configured

    logger.setLevel(logging.DEBUG)

    # console handler with formatting
    handler = logging.StreamHandler(stream=stdout)
    # log level is loaded from env as config is not read yet
    handler.setLevel(get_config(env_var="LOG_LEVEL"))
    formatter = logging.Formatter(
        "(%(asctime)s) [%(levelname)s] -- %(name)s: %(message)s")
    handler.setFormatter(formatter)

    logger.addHandler(handler)

    return logger
