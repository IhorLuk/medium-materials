import requests
import random

print(requests.get('http://127.0.0.1:8000/user/2').json())

headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json',
}

json_data = {
  "user_id": "2",
  "last_sale_amount": random.randint(0, 200000)
}

response = requests.put('http://127.0.0.1:8000/update_user_last_sale/', headers=headers, json=json_data)
print(response.json())

print(requests.get('http://127.0.0.1:8000/user/2').json())