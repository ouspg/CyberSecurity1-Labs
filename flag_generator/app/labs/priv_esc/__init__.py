"""
This package contains the Privilege Escalation lab for the Flag Generator application.
It defines various privilege escalation tasks and groups them into a lab.
"""

from app.injector import Lab, Task


class SUID(Task):
    """
    SUID task for privilege escalation.
    """

    def __init__(self, task_id: str):
        super().__init__(task_id)

    def inject(self):
        """
        Inject the SUID task flag.
        """

        print(f"Injecting SUID flag: {self.get_flag()}")


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

        print(f"Injecting PATH flag: {self.get_flag()}")


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

        print(f"Injecting CRON flag: {self.get_flag()}")


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

        print(f"Injecting SUDO flag: {self.get_flag()}")


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
