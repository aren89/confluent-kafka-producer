import logging
import os
import signal
import sys

from confluent_kafka_producer_api.application import ConfluentKafkaApplication
from util import ROOT_DIR

logger = logging.getLogger(f'confluent-kafka-producer.{__name__}')

with open(os.path.join(ROOT_DIR, 'config', 'logo.txt'), 'r') as logo_file:
    logger.info(logo_file.read())


def shutdown_signal_handler(signum, frame=None):
    logger.info(f'Stop Confluent Kafka Application (signum: {signum}, frame: {str(frame)}).')
    sys.exit(0)


signal.signal(signal.SIGTERM, shutdown_signal_handler)
signal.signal(signal.SIGINT, shutdown_signal_handler)

app = ConfluentKafkaApplication()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4055, debug=False)
