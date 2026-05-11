FROM python:3.14.4-bookworm

WORKDIR /app
COPY src .
COPY pyproject.toml .

RUN python3 -m pip install .

CMD ["fastapi", "run", "webapp/app.py", "--port", "8000"]

