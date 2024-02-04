import boto3

db = boto3.client('dynamodb')

nasdaq_desc = db.describe_table(TableName="Nasdaq-code")
print(nasdaq_desc)
