"""
This package contains the Vulnerability Research lab for the Flag Generator application.
It defines various Vulnerability Research tasks and groups them into a lab.
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
    This task invovles identifying the service namerunning on the lab port.
    """

    def __init__(self, task_id: str, flag_type='static'):
        super().__init__(task_id=task_id, flag_type=flag_type)
        self.set_flag(get_config("task_one", "service_name"))

    def inject(self):
        """
        Inject the flag for this task.
        Since the service name/version is static, there is no actual injection logic
        involved
        """

        pass

class TaskTwo(Task):
    """
    First task for the lab.
    This task invovles identifying the service version running on the lab port.
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

class TaskThree(Task):
    """
    Second task for the lab.
    This task invovles identifying the CVE that allows authentication bypass
    into the target.
    """

    def __init__(self, task_id: str, flag_type: str = "static"):
        super().__init__(task_id=task_id, flag_type=flag_type)
        self.set_flag(get_config("task_three", "cve"))

    def inject(self):
        """
        Inject the flag for this task.
        Since the service name/version is static, there is no actual injection logic
        involved
        """

        pass
