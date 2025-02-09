import requests

url = "http://127.0.0.1:8000/api/decrypt/"
data = {"encrypted_message": "U2FsdGVkX1/UHYzZjwCyBCYsKll2ZXP7tzfFZb6mwOzqbgAuND+POcbcbwe4kT5F"}

response = requests.post(url, json=data)
print(response.json())
