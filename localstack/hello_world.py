def handler(event, context):
    print("Hello, World!\n")
    # You can add more logic here if needed
    return {
        'statusCode': 200,
        'body': 'Hello, World!'
    }