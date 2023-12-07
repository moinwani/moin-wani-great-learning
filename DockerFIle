FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt

COPY . .
RUN apt-get update && apt-get install -y curl


EXPOSE 5000

HEALTHCHECK --interval=30s --timeout=3s CMD curl --fail http://localhost:5000/ || exit 1

CMD ["venv/bin/python", "app.py"]
