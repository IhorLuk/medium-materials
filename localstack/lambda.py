import boto3

endpoint_url = "http://localhost.localstack.cloud:4566"
lambda_client = boto3.client('lambda', endpoint_url=endpoint_url)

# creating function from zip file
zip_filename = "hello_world.zip"
with open(zip_filename, 'rb') as f:
    create_resp = lambda_client.create_function(
        FunctionName="hello-python-test",
        Runtime="python3.10",
        Role="arn:aws:iam::000000000000:role/lambda-role",
        Handler="hello_world.handler",
        Code={'ZipFile': f.read()},
        MemorySize=128,
    )
    
    # print(create_resp)

# create url for invocation
create_url_resp = lambda_client.create_function_url_config(
    FunctionName="hello-python-test",
    AuthType="NONE",
)

function_url = create_url_resp["create_url_resp"]
print(function_url)

# manually invoke from code
invoke_resp = lambda_client.invoke(
    FunctionName='hello-python-test',
)

print(invoke_resp)