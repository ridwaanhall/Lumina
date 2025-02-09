import requests
import json

class EncryptionService:
    def __init__(self, base_url):
        self.base_url = base_url
        self.headers = {"Content-Type": "application/json"}

    def encrypt(self, encrypted_message, new_meet_id):
        url = f"{self.base_url}/encrypt/"
        data = {
            "encrypted_message": encrypted_message,
            "new_meet_id": new_meet_id
        }
        response = requests.post(url, data=json.dumps(data), headers=self.headers)
        return response

    def decrypt(self, encrypted_message):
        url = f"{self.base_url}/decrypt/"
        data = {
            "encrypted_message": encrypted_message
        }
        response = requests.post(url, data=json.dumps(data), headers=self.headers)
        return response

if __name__ == "__main__":
    base_url = "http://127.0.0.1:8000/api"
    encrypted_message = "U2FsdGVkX18yFHUUB+bW79HoXXHHF+1e9bZBZXulYqz5sjpNS4hBir7WVLbE0K71dk69YM+99NY8LMSKajXiVQ=="
    new_meet_id = "300"

    service = EncryptionService(base_url)

    response_encrypt = service.encrypt(encrypted_message, new_meet_id)
    print("Encrypt:")
    print(response_encrypt.status_code)
    print(json.dumps(response_encrypt.json(), indent=4))

    response_decrypt = service.decrypt(encrypted_message)
    print("Decrypt:")
    print(response_decrypt.status_code)
    print(json.dumps(response_decrypt.json(), indent=4))