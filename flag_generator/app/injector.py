"""
This module defines the abstract base class for tasks and a lab that groups multiple tasks.
It provides an interface for injecting flags for tasks and managing multiple tasks within a lab context.
"""

from abc import ABC, abstractmethod
from typing import Dict, List


class Task(ABC):
    """
    Abstract base class for tasks.
    This class defines the interface for injecting flags for a task.

    Attributes:
        task_id (str): Identifier for the task.
    """

    def __init__(self, task_id: str):
        """
        Initialize the task with a task ID.

        Parameters:
            task_id (str): Identifier for the task.
        """

        self.task_id = task_id

    @abstractmethod
    def inject(self, flag: str):
        """
        Inject flags for a task.

        Parameters:
            flag (str): The flag to inject for the task.
        This method must be implemented by subclasses.
        """

        pass


class Lab:
    """
    Class for grouping multiple tasks into a lab.
    This class allows for managing multiple tasks and their flags within a lab context.

    Attributes:
        lab_id (str): Identifier for the lab.
        tasks (List[Task]): List of tasks for the lab.
        flags (Dict[str, str]): Dictionary of flags for the tasks in the lab. The keys are
            task IDs and the values are the corresponding flags.
    """

    def __init__(self, lab_id: str, tasks: List[Task], flags: Dict[str, str]):
        """
        Initialize the lab with a lab ID and a list of tasks.

        Parameters:
            lab_id (str): Identifier for the lab.
            tasks (List[Task]): List of tasks for the lab.
            flags (Dict[str, str]): Dictionary of flags for the tasks in the lab. The keys are
                task IDs and the values are the corresponding flags.
        """
        self.lab_id = lab_id
        self.tasks = tasks
        self.flags = flags

    def add_task(self, task: Task):
        """
        Add a task to the lab.
        """
        self.tasks.append(task)

    def get_tasks(self):
        """
        Get the list of tasks for the lab.
        """
        return self.tasks

    def inject_all(self):
        """
        Inject flags for all tasks in the lab.
        This method iterates through all tasks and injects the corresponding flags by calling Task.inject().

        Raises:
            ValueError: If a flag for a task is not provided in the flags dictionary.
        """
        for task in self.tasks:
            flag = self.flags.get(task.task_id)
            if not flag:
                raise ValueError(
                    f"No flag provided for {self.lab_id}/{task.task_id}")
            task.inject(flag)

    def get_tasks(self):
        """
        Get the list of tasks for the lab.
        """
        return self.tasks

    def inject_all(self):
        """
        Inject flags for all tasks in the lab.
        This method iterates through all tasks and injects the corresponding flags by calling Task.inject().

        Raises:
            ValueError: If a flag for a task is not provided in the flags dictionary.
        """
        for task in self.tasks:
            flag = self.flags.get(task.task_id)
            if not flag:
                raise ValueError(
                    f"No flag provided for {self.lab_id}/{task.task_id}")
            task.inject(flag)
