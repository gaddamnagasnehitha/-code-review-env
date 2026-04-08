FROM python:3.10

WORKDIR /app

COPY . .

# 👇 VERY IMPORTANT LINE (fix import issue)
ENV PYTHONPATH=/app

RUN pip install pydantic openai fastapi uvicorn openenv-core

CMD ["uvicorn", "server.app:app", "--host", "0.0.0.0", "--port", "7860"]