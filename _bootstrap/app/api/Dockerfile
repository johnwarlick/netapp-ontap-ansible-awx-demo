# syntax = docker/dockerfile:1.4
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9-slim AS builder

WORKDIR /api

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . ./app

CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--port=8000", "--reload-dir=/app", "--reload"]