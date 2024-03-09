import boto3

# use this endpoint for localstack
endpoint_url = "http://localhost.localstack.cloud:4566"

s3 = boto3.client("s3", endpoint_url=endpoint_url)
list_buckets_resp = s3.list_buckets()

# create new bucket
create_bucket_resp = s3.create_bucket(Bucket='test-bucket', CreateBucketConfiguration={
    'LocationConstraint': 'us-west-1'})
print(create_bucket_resp)

# put object to the new bucket
put_object_resp = s3.put_object(
    Body='test.txt',
    Bucket='test-bucket',
    Key='test.txt',
)
print(put_object_resp)

# list objects in this bucket
list_obj_resp = s3.list_objects_v2(
    Bucket='test-bucket'
)
print(list_obj_resp['Contents'])
