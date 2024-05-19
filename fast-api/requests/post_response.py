import requests
import random
import names

headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json',
}

for i in range(1, 100):
    json_data = {
        'user_id': str(i),
        'first_name': names.get_first_name(),
        'last_name': names.get_last_name(),
        'last_sale_amount': random.randint(1, 200000),
    }

    response = requests.post('http://127.0.0.1:8000/create_user/', headers=headers, json=json_data)
    print(response.json())
