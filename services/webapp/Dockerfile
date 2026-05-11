FROM python:3.14.4-bookworm

WORKDIR /app
COPY src .
COPY pyproject.toml .

RUN python3 -m pip install .

CMD ["fastapi", "run", "src/webapp/app.py", "--port", "80"]

