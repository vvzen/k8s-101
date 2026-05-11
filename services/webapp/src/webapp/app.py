import socket

from fastapi import FastAPI

app = FastAPI()


@app.get("/api/v1/status")
def status():
    hostname = socket.gethostname()
    return f'hello, world from {hostname}'


def main():
    print("Hello from webapp!")


if __name__ == "__main__":
    main()
