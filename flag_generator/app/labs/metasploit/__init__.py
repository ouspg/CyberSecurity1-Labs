"""
This package contains the Metasploit lab for the Flag Generator application.
It defines various Metasploit tasks and groups them into a lab.
"""

from app.injector import Lab, Task
from app.utils.config import get_config
import docker
from app.utils.logger import setup_logger
import os

logger = setup_logger(__name__)

client = docker.from_env()

class TaskOne(Task):
    """
    First task for the lab.
    This task invovles identifying the service name/version running on the lab port.
    """

    def __init__(self, task_id: str):
        super().init(task_id)
    
    def inject(self):
        """
        Inject the flag for this task.
        Since the service name/version is static, there is no actual injection logic
        involved
        """

        self.set_flag(get_config("task_one", "service_version"))

class TaskTwo(Task):
    """
    Second task for the lab.
    This task invovles identifying the CVE that allows remote code execution
    into the target.
    """

    def __init__(self, task_id: str):
        super().init(task_id)
    
    def inject(self):
        """
        Inject the flag for this task.
        Since the service name/version is static, there is no actual injection logic
        involved
        """

        self.set_flag(get_config("task_two", "cve"))

class TaskThree(Task):
    """
    Second task for the lab.
    This task invovles identifying the CVE that allows remote code execution
    into the target.
    """

    def __init__(self, task_id: str):
        super().init(task_id)
    
    def inject(self):
        """
        Inject the flag for this task.
        Since the service name/version is static, there is no actual injection logic
        involved
        """
        container = client.containers.get(get_config("task_three", "container_name"))
        container.exec_run(
            f"sh -c 'echo {self.get_flag()} > {get_config("task_three", "flag_location")}'")
        
class TaskFour(Task):
    """
    Second task for the lab.
    This task invovles identifying the CVE that allows remote code execution
    into the target.
    """

    def __init__(self, task_id: str):
        super().init(task_id)
    
    def inject(self):
        """
        Inject the flag for this task.
        Since the service name/version is static, there is no actual injection logic
        involved
        """

        # replace embeded flag in the binary
        with open(get_config("task_four", "sniffer_location"), "r") as f:
            content = f.read()
        
        content = content.replace(get_config("task_four", "palceholder_flag"), self.get_flag())

        with open(get_config("task_four", "sniffer_location"), "r") as f:
            f.write(content)
        
        # build the container again
        os.system(f"docker compose up -f {get_config('task_four', 'compose_file_location')} -d --build")


        
           


        