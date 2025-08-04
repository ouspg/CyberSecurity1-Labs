from abc import ABC, abstractmethod
from typing import Dict

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

    def __init__(self, lab_id: str, tasks: list[TaskInjector], flags: Dict[str, str]):
        """
        Initialize the lab injector with a lab ID and a list of task injectors.
        :param lab_id: Identifier for the lab.
        :param tasks: List of task injectors for the lab.
        """
        self.lab_id = lab_id
        self.task_injectors = tasks
        self.flags = flags

    def add_injector(self, injector: TaskInjector):
        """
        Add a task injector to the lab.
        """
        self.task_injectors.append(injector)

    def inject_all(self):
        """
        Inject flags for all task injectors in the lab.
        """
        for injector in self.task_injectors:
            flag = self.flags.get(injector.task_id)
            if not flag:
                raise ValueError(f"No flag provided for {self.lab_id}/{injector.task_id}")
            injector.inject(flag)