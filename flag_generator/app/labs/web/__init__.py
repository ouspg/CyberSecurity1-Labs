"""
This package contains the Web Hacking lab for the Flag Generator application.
It defines various Web Hacking tasks and groups them into a lab.
"""

from app.injector import Lab, Task
from app.utils.logger import setup_logger

logger = setup_logger(__name__)

class Robots(Task):
    """
    This task involves identifying the flag from the robots.txt file.
    """

    def __init__(self, task_id: str, flag_type = 'dynamic'):
        super().__init__(task_id=task_id, flag_type=flag_type)
    
    def inject(self):
        """
        Since the Juice Shop app has its own flag mechanism, no
        injection logic is required.
        """

        pass

class ScoreBoard(Task):
    """
    This task involves finding the hidden scoreboard.
    """

    def __init__(self, task_id: str, flag_type = 'dynamic'):
        super().__init__(task_id=task_id, flag_type=flag_type)
    
    def inject(self):
        """
        Since the Juice Shop app has its own flag mechanism, no
        injection logic is required.
        """

        pass

class DOMXSS(Task):
    """
    This task involves completing the DOM XSS challenge.
    """

    def __init__(self, task_id: str, flag_type = 'dynamic'):
        super().__init__(task_id=task_id, flag_type=flag_type)
    
    def inject(self):
        """
        Since the Juice Shop app has its own flag mechanism, no
        injection logic is required.
        """

        pass

class ConfidentialDocument(Task):
    """
    This task involves acessing a confidential document from the `ftp` directory.
    """

    def __init__(self, task_id: str, flag_type = 'dynamic'):
        super().__init__(task_id=task_id, flag_type=flag_type)
    
    def inject(self):
        """
        Since the Juice Shop app has its own flag mechanism, no
        injection logic is required.
        """

        pass

class BruteForce(Task):
    """
    This task involves logging in with the admin account.
    """

    def __init__(self, task_id: str, flag_type = 'dynamic'):
        super().__init__(task_id=task_id, flag_type=flag_type)
    
    def inject(self):
        """
        Since the Juice Shop app has its own flag mechanism, no
        injection logic is required.
        """

        pass

class ViewBasket(Task):
    """
    This task exploiting an IDOR vulnerability to view another users basket.
    """

    def __init__(self, task_id: str, flag_type = 'dynamic'):
        super().__init__(task_id=task_id, flag_type=flag_type)
    
    def inject(self):
        """
        Since the Juice Shop app has its own flag mechanism, no
        injection logic is required.
        """

        pass

class UserCredentials(Task):
    """
    This task exploiting SQL injection vulnerability to get all user credentials.
    """

    def __init__(self, task_id: str, flag_type = 'dynamic'):
        super().__init__(task_id=task_id, flag_type=flag_type)
    
    def inject(self):
        """
        Since the Juice Shop app has its own flag mechanism, no
        injection logic is required.
        """

        pass