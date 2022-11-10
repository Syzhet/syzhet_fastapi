FROM python:3.10.4-slim

WORKDIR /syzhet_api

COPY requirements.txt .

RUN python -m pip install --upgrade pip && pip install -r /syzhet_api/requirements.txt --no-cache-dir

COPY . .