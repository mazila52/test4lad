FROM python:3.8-slim

RUN mkdir /app

COPY requirements.txt /app

RUN pip3 install -r /app/requirements.txt --no-cache-dir

COPY backend/ /app

WORKDIR /app

CMD ["python3", "manage.py", "runserver", "0:8000"] 