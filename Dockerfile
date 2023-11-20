FROM python:3.6

MAINTAINER Vikram Malik "vikramsamsol@gmail.com"

COPY . /app

WORKDIR /app

EXPOSE 5100

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "app.py"]
