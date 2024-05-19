import requests

delete_user = "5"
print(requests.delete(f"http://127.0.0.1:8000/delete_user/{delete_user}").json())
print(requests.get(f"http://127.0.0.1:8000/user/{delete_user}").json())