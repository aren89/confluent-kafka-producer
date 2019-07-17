from confluent_kafka.avro import AvroProducer
from injector import Module, singleton, provider


class ConfluentModule(Module):

    @singleton
    @provider
    def provide_producer(self
                         # , kafka_host: str, schema_registry_url: str
                         ) -> AvroProducer:
        return AvroProducer(config={
            'bootstrap.servers': 'localhost:9092',
            'schema.registry.url': 'http://localhost:9052'}
        )
