import os

from confluent_kafka.avro import AvroProducer
from injector import Module, singleton, provider
from configparser import ConfigParser

from confluent_kafka_producer_core.injection_keys import SchemaRegistryUrl, BootstrapServers, ConfigurationSections
from confluent_kafka_producer_core.services import ProduceService
from confluent_kafka_producer_services.produce_service import ProduceServiceImpl


class ConfluentModule(Module):

    @singleton
    @provider
    def provide_producer(self, bootstrap_servers: BootstrapServers,
                         schema_registry_url: SchemaRegistryUrl) -> AvroProducer:
        return AvroProducer(config={
            'bootstrap.servers': bootstrap_servers,
            'schema.registry.url': schema_registry_url}
        )


class ConfigurationModule(Module):

    def configure(self, binder):
        configuration = ConfigParser()
        configuration.read([
            os.path.join('config', 'application.ini')
        ])
        sections = configuration.sections()
        sections.append('DEFAULT')
        for section in sections:
            configuration_section_keys = ConfigurationSections.get(section, [])
            for configuration_section_key in configuration_section_keys:
                if configuration_section_key.type is int:
                    value = configuration.getint(section, configuration_section_key.name)
                elif configuration_section_key.type is float:
                    value = configuration.getfloat(section, configuration_section_key.name)
                elif configuration_section_key.type is bool:
                    value = configuration.getboolean(section, configuration_section_key.name)
                elif configuration_section_key.type is list:
                    value = configuration.get(section, configuration_section_key.name)
                    value = [x.strip() for x in value.split(',')]
                elif configuration_section_key.type is dict:
                    value = configuration.get(section, configuration_section_key.name)
                    value = [x.strip() for x in value.split(',')]
                    value = {v[0]: v[1] for v in [x.split('=', maxsplit=1) for x in value]}
                else:
                    value = configuration.get(section, configuration_section_key.name)
                binder.bind(configuration_section_key.injection_key, value)


class ApplicationModule(Module):
    def configure(self, binder):
        binder.bind(interface=ProduceService, to=ProduceServiceImpl, scope=singleton)
