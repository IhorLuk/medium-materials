import os
from dotenv import load_dotenv, dotenv_values

# load .env file to environment
load_dotenv()
API = os.getenv('API')
REQUEST_STRING = os.getenv('REQUEST_STRING')
print(API, REQUEST_STRING)

# store variables to the dict
config = dotenv_values(".env")
print(config)