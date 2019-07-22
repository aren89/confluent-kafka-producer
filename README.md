# Kafka Producer

## Requirements:
  - [docker-compose](https://docs.docker.com/compose/install/)

## Run
```sh
$ docker-compose up -d
```
## Checking messages sent
```sh
$ docker-compose exec kafka bash
$ kafka-console-consumer\
    --bootstrap-server localhost:9092\
    --property schema.registry.url=http://schema_registry:9052\
    --property print.key=true\
    --from-beginning --topic com.confluent-kafka-producer.producer.TestMessage
```