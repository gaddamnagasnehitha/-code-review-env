from env.models import Observation, Action
from env.tasks import TASKS
from env.grader import grade

class CodeReviewEnv:
    def __init__(self):
        self.current_task = None
        self.done = False

    def reset(self):
        self.current_task = TASKS[0]
        self.done = False
        return {
            "observation": Observation(
                code=self.current_task["code"],
                language="python",
                task_type=self.current_task["id"]
            ),
            "done": False
        }

    def step(self, action: Action):
        reward = grade(self.current_task, action)
        self.done = True

        return {
            "observation": Observation(
                code=self.current_task["code"],
                language="python",
                task_type=self.current_task["id"]
            ),
            "reward": reward,
            "done": self.done,
            "info": {}
        }

    def state(self):
        return self.current_task