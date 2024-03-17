import boto3

# use this endpoint for localstack
endpoint_url = "http://localhost.localstack.cloud:4566"

s3 = boto3.client("s3", endpoint_url=endpoint_url)
# list objects in this bucket
list_obj_resp = s3.list_objects_v2(
    Bucket='app-bucket'
)
print(list_obj_resp['Contents'])
