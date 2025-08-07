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
        self.set_flag(get_config("vuln_task_one", "service_name"))

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
        self.set_flag(get_config("vuln_task_two", "service_version"))

    def inject(self):
        """
        Inject the flag for this task.
        Since the service name/version is static, there is no actual injection logic
        involved
        """

        pass


class TaskThree(Task):
    """
    Third task for the lab.
    This task invovles identifying the CVE that allows authentication bypass
    into the target.
    """

    def __init__(self, task_id: str, flag_type: str = "static"):
        super().__init__(task_id=task_id, flag_type=flag_type)
        self.set_flag(get_config("vuln_task_three", "cve"))

    def inject(self):
        """
        Inject the flag for this task.
        Since the service name/version is static, there is no actual injection logic
        involved
        """

        pass


class TaskFour(Task):
    """
    Fourth task for the lab.
    This task invlves finding a specific value in a MYSQL database.
    Flag is injected into the database.
    """

    def __init__(self, task_id: str):
        super().__init__(task_id)

    def inject(self):

        sql_query = get_config("vuln_task_four", "mysql_query")
        print(f'query is {sql_query}')

        # replace the placeholder flag
        sql_query.replace("FLAG{}", self.get_flag())

        sql_command = f"mysql -u {get_config("vuln_task_four", "mysql_user")} -p{get_config("vuln_task_four", "mysql_password")} -e \'{sql_query}\'"

        # insert the flag into the container
        container = client.containers.get(
            get_config("vuln_task_four", "container_name"))
        container.exec_run(f"{sql_command}")


def create_lab() -> Lab:
    """
    Create the Vulnerability Research lab with its tasks.
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
    VulnResearch = Lab("vuln_research", tasks)

    return VulnResearch
