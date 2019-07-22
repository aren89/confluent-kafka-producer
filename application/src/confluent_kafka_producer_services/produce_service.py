import os
from typing import Optional

from confluent_kafka import avro
from confluent_kafka.avro import AvroProducer
from injector import inject

from confluent_kafka_producer_core.services import ProduceService


class ProduceServiceImpl(ProduceService):
    AVRO_PATH = 'avro'
    KEY = 'key.avsc'
    VALUE = 'value.avsc'

    @inject
    def __init__(self, producer: AvroProducer):
        self._producer = producer

    def produce(self, key: dict, value: dict, message_name: str, topic: Optional[str] = None):
        self._producer.produce(
            topic=topic or f'com.confluent-kafka-producer.producer.{message_name}',
            key=key,
            key_schema=avro.load(os.path.join(self.AVRO_PATH, message_name.lower(), self.KEY)),
            value=value,
            value_schema=avro.load(os.path.join(self.AVRO_PATH, message_name.lower(), self.VALUE))
        )
        self._producer.flush()
