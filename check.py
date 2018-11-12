from azure.storage.queue import QueueService
from azure.storage.blob import BlockBlobService
import sys
import json
import datetime
import socket
from os import listdir
from os.path import isfile, join

import logger


log = logger.setup_custom_logger('blobCheck')


try:
    with open('config.json') as config_file:
        config = json.load(config_file)
except FileNotFoundError:
    print("No config.json set")
    exit(1)

blob_service = BlockBlobService(account_name=config['checkUploaded']['accountName'], account_key=config['checkUploaded']['accountKey'])

# source_path = "/data-drive/output"
source_path = config['checkUploaded']['sourcePath']
destination_path = config['checkUploaded']['destinationPath']

onlyfiles = [f for f in listdir(source_path) if isfile(join(source_path, f))]

for file in onlyfiles:

    if blob_service.exists(config['checkUploaded']['container'], destination_path + "/" + file) == False:
        log.info("{} is not in blob store".format(file))