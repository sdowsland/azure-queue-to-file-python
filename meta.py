from azure.storage.queue import QueueService
import sys
import json
import datetime
import socket
import pprint

import logger


log = logger.setup_custom_logger('consumer')


try:
    with open('config.json') as config_file:
        config = json.load(config_file)
except FileNotFoundError:
    print("No config.json set")
    exit(1)

print("Getting meta from: " + config['queueName'])

queue_service = QueueService(account_name=config['accountName'], account_key=config['accountKey'])

metadata = queue_service.get_queue_metadata(config['queueName'])

log.info(metadata.approximate_message_count)