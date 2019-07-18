FROM python:3.6

RUN apt-get update && apt install librdkafka-dev -y

WORKDIR /app

ADD requirements.txt .

RUN pip install -r requirements.txt

ADD application .

CMD python src/kafka_daemon.py