from confluent_kafka.avro import AvroProducer
from injector import Injector

from modules import ConfluentModule, ConfigurationModule
from producer import Producer


def start_kafka_daemon():
    injector = Injector(modules=[ConfigurationModule(), ConfluentModule()])
    test_sender = Producer(injector.get(AvroProducer))
    test_sender.produce(
        key={'id': '123'},
        value={'id': '123', 'trackingId': 'trackingId'},
        message_name='TestMessage')


if __name__ == '__main__':
    start_kafka_daemon()
