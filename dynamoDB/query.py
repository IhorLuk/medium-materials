import boto3

db = boto3.client('dynamodb')
response = db.query(
    TableName='Nasdaq-code',
    ExpressionAttributeValues={
        ':v1': {
            'S': 'AAPL',
        },
    },
    KeyConditionExpression='Symbol = :v1',
    ProjectionExpression='Lastsale',
)

print(response)