from typing import Optional


class ProduceService:
    def produce(self, key: dict, value: dict, message_name: str, topic: Optional[str] = None):
        raise NotImplementedError
