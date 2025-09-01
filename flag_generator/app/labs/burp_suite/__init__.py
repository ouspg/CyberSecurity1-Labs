"""
This package contains the Burp Suite lab for the Flag Generator application.
It defines various Burp Suite tasks and groups them into a lab.
"""


import base64
import os

from app.injector import Lab, Task
from app.utils.config import get_config
from app.utils.logger import setup_logger

logger = setup_logger(__name__)


class Sitemap(Task):
    """
    Sitemap task for privilege escalation.
    """

    def __init__(self, task_id: str):
        super().__init__(task_id)

    def inject(self):
        """
        Inject the Sitemap task flag.
        The flag is injected by replacing the placehodler flag in the web app code
        """

        # replace embeded flag in the binary
        with open(get_config("sitemap", "file_location"), "r") as f:
            content = f.read()

        content = content.replace(get_config(
            "sitemap", "placeholder_flag"), self.get_flag())

        with open(get_config("sitemap", "file_location"), "w") as f:
            f.write(content)


class BruteForce(Task):
    """
    BruteForce task for privilege escalation.
    """

    def __init__(self, task_id: str):
        super().__init__(task_id)

    def inject(self):
        """
        Inject the BruteForce task flag.
        The flag is injected by replacing the placehodler flag in the web app code
        """

        # replace embeded flag in the binary
        with open(get_config("bruteforce", "file_location"), "r") as f:
            content = f.read()

        content = content.replace(get_config(
            "bruteforce", "placeholder_flag"), self.get_flag())

        with open(get_config("bruteforce", "file_location"), "w") as f:
            f.write(content)


class Decoder(Task):
    """
    Decoder task for privilege escalation.
    """

    def __init__(self, task_id: str):
        super().__init__(task_id)

    def inject(self):
        """
        Inject the Decoder task flag.
        The flag is injected by replacing the placehodler flag in the web app code
        """

        # replace embeded flag in the binary
        with open(get_config("decoder", "file_location"), "r") as f:
            content = f.read()

        flag = self.get_flag()
        flag_bytes = flag.encode("utf-8")

        base64_bytes = base64.b64encode(flag_bytes)
        base64_string = base64_bytes.decode("utf-8")

        content = content.replace(get_config(
            "decoder", "placeholder_flag"), base64_string)

        with open(get_config("decoder", "file_location"), "w") as f:
            f.write(content)


class Header(Task):
    """
    Sitemap task for privilege escalation.
    """

    def __init__(self, task_id: str):
        super().__init__(task_id)

    def inject(self):
        """
        Inject the Sitemap task flag.
        The flag is injected by replacing the placehodler flag in the web app code
        """

        # replace embeded flag in the binary
        with open(get_config("header", "file_location"), "r") as f:
            content = f.read()

        content = content.replace(get_config(
            "header", "placeholder_flag"), self.get_flag())

        with open(get_config("header", "file_location"), "w") as f:
            f.write(content)
        
        # build the container again
        os.system(
            f"docker compose -f {get_config('app', 'compose_file_location')} up  -d --build")


def create_lab() -> Lab:
    """
    Create the BurpSuite lab with its tasks.
    This function initializes the lab with the defined tasks and returns it.

    Returns:
        Lab: An instance of the Lab class containing the Metasploit tasks.
    """

    tasks = [
        Sitemap("sitemap"),
        BruteForce("bruteforce"),
        Decoder("decoder"),
        Header("header")
    ]
    BurpSuiteLab = Lab("burpsuite", tasks)

    return BurpSuiteLab
