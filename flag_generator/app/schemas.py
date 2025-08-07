from pydantic import BaseModel

class TaskData(BaseModel):
    task_id: str
    flag: str

class Flags(BaseModel):
    flags: list[TaskData]

class LabInfo(BaseModel):
    lab_id: str
    tasks: list[str]

class LabData(BaseModel):
    lab_id: str
    content: list[Flags]