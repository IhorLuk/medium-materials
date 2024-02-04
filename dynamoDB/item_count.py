import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Nasdaq-code')

print(table.item_count)