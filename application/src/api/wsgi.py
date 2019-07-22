import logging
import os
import signal
import sys

from api.application import ConfluentKafkaApplication

logger = logging.getLogger(f'confluent-kafka-producer.{__name__}')

with open(os.path.join(os.path.dirname(os.path.dirname(__file__)), '../config', 'logo.txt'), 'r') as logo_file:
    logger.info(logo_file.read())


def shutdown_signal_handler(signum, frame=None):
    logger.info(f'Stop Tim Connect application (signum: {signum}, frame: {str(frame)}).')
    sys.exit(0)


signal.signal(signal.SIGTERM, shutdown_signal_handler)
signal.signal(signal.SIGINT, shutdown_signal_handler)

app = ConfluentKafkaApplication()

if __name__ == '__main__':
    app.run(port=4055, debug=False)
