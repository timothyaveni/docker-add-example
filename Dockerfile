FROM python:3.12

WORKDIR /app

COPY server.py ./

ENTRYPOINT ["python3", "server.py"]
