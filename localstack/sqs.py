import boto3
import json
import time

endpoint_url = "http://localhost.localstack.cloud:4566"
sqs = boto3.client('sqs', endpoint_url=endpoint_url)

# create new queue
create_queue_resp = sqs.create_queue(
    QueueName='test-queue',
)
print(create_queue_resp)


list_queues_resp = sqs.list_queues()
queue_url = list_queues_resp['QueueUrls'][0]
#(list_queues_resp)

# send test message to the queue
message = json.dumps({"test": 1})
send_message_resp = sqs.send_message(
    QueueUrl=queue_url,
    MessageBody=message
)
print(send_message_resp)

# get attributes for the queue
# we should see 1 for number of messages, it it was successfuly received
get_att_resp = sqs.get_queue_attributes(
    QueueUrl=queue_url,
    AttributeNames=[
        'ApproximateNumberOfMessages',
        'QueueArn'
    ]
)
print(get_att_resp['Attributes'])

time.sleep(1)

#receive the message
received_message = sqs.receive_message(
    QueueUrl=queue_url,
    MaxNumberOfMessages=1
)

# delete received message
receipt_handle = received_message['Messages']['ReceiptHandle']
delete_message_resp = sqs.delete_message(
    QueueUrl=queue_url,
    ReceiptHandle=receipt_handle,
)

print(received_message['Messages']['Body'])

# delete the queue
response = sqs.delete_queue(
    QueueUrl=queue_url
)
