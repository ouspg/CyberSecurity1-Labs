"""
This module defines the FlagGenerator class that generates flags based on a secret, email, lab names,
and task IDs. It uses HMAC for secure flag generation and truncates the digest to a specified length.
"""

import hashlib
import hmac
from typing import Dict, List

from app.injector import Lab, Task


class FlagGenerator:
    """
    Class for generating flags based on a secret, email, lab names, and task IDs.
    It uses HMAC with SHA-256 to create secure flags and truncates the digest to a specified length.

    Attributes:
        secret (str): The secret key used for HMAC generation.
        labs (List[Lab]): List of labs containing tasks for which flags will be generated.
    """

    def __init__(self, secret: str, labs: List[Lab]):
        """
        Initialize the FlagGenerator with a secret and a list of labs.

        Parameters:
            secret (str): The secret key used for HMAC generation.
            labs (List[Lab]): List of labs containing tasks for which flags will be generated.
        """

        self.secret = secret
        self.labs = labs

    def __make_flag(self, email: str, lab_id: str, task_id: str) -> str:
        """
        Generate a flag based on the email, lab ID, and task ID.
        It uses HMAC with SHA-256 to create a secure flag and truncates the digest to 16 characters.

        Parameters:
            email (str): The email address to use for generating the flag.
            lab_id (str): The identifier for the lab.
            task_id (str): The identifier for the task.

        Returns:
            str: The generated flag in the format `FLAG{<truncated_digest>}`.
        """

        base = f"{email}|{lab_id}|{task_id}"
        digest = hmac.new(self.secret.encode(), base.encode(),
                          hashlib.sha256).hexdigest()
        truncated_digest = digest[:16]  # Truncate to 16 characters
        flag = f"FLAG{{{truncated_digest}}}"
        return flag

    def generate_flags(self, email: str) -> Dict[str, Dict[str, Dict[str, str]]]:
        """
        Generate flags for the given email based on the secret and labs data.
        It iterates through the labs and their tasks, generating a flag for each task.

        Parameters:
            email (str): The email address to use for generating flags.

        Returns:
            Dict[str, Dict[str, str]]: A dictionary where the keys are lab IDs and the values are dictionaries
                of task IDs and their corresponding generated flags.
        """

        flags = {email: {}}
        for lab in self.labs:
            flags[email].update({lab.lab_id: {}})
            for task in lab.get_tasks():

                if task.flag_type == "dynamic":
                    flag = self.__make_flag(email, lab.lab_id, task.task_id)
                    self.assign_flags(task, flag)

                elif task.flag_type == "static":
                    flag = task.get_flag()

                flags[email][lab.lab_id][task.task_id] = flag

        return flags

    def assign_flags(self, task: Task, flag: str) -> None:
        """
        Assign generated flags to each task in the labs.
        This method iterates through all labs and their tasks, injecting the generated flags into each task.
        """

        task.set_flag(flag)
