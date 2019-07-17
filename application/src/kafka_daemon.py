
from confluent_kafka import avro
from confluent_kafka.avro import AvroProducer
from injector import Injector

from modules import ConfluentModule


def start_kafka_daemon():

    injector = Injector(modules=[ConfluentModule()])
    producer: AvroProducer = injector.get(AvroProducer)
    producer.produce(topic='test',
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
                     }'''),
                     value={
                         'id': '123',
                         'trackingId': 'trackingId'
                     },
                     key={'id': '123'})
    producer.flush()


if __name__ == '__main__':
    start_kafka_daemon()
