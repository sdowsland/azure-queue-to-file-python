from azure.storage.queue import QueueService
import sys
import json

config = {
    "accountName": "",
    "accountKey": "",
    "queueName": "",
    "producerCount": 10
}


try:
    with open('config.json') as config_file:
        config = json.load(config_file)
except FileNotFoundError:
    print("No config.json set")


exit(0)

print("Sending events to: " + config.queueName)

queue_service = QueueService(account_name=config.accountName, account_key=config.accountKey)

while True:
    line = sys.stdin.readline()
    if line:
        queue_service.put_message(config.queueName, line)