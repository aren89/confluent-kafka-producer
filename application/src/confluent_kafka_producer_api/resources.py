from flask import Response, request
from flask_restful import Resource
from injector import inject

from confluent_kafka_producer_core.services import ProduceService


class MessageResource(Resource):

    @inject
    def __init__(self, produce_service: ProduceService):
        self._produce_service = produce_service

    def post(self):
        try:
            data: dict = request.json
            self._produce_service.produce(
                key=data.get('key'),
                value=data.get('value'),
                topic=data.get('topic'),
                message_name=data.get('messageName')
            )
        except Exception as e:
            return Response(status=403, response=f'Exception: {e}')
        return Response(status=204)
