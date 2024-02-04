import boto3

db = boto3.client('dynamodb')

response = db.put_item(
    TableName='Nasdaq-code',
    Item={
        'Symbol': {
            'S': 'AAPL',
        },
        'Stockname': {
            'S': 'Apple Inc. Common Stock',
        },
        'Lastsale': {
            'N': '189.97',
        },
        'Country':{
            'S': 'United States'
        },
    },
    ReturnConsumedCapacity='TOTAL',
)

response = db.put_item(
    TableName='Nasdaq-code',
    Item={
        'Symbol': {
            'S': 'ALC',
        },
        'Stockname': {
            'S': 'Alcon Inc. Ordinary Shares',
        },
        'Lastsale': {
            'N': '73.52',
        },
        'Country':{
            'S': 'Switzerland',
        },
        'Sector': {
          'S': 'Healthcare',
        },
    },
    ReturnConsumedCapacity='TOTAL',
)

print(response)