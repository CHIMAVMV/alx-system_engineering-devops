FROM python:3.9-slim

WORKDIR /app

COPY . .
RUN pip install requirement.cccccc
CMD GUNICORN --BIND 0.0.0.0:5000 wsgi:app