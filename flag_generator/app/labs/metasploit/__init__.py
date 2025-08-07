"""
This package contains the Metasploit lab for the Flag Generator application.
It defines various Metasploit tasks and groups them into a lab.
"""

import os

import docker
from app.injector import Lab, Task
from app.utils.config import get_config
from app.utils.logger import setup_logger

logger = setup_logger(__name__)

client = docker.from_env()


class TaskOne(Task):
    """
    First task for the lab.
    This task invovles identifying the service name/version running on the lab port.
    """

    def __init__(self, task_id: str, flag_type='static'):
        super().__init__(task_id=task_id, flag_type=flag_type)
        self.set_flag(get_config("task_one", "service_version"))

    def inject(self):
        """
        Inject the flag for this task.
        Since the service name/version is static, there is no actual injection logic
        involved
        """

        pass


class TaskTwo(Task):
    """
    Second task for the lab.
    This task invovles identifying the CVE that allows remote code execution
    into the target.
    """

    def __init__(self, task_id: str, flag_type: str = "static"):
        super().__init__(task_id=task_id, flag_type=flag_type)
        self.set_flag(get_config("task_two", "cve"))

    def inject(self):
        """
        Inject the flag for this task.
        Since the service name/version is static, there is no actual injection logic
        involved
        """

        pass


class TaskThree(Task):
    """
    Second task for the lab.
    This task invovles gaining remote access to the system. Flag is injecting
    by echoing flag content to flag file
    """

    def __init__(self, task_id: str):
        super().__init__(task_id)

    def inject(self):
        """
        Inject the flag for this task.
        Since the service name/version is static, there is no actual injection logic
        involved
        """
        container = client.containers.get(
            get_config("task_three", "container_name"))
        container.exec_run(
            f"sh -c 'echo {self.get_flag()} > {get_config("task_three", "flag_location")}'")


class TaskFour(Task):
    """
    Second task for the lab.
    This task involves creating a meterpreter session. Flag is injected by modifying
    embeded flag in binary that detects meterpreter session and reveals flag
    """

    def __init__(self, task_id: str):
        super().__init__(task_id)

    def inject(self):
        """
        Inject the flag for this task.
        Since the service name/version is static, there is no actual injection logic
        involved
        """

        # replace embeded flag in the binary
        with open(get_config("task_four", "sniffer_location"), "r") as f:
            content = f.read()

        content = content.replace(get_config(
            "task_four", "palceholder_flag"), self.get_flag())

        with open(get_config("task_four", "sniffer_location"), "r") as f:
            f.write(content)

        # build the container again
        os.system(
            f"docker compose up -f {get_config('task_four', 'compose_file_location')} -d --build")


def create_lab() -> Lab:
    """
    Create the Metasploit lab with its tasks.
    This function initializes the lab with the defined tasks and returns it.

    Returns:
        Lab: An instance of the Lab class containing the Metasploit tasks.
    """

    tasks = [
        TaskOne("one_task"),
        TaskTwo("two_task"),
        TaskThree("three_task"),
        TaskFour("four_task")
    ]
    MetasploitLab = Lab("metasploit", tasks)

    return MetasploitLab
