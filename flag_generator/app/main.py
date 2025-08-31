"""
Main script for the Flag Generator application.
"""

import argparse
import json

from app import labs as plugin
from app.generator import FlagGenerator
from app.utils.config import get_config, load_configs
from app.utils.helpers import (create_all_labs, discover_plugins,
                               load_all_configs)
from app.utils.logger import setup_logger

logger = setup_logger(__name__)


def main(args: argparse.Namespace):
    """
    Main script method.

    Parameters:
        args (argparse.Namespace): Object storing CLI arguments
    """

    # discover the plugins
    plugins = discover_plugins(plugin)
    logger.debug(f"Discovered plugins: {plugins}")

    # load config files
    load_all_configs(plugins)

    # create all the labs i.e. load the plugins
    labs = create_all_labs(plugins)
    logger.debug(f"Labs created: {labs}")

    gen = FlagGenerator(get_config("app", "secret", "SECRET"), labs)

    logger.info(f"Generating flags for email {email}")
    flags = {}
    logger.info(f"Generating flags for {args.email}")
    if args.email:
        flags.update(gen.generate_flags(args.email))

    elif args.file:
        with open(args.file, 'r') as f:
            emails = f.readlines()

        for email in emails:
            flags.update(gen.generate_flags(email.strip()))

    logger.debug(f"Generated flags: {flags}")

    # If email file is provided it will generate multiple flags for same labs so
    # inject flags only under normal operation i.e single email passed via `--email` parameter
    # if export option is provied, do not inject flags
    if not args.file and not args.export:
        for lab in labs:
            lab.inject_all()
            logger.info(f"Injected flags for lab {lab.lab_id}")

    if args.export:
        logger.info(f"Exporting flags to json to file: {args.export}")
        with open(args.export, 'w') as f:
            json.dump(flags, f, indent=2)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Application to generate flags for hacking labs"
    )

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "--email",
        help="User email. These are used to generate dynamic flags"
    )

    group.add_argument(
        "--file",
        help="File with user emails. These are used to generate dynamic flags"
    )

    parser.add_argument(
        "--export",
        help="Exports the generated flags as json to file provided"
    )

    args = parser.parse_args()
    main(args)
