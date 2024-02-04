import boto3

db = boto3.client('dynamodb')

tables = db.list_tables()
print(tables)