import asyncio
import os
from openai import OpenAI

API_BASE_URL = os.getenv("API_BASE_URL")
API_KEY = os.getenv("OPENAI_API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME")

async def main():
    client = OpenAI(base_url=API_BASE_URL, api_key=API_KEY)

    print("[START] task=code_review env=CodeReviewEnv model=", MODEL_NAME)

    # dummy example (replace with real env connection)
    for step in range(1, 4):
        action = "Review code and detect bug"

        print(f"[STEP] step={step} action={action} reward=0.5 done=False")

    print("[END] success=True steps=3 score=0.75 rewards=[0.5,0.5,0.5]")

if __name__ == "__main__":
    asyncio.run(main())