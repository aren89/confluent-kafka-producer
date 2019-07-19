from typing import Type, NewType


BootstrapServers = NewType('kafka.bootstrap.servers', str)
SchemaRegistryUrl = NewType('schema_registry.url', str)


class ConfigurationKey:

    def __init__(self, injection_key: NewType, key_type: Type):
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
