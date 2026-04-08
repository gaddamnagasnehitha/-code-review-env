from pydantic import BaseModel

class Observation(BaseModel):
    code: str
    language: str
    task_type: str

class Action(BaseModel):
    review_comment: str
    bug_detected: bool
    suggestion: str

class Reward(BaseModel):
    score: float