from abc import ABC, abstractmethod

from avro.schema import Schema
from confluent_kafka import avro
from confluent_kafka.avro import AvroProducer
from injector import inject


class GenericSender(ABC):

    def __init__(self, producer: AvroProducer):
        self._producer = producer

    def _produce(self, key: dict, value: dict, topic: str, key_schema: Schema, value_schema: Schema):
        self._producer.produce(topic=topic,
                               key=key,
                               key_schema=key_schema,
                               value=value,
                               value_schema=value_schema)
        self._producer.flush()

    @abstractmethod
    def push(self, key: dict, value: dict):
        pass


class TestSender(GenericSender):

    @inject
    def __init__(self, producer: AvroProducer):
        super().__init__(producer)

    def push(self, key: dict, value: dict):
        self._produce(
            topic='test',
            key=key,
            value=value,
            key_schema=avro.loads('''{
                                            "type": "record",
                                            "name": "Key",
                                            "namespace": "com.confluent.key",
                                            "fields": [
                                                {
                                                    "name": "id",
                                                    "type": {
                                                        "type": "string",
                                                        "avro.java.string": "String"
                                                    }
                                                }
                                            ]
                                        }'''),

            value_schema=avro.loads('''{
                                            "type": "record",
                                            "name": "Test",
                                            "namespace": "com.test.avro",
                                            "fields": [
                                                {
                                                    "name": "trackingId",
                                                    "type": {
                                                        "type": "string",
                                                        "avro.java.string": "String"
                                                    }
                                                },
                                                {
                                                    "name": "id",
                                                    "type": {
                                                        "type": "string",
                                                        "avro.java.string": "String"
                                                    }
                                                }
                                            ]
                                        }'''))
