from confluent_kafka.avro import AvroProducer
from injector import Injector

from modules import ConfluentModule
from sender import TestSender


def start_kafka_daemon():
    injector = Injector(modules=[ConfluentModule()])
    test_sender = TestSender(injector.get(AvroProducer))
    test_sender.push(
        key={'id': '123'},
        value={
            'id': '123',
            'trackingId': 'trackingId'
        }, )


if __name__ == '__main__':
    start_kafka_daemon()
