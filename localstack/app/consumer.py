import boto3
import csv
import datetime
import os


def handler(event, context):
    print(event)
    
    # use this endpoint for localstack
    endpoint_url = "http://localhost.localstack.cloud:4566"
        
    filename = 'app_output-{date:%Y-%m-%d_%H:%M:%S}.txt'.format(date=datetime.datetime.now())
    with open(filename, 'w') as f:
        
        # using csv.writer method from CSV package
        write = csv.writer(f)
        
        write.writerows(event)
    
    s3 = boto3.client("s3", endpoint_url=endpoint_url)
    # put object to the app bucket
    put_object_resp = s3.put_object(
        Body=filename,
        Bucket='app-bucket',
        Key=filename,
    )

    os.remove(filename)