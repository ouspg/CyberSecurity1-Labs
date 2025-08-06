"""
This package contains the Privilege Escalation lab for the Flag Generator application.
It defines various privilege escalation tasks and groups them into a lab.
"""

import docker
from app.injector import Lab, Task
from app.utils.config import get_config
from app.utils.logger import setup_logger

logger = setup_logger(__name__)


client = docker.from_env()


class SUID(Task):
    """
    SUID task for privilege escalation.
    """

    def __init__(self, task_id: str):
        super().__init__(task_id)

    def inject(self):
        """
        Inject the SUID task flag.
        The flag is injected by echoing the flag content into a flag file inside the docker container.
        """

        container = client.containers.get(get_config("suid", "container_name"))
        container.exec_run(
            f"sh -c 'echo {self.get_flag()} > {get_config("suid", "flag_location")}'")
        container.exec_run(
            f"sh -c 'chown {get_config("suid", "user")}:{get_config("suid", "group")} {get_config("suid", "flag_location")}'")
        container.exec_run(
            f"sh -c 'chmod 640 {get_config("suid", "flag_location")}'")
        logger.debug(f"Injecting SUID flag: {self.get_flag()}")


class PATH(Task):
    """
    PATH task for privilege escalation.
    """

    def __init__(self, task_id: str):
        super().__init__(task_id)

    def inject(self):
        """
        Inject the PATH task flag.
        """
        container = client.containers.get(get_config("path", "container_name"))
        container.exec_run(
            f"sh -c 'echo {self.get_flag()} > {get_config("path", "flag_location")}'")
        container.exec_run(
            f"sh -c 'chown {get_config("path", "user")}:{get_config("path", "group")} {get_config("path", "flag_location")}'")
        container.exec_run(
            f"sh -c 'chmod 640 {get_config("path", "flag_location")}'")
    
        logger.debug(f"Injecting PATH flag: {self.get_flag()}")


class CRON(Task):
    """
    CRON task for privilege escalation.
    """

    def __init__(self, task_id: str):
        super().__init__(task_id)

    def inject(self):
        """
        Inject the CRON task flag.
        """

        logger.debug(f"Injecting CRON flag: {self.get_flag()}")


class SUDO(Task):
    """
    SUDO task for privilege escalation.
    """

    def __init__(self, task_id: str):
        super().__init__(task_id)

    def inject(self):
        """
        Inject the SUDO task flag.
        """

        logger.debug(f"Injecting SUDO flag: {self.get_flag()}")


def create_lab() -> Lab:
    """
    Create the Privilege Escalation lab with its tasks.
    This function initializes the lab with the defined tasks and returns it.

    Returns:
        Lab: An instance of the Lab class containing the privilege escalation tasks.
    """

    tasks = [
        SUID("suid_task"),
        PATH("path_task"),
        CRON("cron_task"),
        SUDO("sudo_task")
    ]
    PrivEscLab = Lab("priv_esc", tasks)

    return PrivEscLab
