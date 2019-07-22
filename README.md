# Kafka Producer

## Requirements:
  - [docker-compose](https://docs.docker.com/compose/install/)

## Run
```sh
$ docker-compose up -d
```
## Send custom message (WIP)
curl -X POST 
  http://127.0.0.1:4055/confluent-kafka-producer/api/v1/message

## Checking messages sent
```sh
$ docker-compose exec kafka bash
$ kafka-console-consumer\
    --bootstrap-server localhost:9092\
    --property schema.registry.url=http://schema_registry:9052\
    --property print.key=true\
    --from-beginning --topic com.confluent-kafka-producer.producer.TestMessage
```
