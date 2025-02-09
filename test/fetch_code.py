import requests
import json

url = "http://127.0.0.1:8000/api/decrypt/"

data = {
    "encrypted_message": "U2FsdGVkX18yFHUUB+bW79HoXXHHF+1e9bZBZXulYqz5sjpNS4hBir7WVLbE0K71dk69YM+99NY8LMSKajXiVQ==",
    "new_meet_id": "300"
}

headers = {"Content-Type": "application/json"}

response = requests.post(url, data=json.dumps(data), headers=headers)

print(response.status_code)
print(json.dumps(response.json(), indent=4))