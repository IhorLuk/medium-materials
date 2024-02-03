import boto3

db = boto3.client('dynamodb')
response = db.create_table(
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5,
    },
    TableName='Nasdaq-code',
    AttributeDefinitions=[
        {
            'AttributeName': 'Symbol',
            'AttributeType': 'S',
        },
        {
            'AttributeName': 'Country',
            'AttributeType': 'S',
        },
    ],
    KeySchema=[
        {
            'AttributeName': 'Symbol',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'Country',
            'KeyType': 'RANGE'
        }
    ]
)