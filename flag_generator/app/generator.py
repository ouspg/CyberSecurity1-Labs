from typing import Dict
import hmac
import hashlib


class FlagGenerator:
    def __init__(self, secret:str, labs: Dict[str, list]):
        self.secret = secret
        self.labs = labs
    
    def __make_flag(self, email, lab_name: str, task_id: str) -> str:
        """
        Generate a flag based on the email, lab name, and task ID.
        """
        base = f"{email}|{lab_name}|{task_id}"
        digest = hmac.new(self.secret.encode(), base.encode(), hashlib.sha256).hexdigest()
        truncated_digest = digest[:16]  # Truncate to 16 characters
        flag = f"FLAG{{{truncated_digest}}}"
        return flag
    
    def generate_flags(self, email: str):
        """
        Generate flags for the given email based on the secret and labs.
        """
        
        flags = {}
        for lab_name, tasks in self.labs.items():
            flags.update({lab_name: {}})
            for task_id in tasks:
                flag = self.__make_flag(email, lab_name, task_id)
                flags[lab_name][task_id] = flag
        return flags