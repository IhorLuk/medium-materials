import boto3
import random
import json
import time

# use this endpoint for localstack
endpoint_url = "http://localhost.localstack.cloud:4566"

sqs = boto3.client('sqs', endpoint_url=endpoint_url)
list_queues_resp = sqs.list_queues()
queue_url = list_queues_resp['QueueUrls'][0]

while True:
    message = {random.randint(0, 100000): str(random.randint(1, 100000))}
    message = json.dumps(message)

    sqs.send_message(
        QueueUrl=queue_url,
        MessageBody=message
    )
    
    time.sleep(2)
