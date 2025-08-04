from abc import ABC, abstractmethod

class TaskInjector(ABC):
    """
    Abstract base class for task injectors.
    This class defines the interface for injecting flags for a task.
    """

    @abstractmethod
    def inject(self, task):
        """
        Inject flags for a task.
        """
        pass