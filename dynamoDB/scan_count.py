import boto3

db = boto3.client('dynamodb')

response = db.scan(
    TableName = 'Nasdaq-code',
    Select = 'COUNT',
)

print(response)