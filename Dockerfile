FROM python:3.12-slim

RUN apt-get update && apt-get install -y nmap

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "main.py"]
