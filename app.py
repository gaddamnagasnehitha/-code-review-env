from fastapi import FastAPI
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from env.environment import CodeReviewEnv
from env.models import Action
from env.environment import CodeReviewEnv
from env.models import Action
import uvicorn

app = FastAPI()
env = CodeReviewEnv()

@app.post("/reset")
def reset():
    return env.reset()

@app.post("/step")
def step(action: dict):
    action_obj = Action(**action)
    return env.step(action_obj)

@app.get("/state")
def state():
    return env.state()


# ✅ REQUIRED MAIN FUNCTION
def main():
    uvicorn.run("server.app:app", host="0.0.0.0", port=7860)


# ✅ REQUIRED ENTRY POINT
if __name__ == "__main__":
    main()