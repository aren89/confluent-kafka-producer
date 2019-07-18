from typing import Type

from injector import Key

BootstrapServers = Key('kafka.boostrap.servers')
SchemaRegistryUrl = Key('chili.schema_registry.url')


class ConfigurationKey:

    def __init__(self, injection_key: Key, key_type: Type):
        self._type = key_type
        self._injection_key = injection_key

    @property
    def name(self):
        return self.injection_key.__name__

    @property
    def type(self):
        return self._type

    @property
    def injection_key(self):
        return self._injection_key


ConfigurationSections = {
    'DEFAULT': [
        ConfigurationKey(BootstrapServers, str),
        ConfigurationKey(SchemaRegistryUrl, str)
    ]
}
