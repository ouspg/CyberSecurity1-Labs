from abc import ABC, abstractmethod

class TaskInjector(ABC):
    """
    Abstract base class for task injectors.
    This class defines the interface for injecting flags for a task.
    """

    def __init__(self, task_id: str):
        self.task_id = task_id

    @abstractmethod
    def inject(self, flag: str):
        """
        Inject flags for a task.
        """
        pass

class LabInjector:
    """
    Class for grouping multiple task injectors.
    """

    def __init__(self, tasks: list[TaskInjector]):
        self.task_injectors = tasks

    def add_injector(self, injector: TaskInjector):
        """
        Add a task injector to the lab.
        """
        self.task_injectors.append(injector)

    def inject_all(self, flag: str):
        """
        Inject flags for all task injectors in the lab.
        """
        for injector in self.task_injectors:
            injector.inject(flag)
