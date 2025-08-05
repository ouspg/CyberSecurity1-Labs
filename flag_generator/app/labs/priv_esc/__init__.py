"""
Privelage Escalation lab
"""

from app.injector import LabInjector, TaskInjector
# from app.schemas import LabInfo

class SUID(TaskInjector):
    """
    Task injector for SUID tasks.
    """

    def __init__(self, task_id: str):
        super().__init__(task_id)

    def inject(self, flag: str):
        """
        Inject the SUID flag.
        """
        print(f"Injecting SUID flag: {flag}")

class PATH(TaskInjector):
    """
    Task injector for PATH tasks.
    """

    def __init__(self, task_id: str):
        super().__init__(task_id)

    def inject(self, flag: str):
        """
        Inject the PATH flag.
        """
        print(f"Injecting PATH flag: {flag}")

class Cron(TaskInjector):
    """
    Task injector for CRON tasks.
    """

    def __init__(self, task_id: str):
        super().__init__(task_id)

    def inject(self, flag: str):
        """
        Inject the CRON flag.
        """
        print(f"Injecting CRON flag: {flag}")

class Sudo(TaskInjector):
    """
    Task injector for SUDO tasks.
    """

    def __init__(self, task_id: str):
        super().__init__(task_id)

    def inject(self, flag: str):
        """
        Inject the SUDO flag.
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
        Cron("cron_task"),
        Sudo("sudo_task")
    ]

    PrivEscLab = LabInjector("priv_esc", tasks, flags)
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