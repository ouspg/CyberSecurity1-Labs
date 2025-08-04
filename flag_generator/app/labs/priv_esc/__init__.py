"""
Privelage Escalation lab
"""

from app.injector import LabInjector, TaskInjector

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

def group_tasks():
    """
    Group all task injectors for the Privilege Escalation lab.
    """
    tasks = [
        SUID("suid_task"),
        PATH("path_task"),
        Cron("cron_task"),
        Sudo("sudo_task")
    ]
    flags = {
        "suid_task": "FLAG_SUID",
        "path_task": "FLAG_PATH",
        "cron_task": "FLAG_CRON",
        "sudo_task": "FLAG_SUDO"
    }
    PrivEscLab = LabInjector("priv_esc_lab", tasks, flags)
    PrivEscLab.inject_all()

def get_lab_data():
    """
    Get lab data for the Privilege Escalation lab.
    """
    return {
        "priv_esc_lab": [
            "suid_task",
            "path_task",
            "cron_task",
            "sudo_task"
        ]
    }