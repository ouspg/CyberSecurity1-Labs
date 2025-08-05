"""
This module defines the abstract base class for tasks and a lab that groups multiple tasks.
It provides an interface for injecting flags for tasks and managing multiple tasks within a lab context.
"""

from abc import ABC, abstractmethod
from typing import List


class Task(ABC):
    """
    Abstract base class for tasks.
    This class defines the interface for injecting flags for a task.

    Attributes:
        task_id (str): Identifier for the task.
        __flag (str): The flag for the task, which is private and should be set through the `set_flag` method.
    """

    def __init__(self, task_id: str, flag: str = ''):
        """
        Initialize the task with a task ID and an optional flag.

        Parameters:
            task_id (str): Identifier for the task.
            flag (str): Optional flag for the task.
        """

        self.task_id = task_id
        self.__flag = flag

    @abstractmethod
    def inject(self):
        """
        Inject flags for a task.
        This method must be implemented by subclasses.
        """

        pass

    def set_flag(self, flag: str):
        """
        Set the flag for the task.

        Parameters:
            flag (str): The flag to set for the task.
        """

        self.__flag = flag

    def get_flag(self) -> str:
        """
        Get the flag for the task.

        Returns:
            str: The flag for the task.
        """

        return self.__flag


class Lab:
    """
    Class for grouping multiple tasks into a lab.
    This class allows for managing multiple tasks and their flags within a lab context.

    Attributes:
        lab_id (str): Identifier for the lab.
        tasks (List[Task]): List of tasks for the lab.
    """

    def __init__(self, lab_id: str, tasks: List[Task]):
        """
        Initialize the lab with a lab ID and a list of tasks.

        Parameters:
            lab_id (str): Identifier for the lab.
            tasks (List[Task]): List of tasks for the lab.
        """

        self.lab_id = lab_id
        self.tasks = tasks

    def add_task(self, task: Task):
        """
        Add a task to the lab.

        Parameters:
            task (Task): The task to add to the lab.
        """

        self.tasks.append(task)

    def get_tasks(self) -> List[Task]:
        """
        Get the list of tasks for the lab.

        Returns:
            List[Task]: The list of tasks for the lab.
        """

        return self.tasks

    def inject_all(self):
        """
        Inject flags for all tasks in the lab.
        This method iterates through all tasks and calls their inject method.
        """

        for task in self.tasks:
            task.inject()
