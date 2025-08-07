"""
This package contains the Vulnerability Research lab for the Flag Generator application.
It defines various Vulnerability Research tasks and groups them into a lab.
"""

import docker
from app.injector import Lab, Task
from app.utils.config import get_config
from app.utils.logger import setup_logger

logger = setup_logger(__name__)

client = docker.from_env()


class ServiceName(Task):
    """
    This task invovles identifying the service name running on the lab port.
    """

    def __init__(self, task_id: str, flag_type='static'):
        super().__init__(task_id=task_id, flag_type=flag_type)
        self.set_flag(get_config("service_name_task", "service_name"))

    def inject(self):
        """
        Inject the flag for this task.
        Since the service name/version is static, there is no actual injection logic
        involved
        """

        pass


class ServiceVersion(Task):
    """
    This task invovles identifying the service version running on the lab port.
    """

    def __init__(self, task_id: str, flag_type='static'):
        super().__init__(task_id=task_id, flag_type=flag_type)
        self.set_flag(get_config("service_version_task", "service_version"))

    def inject(self):
        """
        Inject the flag for this task.
        Since the service name/version is static, there is no actual injection logic
        involved
        """

        pass


class AuthBypassCVE(Task):
    """
    This task invovles identifying the CVE that allows authentication bypass
    into the target.
    """

    def __init__(self, task_id: str, flag_type: str = "static"):
        super().__init__(task_id=task_id, flag_type=flag_type)
        self.set_flag(get_config("cve_task", "cve"))

    def inject(self):
        """
        Inject the flag for this task.
        Since the cve is static, there is no actual injection logic
        involved
        """

        pass


class TicketContent(Task):
    """
    This task invlves finding a specific ticket value in a MYSQL database.
    The flag is injected into the database by executing an INSERT query.
    """

    def __init__(self, task_id: str):
        super().__init__(task_id)

    def inject(self):
        mysql_command = (
            f'mysql -u {get_config("ticket_content_task", "mysql_user")} -p{get_config("ticket_content_task", "mysql_password")} '
            f'-e "INSERT INTO {get_config("ticket_content_task", "table")} ({get_config("ticket_content_task", "table_columns")}) '
            f'VALUES ({get_config("ticket_content_task", "values")});"'
        )

        # replace the placeholder flag
        mysql_command = mysql_command.replace("FLAG{}", self.get_flag())

        # insert the flag into the container
        container = client.containers.get(
            get_config("ticket_content_task", "container_name"))
        container.exec_run(f"{mysql_command}")


def create_lab() -> Lab:
    """
    Create the Vulnerability Research lab with its tasks.
    This function initializes the lab with the defined tasks and returns it.

    Returns:
        Lab: An instance of the Lab class containing the Metasploit tasks.
    """

    tasks = [
        ServiceName("service_name"),
        ServiceVersion("service_version"),
        AuthBypassCVE("auth_bypass_cve"),
        TicketContent("ticket_content")
    ]
    VulnResearch = Lab("vuln_research", tasks)

    return VulnResearch
