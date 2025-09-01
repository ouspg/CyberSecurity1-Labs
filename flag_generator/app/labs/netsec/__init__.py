"""
This package contains the Network Security lab for the Flag Generator application.
It defines various Network Security tasks and groups them into a lab.
"""


import os

from app.injector import Lab, Task
from app.utils.config import get_config
from app.utils.logger import setup_logger

logger = setup_logger(__name__)


class UDPPorts(Task):
    """
    UDP Ports task for network security lab.
    """

    def __init__(self, task_id: str, flag_type='static'):
        super().__init__(task_id=task_id, flag_type=flag_type)
        self.set_flag(get_config("udp_ports", "service_name"))

    def inject(self):
        """
        Inject the flag for this task.
        Since the number of ports is static, there is no actual injection logic
        involved
        """

        pass


class ServiceVersion(Task):
    """
    Service Version task for network security lab.
    """

    def __init__(self, task_id: str, flag_type='static'):
        super().__init__(task_id=task_id, flag_type=flag_type)
        self.set_flag(get_config("service_version", "version"))

    def inject(self):
        """
        Inject the flag for this task.
        Since the service version is static, there is no actual injection logic
        involved
        """

        pass


class PortNumber(Task):
    """
    Port Number task for network security lab.
    """

    def __init__(self, task_id: str, flag_type='static'):
        super().__init__(task_id=task_id, flag_type=flag_type)
        self.set_flag(get_config("port_number", "10023"))

    def inject(self):
        """
        Inject the flag for this task.
        Since the port number is static, there is no actual injection logic
        involved
        """

        pass


class HTTPHeader(Task):
    """
    HTTP Header task for network security lab.
    """

    def __init__(self, task_id: str):
        super().__init__(task_id)

    def inject(self):
        """
        Inject the Sitemap task flag.
        The flag is injected by replacing the placehodler flag in the nginx config
        """

        with open(get_config("http_header", "file_location"), "r") as f:
            content = f.read()

        content = content.replace(get_config(
            "http_header", "placeholder_flag"), self.get_flag())

        with open(get_config("header", "file_location"), "w") as f:
            f.write(content)


class FTP(Task):
    """
    FTP task for network security lab.
    """

    def __init__(self, task_id: str):
        super().__init__(task_id)

    def inject(self):
        """
        Inject the FTP task flag.
        The flag is injected by replacing the placehodler flag in the FTP data
        """

        with open(get_config("ftp", "file_location"), "r") as f:
            content = f.read()

        content = content.replace(get_config(
            "ftp", "placeholder_flag"), self.get_flag())

        with open(get_config("ftp", "file_location"), "w") as f:
            f.write(content)

        # build the containers again
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
        UDPPorts("udpPorts"),
        ServiceVersion("serviceVersion"),
        PortNumber("portNumber"),
        HTTPHeader("header"),
        FTP("ftp")
    ]
    NetSecLab = Lab("netsec", tasks)

    return NetSecLab
