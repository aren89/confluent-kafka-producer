from flask import Response
from flask_restful import Resource
from injector import inject

from confluent_kafka_producer_core.services import ProduceService


class MessageResource(Resource):

    @inject
    def __init__(self, produce_service: ProduceService):
        self._produce_service = produce_service

    def post(self):
        self._produce_service.produce(
            key={'id': '123'},
            value={'id': '123', 'trackingId': 'trackingId'},
            message_name='TestMessage')
        return Response(status=204)
