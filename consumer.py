from azure.storage.queue import QueueService
import sys
import json
import datetime
import socket

import logger


log = logger.setup_custom_logger('consumer')


try:
    with open('config.json') as config_file:
        config = json.load(config_file)
except FileNotFoundError:
    print("No config.json set")
    exit(1)

print("Getting events from: " + config['queueName'])

queue_service = QueueService(account_name=config['accountName'], account_key=config['accountKey'])

doneCount = 0
doneInterval = 1000

date = datetime.datetime.now().isoformat()
hostname = socket.gethostname()
filepath = "{}/{}-{}-{}.json".format(config['dataDirectory'], config['queueName'], date, hostname)

with open(filepath, "w") as outfile:

    while True:
        messages = queue_service.get_messages(config['queueName'], num_messages=32)

        

        for message in messages:

            outfile.write(message.content + "\n")

            doneCount = doneCount + 1

            if doneCount % doneInterval == 0:
                log.info(doneCount)

            queue_service.delete_message(config['queueName'], message.id, message.pop_receipt)
