FROM python:3.6

RUN apt-get update && apt install librdkafka-dev -y

WORKDIR /app

ADD requirements.txt .

RUN pip install -r requirements.txt

ADD application .

ENV PYTHONPATH "${PYTHONPATH}:/app/src"

CMD gunicorn --bind 0.0.0.0:8000 confluent_kafka_producer_api.wsgi:app
