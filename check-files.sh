
docker run -it --rm -v $PWD:/usr/local/app -v /data-export/output:/data-export/output -w /usr/local/app azure-queue-to-file-python python check.py