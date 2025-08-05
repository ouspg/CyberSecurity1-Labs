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

    def inject(self, flag: str):
        """
        Inject the SUID task flag.

        Parameters:
            flag (str): The flag to inject for the SUID task.
        """
        print(f"Injecting SUID flag: {flag}")


class PATH(Task):
    """
    PATH task for privilege escalation.
    """

    def __init__(self, task_id: str):
        super().__init__(task_id)

    def inject(self, flag: str):
        """
        Inject the PATH task flag.

        Parameters:
            flag (str): The flag to inject for the PATH task.
        """
        print(f"Injecting PATH flag: {flag}")


class CRON(Task):
    """
    CRON task for privilege escalation.
    """

    def __init__(self, task_id: str):
        super().__init__(task_id)

    def inject(self, flag: str):
        """
        Inject the CRON task flag.
        Parameters:
            flag (str): The flag to inject for the CRON task.
        """
        print(f"Injecting CRON flag: {flag}")


class SUDO(Task):
    """
    SUDO task for privilege escalation.
    """

    def __init__(self, task_id: str):
        super().__init__(task_id)

    def inject(self, flag: str):
        """
        Inject the SUDO task flag.

        Parameters:
            flag (str): The flag to inject for the SUDO task.
        """
        print(f"Injecting SUDO flag: {flag}")


def group_tasks(flags: dict[str, str]):
    """
    Group all task injectors for the Privilege Escalation lab.
    """
    print(flags)
    tasks = [
        SUID("suid_task"),
        PATH("path_task"),
        CRON("cron_task"),
        SUDO("sudo_task")
    ]

    PrivEscLab = Lab("priv_esc", tasks, flags)
    PrivEscLab.inject_all()


def get_lab_data():
    """
    Get lab data for the Privilege Escalation lab.
    """
    return {
        "priv_esc": [
            "suid_task",
            "path_task",
            "cron_task",
            "sudo_task"
        ]
    }
