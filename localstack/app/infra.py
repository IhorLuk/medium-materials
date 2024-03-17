import boto3

# use this endpoint for localstack
endpoint_url = "http://localhost.localstack.cloud:4566"

s3 = boto3.client("s3", endpoint_url=endpoint_url)
sqs = boto3.client('sqs', endpoint_url=endpoint_url)
lambda_client = boto3.client('lambda', endpoint_url=endpoint_url)

# create bucket for an application
create_bucket_resp = s3.create_bucket(Bucket='app-bucket', CreateBucketConfiguration={
    'LocationConstraint': 'us-west-1'})

# create queue for application
create_queue_resp = sqs.create_queue(
    QueueName='app-queue',
)