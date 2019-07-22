import logging

from flask import Flask
from flask_injector import FlaskInjector
from flask_restful import Api
from injector import Injector

from api.resources import MessageResource
from modules import ConfigurationModule, ConfluentModule

logger = logging.getLogger(f'confluent-kafka-producer.{__name__}')


class ConfluentKafkaApplication(Flask):

    def __init__(self, injector=None):
        super().__init__(__name__)
        self._api = ConfluentKafkaApi(self)
        self._api.add_resource(MessageResource, '/message', endpoint='kafka_message_ep')
        if not injector:
            injector = Injector(modules=[ConfigurationModule(), ConfluentModule()])
        FlaskInjector(app=self, injector=injector)


class ConfluentKafkaApi(Api):

    def __init__(self, application):
        super().__init__(app=application, prefix='/confluent-kafka-producer/api/v1')
        logger.info(f'Tim Connect API running (prefix: {self.prefix}).')
