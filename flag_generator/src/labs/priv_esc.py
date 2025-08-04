"""
Privelage Escalation lab
"""

from ..injector import TaskInjector, LabInjector

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