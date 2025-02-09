import hashlib
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

def get_secret_key():
    """Returns a predefined secret key."""
    return "xwbmrperu123"

def caesar_cipher(text, shift):
    """Encrypts text using a simple Caesar cipher."""
    result = ''
    for char in text:
        char_code = ord(char)
        if 65 <= char_code <= 90:
            result += chr((char_code - 65 + shift) % 26 + 65)
        elif 97 <= char_code <= 122:
            result += chr((char_code - 97 + shift) % 26 + 97)
        else:
            result += char
    return result

def caesar_decipher(text, shift):
    """Decrypts text using a simple Caesar cipher."""
    return caesar_cipher(text, 26 - shift)

def derive_key_and_iv(password, salt, key_length=32, iv_length=16):
    """Derives a key and IV from the password and salt, replicating CryptoJS behavior."""
    password_bytes = password.encode('utf-8')
    key_iv = b""
    digest = b""
    
    while len(key_iv) < key_length + iv_length:
        digest = hashlib.md5(digest + password_bytes + salt).digest()
        key_iv += digest
    
    return key_iv[:key_length], key_iv[key_length:key_length + iv_length]

def decrypt_aes_js_style(encrypted_text_b64, key):
    """Decrypts AES encrypted text (Base64 encoded) using the given key."""
    try:
        encrypted_bytes = base64.b64decode(encrypted_text_b64)
        
        if encrypted_bytes[:8] != b"Salted__":
            return None
        
        salt = encrypted_bytes[8:16]
        ciphertext = encrypted_bytes[16:]
        derived_key, derived_iv = derive_key_and_iv(key, salt)
        
        cipher = AES.new(derived_key, AES.MODE_CBC, derived_iv)
        decrypted_bytes = cipher.decrypt(ciphertext)
        return unpad(decrypted_bytes, AES.block_size).decode('utf-8')
    
    except Exception:
        return None

def parse_decrypted_text(decrypted_text):
    """Parses the decrypted text into structured data."""
    try:
        course_id, meet_id, date, start, end = decrypted_text.split(',')
        return {
            "status": "success",
            "message": "Decryption successful.",
            "data": {
                "decrypted_text": decrypted_text,
                "course_id": course_id,
                "meet_id": meet_id,
                "date": date,
                "start": start,
                "end": end
            }
        }
    except ValueError:
        return {
            "status": "error",
            "message": "Invalid decrypted format.",
            "data": {
                "decrypted_text": decrypted_text
            }
        }

@method_decorator(csrf_exempt, name='dispatch')
class UpdateEncryptedView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            encrypted_message = data.get("encrypted_message", "")
            secret_key = get_secret_key()
            shift_value = 3
            decryption_key = caesar_decipher(secret_key, shift_value)
            decrypted_text = decrypt_aes_js_style(encrypted_message, decryption_key)
            
            if decrypted_text:
                return JsonResponse(parse_decrypted_text(decrypted_text), status=200)
            else:
                return JsonResponse({"status": "error", "message": "Decryption failed.", "data": None}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({"status": "error", "message": "Invalid JSON format.", "data": None}, status=400)
