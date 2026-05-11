FROM python:3.14.4-bookworm

WORKDIR /app
COPY main.py .  
COPY pyproject.toml .

RUN python3 -m pip install .

CMD ["fastapi", "run", "main.py", "--port", "80"]

