import hashlib
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
from datetime import datetime, timedelta
from django.conf import settings
import logging
logging.basicConfig(level=logging.ERROR)

def get_secret_key():
    """Returns a predefined secret key."""
    return settings.KODE_AKSES

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

def encrypt_aes_js_style(plaintext, key):
    """Encrypts text using AES encryption (Base64 encoded)."""
    try:
        salt = hashlib.sha256().digest()[:8]
        derived_key, derived_iv = derive_key_and_iv(key, salt)
        
        cipher = AES.new(derived_key, AES.MODE_CBC, derived_iv)
        padded_plaintext = pad(plaintext.encode('utf-8'), AES.block_size)
        encrypted_bytes = cipher.encrypt(padded_plaintext)
        
        return base64.b64encode(b"Salted__" + salt + encrypted_bytes).decode('utf-8')
    
    except Exception:
        return None

@method_decorator(csrf_exempt, name='dispatch')
class DecryptView(View):
    """Handles decryption of an encrypted attendance code."""
    def post(self, request):
        try:
            try:
                data = json.loads(request.body)
            except json.JSONDecodeError:
                return JsonResponse({"status": "error", "message": "Invalid JSON format.", "data": None}, status=400)

            encrypted_message = data.get("encrypted_message", "").strip()
            if not encrypted_message:
                return JsonResponse({"status": "error", "message": "Missing 'encrypted_message' field.", "data": None}, status=400)

            try:
                secret_key = get_secret_key()
                shift_value = 3
                decryption_key = caesar_decipher(secret_key, shift_value)
            except Exception as e:
                logging.error(f"Failed to retrieve decryption key: {str(e)}")
                return JsonResponse({"status": "error", "message": "Failed to retrieve decryption key.", "data": None}, status=500)

            try:
                decrypted_text = decrypt_aes_js_style(encrypted_message, decryption_key)
                if not decrypted_text:
                    raise ValueError("Decryption returned empty result.")
            except Exception as e:
                logging.error(f"Decryption failed: {str(e)}")
                return JsonResponse({"status": "error", "message": "Decryption failed.", "data": None}, status=400)

            try:
                course_id, meet_id, date, start, end = decrypted_text.split(',')
            except ValueError:
                return JsonResponse({"status": "error", "message": "Invalid decrypted message format.", "data": None}, status=400)

            return JsonResponse({
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
            }, status=200)

        except Exception as e:
            logging.error(f"Unexpected error: {str(e)}")
            return JsonResponse({"status": "error", "message": "An unexpected error has occurred.", "data": None}, status=500)

@method_decorator(csrf_exempt, name='dispatch')
class EncryptView(View):
    """Handles encryption of a new attendance code."""
    
    def post(self, request):
        try:
            try:
                data = json.loads(request.body)
            except json.JSONDecodeError:
                return JsonResponse({"status": "error", "message": "Invalid JSON format."}, status=400)

            encrypted_message = data.get("encrypted_message", "").strip()
            new_meet_id = data.get("new_meet_id", "").strip()

            if not encrypted_message:
                return JsonResponse({"status": "error", "message": "Missing 'encrypted_message' field."}, status=400)
            if not new_meet_id:
                return JsonResponse({"status": "error", "message": "Missing 'new_meet_id' field."}, status=400)

            try:
                secret_key = get_secret_key()
                shift_value = 3
                decryption_key = caesar_decipher(secret_key, shift_value)
            except Exception as e:
                return JsonResponse({"status": "error", "message": f"Failed to retrieve decryption key: {str(e)}"}, status=500)

            try:
                decrypted_text = decrypt_aes_js_style(encrypted_message, decryption_key)
                if not decrypted_text:
                    raise ValueError("Decryption returned empty result.")
            except Exception as e:
                return JsonResponse({"status": "error", "message": f"Decryption failed: {str(e)}"}, status=400)

            try:
                course_id, _, _, _, _ = decrypted_text.split(',')
            except ValueError:
                return JsonResponse({"status": "error", "message": "Invalid decrypted message format."}, status=400)

            now = datetime.now()
            new_date = now.strftime("%Y-%m-%d")
            new_start = now.strftime("%H:%M")
            new_end = (now + timedelta(minutes=1)).strftime("%H:%M")

            updated_text = f"{course_id},{new_meet_id},{new_date},{new_start},{new_end}"

            try:
                new_encrypted_message = encrypt_aes_js_style(updated_text, decryption_key)
                if not new_encrypted_message:
                    raise ValueError("Encryption returned empty result.")
            except Exception as e:
                return JsonResponse({"status": "error", "message": f"Encryption failed: {str(e)}"}, status=400)

            return JsonResponse({
                "status": "success",
                "message": "Encryption updated successfully.",
                "data": {
                    "updated_encrypted_message": new_encrypted_message,
                    "updated_details": {
                        "course_id": course_id,
                        "meet_id": new_meet_id,
                        "date": new_date,
                        "start": new_start,
                        "end": new_end
                    }
                }
            }, status=200)

        except Exception as e:
            return JsonResponse({"status": "error", "message": f"Unexpected error: {str(e)}"}, status=500)